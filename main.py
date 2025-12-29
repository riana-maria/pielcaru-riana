import requests  # Gestionare cereri HTTP
from bs4 import BeautifulSoup  # Analiza si extragere date din documente HTML
from datetime import datetime  # Manipulare date si ore sistem
import pandas as pd  # Analiza de date si manipulare tabele CSV
import os  # Interactiune cu sistemul de fisiere local
import tkinter as tk  # Creare interfata grafica utilizator (GUI)
from tkinter import messagebox  # Afisare ferestre de dialog standard
import re  # Procesare text prin expresii regulate

# Clasa pentru extragerea datelor de pe web
class ShopaholicScraper:
    def __init__(self):

        # Initalizare header pentru a simula un browser real
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }

    # Preluare nume articol si pret din url-ul specificat
    def extrage_date(self, url):
        try:

            # Cerere de tip http get catre site
            pagina = requests.get(url, headers=self.headers, timeout=10)
            if pagina.status_code == 200:
                soup = BeautifulSoup(pagina.content, 'html.parser')

                # Extragere nume din H1
                h1_element = soup.find("h1")
                if not h1_element:
                    return None

                # Extragere text cu spatiu intre elementele interne (curatare)
                nume_raw = h1_element.get_text(separator=" ", strip=True)

                # Corectie text lipit prin Regex (numele brand-ului era extras lipit de numele articolului)
                nume_corectat = re.sub(r'([a-z])([A-Z])', r'\1 \2', nume_raw)
                nume_final = " ".join(nume_corectat.split())

                # Localizare pret dupa atributul data-testid
                pret_element = soup.find("span", {"data-testid": "finalPrice"})
                if not pret_element:
                    return None

                # Conversie text pret in valoare numerica float
                pret_raw = pret_element.get_text()
                
                # Curatare de caractere non-numerice
                pret_numeric = float(pret_raw.replace('lei', '').replace(',', '.').replace('\xa0', '').strip())

                return {
                    "nume": nume_final,
                    "pret": pret_numeric,
                    "data": datetime.now().strftime("%Y-%m-%d %H:%M")
                }
        except Exception as e:
            print(f"Eroare scraping: {e}")
            return None

# Clasa pentru a gestiona interfata si logica aplicatiei
class ShopaholicApp:
    def __init__(self, root):

        # Configurare fereastra principala si motor scraping
        self.root = root
        self.root.title("Shopaholic - Price Tracker")
        self.root.geometry("600x450")
        self.scraper = ShopaholicScraper()

        # Interfata grafica (GUI): etichete, camp intrare si buton
        tk.Label(root, text="SHOPAHOLIC", font=("Arial", 18, "bold")).pack(pady=10)

        tk.Label(root, text="Introdu link-ul produsului de pe About You:", font=("Arial", 10)).pack(pady=5)
        self.url_entry = tk.Entry(root, width=70)
        self.url_entry.pack(pady=10)

        # Buton pentru verificare
        tk.Button(root, text="Verifică", command=self.proceseaza_link,
                  bg="black", fg="white", font=("Arial", 10, "bold")).pack(pady=15)

        # Zona afisare rezultate
        self.lbl_info = tk.Label(root, text="", font=("Arial", 10), justify="center")
        self.lbl_info.pack(pady=20)

    # Executie flux: citire url, scrarping, comparare pret si salvare
    def proceseaza_link(self):
        url = self.url_entry.get()
        if not url:
            messagebox.showwarning("Atenție", "Te rugăm să introduci un link!")
            return

        date_noi = self.scraper.extrage_date(url)

        if date_noi:
            nume_fisier = "istoric_preturi.csv"
            msg_status = f"Produs: {date_noi['nume']}\nPreț actual: {date_noi['pret']} RON"

            # Logica de comparare a datelor din csv
            if os.path.isfile(nume_fisier):
                df = pd.read_csv(nume_fisier)
                istoric_produs = df[df['nume'] == date_noi['nume']]

                if not istoric_produs.empty:
                    minim_vechi = istoric_produs['pret'].min()

                    # Verificare daca pretul actual este noul minim
                    if date_noi['pret'] < minim_vechi:
                        msg_status += f"\n\n NOU MINIM DETECTAT! (Anterior: {minim_vechi} RON)"
                    else:
                        msg_status += f"\nMinimul înregistrat în istoric: {minim_vechi} RON"
                else:
                    msg_status += "\n\nAcesta este primul preț înregistrat pentru acest produs."

            # Salvarea datelor prin adaugare la finalul fisierului (mode append)
            df_nou = pd.DataFrame([date_noi])
            df_nou.to_csv(nume_fisier, mode='a', index=False, header=not os.path.isfile(nume_fisier))

            self.lbl_info.config(text=msg_status, fg="blue")
        else:
            messagebox.showerror("Eroare", "Nu am putut extrage datele. Verificați link-ul!")

# Pornire aplicatie
if __name__ == "__main__":
    root = tk.Tk()
    app = ShopaholicApp(root)
    root.mainloop()
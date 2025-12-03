
from flask import Flask, Response, url_for
import pandas as pd
import matplotlib.pyplot as plt
import io
import math

# 1. CONSTANTE (Preluate din tema)
X = 19
Y = 4
FILE_NAME = r'C:\Users\riana\Desktop\tema_parcurs_python_Pielcaru_Riana-Maria_423F\Problema 2\data(in).csv'

app = Flask(__name__)

# 2. LOGICA DE GENERARE A GRAFICULUI (Problema 2.C)
def generate_plot_c():
    """Generează graficul Durata vs. Puls (Ultimele Y valori) și îl scrie în memorie."""
    try:
        df = pd.read_csv(FILE_NAME)
    except FileNotFoundError:
        return None

    # Selectia datelor (Ultimele Y valori pentru Durata si Puls)
    df_ultimele_y = df[['Durata', 'Puls']].tail(Y).reset_index(drop=True)
    
    # Creează figura Matplotlib
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.scatter(df_ultimele_y['Durata'], df_ultimele_y['Puls'], color='red')
    
    # Adaugare etichete pe puncte
    for i, row in df_ultimele_y.iterrows():
        ax.annotate(f"({row['Durata']}, {row['Puls']})", (row['Durata'], row['Puls']), textcoords="offset points", xytext=(0,10), ha='center')

    ax.set_title(f'C. Ultimele {Y} valori: Durata vs. Puls (Integrare Web)')
    ax.set_xlabel('Durata')
    ax.set_ylabel('Puls')
    ax.grid(True)
    
    #Salvarea în Memorie
    output = io.BytesIO()
    # Salvează figura în buffer-ul de memorie ca PNG
    fig.savefig(output, format='png')
    plt.close(fig) # Inchide figura pentru a elibera memoria
    output.seek(0)
    
    return output

# 3. RUTELE FLASK (SERVERUL WEB)

# RUTA 1: Servirea Imaginii (Date Binare PNG)
@app.route('/plot_c.png')
def plot_c_route():
    plot_data = generate_plot_c()
    
    if plot_data:
        # Returneaza imaginea binara cu tipul de continut setat la imagine PNG
        return Response(plot_data.getvalue(), mimetype='image/png')
    else:
        # In caz de eroare de fisier
        return "Eroare: Fisierul CSV nu a putut fi gasit sau citit.", 404


# RUTA 2: Pagina Principală (Interfața HTML)
@app.route('/')
def index():
    # Continut HTML simplu care foloseste ruta /plot_c.png ca sursa a imaginii
    html_content = f"""
    <!doctype html>
    <title>Tema P2 Bonificatie (Flask)</title>
    <h1>Integrare Vizualizare Matplotlib (Problema 2)</h1>
    <p>Graficul generat de codul Python/Pandas:</p>
    
    <img src="{ url_for('plot_c_route') }" alt="Grafic Durata vs Puls">
    
    <p>Aceasta demonstreaza ca logica de vizualizare ruleaza pe serverul Python Flask.</p>
    """
    return html_content


if __name__ == '__main__':
    # Ruleaza serverul pe http://127.0.0.1:5000/
    # debug=True este util in timpul dezvoltarii
    app.run(debug=True)

import pandas as pd
import matplotlib.pyplot as plt

X = 19 
Y = 4 
FILE_NAME = r'C:\Users\riana\Desktop\tema_parcurs_python_Pielcaru_Riana-Maria_423F\Problema 2\data(in).csv'

print(f"Setari tema Problema 2: X={X}, Y={Y}\n")

try:
# 1. Importarea valorilor din fisier
    df = pd.read_csv(FILE_NAME)

# 2. PLOTAREA DATELOR

# A. Plotarea tuturor valorilor
    plt.figure(figsize=(10, 5))
    df.plot(title='A. Toate valorile din data.csv', grid=True, ax=plt.gca(), linewidth=1.5)
    plt.ylabel("Valoare")
    plt.xlabel("Index")
    plt.savefig('plot_a_all_values.png') 
    plt.close()

# B. Plotarea primelor X (19) valori
    df_primele_x = df.head(X)
    
    plt.figure(figsize=(10, 5))
    df_primele_x['Puls'].plot(kind='bar', ax=plt.gca(), title=f'B. Primele {X} valori (Coloana Puls)', color='skyblue')
    plt.ylabel("Puls")
    plt.xlabel("Index (Primele 19 intrari)")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig('plot_b_first_x_values.png')
    plt.close()

# C. Plotarea ultimelor Y (4) valori pentru coloanele Durata si Puls.
    df_ultimele_y = df[['Durata', 'Puls']].tail(Y).reset_index(drop=True)
    
    plt.figure(figsize=(8, 6))
    plt.scatter(df_ultimele_y['Durata'], df_ultimele_y['Puls'], color='red', s=100) 
    
    for i, row in df_ultimele_y.iterrows():
        plt.annotate(f"({row['Durata']}, {row['Puls']})", (row['Durata'], row['Puls']), textcoords="offset points", xytext=(0,10), ha='center')

    plt.title(f'C. Ultimele {Y} valori: Durata vs. Puls')
    plt.xlabel('Durata')
    plt.ylabel('Puls')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('plot_c_last_y_values.png')
    plt.close()
    
except FileNotFoundError:
    print(f"EROARE: Fisierul '{FILE_NAME}' nu a fost gasit.")
except KeyError as e:
    print(f"EROARE: Coloana {e} nu a fost gasita in fisierul CSV. Verifica numele coloanelor.")

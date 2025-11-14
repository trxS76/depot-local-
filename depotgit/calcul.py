import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt


coeff = {
    "UE1": {
        "R101":10, "R102":10, "R103":7, "R104":7, "R106":5, "R108":6,
        "R110":5, "R111":4, "R112":2, "R113":5, "R114":5,
        "SAE11":20, "SAE12":20, "SAE16":7
    },
    "UE2": {
        "R101":4, "R103":2, "R104":8, "R106":5, "R107":15, "R108":6,
        "R110":5, "R111":5, "R112":2, "R113":9, "R114":9,
        "R115":3, "SAE13":29, "SAE16":7
    },
    "UE3": {
        "R101":4, "R103":2, "R105":6, "R109":4, "R110":5, "R111":5,
        "R112":2, "R115":3, "SAE14":20, "SAE15":20, "SAE16":7
    }
}


matieres = []
for ue in coeff.values():  
    for matiere in ue.keys():    
        if matiere not in matieres:  
            matieres.append(matiere)

fenetre = tk.Tk()
fenetre.title("Calcul des moyennes par UE")
fenetre.geometry("750x700")

frm = ttk.Frame(fenetre)
frm.pack(padx=20, pady=20)

titre = ttk.Label(frm, text="Saisis les notes :")
titre.grid(column=0, row=0, pady=10)

a = {}
row = 1
for matiere in matieres:
    ttk.Label(frm, text=matiere, width=15).grid(column=0, row=row, pady=2)
    entry = ttk.Entry(frm, width=5)
    entry.grid(column=1, row=row, pady=2)
    a[matiere] = entry
    row += 1

def calculer():
    notes = {}
    for mat, entry in a.items():
        try:
            notes[mat] = float(entry.get())
        except ValueError:
            messagebox.showerror("Erreur", f"Note invalide ou manquante pour {mat}") # Corrige si il y'a une erreur ou une note manquante
            return
    
    moyennes = {}
    for ue, mat_ue in coeff.items():
        total_points = 0
        total_coef = 0
        for mat, coef in mat_ue.items():
            total_points += notes[mat] * coef
            total_coef += coef
        moyenne = round(total_points / total_coef, 2)
        moyennes[ue] = moyenne
    
    # Affichage des moyennes dans une seconde fenêtre pour afficher le résultat
    resultats = "\n".join([f"{ue} : {moy}" for ue, moy in moyennes.items()])
    messagebox.showinfo("Résultats", f"Moyennes calculées :\n\n{resultats}")
    
    plt.figure(figsize=(5,4))
    def get_color(value):
        if value >10:
            return 'green'
        elif 8 <= value <= 10:
            return 'orange'
        else:
            return 'red'
    
    colors = [get_color(val) for val in moyennes.values()]
    plt.bar(moyennes.keys(), moyennes.values(), color=colors)
    plt.title("Moyenne par UE")
    plt.ylim(0, 20)
    plt.ylabel("Notes")
    plt.show()

btn = ttk.Button(frm, text="Valider", command=calculer)
btn.grid(column=0, row=row, pady=20)

fenetre.mainloop()
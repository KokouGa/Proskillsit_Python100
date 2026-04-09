import tkinter as tk

# Créer la fenêtre principale
root = tk.Tk()
root.title("Ma première application")
root.geometry("400x300")  # largeur x hauteur

# Ajouter un label (texte)
label = tk.Label(root, text="Bonjour Tkinter !")
label.pack()

# Ajouter un bouton
def on_click():
    print("Bouton cliqué !")

button = tk.Button(root, text="Cliquez-moi", command=on_click)
button.pack()

# Lancer l'application
root.mainloop()
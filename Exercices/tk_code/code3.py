import tkinter as tk
from tkinter import ttk, messagebox, filedialog

root = tk.Tk()

### Combobox (liste déroulante)
combo = ttk.Combobox(root, values=["Option 1", "Option 2", "Option 3"])
combo.pack()

### Checkbutton (case à cocher)
check_var = tk.BooleanVar()
check = tk.Checkbutton(root, text="Accepter", variable=check_var)
check.pack()

### Radiobutton (boutons radio)
radio_var = tk.StringVar()
radio1 = tk.Radiobutton(root, text="Choix A", variable=radio_var, value="A")
radio2 = tk.Radiobutton(root, text="Choix B", variable=radio_var, value="B")
radio1.pack()
radio2.pack()

### Listbox (liste sélectionnable)
listbox = tk.Listbox(root)
listbox.insert(1, "Élément 1")
listbox.insert(2, "Élément 2")
listbox.insert(3, "Élément 3")
listbox.pack()

### Scrollbar (barre de défilement)
scrollbar = tk.Scrollbar(root)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

### Canvas (zone de dessin)
canvas = tk.Canvas(root, width=200, height=200, bg="white")
canvas.pack()
canvas.create_line(0, 0, 200, 200, fill="red")
canvas.create_rectangle(50, 50, 150, 150, fill="blue")

### Messagebox (boîte de dialogue)
def show_msg():
    messagebox.showinfo("Titre", "Message d'information")
    messagebox.showwarning("Attention", "Message d'avertissement")
    messagebox.showerror("Erreur", "Message d'erreur")
    reponse = messagebox.askyesno("Question", "Voulez-vous continuer ?")
    if reponse:
        print("Oui")

### Filedialog (sélection de fichiers)
def open_file():
    filename = filedialog.askopenfilename()
    print(f"Fichier sélectionné: {filename}")

button_file = tk.Button(root, text="Ouvrir fichier", command=open_file)
button_file.pack()

root.mainloop()
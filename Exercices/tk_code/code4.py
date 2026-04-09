import tkinter as tk
from tkinter import filedialog, messagebox

# Variables globales
current_file = None
text_area = None
root = None

def new_file():
    global current_file, text_area
    
    if messagebox.askyesno("Nouveau", "Voulez-vous enregistrer ?"):
        save_file()
    
    text_area.delete(1.0, tk.END)
    current_file = None
    root.title("Mini Éditeur de Texte")

def open_file():
    global current_file, text_area, root
    
    file = filedialog.askopenfilename(defaultextension=".txt",
                                      filetypes=[("Fichiers texte", "*.txt"),
                                                ("Tous les fichiers", "*.*")])
    if file:
        current_file = file
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        text_area.delete(1.0, tk.END)
        text_area.insert(1.0, content)
        root.title(f"Mini Éditeur - {file}")

def save_file():
    global current_file, text_area
    
    if current_file:
        content = text_area.get(1.0, tk.END)
        with open(current_file, 'w', encoding='utf-8') as f:
            f.write(content)
    else:
        save_as_file()

def save_as_file():
    global current_file, text_area, root
    
    file = filedialog.asksaveasfilename(defaultextension=".txt",
                                        filetypes=[("Fichiers texte", "*.txt"),
                                                  ("Tous les fichiers", "*.*")])
    if file:
        current_file = file
        content = text_area.get(1.0, tk.END)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        root.title(f"Mini Éditeur - {file}")

def quit_app():
    root.quit()

def main():
    global root, text_area
    
    # Création de la fenêtre
    root = tk.Tk()
    root.title("Mini Éditeur de Texte")
    root.geometry("600x400")
    
    # Menu
    menubar = tk.Menu(root)
    root.config(menu=menubar)
    
    # Menu Fichier
    file_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Fichier", menu=file_menu)
    file_menu.add_command(label="Nouveau", command=new_file)
    file_menu.add_command(label="Ouvrir", command=open_file)
    file_menu.add_command(label="Enregistrer", command=save_file)
    file_menu.add_command(label="Enregistrer sous", command=save_as_file)
    file_menu.add_separator()
    file_menu.add_command(label="Quitter", command=quit_app)
    
    # Zone de texte
    text_area = tk.Text(root, wrap=tk.WORD, undo=True)
    text_area.pack(expand=True, fill=tk.BOTH)
    
    # Barre de défilement
    scrollbar = tk.Scrollbar(text_area)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    text_area.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=text_area.yview)
    
    root.mainloop()

if __name__ == "__main__":
    main()
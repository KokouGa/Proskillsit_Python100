import tkinter as tk

# Variables globales
expression = ""
resultat_label = None
root = None

def ajouter_valeur(valeur):
    """Ajoute un chiffre ou un opérateur à l'expression"""
    global expression
    expression += str(valeur)
    resultat_label.config(text=expression)

def effacer():
    """Efface tout"""
    global expression
    expression = ""
    resultat_label.config(text="0")

def supprimer_dernier():
    """Supprime le dernier caractère"""
    global expression
    expression = expression[:-1]
    if expression == "":
        resultat_label.config(text="0")
    else:
        resultat_label.config(text=expression)

def calculer():
    """Calcule le résultat de l'expression"""
    global expression
    
    try:
        # Remplacer × par * et ÷ par /
        expression_calc = expression.replace("×", "*").replace("÷", "/")
        
        # Évaluer l'expression (attention: eval peut être dangereux avec des entrées utilisateur)
        resultat = eval(expression_calc)
        
        # Arrondir si nécessaire (éviter les trop longues décimales)
        if isinstance(resultat, float) and resultat == int(resultat):
            resultat = int(resultat)
        elif isinstance(resultat, float):
            resultat = round(resultat, 10)
        
        expression = str(resultat)
        resultat_label.config(text=expression)
        
    except ZeroDivisionError:
        resultat_label.config(text="Erreur: division par zero")
        expression = ""
    except Exception:
        resultat_label.config(text="Erreur")
        expression = ""

def creer_bouton(parent, texte, ligne, colonne, commande, colspan=1):
    """Fonction utilitaire pour créer des boutons plus facilement"""
    bouton = tk.Button(parent, text=texte, font=("Arial", 18), 
                       command=commande, width=5, height=2)
    bouton.grid(row=ligne, column=colonne, columnspan=colspan, padx=2, pady=2)
    return bouton

def main():
    global root, resultat_label
    
    # Création de la fenêtre
    root = tk.Tk()
    root.title("Calculatrice")
    root.geometry("350x450")
    root.resizable(False, False)
    
    # Frame pour l'affichage
    frame_affichage = tk.Frame(root)
    frame_affichage.pack(pady=10)
    
    # Label pour afficher le résultat
    resultat_label = tk.Label(frame_affichage, text="0", font=("Arial", 24),
                              bg="white", width=15, anchor="e", relief="sunken")
    resultat_label.pack(padx=10, pady=10)
    
    # Frame pour les boutons
    frame_boutons = tk.Frame(root)
    frame_boutons.pack()
    
    # Ligne 1 : C, CE, %, /
    creer_bouton(frame_boutons, "C", 0, 0, effacer)
    creer_bouton(frame_boutons, "CE", 0, 1, supprimer_dernier)
    creer_bouton(frame_boutons, "%", 0, 2, lambda: ajouter_valeur("%"))
    creer_bouton(frame_boutons, "÷", 0, 3, lambda: ajouter_valeur("÷"))
    
    # Ligne 2 : 7, 8, 9, ×
    creer_bouton(frame_boutons, "7", 1, 0, lambda: ajouter_valeur(7))
    creer_bouton(frame_boutons, "8", 1, 1, lambda: ajouter_valeur(8))
    creer_bouton(frame_boutons, "9", 1, 2, lambda: ajouter_valeur(9))
    creer_bouton(frame_boutons, "×", 1, 3, lambda: ajouter_valeur("×"))
    
    # Ligne 3 : 4, 5, 6, -
    creer_bouton(frame_boutons, "4", 2, 0, lambda: ajouter_valeur(4))
    creer_bouton(frame_boutons, "5", 2, 1, lambda: ajouter_valeur(5))
    creer_bouton(frame_boutons, "6", 2, 2, lambda: ajouter_valeur(6))
    creer_bouton(frame_boutons, "-", 2, 3, lambda: ajouter_valeur("-"))
    
    # Ligne 4 : 1, 2, 3, +
    creer_bouton(frame_boutons, "1", 3, 0, lambda: ajouter_valeur(1))
    creer_bouton(frame_boutons, "2", 3, 1, lambda: ajouter_valeur(2))
    creer_bouton(frame_boutons, "3", 3, 2, lambda: ajouter_valeur(3))
    creer_bouton(frame_boutons, "+", 3, 3, lambda: ajouter_valeur("+"))
    
    # Ligne 5 : 0, 00, ., =
    creer_bouton(frame_boutons, "0", 4, 0, lambda: ajouter_valeur(0))
    creer_bouton(frame_boutons, "00", 4, 1, lambda: ajouter_valeur("00"))
    creer_bouton(frame_boutons, ".", 4, 2, lambda: ajouter_valeur("."))
    
    # Bouton égal (colspan=2 pour être plus large)
    bouton_egal = tk.Button(frame_boutons, text="=", font=("Arial", 18),
                            command=calculer, width=12, height=2, bg="#4CAF50")
    bouton_egal.grid(row=4, column=3, padx=2, pady=2)
    
    root.mainloop()

if __name__ == "__main__":
    main()
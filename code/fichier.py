age_max = -1
personne_agee = ""
compte_lignes = 0
with open("data/donne.txt", "r") as fichier:
    fichier.readline()
    contenu = fichier.readlines()
    for ligne in contenu:
        compte_lignes += 1
        print(compte_lignes)
        nom, prenom, age = ligne.split()
        age = int(age)
        if age > age_max:
            age_max = age
            personne_agee = f"{prenom} {nom}"



print(f"La personne la plus âgée est {personne_agee} avec {age_max} ans.")


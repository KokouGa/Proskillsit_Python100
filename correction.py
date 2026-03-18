def verifier_meme_lettres(mot1,mot2):
    differences=list()
    memelettres = None
    lettresdifferees = None
    #lettrestraitees = list()
    x=0
    for l in mot1:
        calcul = mot1.count(l) - mot2.count(l)
        if l not in mot2:
            print(f"Les mots {mot1} et {mot2} ne contiennent pas les memes lettres!")
            memelettres= False
            break
        elif l in mot2:
            if calcul < 0:
                lettresdifferees = True
                differences.append({"id":mot2 , "lettre": l , "qte": abs(calcul)})
            if calcul > 0:
                lettresdifferees = True
                differences.append({"id":mot1 , "lettre": l , "qte": abs(calcul)})
            if mot1.count(l) == mot2.count(l):
                x+=1
                continue
    if x == len(mot1) and len(mot1) == len(mot2):
        print(f"Les mots {mot1} et {mot2} contiennent exactement les memes lettres!")
    elif lettresdifferees and memelettres != False:
        print(f"Les mots {mot1} et {mot2} contiennent les memes lettres mais:")
        for p in differences:
            print(f"Le mot {p['id']} contient {p['qte']} {p['lettre']} de plus")

with open ("listemots.txt", "r") as fichier:
    for ligne in fichier:
        mot1, mot2 = ligne.split()
        verifier_meme_lettres(mot1, mot2)



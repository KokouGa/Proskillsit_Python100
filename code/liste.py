ma_liste = ["a", "b", "c", "d", "e", "f"]
print(ma_liste)
print(ma_liste[1:5:3])  # Affiche le premier élément
print(6 in [1,2,3,4,5])


nom = "Gawonou"

for lettre in nom: 
    print(lettre)


ma_liste = ["a", "b", "c", "d", "e", "f"]
listes = [1, 2, 3, 4, 5, 6, 7, 8]
print(ma_liste)
print(ma_liste[1:5:3])  # Affiche le premier élément
print(6 in [1,2,3,4,5])



for element in ma_liste:
    print(element)


sum_impair =  0
sum_pair = 0


for i in listes:
    if i % 2 == 0:
        sum_pair += i
    else:
        sum_impair += i
    

print("La somme des nombres impairs est:", sum_impair)
print("La somme des nombres pairs est:", sum_pair)
print("La somme totale est:", sum_pair - sum_impair)


nom = "Gawonou"

for lettre in nom:
    print(lettre)

voyales = "aeiouyAEIOUY"
index = 1
for lettre in nom:
    if lettre in voyales:
        print(f"La voyelle {lettre} est à l'index {index}")
    index += 1

# C:\Users\gawon\OneDrive\Desktop\ProskillsitPython100\Cours_Python110\code\list.py
nom = input("entrer le nom du fichier a exploiter ")

def liste(name):
    lignes = []
    mot = []
    with open(name, "r") as f:
        for line in f:
          line= line.split()
          lignes.append(line)
    return lignes



def palindrome(mot):
   resultats = []
   for i in range(len(mot)):
      for j in range(len(mot[i])):
         palindrome = mot[i][j] == mot[i][j][::-1]
         if palindrome:
            verdict = (f"le mot {j+1} de la ligne {i+1} : {mot[i][j]} est un palindrome")
         else:
            verdict = (f"le mot {j+1} de la ligne {i+1} : {mot[i][j]} n'est pas un palindrome")
         resultats.append(verdict)
   return resultats 
      


def anagrame(mot):
   resultats = []
   for i in range(len(mot)):
      for j in range(len(mot[i])-1):
         mot1 = mot[i][j]
         mot2 = mot[i][j+1]
         mot1_new = mot1
         mot2_new = mot2
         for x in mot1:
            if x in mot2:
               mot2_new = mot2_new.replace(x,"")
               mot1_new = mot1_new.replace(x,"")

         if mot1_new == "" and mot2_new == "":
               
               verdict = (f"les mots de la ligne {i+1} : {mot[i]} sont des anagrames")
         else:
               
               verdict = (f"les mots de la ligne {i+1} : {mot[i]} ne sont pas des anagrames")
         resultats.append(verdict)
   return resultats 

mot = liste(nom)

for v in palindrome(mot):
   print(v)


for v in anagrame(mot):
   print(v)
         
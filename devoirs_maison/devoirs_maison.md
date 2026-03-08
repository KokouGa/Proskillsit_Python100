
# TP Python — Lecture de Fichiers et Validation de Données

Ce TP contient plusieurs exercices permettant de pratiquer :

- la lecture de fichiers
- la validation de données
- les chaînes de caractères
- les algorithmes simples
- les calculs mathématiques

Chaque exercice est indépendant.

---

# Exercice 1 — Validation des parenthèses

## Objectif

Écrire un programme Python qui vérifie si une chaîne contenant des parenthèses est valide.

Les symboles à considérer sont :

()  
[]  
{}

Une expression est valide si :
- chaque parenthèse ouvrante possède une parenthèse fermante correspondante
- l’ordre de fermeture est respecté

## Exemple à tester

```
({[()]})
```

Résultat attendu :

```
Expression valide
```

Exemple invalide :

```
({}([{()}]{)){})
```

Résultat attendu :

```
Expression invalide
```

---

# Exercice 2 — Vérifier si deux mots contiennent les mêmes lettres

## Objectif

Écrire un programme Python qui lit un fichier texte et vérifie si les deux mots présents sur chaque ligne contiennent les mêmes lettres.

## Exemple de fichier

```
chien niche
python typhon
chat chien
abc cab
```

## Travail demandé

Le programme doit :

- lire le fichier ligne par ligne
- récupérer les deux mots
- vérifier si les deux mots contiennent les mêmes lettres
- afficher le résultat

## Exemple de sortie

```
chien et niche ---- contiennent les mêmes lettres
python et typhon ---- contiennent les mêmes lettres
chat et chien ---- ne contiennent pas les mêmes lettres
abc et cab ---- contiennent les mêmes lettres
```

---

# Exercice 3 — Vérification de palindrome

## Objectif

Un palindrome est un mot qui se lit de la même façon de gauche à droite et de droite à gauche.

Exemples :

```
radar
kayak
level
```

## Travail demandé

Écrire un programme Python qui :

- lit un fichier contenant plusieurs mots
- vérifie si chaque mot est un palindrome
- affiche le résultat

## Exemple

```
radar ---- est un palindrome
python ---- n'est pas un palindrome
kayak ---- est un palindrome
```

---

# Exercice 4 — Calcul simple à partir d’un fichier

## Objectif

Lire un fichier contenant des opérations mathématiques et afficher les résultats.

## Exemple de fichier

```
5 + 3
10 - 2
4 * 6
8 / 2
```

## Travail demandé

Le programme doit :

- lire chaque ligne
- identifier l'opération
- calculer le résultat
- afficher le résultat

## Exemple de sortie

```
5 + 3 = 8
10 - 2 = 8
4 * 6 = 24
8 / 2 = 4
```

---

# Exercice 5 — Résolution d'équation du second degré

## Objectif

Écrire un programme qui lit les coefficients d’équations du second degré dans un fichier et affiche les solutions.

Une équation du second degré a la forme :

ax² + bx + c = 0

## Exemple de fichier

```
10, 5, 1
-4, 1, 3
20, 10, 5, 3, 4, 8
3, 5, 7, 8
```

## Règles

- si une ligne contient 3 entiers → résoudre 1 équation
- si une ligne contient 6 entiers → résoudre 2 équations
- si le déterminant Δ < 0 → afficher `NaN`
- si Δ = 0 → afficher `x=val`
- si Δ > 0 → afficher `x1=val, x2=val`

---

# Exercice 6 — Validation d’un fichier avec syntaxe a à g

## Objectif

Lire un fichier contenant des mots composés des lettres `a` à `g`.

Les lettres `a`, `b`, `c`, `d` peuvent être suivies d’un nombre entre parenthèses.

## Exemple valide

```
a(2)
b(10)
c
d(4)
e
f
g
```

Les espaces autour des parenthèses sont permis :

```
a( 16 )
b ( 8 )
```

## Travail demandé

Le programme doit :

- lire le fichier
- vérifier la validité de chaque mot
- détecter les erreurs de syntaxe

Si une erreur est détectée, afficher :

```
Erreur de syntaxe ligne X colonne Y
```

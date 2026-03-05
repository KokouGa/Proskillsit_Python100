# Les fonctions en Python — Cours + Exercices

## Objectifs du cours
À la fin de cette série d’exercices, tu sauras :
- écrire une fonction avec `def`
- utiliser des paramètres (arguments)
- retourner une valeur avec `return`
- gérer des cas particuliers (division par zéro, liste vide, etc.)
- utiliser des fonctions avancées : closures, générateurs, récursivité, décorateurs, `lambda`, `map`, `filter`
- réaliser de petits projets structurés uniquement avec des fonctions

---

## Rappel rapide (à connaître)

### Structure d’une fonction
```python
def nom_fonction(param1, param2):
    """Courte description (docstring)."""
    # instructions
    return resultat
```

### Paramètres vs arguments
- **Paramètres** : variables dans la définition (`param1`, `param2`)
- **Arguments** : valeurs passées lors de l’appel (`nom_fonction(3, 5)`)

### `print` vs `return`
- `print()` : affiche seulement
- `return` : renvoie une valeur réutilisable dans le programme

---

# EXERCICES : LES FONCTIONS EN PYTHON

## NIVEAU 1 — DÉBUTANT

### Exercice 1.1 — Première fonction
**Objectif :** créer une fonction simple sans paramètre.  
**Consigne :** écris une fonction appelée `dire_bonjour` qui affiche `Bonjour !`

**Tests :**
- `dire_bonjour()` → `Bonjour !`

---

### Exercice 1.2 — Fonction avec paramètre
**Objectif :** créer une fonction qui utilise un paramètre.  
**Consigne :** écris une fonction `saluer` qui prend un paramètre `nom` et affiche `Bonjour, [nom] !`

**Tests :**
- `saluer("Alice")` → `Bonjour, Alice !`
- `saluer("Bob")` → `Bonjour, Bob !`

---

### Exercice 1.3 — Fonction avec retour
**Objectif :** créer une fonction qui retourne une valeur.  
**Consigne :** écris une fonction `carre` qui prend un nombre en paramètre et retourne son carré.

**Tests :**
- `carre(4)` → `16`
- `carre(2.5)` → `6.25`

---

### Exercice 1.4 — Conversion température
**Objectif :** fonction avec calcul et retour.  
**Consigne :** écris une fonction `celsius_vers_fahrenheit` qui convertit une température de Celsius vers Fahrenheit.  
Formule : `°C × 9/5 + 32 = °F`

**Tests :**
- `celsius_vers_fahrenheit(0)` → `32.0`
- `celsius_vers_fahrenheit(100)` → `212.0`
- `celsius_vers_fahrenheit(37)` → `98.6`

---

### Exercice 1.5 — Aire d'un rectangle
**Objectif :** fonction avec deux paramètres.  
**Consigne :** crée une fonction `aire_rectangle` qui prend la longueur et la largeur et retourne l’aire du rectangle.

**Tests :**
- `aire_rectangle(5, 3)` → `15`
- `aire_rectangle(10, 2)` → `20`

---

## NIVEAU 2 — INTERMÉDIAIRE

### Exercice 2.1 — Calculatrice simple
**Objectif :** fonction avec opérations conditionnelles.  
**Consigne :** crée une fonction `calculer` qui prend 3 paramètres : `a`, `b`, `operation` (string : `"+"`, `"-"`, `"*"`, `"/"`).  
La fonction doit retourner le résultat de l’opération.  
Gérer la division par zéro en retournant : `Erreur: division par zéro`.

**Tests :**
- `calculer(10, 5, "+")` → `15`
- `calculer(10, 5, "-")` → `5`
- `calculer(10, 5, "*")` → `50`
- `calculer(10, 5, "/")` → `2.0`
- `calculer(10, 0, "/")` → `Erreur: division par zéro`

---

### Exercice 2.2 — Pair ou impair
**Objectif :** fonction avec retour booléen.  
**Consigne :** écris une fonction `est_pair` qui prend un nombre en paramètre et retourne `True` s’il est pair, `False` sinon.

**Tests :**
- `est_pair(4)` → `True`
- `est_pair(7)` → `False`
- `est_pair(0)` → `True`
- `est_pair(-2)` → `True`

---

### Exercice 2.3 — Maximum de trois nombres
**Objectif :** fonction avec comparaisons.  
**Consigne :** crée une fonction `max_trois` qui prend trois nombres et retourne le plus grand **sans utiliser `max()`**.

**Tests :**
- `max_trois(5, 8, 3)` → `8`
- `max_trois(10, 10, 5)` → `10`
- `max_trois(-5, -2, -8)` → `-2`

---

### Exercice 2.4 — Validation de mot de passe
**Objectif :** fonction avec plusieurs conditions.  
**Consigne :** écris une fonction `est_mot_de_passe_fort` qui vérifie si un mot de passe est sécurisé.

**Critères :**
- au moins 8 caractères
- contient au moins une majuscule
- contient au moins un chiffre
- contient au moins un caractère spécial parmi : `!@#$%^&*`

**Tests :**
- `est_mot_de_passe_fort("abc123")` → `False`
- `est_mot_de_passe_fort("Motdepasse123")` → `False`
- `est_mot_de_passe_fort("Mot2p@ss")` → `True`
- `est_mot_de_passe_fort("MOTDEPASSE!")` → `False`

---

### Exercice 2.5 — Compteur de voyelles
**Objectif :** fonction avec boucle et comptage.  
**Consigne :** écris une fonction `compter_voyelles` qui prend une chaîne et retourne le nombre de voyelles (`a, e, i, o, u, y`) qu’elle contient.

**Tests :**
- `compter_voyelles("bonjour")` → `3`
- `compter_voyelles("Python")` → `2`
- `compter_voyelles("aeiouy")` → `6`
- `compter_voyelles("bcdfg")` → `0`

---

### Exercice 2.6 — Analyse de liste
**Objectif :** fonction avec retour multiple.  
**Consigne :** crée une fonction `analyser_liste` qui prend une liste de nombres et retourne un tuple :
1. somme des éléments
2. moyenne
3. minimum
4. maximum

Si la liste est vide, retourner `(0, 0, None, None)`.

**Tests :**
- `analyser_liste([10, 5, 8, 12, 3])` → `(38, 7.6, 3, 12)`
- `analyser_liste([])` → `(0, 0, None, None)`

---

### Exercice 2.7 — Factorielle
**Objectif :** fonction avec boucle.  
**Consigne :** écris une fonction `factorielle(n)` qui calcule `n! = n × (n-1) × ... × 1`.  
Par convention, `0! = 1`.

**Tests :**
- `factorielle(5)` → `120`
- `factorielle(0)` → `1`
- `factorielle(3)` → `6`

---

### Exercice 2.8 — Palindrome
**Objectif :** manipulation de chaînes.  
**Consigne :** crée une fonction `est_palindrome` qui vérifie si une chaîne se lit pareil dans les deux sens.  
Ignorer la casse.

**Tests :**
- `est_palindrome("radar")` → `True`
- `est_palindrome("kayak")` → `True`
- `est_palindrome("bonjour")` → `False`
- `est_palindrome("Radar")` → `True`

---

### Exercice 2.9 — Paramètres par défaut
**Objectif :** utiliser des valeurs par défaut.  
**Consigne :** écris une fonction `creer_email(prenom, nom, domaine="@gmail.com")` qui retourne l’adresse email formatée :
`prenom.nom` + `domaine`

**Tests :**
- `creer_email("john", "doe")` → `john.doe@gmail.com`
- `creer_email("jane", "smith", "@yahoo.fr")` → `jane.smith@yahoo.fr`

---

### Exercice 2.10 — Nombre premier
**Objectif :** algorithmique simple.  
**Consigne :** crée une fonction `est_premier(n)` qui vérifie si un nombre est premier (divisible seulement par 1 et lui-même).

**Tests :**
- `est_premier(7)` → `True`
- `est_premier(10)` → `False`
- `est_premier(2)` → `True`
- `est_premier(17)` → `True`

---

## NIVEAU 3 — AVANCÉ

### Exercice 3.1 — Fonction dans fonction (closure)
**Objectif :** créer une fonction qui retourne une fonction.  
**Consigne :** écris une fonction `multiplier_par(n)` qui retourne une fonction qui multiplie son paramètre par `n`.

**Tests :**
```python
fois_3 = multiplier_par(3)
fois_5 = multiplier_par(5)

fois_3(10)  # 30
fois_5(10)  # 50
fois_3(7)   # 21
```

---

### Exercice 3.2 — Générateur de nombres pairs
**Objectif :** créer une fonction génératrice avec `yield`.  
**Consigne :** écris un générateur `nombres_pairs(limite)` qui génère les nombres pairs de 0 à `limite`.

**Test :**
```python
for pair in nombres_pairs(10):
    print(pair, end=" ")
# 0 2 4 6 8 10
```

---

### Exercice 3.3 — Générateur de Fibonacci (infini)
**Objectif :** générateur pour une suite infinie.  
**Consigne :** crée `fibonacci_generator()` qui génère à l’infini : `0, 1, 1, 2, 3, 5, ...`

**Test :**
Récupérer les 10 premiers termes → `[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]`

---

### Exercice 3.4 — Fonction récursive : Fibonacci
**Objectif :** implémenter une fonction récursive.  
**Consigne :** écris `fibonacci_rec(n)` avec :
- `fib(0)=0`
- `fib(1)=1`
- `fib(n)=fib(n-1)+fib(n-2)`

**Tests :**
- `fibonacci_rec(7)` → `13`
- `fibonacci_rec(10)` → `55`
- `fibonacci_rec(0)` → `0`
- `fibonacci_rec(1)` → `1`

---

### Exercice 3.5 — Fonction récursive : somme des chiffres
**Objectif :** récursivité sur les nombres.  
**Consigne :** écris `somme_chiffres(n)` qui calcule la somme des chiffres d’un entier positif.

**Tests :**
- `somme_chiffres(1234)` → `10`
- `somme_chiffres(999)` → `27`
- `somme_chiffres(5)` → `5`
- `somme_chiffres(0)` → `0`

---

### Exercice 3.6 — Décorateur simple (chronomètre)
**Objectif :** mesurer le temps d’exécution d’une fonction.  
**Consigne :** crée un décorateur `chronometre` qui prend une fonction et retourne une nouvelle fonction affichant le temps d’exécution (module `time`).

**Test :**
Une fonction décorée avec `@chronometre` doit afficher son temps d’exécution.

---

### Exercice 3.7 — Lambda avec `map`
**Objectif :** utiliser `lambda` avec `map()`.  
**Consigne :** transformer une liste de températures Celsius en Fahrenheit.

**Test :**
`[0, 20, 37, 100]` → `[32.0, 68.0, 98.6, 212.0]`

---

### Exercice 3.8 — Lambda avec `filter`
**Objectif :** utiliser `lambda` avec `filter()`.  
**Consigne :** garder uniquement les mots de plus de 5 lettres.

**Test :**
`["Python", "est", "un", "langage", "génial", "!"]` → `["Python", "langage", "génial"]`

---

## NIVEAU 4 — PROJETS COMPLETS

### Projet 4.1 — Système de gestion d'étudiants
**Consigne :** créer un système complet avec fonctions pour gérer des notes.

**Structure de données :**
- dictionnaire : `etudiants`
- clés : noms des étudiants
- valeurs : listes de notes

**Fonctions à créer :**
- `ajouter_etudiant(etudiants, nom)` → ajoute un étudiant
- `ajouter_note(etudiants, nom, note)` → ajoute une note
- `moyenne_etudiant(etudiants, nom)` → moyenne d’un étudiant
- `moyenne_classe(etudiants)` → moyenne de la classe
- `meilleur_etudiant(etudiants)` → nom du meilleur étudiant
- `afficher_bulletin(etudiants, nom)` → affiche un bulletin formaté

**Tests à effectuer :**
1. ajouter les étudiants `Alice`, `Bob`, `Charlie`
2. ajouter des notes variées
3. calculer les moyennes individuelles
4. calculer la moyenne de classe
5. identifier le meilleur étudiant
6. afficher un bulletin

---

### Projet 4.2 — Mini-jeu de devinette
**Consigne :** créer un jeu de devinette (1 à 100) avec fonctions.

**Fonctions à créer :**
- `choisir_nombre()` → nombre aléatoire entre 1 et 100
- `comparer(proposition, secret)` → retourne `"trop grand"`, `"trop petit"` ou `"gagné"`
- `jouer()` → fonction principale :
  - choisit un nombre secret
  - demande des propositions à l’utilisateur
  - donne des indices
  - compte les tentatives
  - affiche un message final

---

### Projet 4.3 — Générateur de mots de passe
**Consigne :** créer une fonction `generer_mdp` qui génère un mot de passe aléatoire.

**Paramètres (optionnels) :**
- `longueur` (défaut : `12`)
- `avec_majuscules` (défaut : `True`)
- `avec_chiffres` (défaut : `True`)
- `avec_speciaux` (défaut : `True`)

**Contraintes :**
- si `avec_majuscules=True`, inclure des lettres A–Z
- si `avec_chiffres=True`, inclure des chiffres 0–9
- si `avec_speciaux=True`, inclure des caractères spéciaux (ex : `!@#$%^&*`)
- le mot de passe final doit avoir exactement `longueur` caractères

**Tests :**
- `generer_mdp()` → chaîne de 12 caractères
- `generer_mdp(8, False, True, False)` → 8 caractères, minuscules + chiffres uniquement
- `generer_mdp(16, True, True, True)` → 16 caractères avec mélange complet

---

## Conseils pour réussir
- commence par écrire les tests (même “à la main”)
- fais simple, puis améliore
- teste les cas limites : `0`, négatifs, chaîne vide, liste vide, division par zéro
- garde des fonctions courtes : une fonction = une responsabilité


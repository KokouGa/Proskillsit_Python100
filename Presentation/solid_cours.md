# SOLID (niveau fonctions) — Cours débutant

## Objectif
Comprendre les principes SOLID sans classes, uniquement avec des fonctions.  
But : écrire un code plus lisible, plus testable et plus facile à modifier.

---

## Définition rapide
SOLID = 5 principes de conception :

- S : Single Responsibility (une fonction = une responsabilité)
- O : Open/Closed (ajouter sans casser / sans modifier partout)
- L : Liskov Substitution (même contrat d’entrée/sortie)
- I : Interface Segregation (petites fonctions ciblées)
- D : Dependency Inversion (dépendre d’abstractions, injecter les dépendances)

---

# S — Single Responsibility Principle (SRP)
## Idée
Une fonction doit faire une seule tâche.

### Mauvais exemple
```python
def traiter_commande(cmd):
    total = sum(cmd["items"])
    print("Total:", total)
    with open("log.txt", "a") as f:
        f.write(str(total) + "\n")
```

### Bon exemple (séparation)
```python
def calculer_total(cmd):
    return sum(cmd["items"])

def afficher_total(total):
    print("Total:", total)

def sauvegarder_total(total, fichier):
    with open(fichier, "a", encoding="utf-8") as f:
        f.write(str(total) + "\n")
```

Avantage : on peut changer l’affichage ou la sauvegarde sans toucher au calcul.

---

# O — Open/Closed Principle (OCP)
## Idée
Le code doit être ouvert à l’extension, mais fermé à la modification.

### Exemple
On veut plusieurs stratégies de calcul, sans changer la logique principale.

```python
def total_simple(items):
    return sum(items)

def total_avec_taxe(items, taxe):
    return sum(items) * (1 + taxe)

def calculer(items, methode):
    # methode est une fonction passée en paramètre
    return methode(items)
```

Avantage : on ajoute une nouvelle méthode (promo, remise, etc.) sans modifier `calculer`.

---

# L — Liskov Substitution Principle (LSP)
## Idée (niveau fonctions)
Si une fonction remplace une autre, elle doit respecter le même contrat :
- mêmes types d’entrées attendus
- même type de sortie
- même sens (ne pas surprendre)

### Exemple OK
```python
def calcul_a(items):
    return sum(items)

def calcul_b(items):
    return sum(items) + 10
```

### Exemple pas OK
```python
def calcul_c(items):
    return "total=" + str(sum(items))
```

---

# I — Interface Segregation Principle (ISP)
## Idée
Au lieu d’avoir une grosse fonction avec trop d’options/paramètres, créer des fonctions plus petites et ciblées.

### Mauvais exemple
```python
def creer_user(nom, prenom, age, email, tel, adresse, pays, ville):
    ...
```

### Bon exemple
```python
def creer_identite(nom, prenom):
    return {"nom": nom, "prenom": prenom}

def ajouter_contact(user, email=None, tel=None):
    user["email"] = email
    user["tel"] = tel
    return user
```

Avantage : plus simple à comprendre et plus facile à tester.

---

# D — Dependency Inversion Principle (DIP)
## Idée simple
Ne pas “coller” ta logique métier à un détail technique (fichier, console, DB).  
Au lieu de ça, tu passes ce détail comme dépendance (injection).

## Mauvais : dépendance fixée (fichier imposé)
```python
def log_message(msg):
    with open("log.txt", "a") as f:
        f.write(msg + "\n")
```

## Bon : injection (writer en paramètre)
```python
def log_message(msg, writer):
    writer(msg)

def writer_console(msg):
    print(msg)

def writer_fichier(msg):
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(msg + "\n")
```

### Utilisation
```python
log_message("Erreur réseau", writer_console)
log_message("Erreur réseau", writer_fichier)
```

## Exemple concret (incident)
```python
def diagnostiquer_dns(logger):
    logger("Test DNS en cours...")
    # ... tests ...
    logger("DNS OK")
```

```python
diagnostiquer_dns(writer_console)
diagnostiquer_dns(writer_fichier)
```

Avantage : ta logique ne change pas, tu changes seulement la manière de logger.

---

# Exercices (niveau débutant)

## Exercice 1 — SRP
On te donne une fonction qui fait trop de choses. Sépare-la en 3 fonctions.

```python
def envoyer_argent(numero, montant):
    print("Envoi vers", numero)
    if montant <= 0:
        print("Montant invalide")
        return
    print("Transaction OK")
```

À créer :
- `valider_numero(numero)`
- `valider_montant(montant)`
- `afficher_resultat(message)`

---

## Exercice 2 — DIP
Ajoute un paramètre `logger` à la fonction pour pouvoir choisir :
- console
- fichier

---

## Exercice 3 — Contrat (LSP)
Écris deux fonctions de calcul `calcul_total_v1(items)` et `calcul_total_v2(items)` qui respectent le même contrat :
- entrée : liste de nombres
- sortie : nombre

---

# Résumé final (à mémoriser)
- S : une fonction = une tâche
- O : on ajoute sans modifier partout
- L : une alternative doit garder le même contrat
- I : mieux vaut plusieurs petites fonctions
- D : on injecte les dépendances (console/fichier/DB)

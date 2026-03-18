# TP — Analyse de logs serveur web

## Objectif

Développer un programme Python capable de :

- lire un fichier de logs serveur  
- analyser les requêtes HTTP  
- calculer des statistiques  
- détecter des comportements anormaux  
- proposer une utilisation via un menu interactif  

---

## Données

Vous disposez d’un fichier nommé `logs.txt`.

Chaque ligne du fichier correspond à une requête effectuée sur un serveur web.

### Exemple

```
2026-03-01 10:15:23 | 192.168.1.10 | GET | /index.html | 200 | 120ms
```

---

## Structure d’une ligne

Chaque ligne contient les informations suivantes :

```
Date Heure | Adresse IP | Méthode | URL | Code HTTP | Temps
```

### Description des champs

- Date Heure : moment où la requête a été effectuée  
- Adresse IP : identifiant de l’utilisateur  
- Méthode :
  - GET : consultation d’une page  
  - POST : envoi de données (ex : connexion)  
- URL : ressource demandée  
- Code HTTP :
  - 200 : succès  
  - 404 : page non trouvée  
  - 500 : erreur serveur  
- Temps : durée de réponse (en millisecondes)  

---

## Travail demandé

### Partie 1 — Lecture et traitement

Le programme doit :

1. Lire le fichier ligne par ligne  
2. Séparer les informations avec `split("|")`  
3. Nettoyer les espaces avec `strip()`  
4. Stocker les données dans une structure adaptée (liste de dictionnaires)  

---

### Partie 2 — Statistiques

Calculer et afficher :

- le nombre total de requêtes  
- le nombre de requêtes GET  
- le nombre de requêtes POST  
- le nombre d’erreurs (codes 404 et 500)  
- le temps moyen de réponse  

---

### Partie 3 — Analyse de sécurité

Le programme doit :

- identifier les adresses IP suspectes  
  - une IP est suspecte si elle génère plusieurs erreurs  
- compter le nombre de tentatives de connexion  
  - requêtes de type POST sur `/login`  

---

### Partie 4 — Analyse avancée

Déterminer :

- l’URL la plus demandée  
- la requête la plus lente  

---

### Partie 5 — Menu interactif

Le programme doit proposer un menu permettant de choisir une action :

```
1. Afficher les statistiques
2. Analyse de sécurité
3. Analyse avancée
4. Générer un rapport
5. Quitter
```

Le programme doit rester actif jusqu’au choix de quitter.

---

### Partie 6 — Génération de rapport

Le programme doit :

- créer un fichier `rapport.txt`  
- écrire dans ce fichier :
  - les statistiques  
  - les résultats de l’analyse de sécurité  
  - les résultats de l’analyse avancée  

---

## Contraintes

- utiliser uniquement Python standard  
- ne pas utiliser de bibliothèques externes  
- gérer les erreurs possibles dans le fichier  
- structurer le code avec des fonctions  

# TP — Analyse de logs serveur web à partir de plusieurs fichiers CSV

## Objectif

Développer un programme Python capable de :

- parcourir un dossier contenant plusieurs fichiers de logs CSV
- lire et nettoyer les données de chaque fichier
- fusionner toutes les données valides
- analyser les requêtes HTTP
- calculer des statistiques globales
- détecter des comportements anormaux
- proposer une utilisation via un menu interactif
- générer un rapport final
- exporter les lignes invalides dans un fichier séparé

---

## Contexte

Dans un environnement réel, les logs d’un serveur web ne sont pas toujours stockés dans un seul fichier propre.  
Ils peuvent être répartis dans plusieurs fichiers, contenir des lignes invalides, des formats irréguliers, ou des données incomplètes.

Dans ce TP, vous devez construire un programme Python capable de lire **tous les fichiers CSV** présents dans un dossier, de traiter les données valides, d’ignorer les lignes corrompues, puis de produire une analyse globale.

---

## Organisation des données

Les fichiers de logs seront placés dans un dossier nommé :

```text
log_data/
```

### Exemple d’arborescence

```text
projet_logs/
│
├── main.py
├── rapport.txt
├── lignes_invalides.txt
├── log_data/
│   ├── fichier_a.csv
│   ├── fichier_b.csv
│   ├── fichier_c.csv
│   └── ...
```

### Important

Les noms des fichiers présents dans `log_data/` ne sont **pas imposés**.

Le programme doit :

- parcourir automatiquement le dossier `log_data/`
- détecter tous les fichiers ayant l’extension `.csv`
- lire et traiter **tous** les fichiers CSV trouvés dans ce dossier

Autrement dit, le programme ne doit pas dépendre de noms précis de fichiers. Il doit fonctionner avec **n’importe quels fichiers CSV** placés dans `log_data/`.

---

## Données

Vous disposez de plusieurs fichiers CSV contenant des logs serveur web.

Chaque ligne valide correspond à une requête effectuée sur un serveur web.

### Exemple de ligne valide

```text
2026-03-01 10:15:23 | 192.168.1.10 | GET | /index.html | 200 | 120ms
```

---

## Structure d’une ligne

Chaque ligne contient les informations suivantes :

```text
Date Heure | Adresse IP | Méthode | URL | Code HTTP | Temps
```

---

## Description des champs

**Date Heure** : moment où la requête a été effectuée  
**Adresse IP** : identifiant du client  
**Méthode** :

- `GET` : consultation d’une ressource
- `POST` : envoi de données, par exemple une connexion

**URL** : ressource demandée  
**Code HTTP** :

- `200` : succès
- `404` : page non trouvée
- `500` : erreur serveur

**Temps** : durée de réponse en millisecondes

---

## Particularité importante

Les fichiers peuvent être **sales** ou **partiellement corrompus**.

Votre programme doit donc gérer des impuretés comme par exemple :

- lignes vides
- espaces inutiles
- lignes incomplètes
- lignes avec trop de colonnes
- lignes avec mauvais séparateur
- code HTTP invalide
- temps invalide
- méthode invalide
- texte parasite
- commentaires éventuels

Le programme **ne doit pas s’arrêter brutalement** lorsqu’une ligne est incorrecte.  
Il doit lire tout ce qui est exploitable, ignorer les lignes invalides, et continuer le traitement.

---

# Travail demandé

## Partie 1 — Lecture du dossier et chargement des fichiers

Le programme doit :

- accéder au dossier `log_data/`
- repérer tous les fichiers ayant l’extension `.csv`
- lire chaque fichier ligne par ligne
- traiter les données de tous les fichiers
- regrouper toutes les lignes valides dans une structure commune

### À faire

- utiliser `os.listdir()` ou une autre solution standard Python
- vérifier qu’un fichier est bien un fichier `.csv`
- ouvrir chaque fichier avec `open(..., encoding="utf-8")`
- lire son contenu ligne par ligne

---

## Partie 2 — Nettoyage et validation des lignes

Pour chaque ligne lue, le programme doit :

- supprimer les espaces inutiles avec `strip()`
- séparer les champs avec `split("|")`
- vérifier que la ligne contient bien 6 champs
- convertir le code HTTP en entier
- extraire le temps en millisecondes
- stocker uniquement les lignes valides
- enregistrer les lignes invalides séparément

Les données valides doivent être stockées dans une structure adaptée, par exemple une **liste de dictionnaires**.

### Exemple de structure possible

```python
{
    "date": "2026-03-01 10:15:23",
    "ip": "192.168.1.10",
    "methode": "GET",
    "url": "/index.html",
    "code": 200,
    "temps": 120,
    "fichier": "fichier_a.csv"
}
```

L’ajout du champ `fichier` permet de savoir de quel fichier provient la ligne.

---

## Partie 3 — Statistiques globales

Le programme doit calculer et afficher, sur l’ensemble des fichiers valides :

- le nombre total de requêtes
- le nombre de requêtes `GET`
- le nombre de requêtes `POST`
- le nombre d’erreurs HTTP (`404` et `500`)
- le temps moyen de réponse
- le **nombre de requêtes par code HTTP**

### Exemple attendu

- 200 : 1540 requêtes
- 404 : 233 requêtes
- 500 : 112 requêtes
- 503 : 45 requêtes

---

## Partie 4 — Analyse de sécurité

Le programme doit :

- identifier les adresses IP suspectes
- considérer qu’une IP est suspecte si elle produit plusieurs erreurs
- compter le nombre de tentatives de connexion
- une tentative de connexion correspond à une requête `POST` sur `/login`
- afficher les **3 IP les plus actives**

### Les 3 IP les plus actives

Le programme doit compter le nombre total de requêtes envoyées par chaque IP et afficher les 3 adresses IP ayant effectué le plus de requêtes.

### Exemple attendu

- 192.168.1.10 : 321 requêtes
- 192.168.1.11 : 280 requêtes
- 10.0.0.5 : 245 requêtes

---

## Partie 5 — Analyse avancée

Le programme doit déterminer :

- l’URL la plus demandée
- les **5 URLs les plus demandées**
- la requête la plus lente
- le fichier contenant le plus de lignes valides
- le nombre de lignes invalides ignorées
- le nombre total de fichiers traités

### Top 5 des URLs les plus demandées

Le programme doit classer les URLs par fréquence et afficher les 5 plus demandées.

### Exemple attendu

1. `/index.html` : 520 requêtes  
2. `/login` : 410 requêtes  
3. `/dashboard` : 389 requêtes  
4. `/profile` : 305 requêtes  
5. `/settings` : 210 requêtes  

---

## Partie 6 — Analyse par fichier

En plus de l’analyse globale, le programme doit être capable de donner quelques informations **par fichier** :

- nombre de lignes lues
- nombre de lignes valides
- nombre de lignes invalides
- nombre d’erreurs HTTP
- temps moyen de réponse du fichier

Cette partie permet de voir quels fichiers sont les plus propres ou les plus problématiques.

---

## Partie 7 — Export des lignes invalides

Le programme doit créer un fichier séparé nommé :

```text
lignes_invalides.txt
```

Ce fichier doit contenir toutes les lignes rejetées pendant le traitement, avec au minimum :

- le nom du fichier source
- le numéro de ligne
- le contenu de la ligne
- la raison du rejet

### Exemple attendu

```text
Fichier : fichier_b.csv
Ligne   : 15
Raison  : nombre de colonnes incorrect
Contenu : 2026-03-01 10:01:20 ; 192.168.1.17 ; GET ; /profile ; 404 ; 90ms
```

---

## Partie 8 — Menu interactif

Le programme doit proposer un menu permettant à l’utilisateur de choisir une action.

### Exemple de menu

1. Afficher les statistiques globales  
2. Afficher l’analyse de sécurité  
3. Afficher l’analyse avancée  
4. Afficher le résumé par fichier  
5. Générer un rapport  
6. Exporter les lignes invalides  
7. Quitter  

Le programme doit rester actif jusqu’au choix de quitter.

---

## Partie 9 — Génération d’un rapport

Le programme doit créer un fichier nommé :

```text
rapport.txt
```

Ce fichier doit contenir :

- le nombre de fichiers analysés
- le nombre total de lignes lues
- le nombre total de lignes valides
- le nombre total de lignes invalides
- les statistiques globales
- le nombre de requêtes par code HTTP
- les résultats de l’analyse de sécurité
- les 3 IP les plus actives
- les résultats de l’analyse avancée
- le top 5 des URLs les plus demandées
- un résumé par fichier

---

# Contraintes

Le programme doit respecter les contraintes suivantes :

- utiliser uniquement **Python standard**
- ne pas utiliser de bibliothèques externes
- utiliser des fonctions
- gérer les erreurs de lecture de fichiers
- gérer les lignes invalides sans bloquer le programme
- écrire un code clair, structuré et réutilisable

---

## Organisation du code

Vous êtes libres d’organiser votre programme comme vous le souhaitez, à condition que le code reste :

- clair
- structuré
- lisible
- découpé en fonctions

### Remarque

Les fonctions à utiliser ne sont **pas imposées**.  
Vous pouvez choisir vos propres noms de fonctions et votre propre découpage du programme.

### Exemples de fonctions possibles

Voici quelques exemples de fonctions que vous pourriez créer :

- `lire_dossier_logs(nom_dossier)`
- `lire_fichier_log(chemin_fichier)`
- `valider_ligne(ligne, nom_fichier, numero_ligne)`
- `afficher_statistiques(logs)`
- `compter_requetes_par_code(logs)`
- `analyse_securite(logs)`
- `top_3_ip_actives(logs)`
- `analyse_avancee(logs)`
- `top_5_urls(logs)`
- `resume_par_fichier(logs, invalides_par_fichier)`
- `exporter_lignes_invalides(lignes_invalides)`
- `generer_rapport(...)`
- `menu()`
- `main()`

Ces fonctions sont seulement données à titre d’exemple pour vous aider à structurer votre travail.

---

# Résultat attendu

À la fin, votre projet doit être un **mini analyseur robuste de logs serveur** capable de :

- parcourir un dossier complet
- lire plusieurs fichiers
- tolérer des données sales
- fusionner les données
- faire des statistiques globales
- afficher le nombre de requêtes par code HTTP
- détecter des anomalies
- afficher les 3 IP les plus actives
- afficher le top 5 des URLs les plus demandées
- exporter les lignes invalides
- produire un rapport exploitable

---

# Éléments obligatoires

Les éléments suivants font partie intégrante du TP et doivent obligatoirement être implémentés :

- lecture de tous les fichiers CSV d’un dossier
- fusion des lignes valides
- gestion des lignes invalides
- menu interactif
- génération de `rapport.txt`
- export de `lignes_invalides.txt`
- détection des IP suspectes
- détection des **3 IP les plus actives**
- affichage du **top 5 des URLs les plus demandées**
- affichage du **nombre de requêtes par code HTTP**

---

# Sujet résumé

Écrire un programme Python qui parcourt un dossier `log_data/`, lit tous les fichiers CSV de logs, nettoie les données, ignore les lignes invalides, fusionne les lignes valides, calcule des statistiques globales, affiche les requêtes par code HTTP, détecte les comportements suspects, affiche les 3 IP les plus actives, affiche le top 5 des URLs les plus demandées, exporte les lignes invalides dans un fichier séparé, propose un menu interactif et génère un fichier `rapport.txt`.

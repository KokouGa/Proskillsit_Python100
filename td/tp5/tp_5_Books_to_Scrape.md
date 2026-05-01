# TP Python – Web Scraping avec Books to Scrape

## Titre
**Extraction, analyse approfondie et visualisation de données de livres avec Python et Tkinter**

---

## 1. Contexte

Vous avez déjà pratiqué le web scraping. Ce TP va plus loin sur deux aspects :
- la **richesse des analyses** produites à partir des données collectées ;
- la **qualité de l'interface graphique** proposée à l'utilisateur.

Vous allez développer une application Python complète permettant de scraper le site **Books to Scrape**, d'effectuer des calculs statistiques poussés sur les données, et de les présenter dans une interface Tkinter claire et bien organisée.

---

## 2. Site à utiliser

```
https://books.toscrape.com/index.html
```

---

## 3. Données à extraire

Pour chaque livre, extraire les informations suivantes :

| Champ | Source | Remarque |
|---|---|---|
| Titre | Page catalogue | |
| Prix | Page catalogue | Stocker comme `float` (enlever le `£`) |
| Disponibilité | Page catalogue | Stocker comme `"In stock"` ou `"Out of stock"` |
| Note | Page catalogue | Convertir en entier : `One`→1, `Two`→2, etc. |
| URL de la page détail | Page catalogue | |
| Catégorie | Page catalogue ou détail | |
| Description | Page détail | |
| UPC | Page détail | Code produit unique |
| Nombre d'avis | Page détail | Stocker comme `int` |

> La note est encodée en texte dans le HTML (`class="star-rating Three"`). Vous devez la convertir en entier.

---

## 4. Partie 1 — Exploration du site

Avant de commencer le développement, observez la structure du site et identifiez :

- la page d'accueil et les catégories disponibles dans le menu latéral ;
- les informations visibles sur chaque livre dans la page catalogue ;
- le lien vers la page suivante (pagination) ;
- le lien vers la page détail d'un livre ;
- comment est indiquée la catégorie dans la page détail (fil d'Ariane).

---

## 5. Partie 2 — Extraction et navigation

### 5.1 Navigation

Le programme doit pouvoir :

- parcourir les **N premières pages** du catalogue général (N saisi par l'utilisateur) ;
- **ou** parcourir **toutes les pages d'une catégorie** choisie par l'utilisateur.

### 5.2 Récupération des catégories

Au lancement de l'application, le programme doit automatiquement récupérer la liste de toutes les catégories depuis la page d'accueil (menu latéral gauche) pour les proposer dans un menu déroulant.

### 5.3 Données manquantes

Si la page détail d'un livre est inaccessible, le livre est quand même conservé avec les données de la page catalogue. Les champs manquants (description, UPC, nb avis) sont mis à `None`.

---

## 6. Partie 3 — Sauvegarde des données

Les données collectées doivent être enregistrées dans les deux formats suivants :

### CSV

Un fichier `books.csv` avec une ligne par livre et les colonnes :
`titre, prix, disponibilite, note, categorie, upc, nb_avis, description, url`

### JSON

Un fichier `books.json` structuré **par catégorie** :

```json
{
  "meta": {
    "total_livres": 142,
    "categories_presentes": 12,
    "date_export": "2025-01-15 14:32:00"
  },
  "categories": {
    "Mystery": [
      {
        "titre": "Sharp Objects",
        "prix": 9.99,
        "note": 4,
        "disponibilite": "In stock"
      }
    ]
  }
}
```

---

## 7. Partie 4 — Analyses et calculs

C'est la partie centrale du TP. À partir des données collectées, le programme doit calculer et afficher les résultats suivants.

### 7.1 Statistiques globales

- Nombre total de livres extraits
- Nombre de livres disponibles et indisponibles
- Pourcentage de livres disponibles (arrondi à 1 décimale)
- Prix minimum, maximum et moyen (arrondi à 2 décimales)
- **Prix médian** des livres
- **Écart-type** des prix (sans utiliser de librairie externe — calculer manuellement)
- Note moyenne globale (arrondie à 1 décimale)
- Nombre total d'avis sur l'ensemble des livres

### 7.2 Analyses par note

Pour chaque note de 1 à 5 :
- Nombre de livres ayant cette note
- Pourcentage de livres ayant cette note
- Prix moyen des livres ayant cette note
- Livre le moins cher et le plus cher pour cette note

### 7.3 Analyses par catégorie

Pour chaque catégorie présente dans les données :
- Nombre de livres
- Prix moyen, min, max
- Note moyenne
- Livre le moins cher de la catégorie
- Livre le plus cher de la catégorie
- Nombre de livres disponibles dans la catégorie

Puis, en synthèse :
- Catégorie avec le plus de livres
- Catégorie avec le moins de livres
- Catégorie dont le prix moyen est le plus élevé
- Catégorie dont le prix moyen est le plus bas
- Catégorie avec la meilleure note moyenne
- Catégorie avec le plus de livres indisponibles

### 7.4 Classements

- Les **10 livres les moins chers** disponibles
- Les **10 livres les plus chers**
- Les **10 livres les mieux notés** (en cas d'égalité de note, trier par prix croissant)
- Les **10 livres les moins bien notés**
- Les **10 livres avec le plus d'avis**

### 7.5 Analyses de prix

- Répartition des livres par **tranche de prix** :
  - Moins de 10£
  - De 10£ à 20£
  - De 20£ à 30£
  - De 30£ à 40£
  - Plus de 40£
- Pour chaque tranche : nombre de livres et pourcentage
- **Rapport qualité/prix** : pour chaque livre, calculer `note / prix`. Afficher le top 5 des meilleurs rapports.

### 7.6 Recherche par mot-clé

L'utilisateur peut saisir un mot-clé. Le programme affiche :
- Tous les livres dont le **titre** contient ce mot-clé (insensible à la casse)
- Tous les livres dont la **description** contient ce mot-clé (si disponible)
- Le nombre de résultats trouvés pour chaque type de recherche

### 7.7 Calculs à implémenter manuellement

Les fonctions suivantes doivent être codées **sans librairie externe** (pas de `statistics`, pas de `numpy`) :

```python
def calculer_moyenne(valeurs):
    ...

def calculer_mediane(valeurs):
    ...

def calculer_ecart_type(valeurs):
    ...

def calculer_mode(valeurs):
    # Retourne la valeur la plus fréquente
    ...
```

> **Challenge :** La médiane nécessite de trier la liste et de traiter différemment les cas pair et impair.
> L'écart-type se calcule avec : `sqrt( somme( (xi - moyenne)² ) / n )`

---

## 8. Partie 5 — Interface graphique Tkinter

L'interface doit être organisée en **trois zones principales**.

### 8.1 Zone de contrôle (haut)

| Élément | Description |
|---|---|
| Champ "Nombre de pages" | Entier, validé (refuser les valeurs non numériques) |
| Menu déroulant "Catégorie" | "Toutes" + liste des catégories (chargée au lancement) |
| Bouton **Lancer le scraping** | Lance le scraping et désactive les boutons pendant l'opération |
| Bouton **Exporter CSV** | Actif seulement si des données ont été scrapées |
| Bouton **Exporter JSON** | Actif seulement si des données ont été scrapées |
| Bouton **Réinitialiser** | Efface les données en mémoire et réinitialise l'affichage |
| Bouton **Quitter** | Ferme l'application |

### 8.2 Zone de résultats (milieu)

Un tableau (`ttk.Treeview`) affichant les livres avec les colonnes :
- Titre (tronqué à 40 caractères si trop long)
- Catégorie
- Prix
- Note (affichée avec des étoiles : ★★★☆☆)
- Disponibilité

**Fonctionnalités du tableau :**
- **Tri** : cliquer sur un en-tête de colonne trie le tableau selon cette colonne (cliquer deux fois inverse l'ordre)
- **Filtre rapide** : un champ de texte au-dessus du tableau filtre les livres par titre en temps réel (à chaque touche)
- **Double-clic** sur un livre : ouvre une fenêtre popup affichant toutes ses informations (titre, prix, note, description, UPC, nb avis, URL)

### 8.3 Zone d'analyse (bas ou onglet séparé)

Un widget `ttk.Notebook` avec les onglets suivants :

**Onglet "Statistiques globales"**
Afficher sous forme de texte formaté toutes les statistiques de la section 7.1.

**Onglet "Par catégorie"**
Un menu déroulant permet de choisir une catégorie et d'afficher ses statistiques détaillées (section 7.3).

**Onglet "Classements"**
Afficher les classements de la section 7.4 avec un menu pour choisir lequel afficher.

**Onglet "Recherche"**
Un champ de saisie + bouton Rechercher + zone d'affichage des résultats (section 7.6).

---

## 9. Contraintes techniques

| Contrainte | Détail |
|---|---|
| Langage | Python 3.x |
| Bibliothèques autorisées | `requests`, `beautifulsoup4`, `tkinter` |
| Stockage | Fichiers CSV et JSON uniquement |
| Calculs | Moyenne, médiane, écart-type codés manuellement |
| Validation | Les champs de saisie doivent être validés avant toute action |

---

## 10. Organisation du projet

```text
tp_books_scraper/
│
├── main.py          ← lancement de l'application
├── scraper.py       ← requêtes HTTP et pagination
├── parser.py        ← extraction HTML avec BeautifulSoup
├── analysis.py      ← tous les calculs et statistiques
├── gui.py           ← interface graphique Tkinter
├── utils.py         ← fonctions utilitaires (conversion note, nettoyage prix...)
├── books.csv        ← généré par l'application
├── books.json       ← généré par l'application
└── README.md
```

**Règle importante :** aucune logique de scraping ou de calcul ne doit se trouver dans `gui.py`. L'interface appelle les fonctions des autres modules, elle ne les remplace pas.

---

## 11. Consignes de réalisation

Le code doit :

- utiliser des **fonctions** (pas de code à plat) ;
- avoir des **noms de variables explicites** ;
- contenir des **commentaires** sur les parties complexes ;
- **valider les entrées** utilisateur (pages = entier positif, etc.) ;
- **gérer les erreurs** réseau avec un message clair dans l'interface ;
- séparer proprement scraping, analyse et interface.

---

## 12. Conseils pour réussir

1. Commencer par scraper **une seule page** et afficher les données dans le terminal
2. Vérifier que l'extraction est correcte avant d'ajouter la pagination
3. Coder et tester les fonctions d'analyse **séparément** dans un petit script de test
4. Construire l'interface **progressivement** : d'abord la zone de contrôle, puis le tableau, puis les onglets
5. Tester chaque fonctionnalité indépendamment avant de tout relier

---

## 13. Livrables attendus

- Le code source complet
- Un fichier `books.csv` et `books.json` générés
- Un `README.md` expliquant comment lancer le programme
- Une capture d'écran de l'interface avec des données affichées

---

## 14. Résumé rapide

Scraper **Books to Scrape**, extraire titre, prix, dispo, note, catégorie, description, UPC, nb avis.
Calculer : moyenne, médiane, écart-type des prix ; analyses par note et par catégorie ; classements ; rapport qualité/prix.
Interface Tkinter avec tableau triable et filtrable, onglets d'analyse, recherche par mot-clé, exports CSV et JSON.

# TP Python --- Gestion des Transactions Clients 

## Objectif du TP

Créer un programme Python capable de :

-   Lire plusieurs fichiers de données (CSV et JSON)
-   Associer les informations entre fichiers
-   Traiter des transactions contenant plusieurs articles
-   Calculer des montants financiers (sous-total, remise, taxes, total)
-   Produire des statistiques globales
-   Répondre à des questions analytiques
-   Proposer un menu interactif

------------------------------------------------------------------------

## Fichiers fournis

### 1. clients.csv

    id_client,nom,adresse,ville
    1,Jean Dupont,123 rue A,Montreal
    2,Marie Martin,456 rue B,Quebec
    3,Paul Durand,789 rue C,Laval

### 2. articles.json

``` json
[
    {"id": 101, "nom": "Stylo", "prix": 2.5},
    {"id": 102, "nom": "Cahier", "prix": 5.0},
    {"id": 103, "nom": "Sac", "prix": 25.0}
]
```

### 3. achats.csv

    id_transaction,date,id_client,articles,remise,methode_paiement,statut
    T001,2026-01-10,1,"101:3;102:2",0,Carte,complete
    T002,2026-01-11,2,"103:1",10,Especes,complete
    T003,2026-01-11,1,"101:5;103:1",5,Carte,complete
    T004,2026-01-12,3,"102:10",0,Virement,annule
    T005,2026-01-15,2,"101:2;102:1",0,Carte,complete
    T006,2026-01-16,1,"103:2",15,Carte,complete

------------------------------------------------------------------------

## IMPORTANT --- Tests supplémentaires

Les étudiants doivent créer et utiliser d'autres fichiers de test
(clients, articles, achats) pour vérifier que leur programme fonctionne
correctement dans différents cas.

Ils ne doivent pas modifier les fichiers fournis, mais peuvent créer : -
clients_test.csv - articles_test.json - achats_test.csv

------------------------------------------------------------------------

## Explication de la colonne articles

Format général :

    id_article:quantite;id_article:quantite

Exemple :

    101:3;102:2

Signifie : - Article 101 → quantité 3 - Article 102 → quantité 2

⚠️ Une transaction peut contenir un seul article. ⚠️ Les espaces
éventuels doivent être ignorés.

------------------------------------------------------------------------

## Convention de calcul (IMPORTANT)

Dans ce TP :

-   Les taxes sont calculées AVANT la remise.
-   Toutes les valeurs monétaires doivent être arrondies à 2 décimales.
-   Seules les transactions avec statut = "complete" sont considérées
    valides.

------------------------------------------------------------------------

## Formules à utiliser

Sous-total :

    sous_total = somme(quantite × prix)

Remise :

    montant_remise = sous_total * (remise / 100)

Taxes :

    taxes = sous_total * 0.15

Total final :

    total = sous_total - montant_remise + taxes

------------------------------------------------------------------------

# Travail demandé

## Partie 1 --- Chargement des données

Créer des fonctions :

-   charger_clients()
-   charger_articles()
-   charger_achats()

Stocker les données dans des structures adaptées (listes et
dictionnaires).

------------------------------------------------------------------------

## Partie 2 --- Affichage des transactions valides

Afficher pour chaque transaction valide :

-   ID transaction
-   Date
-   Nom du client
-   Ville
-   Liste détaillée des articles (nom, quantité, prix, total ligne)
-   Sous-total
-   Remise (%)
-   Taxes (15 %)
-   Total final

Les montants doivent être arrondis à 2 décimales.

------------------------------------------------------------------------

## Partie 3 --- Statistiques globales

Le menu doit permettre d'afficher :

-   Total global des ventes
-   Nombre de transactions valides
-   Montant dépensé par chaque client
-   Client ayant dépensé le plus (Client VIP)
-   Article le plus vendu (quantité totale)
-   Article ayant généré le plus de revenu (quantité × prix, sans
    répartir la remise)

------------------------------------------------------------------------

## Partie 4 --- Analyse avancée

Le programme doit permettre de répondre aux questions suivantes :

-   Quel client a effectué le plus de transactions ?
-   Quelle est la transaction la plus chère ?
-   Filtrer les transactions par méthode de paiement
-   Trier les transactions par date

------------------------------------------------------------------------

## Structure recommandée

Fonctions suggérées :

-   parser_articles(chaine)
-   calculer_totaux(transaction)
-   afficher_transaction(transaction)
-   afficher_statistiques()
-   menu()

------------------------------------------------------------------------

## Contraintes

-   Utiliser des fonctions
-   Commenter le code
-   Respecter l'indentation Python
-   Ne pas modifier les fichiers fournis

------------------------------------------------------------------------

## Bonus (Optionnel)

Choisir au moins une option :

-   Générer un fichier rapport.txt
-   Exporter un fichier rapport.csv
-   Implémenter la solution en Programmation Orientée Objet
-   ne pas utiliser pandas et autres 


------------------------------------------------------------------------

## Compétences développées

-   Lecture et traitement CSV / JSON
-   Parsing de chaînes complexes
-   Calculs financiers
-   Analyse statistique
-   Organisation d'un programme structuré
-   Conception d'un menu interactif

# COURS — Introduction aux requêtes HTTP (pour comprendre les logs)

## 1. Qu’est-ce que HTTP ?

HTTP (HyperText Transfer Protocol) est le protocole utilisé pour communiquer sur le web.

Quand tu ouvres un site web :
- ton navigateur envoie une requête
- le serveur répond

Exemple :
Tu ouvres un site → une requête est envoyée au serveur

---

## 2. Structure d’un échange HTTP

Il y a toujours 2 parties :

### 1. La requête (client → serveur)
### 2. La réponse (serveur → client)

---

## 3. Les méthodes HTTP (très important)

Dans les logs, tu vas souvent voir :

### GET
- Sert à demander une page
- Ne modifie rien

Exemple :
GET /index.html

---

### POST
- Sert à envoyer des données

Exemple :
POST /login

---

## 4. Les codes HTTP (réponse du serveur)

Le serveur répond avec un code :

### 200 — Succès
Tout fonctionne bien

### 404 — Not Found
Page introuvable

### 500 — Erreur serveur
Problème côté serveur

---

## 5. Exemple simple

Requête :
GET /index.html

Réponse :
200

---

## 6. Structure d’un log serveur

Un log est une ligne qui enregistre une requête :

2026-03-01 10:15:23 | 192.168.1.10 | GET | /index.html | 200 | 120ms

---

## 7. Explication de chaque élément

### Date et heure
Moment de la requête

### Adresse IP
Utilisateur (ordinateur ou téléphone)

### Méthode
GET ou POST

### URL
Page demandée

### Code
Résultat de la requête

### Temps
Durée de réponse (en millisecondes)

---

## 8. Exemple expliqué

2026-03-01 10:16:45 | 192.168.1.10 | GET | /dashboard | 500 | 300ms

Interprétation :

- Un utilisateur (IP 192.168.1.10)
- demande la page /dashboard
- avec GET
- le serveur a une erreur (500)
- réponse en 300ms

---

## 9. Pourquoi analyser les logs ?

Les logs servent à :

- comprendre le comportement des utilisateurs
- détecter des erreurs
- analyser les performances
- détecter des activités suspectes

---

## 10. Cas pratiques

### Beaucoup de 404
pages inexistantes ou liens cassés

### Beaucoup de 500
erreur côté serveur

### Beaucoup de POST /login
tentatives de connexion

### Une IP avec beaucoup d’erreurs
activité suspecte

---

## 11. Objectif pour le TP

Avec Python, vous allez :

- lire les logs
- extraire les informations
- compter les requêtes
- analyser les erreurs
- détecter des comportements anormaux

---

## 12. Résumé

- GET = lire
- POST = envoyer
- 200 = succès
- 404 = introuvable
- 500 = erreur serveur

Les logs permettent de comprendre ce qui se passe sur un serveur.

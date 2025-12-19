# 🧩 Mini‑Projet — Assistant Météo Intelligent (Challenge)

## 🎯 Objectif
Créer un programme Python qui analyse une température saisie par l’utilisateur, la convertit dans l’autre unité et affiche un rapport clair avec une interprétation météo.

Ce projet est **strictement aligné avec le cours** : aucune notion non vue (pas de fonctions, pas de boucles, pas de try/except).

---

## 📚 Notions utilisées
- `input()`
- chaînes de caractères (`strip`, `replace`, slicing)
- conversion de type (`float`)
- conditions `if / elif / else`
- calculs mathématiques
- affichage formaté avec f‑strings

---

## 📝 Consignes

### 1) Saisie utilisateur
Le programme demande à l’utilisateur une température au format :
```
valeur + unité
```
Exemples :
- `22C`
- `-5 C`
- `36.6F`
- `25°C`

L’unité peut être `C` ou `F` (majuscules ou minuscules).

---

### 2) Analyse et validation
Le programme doit :
- supprimer les espaces inutiles
- accepter le symbole `°`
- extraire la valeur numérique
- extraire l’unité
- vérifier que la valeur est bien un nombre
- afficher un message d’erreur simple si l’entrée est invalide

⚠️ Une seule saisie est demandée (pas de répétition).

---

### 3) Conversion
- Si l’unité est `C`, convertir en Fahrenheit :
```
F = C × 9 / 5 + 32
```
- Si l’unité est `F`, convertir en Celsius :
```
C = (F − 32) × 5 / 9
```

---

### 4) Interprétation (en degrés Celsius)
- ≤ -10 : Très grand froid
- -10 < T ≤ 0 : Gel
- 0 < T < 10 : Froid
- 10 ≤ T < 20 : Frais
- 20 ≤ T < 25 : Tempéré
- 25 ≤ T < 32 : Chaud
- ≥ 32 : Très chaud

Chaque catégorie doit afficher un **conseil météo** adapté.

---

### 5) Comparaisons
Comparer la température en Celsius :
- au point de gel (0°C)
- à la température corporelle (37°C)

---

### 6) Affichage final
Le programme affiche un rapport formaté :

```
=== RAPPORT MÉTÉO ===
Entrée : 22C
En Celsius : 22.0°C
En Fahrenheit : 71.6°F
Catégorie : Tempéré
Conseil : Temps agréable.
Point de gel : au-dessus
Température corporelle : plus basse
=====================
```

---

## 🧮 Évaluation (suggestion /20)
- Analyse et validation de l’entrée : 5 pts
- Conversion correcte : 4 pts
- Interprétation météo : 4 pts
- Comparaisons : 3 pts
- Affichage clair et lisible : 4 pts

**Total : 20 pts**

---

## ✅ Remarque pédagogique
Ce projet est volontairement exigeant sur le raisonnement, mais respecte totalement le niveau du cours.  
Il constitue un excellent **mini‑projet de fin de chapitre**.

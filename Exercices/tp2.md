#  Exercices  Listes en Python

Ce document contient une série d’exercices **intermédiaires et difficiles** sur les listes en Python.  
Les notions couvertes :

- Création de listes  
- Accès par index  
- Modification d’éléments  
- Slicing (`start:end:step`)  
- Opérateurs (`+`, `*`, `in`)  

---

## ⭐ Exercice 1 — Extraction avancée

```python
data = [12, 5, 7, 20, 33, 2, 19, 40, 8, 11]
```

1. Affichez les 3 premiers éléments  
2. Affichez les 4 derniers  
3. Affichez un élément sur deux  
4. Affichez les éléments du 3ᵉ au 7ᵉ (inclus)  
5. Affichez la liste en ordre inversé  
6. Affichez uniquement les valeurs > 10 (en utilisant slicing ou indexation uniquement)

---

## ⭐ Exercice 2 — Reconstruction d’une liste

```python
part1 = ["a", "b", "c"]
part2 = ["d", "e"]
part3 = ["f", "g", "h"]
```

1. Assemblez les 3 listes sans `append()`  
2. Insérez `"z"` entre `"e"` et `"f"` en utilisant uniquement `+`, slicing ou index  

---

## ⭐ Exercice 3 — Manipulation et remplacement

```python
nombres = [3, 12, 7, 18, 5, 9, 21, 14]
```

1. Remplacez le 2ᵉ élément par 99  
2. Remplacez le dernier élément par 0  
3. Remplacez le 4ᵉ élément par la somme des 2 premiers  
4. Doublez l’élément d’index 5  
5. Affichez la liste finale  

---

## ⭐ Exercice 4 — Slicing complexe

```python
letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
```

Affichez :

1. Les éléments entre `'b'` et `'g'` inclus  
2. Sans les 2 premiers et 2 derniers  
3. Les éléments aux positions paires  
4. Les éléments aux positions impaires  
5. La liste inversée avec un pas de 2  

---

## ⭐ Exercice 5 — Opérateurs et index (sans if)

```python
noms = ["Alice", "Bob", "Charlie", "Dora", "Eli", "Fatima"]
```

1. Affichez si `"Charlie"` est dans la liste  
2. Affichez si `"George"` n'est pas dans la liste  
3. Remplacez `"Dora"` par `"Dora-Marie"` **sans utiliser if**  
4. Affichez l’index de `"Fatima"`  
5. Affichez la liste finale  

---

## ⭐ Exercice 6 — Slicing + opérateurs

```python
liste = [10, 20, 30, 40, 50, 60, 70]
```

1. Créez une liste contenant les 3 premiers éléments répétés 2 fois  
2. Créez une liste contenant les éléments aux index 1, 3 et 5  
3. Créez une liste contenant la liste sans les extrémités  
4. Créez une liste contenant la liste inversée sauf le premier élément  

---

## ⭐ Exercice 7 — Remplacer une section entière

```python
L = [1, 2, 3, 4, 5, 6, 7]
```

Remplacez **3, 4 et 5** par `["a", "b"]` en utilisant **uniquement le slicing**.

---

## ⭐ Exercice 8 — Nettoyage d’une liste (sans boucle)

```python
brut = ["ok", "?", "valide", "STOP", "ok", "?", "ok"]
```

Créez une liste `propre` contenant tous les éléments **sauf** `"?"` et `"STOP"`  
→ Sans boucle, sans `remove()`, sans `pop()`  

---

## ⭐ Exercice 9 — Fusion intelligente

```python
A = [1, 3, 5, 7]
B = [2, 4, 6, 8]
```

Fusionnez les deux listes pour obtenir :

```python
[1, 2, 3, 4, 5, 6, 7, 8]
```

→ Sans boucle, sans `append()`

---

## ⭐ Exercice 10 — Challenge final

```python
data = [3, 9, 15, 21, 27, 33, 39, 45]
```

1. `pair_index` : éléments aux index pairs  
2. `impair_index` : éléments aux index impairs  
3. `multiples_de_3` : uniquement slicing ou copie  
4. `centre` : les 4 éléments du milieu  
5. `reverse_step3` : liste inversée avec un pas de 3  

---


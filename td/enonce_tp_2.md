# 🧪 TP Python — Factorisation d’un trinôme via discriminant (CLI)

## 1) Contexte scientifique
On considère le polynôme du second degré :

\[
P(x)=ax^2+bx+c,\qquad a\neq 0
\]

La factorisation sur \(\mathbb{R}\) dépend du discriminant :

\[
\Delta=b^2-4ac
\]

- Si \(\Delta>0\) : deux racines réelles \(x_1,x_2\) et  
  \[
  P(x)=a(x-x_1)(x-x_2)
  \]
- Si \(\Delta=0\) : racine double \(x_0\) et  
  \[
  P(x)=a(x-x_0)^2
  \]
- Si \(\Delta<0\) : pas de factorisation sur \(\mathbb{R}\) (racines complexes possibles)

---

## 2) Objectifs
Écrire un programme **Python** `tp.py` (script) qui :

1. lit une liste de triplets \((a,b,c)\) représentant des polynômes \(P(x)\),
2. calcule \(\Delta\),
3. déduit la factorisation **sur \(\mathbb{R}\)** quand elle existe,
4. affiche un résultat complet,
5. et peut écrire le même résultat dans un fichier.

---

## 3) Interface en ligne de commande (obligatoire)

Votre programme doit accepter les commandes suivantes **toutes valides** (ordre libre des options) :

```bash
python tp.py
python tp.py -i input.txt
python tp.py -o output.txt
python tp.py -i input.txt -o output.txt
python tp.py -o output.txt -i input.txt
```

- `-i input.txt` : lecture des données depuis un fichier
- `-o output.txt` : écriture des résultats dans un fichier (en plus de l’affichage écran)
- Sans `-i` : lecture interactive depuis le clavier

> ⚠️ L’ordre de `-i` et `-o` ne doit pas influencer le fonctionnement.

---

## 4) Format des données d’entrée

### 4.1 Lecture fichier (`-i`)
Le fichier contient **une équation par ligne** sous la forme :

\[
a\;\;b\;\;c
\]

Exemple (`input.txt`) :
```txt
# a b c
1 -5 6
1 4 4
2 1 3
0.5 -1 0.5
```

**Règles :**
- ignorer les lignes vides
- ignorer les lignes qui commencent par `#`
- chaque ligne valide contient exactement **3 nombres** (entiers ou réels)
- ignorer les lignes invalides moins ou plus de **3 nombres**

### 4.2 Lecture clavier (sans `-i`)
Le programme demande des lignes `a b c` successives.
La saisie se termine quand l’utilisateur entre :

```txt
0 0 0
```

---

## 5) Traitement mathématique attendu

Pour chaque triplet \((a,b,c)\) :

1) Vérifier que \(a\neq 0\).  
- Si \(a=0\), indiquer :  
  **« Cas non traité : ce n’est pas un polynôme du second degré. »**  
  (et passer à la ligne suivante)

2) Calculer :
\[
\Delta=b^2-4ac
\]

3) Selon \(\Delta\) :
- \(\Delta>0\) : calculer
  \[
  x_{1,2}=\frac{-b\pm\sqrt{\Delta}}{2a}
  \]
  puis afficher \(x_1,x_2\) et la factorisation \(a(x-x_1)(x-x_2)\)

- \(\Delta=0\) : calculer
  \[
  x_0=\frac{-b}{2a}
  \]
  puis afficher \(x_0\) et la factorisation \(a(x-x_0)^2\)

- \(\Delta<0\) : afficher  
  **« Pas de factorisation sur \(\mathbb{R}\) (Δ < 0). »**

---

## 6) Format de sortie attendu (écran + fichier)

Pour chaque équation, produire un bloc de sortie (séparé par une ligne vide).  
Exemple :

```txt
P(x) = 1x² -5x + 6
Δ = 1
Racines réelles : x1 = 2.0000 ; x2 = 3.0000
Factorisation sur R : 1(x - 2.0000)(x - 3.0000)
```

Cas \(\Delta=0\) :

```txt
P(x) = 1x² +4x + 4
Δ = 0
Racine double : x0 = -2.0000
Factorisation sur R : 1(x - (-2.0000))²
```

Cas \(\Delta<0\) :

```txt
P(x) = 2x² +1x + 3
Δ = -23
Pas de factorisation sur R (Δ < 0).
```

---

## 7) Résumé final (obligatoire)

À la fin du programme, afficher un résumé :

- nombre total de triplets traités
- nombre de polynômes factorisables sur \(\mathbb{R}\)
- nombre de cas \(a=0\)
- nombre de cas \(\Delta<0\)

Exemple :

```txt
----- Résumé -----
Total : 4
Factorisables sur R : 2
Cas a = 0 : 0
Cas Δ < 0 : 1
```

Le résumé doit aussi être écrit dans `output.txt` si `-o` est fourni.

---

## 8) Contraintes techniques

- Fichier : `tp.py`
- Langage : Python 3
- Autorisé : `sys`, `math`
- Interdit : bibliothèques externes (numpy, sympy, etc.)
- Le programme doit être robuste :
  - ignorer les lignes invalides (ou signaler clairement)
  - ne pas planter sur un fichier vide

---

## 9) Bonus (facultatif)

1) Support des racines complexes si \(\Delta<0\) (afficher \(x = \alpha \pm i\beta\))  
2) Affichage “mathématique” plus propre (simplification des signes)

---

## Livrables

- `tp.py`
- un exemple de fichier `input.txt`
- un exemple de sortie `output.txt` (généré)

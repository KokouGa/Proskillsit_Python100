""""Tests unitaires pour le jeu - version fonctionnelle sans classes"""

import pytest
from jeu import (
    creer_balle, deplacer_balle, est_tombee, collision_avec_raquette,
    creer_raquette, deplacer_raquette, gerer_score, gerer_vies,
    partie_terminee, LARGEUR_ECRAN, HAUTEUR_ECRAN
)


# ============================================================
# Tests pour les balles
# ============================================================

def test_creer_balle_valeurs_par_defaut():
    """Test : création d'une balle avec valeurs par défaut"""
    balle = creer_balle()
    
    assert balle["x"] == LARGEUR_ECRAN // 2
    assert balle["y"] == 0
    assert balle["vitesse"] == 5
    assert balle["couleur"] == "bleu"
    assert balle["rayon"] == 12


def test_creer_balle_valeurs_personnalisees():
    """Test : création d'une balle avec valeurs personnalisées"""
    balle = creer_balle(x=100, y=50, vitesse=10, couleur="rouge")
    
    assert balle["x"] == 100
    assert balle["y"] == 50
    assert balle["vitesse"] == 10
    assert balle["couleur"] == "rouge"


def test_deplacer_balle():
    """Test : déplacement d'une balle vers le bas"""
    balle = creer_balle(y=100, vitesse=5)
    
    balle = deplacer_balle(balle)
    
    assert balle["y"] == 105


def test_deplacer_balle_plusieurs_fois():
    """Test : déplacement multiple d'une balle"""
    balle = creer_balle(y=100, vitesse=3)
    
    for _ in range(4):
        balle = deplacer_balle(balle)
    
    assert balle["y"] == 112  # 100 + 4*3


def test_est_tombee_faux():
    """Test : balle pas encore tombée (y < HAUTEUR)"""
    balle = creer_balle(y=590, vitesse=5)
    balle = deplacer_balle(balle)  # y = 595
    assert est_tombee(balle) is False  # 595 < 600


def test_est_tombee_limite():
    """Test : balle exactement à la limite (y == HAUTEUR) n'est PAS tombée"""
    balle = creer_balle(y=590, vitesse=10)
    balle = deplacer_balle(balle)  # y = 600
    assert est_tombee(balle) is False  # 600 n'est PAS > 600


def test_est_tombee_vrai():
    """Test : balle est tombée (y > HAUTEUR)"""
    balle = creer_balle(y=595, vitesse=10)
    balle = deplacer_balle(balle)  # y = 605
    assert est_tombee(balle) is True


@pytest.mark.parametrize("y_depart, vitesse, attendu_tombee", [
    (590, 5, False),   # 590+5=595 → 595 < 600 → PAS TOMBÉE
    (590, 10, False),  # 590+10=600 → 600 == 600 → PAS TOMBÉE
    (595, 10, True),   # 595+10=605 → 605 > 600 → TOMBÉE
    (500, 5, False),   # 500+5=505 → 505 < 600 → PAS TOMBÉE
    (599, 1, False),   # 599+1=600 → 600 == 600 → PAS TOMBÉE
    (599, 2, True),    # 599+2=601 → 601 > 600 → TOMBÉE
])
def test_est_tombee_parametres(y_depart, vitesse, attendu_tombee):
    """Test paramétré : différentes positions de balle"""
    balle = creer_balle(y=y_depart, vitesse=vitesse)
    balle = deplacer_balle(balle)
    assert est_tombee(balle) is attendu_tombee


# ============================================================
# Tests pour la raquette
# ============================================================

def test_creer_raquette_valeurs_par_defaut():
    """Test : création d'une raquette avec valeurs par défaut"""
    raquette = creer_raquette()
    
    assert raquette["x"] == (800 - 100) // 2  # 350
    assert raquette["y"] == 600 - 40  # 560
    assert raquette["largeur"] == 100
    assert raquette["hauteur"] == 15


def test_creer_raquette_valeurs_personnalisees():
    """Test : création d'une raquette avec valeurs personnalisées"""
    raquette = creer_raquette(x=200, largeur=80, y=500)
    
    assert raquette["x"] == 200
    assert raquette["largeur"] == 80
    assert raquette["y"] == 500


def test_deplacer_raquette_gauche():
    """Test : déplacement de la raquette à gauche"""
    raquette = creer_raquette(x=400)
    
    raquette = deplacer_raquette(raquette, "gauche", vitesse=5)
    
    assert raquette["x"] == 395


def test_deplacer_raquette_droite():
    """Test : déplacement de la raquette à droite"""
    raquette = creer_raquette(x=400)
    
    raquette = deplacer_raquette(raquette, "droite", vitesse=5)
    
    assert raquette["x"] == 405


def test_deplacer_raquette_bord_gauche():
    """Test : la raquette ne sort pas à gauche"""
    raquette = creer_raquette(x=10)
    
    raquette = deplacer_raquette(raquette, "gauche", vitesse=20)
    
    assert raquette["x"] == 0  # Bloquée au bord


def test_deplacer_raquette_bord_droit():
    """Test : la raquette ne sort pas à droite"""
    raquette = creer_raquette(x=750, largeur=100)
    
    raquette = deplacer_raquette(raquette, "droite", vitesse=20)
    
    assert raquette["x"] == 700  # 800 - 100


# ============================================================
# Tests pour les collisions
# ============================================================

def test_collision_avec_raquette_centre():
    """Test : collision quand la balle est au centre de la raquette"""
    balle = creer_balle(x=400, y=550)
    raquette_x = 350
    raquette_largeur = 100
    
    assert collision_avec_raquette(balle, raquette_x, raquette_largeur) is True


def test_collision_avec_raquette_bord_gauche():
    """Test : collision quand la balle est au bord gauche"""
    balle = creer_balle(x=351, y=550)  # Juste après le bord gauche
    raquette_x = 350
    raquette_largeur = 100
    
    assert collision_avec_raquette(balle, raquette_x, raquette_largeur) is True


def test_collision_avec_raquette_bord_droit():
    """Test : collision quand la balle est au bord droit"""
    balle = creer_balle(x=449, y=550)  # Juste avant le bord droit (350+100=450)
    raquette_x = 350
    raquette_largeur = 100
    
    assert collision_avec_raquette(balle, raquette_x, raquette_largeur) is True


def test_pas_collision_trop_a_gauche():
    """Test : pas de collision quand la balle est trop à gauche"""
    balle = creer_balle(x=340, y=550)
    raquette_x = 350
    raquette_largeur = 100
    
    assert collision_avec_raquette(balle, raquette_x, raquette_largeur) is False


def test_pas_collision_trop_a_droite():
    """Test : pas de collision quand la balle est trop à droite"""
    balle = creer_balle(x=460, y=550)
    raquette_x = 350
    raquette_largeur = 100
    
    assert collision_avec_raquette(balle, raquette_x, raquette_largeur) is False


# ============================================================
# Tests pour le score
# ============================================================

def test_score_balle_bleue_attrapee():
    """Test : attraper une balle bleue augmente le score"""
    balle = creer_balle(couleur="bleu")
    
    nouveau_score = gerer_score(score=5, balle=balle, attrapee=True)
    
    assert nouveau_score == 6


def test_score_balle_rouge_attrapee():
    """Test : attraper une balle rouge diminue le score"""
    balle = creer_balle(couleur="rouge")
    
    nouveau_score = gerer_score(score=5, balle=balle, attrapee=True)
    
    assert nouveau_score == 4


def test_score_balle_bleue_ratee():
    """Test : rater une balle bleue ne change pas le score"""
    balle = creer_balle(couleur="bleu")
    
    nouveau_score = gerer_score(score=5, balle=balle, attrapee=False)
    
    assert nouveau_score == 5


def test_score_balle_rouge_ratee():
    """Test : rater une balle rouge augmente le score (bonus)"""
    balle = creer_balle(couleur="rouge")
    
    nouveau_score = gerer_score(score=5, balle=balle, attrapee=False)
    
    assert nouveau_score == 6


# ============================================================
# Tests pour les vies
# ============================================================

def test_vies_balle_bleue_attrapee():
    """Test : attraper une balle bleue ne change pas les vies"""
    balle = creer_balle(couleur="bleu")
    
    nouvelles_vies = gerer_vies(vies=3, balle=balle, attrapee=True)
    
    assert nouvelles_vies == 3


def test_vies_balle_rouge_attrapee():
    """Test : attraper une balle rouge diminue les vies"""
    balle = creer_balle(couleur="rouge")
    
    nouvelles_vies = gerer_vies(vies=3, balle=balle, attrapee=True)
    
    assert nouvelles_vies == 2


def test_vies_balle_rouge_attrapee_multiple():
    """Test : attraper plusieurs balles rouges diminue les vies plusieurs fois"""
    balle = creer_balle(couleur="rouge")
    
    vies = 5
    for _ in range(3):
        vies = gerer_vies(vies=vies, balle=balle, attrapee=True)
    
    assert vies == 2  # 5 - 3


def test_vies_balle_ratee():
    """Test : rater une balle (peu importe la couleur) ne change pas les vies"""
    balle_bleue = creer_balle(couleur="bleu")
    balle_rouge = creer_balle(couleur="rouge")
    
    vies_bleu = gerer_vies(vies=3, balle=balle_bleue, attrapee=False)
    vies_rouge = gerer_vies(vies=3, balle=balle_rouge, attrapee=False)
    
    assert vies_bleu == 3
    assert vies_rouge == 3


# ============================================================
# Tests pour la fin de partie
# ============================================================

def test_partie_terminee_plus_de_vies():
    """Test : partie terminée quand plus de vies"""
    assert partie_terminee(vies=0, temps_restant=60) is True


def test_partie_terminee_temps_ecoule():
    """Test : partie terminée quand temps écoulé"""
    assert partie_terminee(vies=3, temps_restant=0) is True


def test_partie_terminee_continue():
    """Test : partie continue quand vies > 0 et temps > 0"""
    assert partie_terminee(vies=3, temps_restant=60) is False
    assert partie_terminee(vies=1, temps_restant=1) is False
    assert partie_terminee(vies=3, temps_restant=0.5) is False  # > 0
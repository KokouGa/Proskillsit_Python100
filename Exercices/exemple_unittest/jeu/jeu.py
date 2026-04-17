"""Module du jeu de balles - version fonctionnelle avec Pygame"""

import pygame
import random
import sys

# Constantes
LARGEUR_ECRAN = 800
HAUTEUR_ECRAN = 600
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
ROUGE = (255, 0, 0)
BLEU = (0, 0, 255)
VERT = (0, 255, 0)

# ============================================================
# Fonctions du jeu
# ============================================================

def creer_balle(x=None, y=None, vitesse=None, couleur="bleu"):
    """Crée une nouvelle balle"""
    if x is None:
        x = random.randint(20, LARGEUR_ECRAN - 20)  # Position X aléatoire
    if y is None:
        y = 0
    if vitesse is None:
        vitesse = 5
    return {
        "x": x,
        "y": y,
        "vitesse": vitesse,
        "couleur": couleur,  # "bleu" ou "rouge" (string)
        "rayon": 12
    }

def deplacer_balle(balle):
    """Déplace la balle vers le bas"""
    balle["y"] += balle["vitesse"]
    return balle

def est_tombee(balle):
    """Vérifie si la balle est tombée en bas de l'écran"""
    return balle["y"] > HAUTEUR_ECRAN

def collision_avec_raquette(balle, raquette_x, raquette_largeur):
    """Vérifie si la balle touche la raquette"""
    balle_x = balle["x"]
    return raquette_x < balle_x < raquette_x + raquette_largeur

def creer_raquette(x=None, largeur=100, y=None):
    """Crée une nouvelle raquette"""
    if x is None:
        x = (LARGEUR_ECRAN - largeur) // 2
    if y is None:
        y = HAUTEUR_ECRAN - 40
    return {
        "x": x,
        "y": y,
        "largeur": largeur,
        "hauteur": 15
    }

def deplacer_raquette(raquette, direction, vitesse=7):
    """Déplace la raquette à gauche ou droite"""
    if direction == "gauche":
        raquette["x"] -= vitesse
    elif direction == "droite":
        raquette["x"] += vitesse
    
    # Empêcher de sortir de l'écran
    if raquette["x"] < 0:
        raquette["x"] = 0
    if raquette["x"] > LARGEUR_ECRAN - raquette["largeur"]:
        raquette["x"] = LARGEUR_ECRAN - raquette["largeur"]
    
    return raquette

def gerer_score(score, balle, attrapee):
    """Gère le score selon la balle et si elle est attrapée"""
    nouveau_score = score
    
    if attrapee:
        if balle["couleur"] == "bleu":
            nouveau_score += 1
        else:  # rouge
            nouveau_score -= 1
    else:
        # Balle tombée (ratée)
        if balle["couleur"] == "rouge":
            nouveau_score += 1  # Bonus : rater une rouge rapporte un point
    
    return nouveau_score

def gerer_vies(vies, balle, attrapee):
    """Gère les vies (seulement pour les balles rouges attrapées)"""
    nouvelles_vies = vies
    
    if attrapee and balle["couleur"] == "rouge":
        nouvelles_vies -= 1
    
    return nouvelles_vies

def partie_terminee(vies, temps_restant):
    """Vérifie si la partie est terminée"""
    return vies <= 0 or temps_restant <= 0


# ============================================================
# Fonctions d'affichage
# ============================================================

def afficher_texte(screen, texte, x, y, couleur, taille=30):
    """Affiche du texte à l'écran"""
    police = pygame.font.SysFont("Arial", taille)
    surface = police.render(texte, True, couleur)
    screen.blit(surface, (x, y))

def afficher_vies(screen, vies):
    """Affiche les vies sous forme de cœurs"""
    coeurs = "❤️" * vies + "🖤" * (3 - vies)
    afficher_texte(screen, f"Vies : {coeurs}", 10, 50, ROUGE, 25)

def afficher_timer(screen, temps_restant):
    """Affiche le timer et la barre de progression"""
    afficher_texte(screen, f"Temps : {int(temps_restant)} s", LARGEUR_ECRAN - 150, 10, NOIR, 25)
    
    largeur_barre = 300
    proportion = max(0, temps_restant / 120)
    pygame.draw.rect(screen, VERT, ((LARGEUR_ECRAN - largeur_barre) // 2, 10, 
                                     int(largeur_barre * proportion), 20))
    pygame.draw.rect(screen, NOIR, ((LARGEUR_ECRAN - largeur_barre) // 2, 10, 
                                     largeur_barre, 20), 2)

def afficher_ecran_fin(screen, score, vies):
    """Affiche l'écran de fin de partie"""
    overlay = pygame.Surface((LARGEUR_ECRAN, HAUTEUR_ECRAN))
    overlay.set_alpha(200)
    overlay.fill((128, 128, 128))
    screen.blit(overlay, (0, 0))
    
    if vies <= 0:
        afficher_texte(screen, "GAME OVER !", LARGEUR_ECRAN // 2 - 120, 
                      HAUTEUR_ECRAN // 2 - 80, ROUGE, 60)
    else:
        afficher_texte(screen, "TEMPS ÉCOULÉ !", LARGEUR_ECRAN // 2 - 140, 
                      HAUTEUR_ECRAN // 2 - 80, BLEU, 60)
    
    afficher_texte(screen, f"Score final : {score}", LARGEUR_ECRAN // 2 - 100, 
                  HAUTEUR_ECRAN // 2, NOIR, 35)
    afficher_texte(screen, "Appuyez sur R pour rejouer   ou   Q pour quitter", 
                  LARGEUR_ECRAN // 2 - 320, HAUTEUR_ECRAN // 2 + 60, NOIR, 25)


# ============================================================
# Boucle principale du jeu
# ============================================================

def lancer_jeu():
    """Lance le jeu complet"""
    
    pygame.init()
    screen = pygame.display.set_mode((LARGEUR_ECRAN, HAUTEUR_ECRAN))
    pygame.display.set_caption("Attrape les balles bleues !")
    horloge = pygame.time.Clock()
    
    score = 0
    vies = 3
    balles = []
    raquette = creer_raquette()
    DUREE_JEU = 120
    start_time = pygame.time.get_ticks()
    jeu_termine = False
    
    running = True
    while running:
        # --- Événements ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if jeu_termine and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    # Reset complet
                    score = 0
                    vies = 3
                    balles = []
                    raquette = creer_raquette()
                    start_time = pygame.time.get_ticks()
                    jeu_termine = False
                if event.key == pygame.K_q:
                    running = False
        
        # --- Mouvement raquette ---
        touches = pygame.key.get_pressed()
        if touches[pygame.K_LEFT]:
            raquette = deplacer_raquette(raquette, "gauche")
        if touches[pygame.K_RIGHT]:
            raquette = deplacer_raquette(raquette, "droite")
        
        # --- Timer ---
        temps_ecoule = (pygame.time.get_ticks() - start_time) / 1000
        temps_restant = max(0, DUREE_JEU - temps_ecoule)
        
        if temps_restant <= 0 and not jeu_termine:
            jeu_termine = True
        
        # --- Logique du jeu ---
        if not jeu_termine:
            # Apparition des balles (1 chance sur 25 par frame)
            if random.randint(1, 25) == 1:
                # Choix aléatoire entre bleu et rouge
                couleur = random.choice(["bleu", "rouge"])
                balle = creer_balle(couleur=couleur)
                balles.append(balle)
                print(f"Balle créée : {couleur}")  # Pour déboguer
            
            # Déplacement et collisions
            nouvelles_balles = []
            for balle in balles:
                balle = deplacer_balle(balle)
                
                # Collision avec raquette
                if collision_avec_raquette(balle, raquette["x"], raquette["largeur"]):
                    score = gerer_score(score, balle, attrapee=True)
                    vies = gerer_vies(vies, balle, attrapee=True)
                    print(f"Collision ! Score: {score}, Vies: {vies}")
                    continue  # Balle capturée, on ne la garde pas
                
                # Balle tombée
                if est_tombee(balle):
                    score = gerer_score(score, balle, attrapee=False)
                    vies = gerer_vies(vies, balle, attrapee=False)
                    print(f"Balle tombée ! Score: {score}")
                    continue
                
                nouvelles_balles.append(balle)
            
            balles = nouvelles_balles
            
            if vies <= 0:
                jeu_termine = True
        
        # --- Affichage ---
        screen.fill(BLANC)
        
        # Raquette
        pygame.draw.rect(screen, NOIR, (raquette["x"], raquette["y"], 
                                       raquette["largeur"], raquette["hauteur"]))
        
        # Balles
        for balle in balles:
            if balle["couleur"] == "bleu":
                couleur_rgb = BLEU
            else:
                couleur_rgb = ROUGE
            pygame.draw.circle(screen, couleur_rgb, (int(balle["x"]), int(balle["y"])), balle["rayon"])
        
        # UI
        afficher_texte(screen, f"Score : {score}", 10, 10, NOIR, 30)
        afficher_vies(screen, vies)
        afficher_timer(screen, temps_restant)
        
        if jeu_termine:
            afficher_ecran_fin(screen, score, vies)
        
        pygame.display.flip()
        horloge.tick(60)
    
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    lancer_jeu()
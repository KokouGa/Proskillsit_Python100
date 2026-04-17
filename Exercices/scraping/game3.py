import pygame
import random
import sys

# Initialisation
pygame.init()

# Constantes
LARGEUR, HAUTEUR = 800, 600
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
ROUGE = (255, 0, 0)
BLEU = (0, 0, 255)
VERT = (0, 255, 0)
GRIS = (128, 128, 128)

# Fenêtre
screen = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Attrape les balles bleues - 3 vies")
horloge = pygame.time.Clock()

# Raquette
raquette_largeur = 100
raquette_hauteur = 15
raquette_x = (LARGEUR - raquette_largeur) // 2
raquette_y = HAUTEUR - 40
vitesse_raquette = 7

# Balles
balles = []
rayon_balle = 12
balle_vitesse = 5

# Score et vies
score = 0
vies = 3
police = pygame.font.SysFont("Arial", 30)
police_grande = pygame.font.SysFont("Arial", 60)

# Timer (2 minutes = 120 secondes)
DUREE_JEU = 120
start_time = pygame.time.get_ticks()

# État du jeu
jeu_termine = False

# Fonction pour afficher du texte centré
def texte_centre(texte, police, couleur, y):
    surface = police.render(texte, True, couleur)
    rect = surface.get_rect(center=(LARGEUR // 2, y))
    screen.blit(surface, rect)

# Boucle principale
running = True
while running:
    # --- Gestion des événements ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if jeu_termine and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:  # Appuyer sur R pour rejouer
                # Reset du jeu
                score = 0
                vies = 3
                balles = []
                start_time = pygame.time.get_ticks()
                jeu_termine = False
            if event.key == pygame.K_q:  # Appuyer sur Q pour quitter
                running = False
    
    # --- Mouvement de la raquette ---
    touches = pygame.key.get_pressed()
    if touches[pygame.K_LEFT] and raquette_x > 0:
        raquette_x -= vitesse_raquette
    if touches[pygame.K_RIGHT] and raquette_x < LARGEUR - raquette_largeur:
        raquette_x += vitesse_raquette
    
    # --- Timer et vérification fin de partie (temps écoulé) ---
    temps_ecoule = (pygame.time.get_ticks() - start_time) / 1000
    temps_restant = max(0, DUREE_JEU - temps_ecoule)
    
    # Si le temps est écoulé ET qu'on est pas déjà en game over
    if temps_restant <= 0 and not jeu_termine:
        jeu_termine = True
        print(f"Temps écoulé ! Score final : {score}")
    
    # --- Gestion des balles (seulement si jeu pas terminé) ---
    if not jeu_termine:
        # Apparition des balles
        if random.randint(1, 30) == 1:
            couleur = random.choice([BLEU, ROUGE])
            x = random.randint(rayon_balle, LARGEUR - rayon_balle)
            balles.append({"x": x, "y": 0, "couleur": couleur})
        
        # Déplacement et collisions
        nouvelles_balles = []
        for balle in balles:
            balle["y"] += balle_vitesse
            
            # Collision avec la raquette ?
            if (raquette_y < balle["y"] + rayon_balle < raquette_y + raquette_hauteur and
                raquette_x < balle["x"] < raquette_x + raquette_largeur):
                
                if balle["couleur"] == BLEU:
                    score += 1
                else:  # ROUGE
                    vies -= 1
                    # Vérifier si plus de vies
                    if vies <= 0:
                        jeu_termine = True
                        print(f"GAME OVER ! Plus de vies. Score final : {score}")
                continue  # Balle capturée, on ne la garde pas
            
            # Balle tombée en bas (ratée)
            if balle["y"] > HAUTEUR:
                if balle["couleur"] == ROUGE:
                    score += 1  # Bonus : rater une rouge rapporte un point
                # Si bleue ratée : rien ne se passe
                continue
            
            nouvelles_balles.append(balle)
        
        balles = nouvelles_balles
    
    # --- Affichage ---
    screen.fill(BLANC)
    
    # Raquette
    pygame.draw.rect(screen, NOIR, (raquette_x, raquette_y, raquette_largeur, raquette_hauteur))
    
    # Balles
    for balle in balles:
        pygame.draw.circle(screen, balle["couleur"], (balle["x"], int(balle["y"])), rayon_balle)
    
    # Score
    texte_score = police.render(f"Score : {score}", True, NOIR)
    screen.blit(texte_score, (10, 10))
    
    # Vies (avec des cœurs)
    coeurs = "❤️" * vies + "🖤" * (3 - vies)
    texte_vies = police.render(f"Vies : {coeurs}", True, ROUGE)
    screen.blit(texte_vies, (10, 50))
    
    # Timer
    texte_timer = police.render(f"Temps : {int(temps_restant)} s", True, NOIR)
    screen.blit(texte_timer, (LARGEUR - 150, 10))
    
    # Barre de progression du timer
    largeur_barre = 300
    proportion = temps_restant / DUREE_JEU
    pygame.draw.rect(screen, VERT, ((LARGEUR - largeur_barre) // 2, 10, int(largeur_barre * proportion), 20))
    pygame.draw.rect(screen, NOIR, ((LARGEUR - largeur_barre) // 2, 10, largeur_barre, 20), 2)
    
    # --- Écran de fin de jeu ---
    if jeu_termine:
        # Fond semi-transparent
        overlay = pygame.Surface((LARGEUR, HAUTEUR))
        overlay.set_alpha(200)
        overlay.fill(GRIS)
        screen.blit(overlay, (0, 0))
        
        # Message de fin
        if vies <= 0:
            texte_fin = police_grande.render("GAME OVER !", True, ROUGE)
        else:
            texte_fin = police_grande.render("TEMPS ÉCOULÉ !", True, BLEU)
        screen.blit(texte_fin, (LARGEUR//2 - texte_fin.get_width()//2, HAUTEUR//2 - 80))
        
        texte_score_fin = police.render(f"Score final : {score}", True, NOIR)
        screen.blit(texte_score_fin, (LARGEUR//2 - texte_score_fin.get_width()//2, HAUTEUR//2))
        
        texte_replay = police.render("Appuyez sur R pour rejouer   ou   Q pour quitter", True, NOIR)
        screen.blit(texte_replay, (LARGEUR//2 - texte_replay.get_width()//2, HAUTEUR//2 + 60))
    
    pygame.display.flip()
    horloge.tick(60)

pygame.quit()
sys.exit()
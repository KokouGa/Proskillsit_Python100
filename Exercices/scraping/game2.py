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

# Fenêtre
screen = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Attrape les balles bleues !")
horloge = pygame.time.Clock()

# Raquette (en bas)
raquette_largeur = 100
raquette_hauteur = 15
raquette_x = (LARGEUR - raquette_largeur) // 2
raquette_y = HAUTEUR - 40
vitesse_raquette = 7

# Balles
balles = []
rayon_balle = 12
balle_vitesse = 5

# Score
score = 0
police = pygame.font.SysFont("Arial", 30)

# Timer (2 minutes = 120 secondes)
DUREE_JEU = 120  # en secondes
start_time = pygame.time.get_ticks()  # temps de début en millisecondes
temps_restant = DUREE_JEU

# Boucle principale
running = True
while running:
    # --- Gestion des événements ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # --- Mouvement de la raquette (flèches gauche/droite) ---
    touches = pygame.key.get_pressed()
    if touches[pygame.K_LEFT] and raquette_x > 0:
        raquette_x -= vitesse_raquette
    if touches[pygame.K_RIGHT] and raquette_x < LARGEUR - raquette_largeur:
        raquette_x += vitesse_raquette
    
    # --- Timer : calcul du temps restant ---
    temps_ecoule = (pygame.time.get_ticks() - start_time) / 1000  # en secondes
    temps_restant = max(0, DUREE_JEU - temps_ecoule)
    
    # --- Vérifier si le jeu est terminé (temps écoulé) ---
    if temps_restant <= 0:
        running = False
        print(f"Partie terminée ! Score final : {score}")
        continue
    
    # --- Faire tomber les balles (apparition aléatoire) ---
    if random.randint(1, 30) == 1:  # 1 chance sur 30 par frame
        couleur = random.choice([BLEU, ROUGE])
        x = random.randint(rayon_balle, LARGEUR - rayon_balle)
        balle = {"x": x, "y": 0, "couleur": couleur}
        balles.append(balle)
    
    # --- Déplacer les balles et gérer les collisions avec la raquette ---
    nouvelles_balles = []
    for balle in balles:
        balle["y"] += balle_vitesse
        
        # Collision avec la raquette ?
        if (raquette_y < balle["y"] + rayon_balle < raquette_y + raquette_hauteur and
            raquette_x < balle["x"] < raquette_x + raquette_largeur):
            
            if balle["couleur"] == BLEU:
                score += 1      # Balle bleue = +1 point
            else:  # ROUGE
                score -= 1      # Balle rouge = -1 point
            # Ne pas ajouter la balle aux nouvelles (elle est "capturée")
            continue
        
        # Balle en bas de l'écran (ratée)
        if balle["y"] > HAUTEUR:
            if balle["couleur"] == ROUGE:
                score += 1      # Rater une rouge = +1 (bonus)
            # Si c'est une bleue ratée, rien ne se passe (pas de pénalité)
            continue
        
        # Sinon, garder la balle
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
    
    # Timer (barre + texte)
    texte_timer = police.render(f"Temps : {int(temps_restant)} s", True, NOIR)
    screen.blit(texte_timer, (LARGEUR - 150, 10))
    
    # Barre de progression du timer
    largeur_barre = 300
    proportion = temps_restant / DUREE_JEU
    pygame.draw.rect(screen, VERT, ((LARGEUR - largeur_barre) // 2, 10, int(largeur_barre * proportion), 20))
    pygame.draw.rect(screen, NOIR, ((LARGEUR - largeur_barre) // 2, 10, largeur_barre, 20), 2)
    
    pygame.display.flip()
    horloge.tick(60)  # 60 images par seconde

# Fin du jeu
pygame.quit()
sys.exit()
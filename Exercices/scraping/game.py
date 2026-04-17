import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Super Ball")

ball_x, ball_y = 50, 50
ball_change_x, ball_change_y = 3, 3

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    ball_x += ball_change_x
    ball_y += ball_change_y
    
    if ball_y > 300 or ball_y < 0:
        ball_change_y = -ball_change_y
    if ball_x > 400 or ball_x < 0:
        ball_change_x = -ball_change_x
    
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), (ball_x, ball_y), 10)
    pygame.display.flip()

pygame.quit()
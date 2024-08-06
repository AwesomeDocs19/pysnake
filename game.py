import pygame
pygame.init()

# Display settings
dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    dis.fill((0, 0, 0))
    pygame.display.update()

pygame.quit()

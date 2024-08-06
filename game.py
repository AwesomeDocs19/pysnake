import pygame
import random
pygame.init()

# Display settings
dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')

snake_block = 10
x1 = dis_width / 2
y1 = dis_height / 2
x1_change = 0
y1_change = 0

foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -snake_block
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = snake_block
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -snake_block
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = snake_block
                x1_change = 0

    x1 += x1_change
    y1 += y1_change
    dis.fill((0, 0, 0))
    pygame.draw.rect(dis, (255, 255, 255), [x1, y1, snake_block, snake_block])
    pygame.draw.rect(dis, (0, 255, 0), [foodx, foody, snake_block, snake_block])
    pygame.display.update()

pygame.quit()

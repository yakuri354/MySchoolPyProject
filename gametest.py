import pygame
pygame.init()
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
sc = pygame.display.set_mode((600, 400))
x = 300
y = 200
run = True

while run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT:
                x -= 3
            elif i.key == pygame.K_RIGHT:
                x += 3
            elif i.key == pygame.K_UP:
                y -= 3
            elif i.key == pygame.K_DOWN:
                y += 3
    sc.fill((255, 255, 255))
    pygame.draw.circle(sc, RED, (x, y), 50)

    pygame.display.update()
    pygame.time.delay(20)

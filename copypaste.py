import pygame

FPS = 60
W = 700
H = 300
WHITE = (255, 255, 255)
BLUE = (0, 70, 225)

pygame.init()
sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

x = W // 2
y = H // 2
r = 50

while 1:
    sc.fill(WHITE)

    pygame.draw.circle(sc, BLUE, (x, y), r)

    pygame.display.update()

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT:
                x -= 3
            elif i.key == pygame.K_RIGHT:
                x += 3

    clock.tick(FPS)

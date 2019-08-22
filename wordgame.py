import pygame
import random

FPS = 60
W = 600
H = 400
WHITE = (255, 255, 255)
LBLUE = (122, 184, 225)

pygame.init()
pygame.font.init()
sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
timetonew = 0
y1 = 55
y2 = 150
x1 = 545
r = 46
inf = True
words = ['fine', 'test', 'good', 'nope', 'maze']
circs = []


class Circword:
    def __init__(self, word):
        self.word = word
        self.x = x1
        self.y = random.randint(0, H)

    def update(self, t):
        self.x -= t / 1000
        self.x = int(self.x)

    def draw(self, sc):
        print(self)
        pygame.draw.circle(sc, LBLUE, (self.x, self.y), r)
        pygame.font.SysFont('arial', 20)
        font = pygame.font.Font(None, 72)
        text = font.render(self.word, 1, (0, 100, 0))
        place = text.get_rect(center=(self.x, self.y))
        sc.blit(text, place)


circ = Circword(random.choice(words))

while inf:
    sc.fill(WHITE)
    circ.draw(sc)
    if timetonew < 0:
        circs.append(Circword(random.choice(words)))
        timetonew = 1000
    # pygame.draw.circle(sc, LBLUE, (x1, y1), r)
    # pygame.draw.circle(sc, LBLUE, (x1, y2), r)
    #x1 -= 1
    delta = clock.tick(FPS)
    circ.update(delta)
    timetonew -= delta
    for c in circs:
        c.update(delta)
        c.draw(sc)
    circs = filter(lambda c: not c.died, circs)
    pygame.display.update()

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
    #     elif i.type == pygame.KEYDOWN:
    #         if i.key == pygame.K_LEFT:
    #             x -= 3
    #         elif i.key == pygame.K_RIGHT:
    #             x += 3

font = pygame.font.SysFont('arial', 100)
text = font.render('Game Over', 1, (0, 100, 0))
place = text.get_rect(center=(W / 2, H / 2))
sc.blit(text, place)

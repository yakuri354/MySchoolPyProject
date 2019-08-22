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
close = 0
lastwords = []
func = 0
letter = None
keypressed = 'a'
lastletter = 1
pressed = False



class Circword:
    def __init__(self, word):
        self.word = word
        self.x = x1
        self.y = random.randint(0, H)

    def update(self, t):
        self.x -= t / 1000
        self.x = int(self.x)

    def draw(self, sc):
        pygame.draw.circle(sc, LBLUE, (self.x, self.y), r)
        pygame.font.SysFont('arial', 20)
        font = pygame.font.Font(None, 72)
        text = font.render(self.word, 1, (0, 100, 0))
        place = text.get_rect(center=(self.x, self.y))
        lastwords.append(self.word)
        sc.blit(text, place)


circ = Circword(random.choice(words))


while inf:
    sc.fill(WHITE)
    circ.draw(sc)
    if timetonew < 0:
        circs.append(Circword(random.choice(words)))
        timetonew = 6000
        letter = 0
    delta = clock.tick(FPS)
    circ.update(delta)
    timetonew -= delta
    for c in circs:
        c.update(delta)
        c.draw(sc)
    circls = filter(lambda c: not c.died, circs)
    pygame.display.update()
    lastword = lastwords[0]
    letter = lastword[lastletter]
    if letter == None:
        letter = 'a'
    print('letter', letter)
    print('lastletter', lastletter)
    print('lastword', lastword)
    if keypressed == letter:
        if lastletter < 4:
            lastletter += 1
            print('You pressed the right key!')
        else:
            lastletter = 0
            lastwords.remove(0)
            circs.remove(0)
            print('The word is complete! Next word is', lastwords[0])
    # else:
    #     print('nah')
    #     pressed = False



    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()


        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_ESCAPE:
                inf = False
            else:
                keypressed = i.unicode
                pressed = True


while close < 2000:
    pygame.display.update()
    sc.fill(WHITE)
    font = pygame.font.SysFont('arial', 100)
    text = font.render('Game Over', 1, (0, 100, 0))
    place = text.get_rect(center=(W / 2, H / 2))
    sc.blit(text, place)
    pygame.time.delay(1)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
    close += 1

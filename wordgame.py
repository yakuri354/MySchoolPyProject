import random

import pygame

FPS = 60
W = 600
H = 400
WHITE = (255, 255, 255)
LBLUE = (122, 184, 225)
infinity = True

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
words = ['fine', 'test', 'good', 'nope', 'maze', 'dictionary', 'record', 'follow', 'cause', 'voter', 'bold',
         'residence',
         'extreme', 'master', 'cupboard', 'tendency', 'minimum', 'weapon', 'front', 'perfume', 'cane', 'length',
         'sunrise', 'general', 'breakfast', 'circulate', 'appreciate', 'question', 'pour', 'blue', 'jean', 'ghost',
         'aloof', 'initiative', 'constituency', 'reasonable', 'background']
circs = []
close = 0
lastwords = []
func = 0
letter = None
keypressed = 'a'
lastletter = 1
pressed = False
lastword = None
lastwordscount = 0


class Circword:
    def __init__(self, word):
        self.word = word
        self.x = x1
        self.y = random.randint(0, H)
        self.died = False
        lastwords.append(self.word)
    def update(self, t):
        self.x -= t / 1000
        self.x = int(self.x)

    def draw(self, sc):
        pygame.draw.circle(sc, LBLUE, (self.x, self.y), r)
        pygame.font.SysFont('arial', 20)
        font = pygame.font.Font(None, 72)
        text = font.render(self.word, 1, (0, 100, 0))
        place = text.get_rect(center=(self.x, self.y))
        sc.blit(text, place)
        if self.x == 0:
            global inf
            print("X =", self.x)
            print(inf)
            inf = False



while inf:
    pygame.display.update()
    sc.fill(WHITE)
    if timetonew <= 0:
        circs.append(Circword(random.choice(words)))
        timetonew = 2500
        letter = 0
    delta = clock.tick(FPS)
    # circ.update(delta)
    timetonew -= delta
    for c in circs:
        c.update(delta)
        c.draw(sc)
    # circs = filter(lambda c: c.died, circs)
    print('letter', letter)
    print('lastletter', lastletter)
    print('lastword', lastword)
    lastwordscount = len(lastwords)
    if lastwordscount > 0:
        lastword = lastwords[0]
        letter = lastword[lastletter]
    if letter == None:
        letter = 'a'
    print('letter', letter)
    print('lastletter', lastletter)
    print('lastword', lastword)
    wordlen = len(lastword) - 1
    if keypressed == letter:
        lastwordscount = len(lastwords)
        if lastletter < wordlen and lastwordscount > 0:
            lastletter += 1
            print('You pressed the right key!')
        elif lastletter >= wordlen and lastwordscount > 0:
            lastletter = 0
            print('lastwords', lastwords)
            print(lastwordscount)
            lastwords = lastwords[1:]
            circs = circs[1:]
            # print('The word is complete! Next word is', lastwords[0])
    #
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

while infinity:
    pygame.display.update()
    sc.fill(WHITE)


    def drawtext(x, y, font, size, text):
        font = pygame.font.SysFont(font, size)
        text = font.render(text, 1, (0, 100, 0))
        place = text.get_rect(center=(x, y))
        sc.blit(text, place)


    drawtext(W / 2, H / 2, 'arial', 100, 'Game over!')
    drawtext(W / 2, H / 2 + 70, 'arial', 30, 'Press Esc to exit or E to restart')
    pygame.time.delay(1)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_ESCAPE:
                exit()
            elif i.key == pygame.K_e:
                pass

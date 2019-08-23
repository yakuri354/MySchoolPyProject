import random

import pygame

gamemodetext = 'Normal'
gamemode = 3
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
         'aloof', 'initiative', 'reasonable', 'background']
impossible_words = ['television', 'literature', 'laboratory',
                    'incredible', 'compliance',
                    'engagement', 'reasonable',
                    'exaggerate', 'prediction', 'houseplant',
                    'relaxation', 'correspond']
very_easy_words = ['bill', 'jump', 'rest', 'seat', 'mess', 'miss', 'mold', 'stun', 'skin', 'deep', 'pawn', 'read',
                   'bike']
rightkeys = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
             'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
             'w', 'x', 'y', 'z')
circspeed = 1
circs = []
close = 0
lastwords = []
func = 0
letter = None
keypressed = '$'
lastletter = 1
pressed = False
lastword = None
lastwordscount = 0
starting = True
score = 0
errors = 0
currentword = ''
if gamemode == 5:
    words = words[:11]
    words = words + impossible_words
elif gamemode == 1:
    words = words + very_easy_words


def drawtext(x, y, font, size, text):
    font = pygame.font.SysFont(font, size)
    text = font.render(text, 1, (0, 100, 0))
    place = text.get_rect(center=(x, y))
    sc.blit(text, place)


def gmtext():
    global gamemode
    global gamemodetext
    if gamemode == 1:
        gamemodetext = 'Very Easy'
    elif gamemode == 2:
        gamemodetext = 'Easy'
    elif gamemode == 3:
        gamemodetext = 'Normal'
    elif gamemode == 4:
        gamemodetext = 'Hard'
    elif gamemode == 5:
        gamemodetext = 'Impossible'


def setspeed():
    global gamemode
    global circspeed
    if gamemode == 1:
        circspeed = 0.75
    elif gamemode == 2:
        circspeed = 0.85
    elif gamemode == 3:
        circspeed = 1
    elif gamemode == 4:
        circspeed = 1.2
    elif gamemode == 5:
        circspeed = 1.3

while starting:
    pygame.display.update()
    sc.fill(WHITE)
    setspeed()
    gmtext()
    drawtext(W / 2, H / 2, 'arial', 70, 'Press E to start')
    drawtext(W / 2, H / 2 + 100, 'arial', 70, '<-' + gamemodetext + '->')
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            print('Quitting via exit()')
            exit()
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_ESCAPE:
                print('Esc is pressed. Quitting via exit()')
                exit()
            elif i.key == pygame.K_e or i.key == pygame.K_KP_ENTER:
                print('Start!')
                starting = False
            elif i.key == pygame.K_LEFT:
                if gamemode > 1:
                    gamemode -= 1
                gmtext()
                print('New gamemode is ' + str(gamemode) + ' ' + gamemodetext)
                drawtext(W / 2, H / 2 + 100, 'arial', 70, '<' + gamemodetext + '>')

            elif i.key == pygame.K_RIGHT:
                if gamemode < 5:
                    gamemode += 1
                gmtext()
                print('New gamemode is ' + str(gamemode) + ' ' + gamemodetext)
                drawtext(W / 2, H / 2 + 100, 'arial', 70, '<' + gamemodetext + '>')

class Circword:
    def __init__(self, word):
        global circspeed
        self.word = word
        self.x = x1
        self.y = random.randint(20, H - 20)
        self.died = False
        self.speed = circspeed
        lastwords.append(self.word)

    def update(self, t):
        self.x -= t / 1000 * self.speed
        self.x = int(self.x)

    def draw(self, sc):
        pygame.draw.circle(sc, LBLUE, (self.x, self.y), r)
        font = pygame.font.Font(None, 200 // len(self.word))
        text = font.render(self.word, 1, (0, 100, 0))
        place = text.get_rect(center=(self.x, self.y))
        sc.blit(text, place)
        if self.x == 0:
            global inf
            print("X =", self.x)
            print(inf)
            inf = False


class Bullet():
    def __init__(self, sc, target, x=W / 2, y=20):
        self.x = x
        self.y = y
        self.t = target
        self.sc = sc

    def draw(self):
        pygame.draw.circle(sc, (0, 0, 0), (self.x, self.y), 10)

    def update(self, t):
        self.x = (self.x - self.t.x) * 10 * (t / 1000)
        self.y = (self.x - self.t.y) * 10 * (t / 1000)
        self.x = int(self.x)
        self.y = int(self.y)
        if self.t.x - self.x <= 27 or self.t.y - self.y <= 27:
            pass
while inf:
    pygame.display.update()
    sc.fill(WHITE)
    if timetonew <= 0:
        # circs.append(Circword(random.choice(words)))
        random.shuffle(words)
        circs.append(Circword((words[3])))
        if gamemode == 2 or 1:
            timetonew = 3200
        elif gamemode == 3:
            timetonew = 2500
        elif gamemode == 4 or 5:
            timetonew = 2000
        letter = 0
    delta = clock.tick(FPS)
    # circ.update(delta)
    timetonew -= delta
    for c in circs:
        c.update(delta)
        c.draw(sc)
    drawtext(W / 7, H / 7, 'arial', 40, str(score))
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
    drawtext(W / 2, 20, 'arial', 40, currentword)
    if keypressed in rightkeys:
        currentword += keypressed
        print(currentword)
        print('"', keypressed, '"')

    if keypressed == ' ':
        if currentword in words:
            circs = list(filter(lambda c: currentword != c.word, circs))
            currentword = ''

        else:
            currentword = ''

    # if keypressed == letter:
    #     score += 1
    #     lastwordscount = len(lastwords)
    #     if lastletter < wordlen and lastwordscount > 0:
    #         lastletter += 1
    #         print('You pressed the right key!')
    #     elif lastletter >= wordlen and lastwordscount > 0:
    #         lastletter = 0
    #         print('lastwords', lastwords)
    #         print(lastwordscount)
    #         lastwords = lastwords[1:]
    #         circs = circs[1:]
    #         # print('The word is complete!)s
    # elif keypressed != "$":
    #     print('Error!')
    #     score -= 2
    #     errors += 1

    #     pressed = False

    keypressed = '$'
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            print("QUIT is received. Exiting via exit()")
            exit()



        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_F12:
                inf = False
            else:
                keypressed = i.unicode
                pressed = True

print('Game Over!')

while infinity:
    pygame.display.update()
    sc.fill(WHITE)


    def drawtext(x, y, font, size, text):
        font = pygame.font.SysFont(font, size)
        text = font.render(text, 1, (0, 100, 0))
        place = text.get_rect(center=(x, y))
        sc.blit(text, place)


    drawtext(W / 2, H / 2, 'arial', 100, 'Game over!')
    drawtext(W / 2, H / 2 + 70, 'arial', 30, 'Press Esc to exit')
    drawtext(W / 2, H / 2 + 100, 'arial', 25, 'Your score is ' + str(score))
    if errors == 0 and score > 1:
        drawtext(W / 2, H / 2 + 150, 'arial', 25, 'You did no errors!')
    elif errors == 1:
        drawtext(W / 2, H / 2 + 150, 'arial', 25, 'You did 1 error!')
    else:
        drawtext(W / 2, H / 2 + 150, 'arial', 25, 'You did ' + str(errors) + ' errors!')
    pygame.time.delay(1)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_ESCAPE:
                print('Esc is pressed. Quitting via exit()')
                exit()
            elif i.key == pygame.K_e:
                print('Feature not added yet')
                pass

import random

import pygame

gamemodetext = 'Normal'
gamemode = 3
FPS = 60
W = 1200
H = 800
BGROUND = (68, 36, 52)
LBLUE = (122, 184, 225)
TEXTCOLOR = (89, 125, 206)
CIRCTEXTCOLOR = (2, 164, 211)
infinity = True
font1 = 'font.ttf'

pygame.init()
pygame.font.init()
sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
timetonew = 0
y1 = 55
y2 = 150
x1 = 1150
r = 46
inf = True
words = ['fine', 'test', 'good', 'nope', 'maze', 'dictionary', 'record', 'follow', 'cause', 'voter', 'bold',
         'residence',
         'extreme', 'master', 'cupboard', 'tendency', 'minimum', 'weapon', 'front', 'perfume', 'cane', 'length',
         'sunrise', 'general', 'breakfast', 'circulate', 'appreciate', 'question', 'pour', 'blue', 'jean', 'ghost',
         'aloof', 'initiative', 'reasonable', 'background', 'sweater', 'earthflax', 'copy', 'feeling', 'free', 'mail',
         'carrier', 'galaxy', 'election', 'reproduce', 'change', 'trap', 'ticket', 'flour', 'loan', 'place', 'despise',
         'runner', 'ranch', 'advance', 'repetition', 'human', 'body', 'society', 'conventional', 'pair', 'twist',
         'minimize',
         'balance', 'drum', 'staircase', 'touch', 'grant', 'electronics', 'vigorous', 'floor', 'effective', 'scatter',
         'yearn', 'motorist', 'fraud', 'swipe'
         ]
impossible_words = ['television', 'literature', 'laboratory',
                    'incredible', 'compliance',
                    'engagement', 'reasonable',
                    'exaggerate', 'prediction', 'houseplant',
                    'relaxation', 'correspond']
very_easy_words = ['bill', 'jump', 'rest', 'seat', 'mess', 'miss',
                   'mold', 'stun', 'skin', 'deep', 'pawn', 'read', 'bike']
rightkeys = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
             'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
             'w', 'x', 'y', 'z')
random.shuffle(words)
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
bullet = None
isdebug = False
wordnumber = 0
lettersentered = 0
play_time = 0


def drawtext(x, y, size, text):
    global font1
    font = pygame.font.Font(font1, size)
    text = font.render(text, 1, (TEXTCOLOR))
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
        circspeed = 0.6
    elif gamemode == 2:
        circspeed = 0.6
    elif gamemode == 3:
        circspeed = 1
    elif gamemode == 4:
        circspeed = 1.2
    elif gamemode == 5:
        circspeed = 1.3


while starting:
    pygame.display.update()
    sc.fill(BGROUND)
    setspeed()
    gmtext()
    drawtext(W / 2, H / 2 - 20, 70, 'Press E to start')
    drawtext(W / 2, H / 2 + 100, 70, '<-' + gamemodetext + '->')
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            print('Quitting via exit()')
            exit()
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_ESCAPE:
                print('Esc is pressed. Quitting via exit()')
                exit()
            elif i.key == pygame.K_e or i.key == pygame.K_KP_ENTER:
                starting = False
                print('Start!')
            elif i.key == pygame.K_INSERT:
                isdebug = True
                print('Debug mode on!')
            elif i.key == pygame.K_LEFT:
                if gamemode > 1:
                    gamemode -= 1
                gmtext()
                print('New gamemode is ' + str(gamemode) + ' ' + gamemodetext)
                drawtext(W / 2, H / 2 + 100, 70, '<' + gamemodetext + '>')

            elif i.key == pygame.K_RIGHT:
                if gamemode < 5:
                    gamemode += 1
                gmtext()
                print('New gamemode is ' + str(gamemode) + ' ' + gamemodetext)
                drawtext(W / 2, H / 2 + 100, 70, '<' + gamemodetext + '>')

if gamemode == 5:
    words = words[:11]
    words = words + impossible_words
elif gamemode == 1:
    words = words[:5]
    print(words)
    print(very_easy_words)
    words = words + very_easy_words


class Circword(pygame.sprite.Sprite):
    def __init__(self, word, size=27, filename='bubble.png'):
        global circspeed
        pygame.sprite.Sprite.__init__(self)
        self.word = word
        self.x = x1
        self.size = int(size * len(self.word))

        self.y = random.randint(self.size // 2, H - self.size // 2)
        self.died = False
        self.speed = circspeed / len(self.word) * 350
        lastwords.append(self.word)
        self.image = pygame.transform.scale(pygame.image.load(filename).convert_alpha(), (self.size, self.size))

    def update(self, t):

        self.x -= t / 1000 * self.speed

    def draw(self, sc):
        global isdebug
        pygame.sprite.Sprite.__init__(self)
        global TEXTCOLOR
        x = int(self.x)
        rect = self.image.get_rect(center=(x, self.y))
        font = pygame.font.Font('font.ttf', self.size // 5)
        text = font.render(self.word, 1, (CIRCTEXTCOLOR))
        place = text.get_rect(center=(x, self.y))
        sc.blit(self.image, rect)
        sc.blit(text, place)
        if x <= 10 and isdebug == False:
            global inf
            print(inf)
            inf = False


class Bullet():
    def __init__(self, sc, target, x=W / 2, y=20):
        self.x = x
        self.y = y
        self.t = target
        self.sc = sc
        self.died = False

    def draw(self):
        pygame.draw.circle(sc, (208, 70, 72), (int(self.x), int(self.y)), 10)

    def update(self, t):
        global lettersentered
        global score
        global circs
        self.x += (self.t.x - self.x) * 10 * (t / 1000)
        self.y += (self.t.y - self.y) * 10 * (t / 1000)
        if self.t.x - self.x <= 2 and self.t.y - self.y <= 2:
            self.died = True
            circs = list(filter(lambda c: self.t.word != c.word, circs))
            circs = list(filter(lambda c: self.t.word != c.word, circs))
            score += len(self.t.word)


setspeed()
if gamemode == 2 or 1:
    timetonew = 3200
elif gamemode == 3:
    timetonew = 2500
elif gamemode == 4 or 5:
    timetonew = 2000
while inf:

    pygame.display.update()
    sc.fill(BGROUND)
    delta = clock.tick(FPS)
    play_time += delta
    timetonew -= delta
    if timetonew <= 0:
        if wordnumber >= int(len(words) - 1):
            random.shuffle(words)
            wordnumber = 0
        circs.append(Circword((words[wordnumber])))
        wordnumber += 1
        if gamemode == 2 or 1:
            timetonew = 3200
        elif gamemode == 3:
            timetonew = 2500
        elif gamemode == 4 or 5:
            timetonew = 2000
        letter = 0

    for c in circs:
        c.update(delta)
        c.draw(sc)
    if bullet is not None:
        bullet.update(delta)
        bullet.draw()
        if bullet.died:
            bullet = None
    drawtext(W / 7, H / 7, 40, str(int((score / play_time * 1000 * 60) // 1)) + 'Char/min')
    print('letter', letter)
    print('lastletter', lastletter)
    print('lastword', lastword)
    lastwordscount = len(lastwords)
    if lastwordscount > 0:
        lastword = lastwords[0]
        letter = lastword[lastletter]
    if letter is None:
        letter = 'a'
    print('letter', letter)
    print('lastletter', lastletter)
    print('lastword', lastword)
    drawtext(W / 2, 20, 40, currentword)
    if keypressed in rightkeys:
        currentword += keypressed
        print(currentword)
        print('"', keypressed, '"')

    if keypressed == ' ':
        if currentword in [c.word for c in circs]:
            bullet = Bullet(sc, list(filter(lambda c: currentword == c.word, circs))[0])
            currentword = ''

        else:
            currentword = ''
            errors += 1

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
    sc.fill(BGROUND)
    drawtext(W / 2, H / 2, 100, 'Game over!')
    drawtext(W / 2, H / 2 + 70, 30, 'Press Esc to exit')
    drawtext(W / 2, H / 2 + 100, 25, 'Your score is ' + str(score))
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

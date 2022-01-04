import pygame as pg
import sys
import random
import operator
import login
log = False
while not log:
    reg = input("Would you like to create account (c), login (l), or play as guest (g)?\n")

    if reg == 'c':
        login.registry()

    if reg == 'l':
        username = login.login()
        if username == False:
            print("Username or password is inccorrect\n")
        else:
            log = True
            guest = False

    if reg == 'g':
        guest = True
        log = True

ops = {'+': operator.add, '-': operator.sub,
       '*': operator.mul,'/': operator.truediv}

pg.init()
clock = pg.time.Clock()
screen = pg.display.set_mode([800,500])
font = pg.font.Font(None,35)
font2 = pg.font.Font(None,80)
font3 = pg.font.Font(None,50)

anstxt = ''
newproblem = True
correct = 0
incorrect = 0
operation = ('+','-','*','/')
state = 'settings'
numbers = ('0987654321-.')
nonprimes = (4,6,8,10)
ansinput = ''
color = [0,255,0]
score = 0
globalspeed = 1000

start_button = pg.Rect(300,250,200,50)
player = pg.Rect(375,225,50,50)
spawnpos = ('','top','bot','left','right')

def respawn(amount,default=1):
    for i in range(default,amount):
        spawn = spawnpos[i]
        if spawn == 'left' or spawn == 'right':
            globals()[f"y{i}"] = random.randint(0,500)
            if spawn == 'left':
                globals()[f"x{i}"] = -50
            if spawn == 'right':
                globals()[f"x{i}"] = 800
        if spawn == 'top' or spawn == 'bot':
            globals()[f"x{i}"] = random.randint(0,800)
            if spawn == 'top':
                globals()[f"y{i}"] = -50
            if spawn == 'bot':
                globals()[f"y{i}"] = 500
        globals()[f"rect{i}"] = pg.Rect(globals()[f"x{i}"], globals()[f"y{i}"], 50, 50)
        globals()[f"xspd{i}"] = (375-globals()[f"x{i}"])/globalspeed
        globals()[f"yspd{i}"] = (225-globals()[f"y{i}"])/globalspeed
        globals()[f"op{i}"] = random.choice(operation)
        if globals()[f"op{i}"] == '/':
            globals()[f"1num{i}"] = random.randint(1, 10)
            if globals()[f"1num{i}"] != 1:
                globals()[f"2num{i}"] = random.randint(1, globals()[f"1num{i}"])
                while not float(globals()[f"1num{i}"]/globals()[f"2num{i}"]).is_integer():
                    globals()[f"2num{i}"] = random.randint(1, globals()[f"1num{i}"])
            else:
                globals()[f"2num{i}"] = 1
        else:
            globals()[f"1num{i}"] = random.randint(0, 10)
            globals()[f"2num{i}"] = random.randint(0, 10)
        globals()[f"newans{i}"] = True

respawn(5)

while True:
    screen.fill((0, 0, 0))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()

        if state == 'settings' or state == 'gameover':
            if event.type == pg.MOUSEBUTTONDOWN:
                mousepos = event.pos
                if start_button.collidepoint(mousepos):
                    score = 0
                    scorewritten = False
                    state = 'test'

        if state == 'test':
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_BACKSPACE:
                    anstxt = anstxt[:-1]
                elif event.key == pg.K_RETURN:
                    ansinput = anstxt
                    anstxt = ''
                if event.unicode in numbers:
                    anstxt += event.unicode

    if state == 'test':
        ans_surface = font.render(anstxt, True, (255, 255, 255))
        screen.blit(ans_surface, (380, 200))
        pg.draw.rect(screen, color, player)

        if newproblem == True:
            num1 = random.randint(1,15)
            num2 = random.randint(1,15)
            op = random.choice(operation)
            if op == '+':
                ans = num1+num2
            if op == '-':
                ans = num1-num2
            if op == '*':
                ans = num1*num2
            newproblem = False

        for i in range(1,5):
            globals()[f"x{i}"] += globals()[f"xspd{i}"]
            globals()[f"y{i}"] += globals()[f"yspd{i}"]
            globals()[f"rect{i}"] = pg.Rect(globals()[f"x{i}"], globals()[f"y{i}"], 50, 50)
            pg.draw.rect(screen, [255,255,255], globals()[f"rect{i}"])
            question_surface = font.render(str(globals()[f"1num{i}"]) + " " + globals()[f"op{i}"] + " " + str(globals()[f"2num{i}"]), True, (255, 255, 255))
            screen.blit(question_surface, (globals()[f"x{i}"], globals()[f"y{i}"]+55))
            if ansinput == str(int(ops[globals()[f"op{i}"]](globals()[f"1num{i}"],globals()[f"2num{i}"]))):
                score += 1
                globalspeed -= 10
                respawn(i+1,i)

            if player.colliderect(globals()[f"rect{i}"]):
                globalspeed = 1000
                anstxt = ''
                ansinput = ''
                respawn(5)
                state = 'gameover'
        score_surface = font.render("Score: " + str(score), True, (255, 255, 255))
        screen.blit(score_surface, (650, 10))

    if state == 'settings':
        pg.draw.rect(screen, [255,255,255], start_button)
        start = font2.render('Start', True, (0, 0, 0))
        screen.blit(start,(335,250))
        title = font2.render('Math Attack', True, (255, 255, 255))
        screen.blit(title, (240, 40))

    if state == 'gameover':
        pg.draw.rect(screen, [255,255,255], start_button)
        gotext = start = font2.render('Game Over!', True, (255, 255, 255))
        screen.blit(gotext,(250,30))
        playagain = font.render('Play Again', True, (0, 0, 0))
        screen.blit(playagain, (335, 260))
        finalscore = font.render('Score: '+str(score), True, (255, 255, 255))
        screen.blit(finalscore, (335, 150))
        if not guest:
            counter = 0
            existing = False
            if not scorewritten:
                scores = open('scores.txt', 'r')
                for line in scores:
                    s = line.split()
                    if username in s:
                        existing = True
                        oldscore = s[1]
                        scores.close()
                        break
                    if not existing:
                        counter += 1
                if existing:
                    scores = open('scores.txt', 'r')
                    lines = scores.readlines()
                    scores.close()
                    lines[counter] = str(username + ' ' + str(score) + '\n')
                    if int(oldscore) < score:
                        scores = open('scores.txt', 'w')
                        for line in lines:
                            scores.write(line)
                        scores.close()
                    scorewritten = True

                if not existing:
                    scores.close()
                    scores = open('scores.txt', 'a')
                    scores.write(username + ' ' + str(score) + '\n')
                    scores.close()
                    scorewritten = True

    pg.display.flip()

    clock.tick(60)
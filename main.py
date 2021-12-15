import pygame as pg
import sys
import random

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
operation = ('+','-','*')
state = 'test'
numbers = ('0987654321')
ansinput = ''

start_button = pg.Rect(300,250,200,50)
practice_button = pg.Rect(100,100,150,50)
test_button = pg.Rect(550,100,150,50)
back_button = pg.Rect(50,400,150,50)
player = pg.Rect(375,225,50,50)

spawnpos = ('top','bot','left','right')

for i in range(1,11):
    spawn = random.choice(spawnpos)
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
    globals()[f"xspd{i}"] = (375-globals()[f"x{i}"])/1000
    globals()[f"yspd{i}"] = (225-globals()[f"y{i}"])/1000
    globals()[f"1num{i}"] = random.randint(0,10)
    globals()[f"2num{i}"] = random.randint(0,10)
    globals()[f"newans{i}"] = True

while True:
    screen.fill((0, 0, 0))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()

        if state == 'settings':
            if event.type == pg.MOUSEBUTTONDOWN:
                mousepos = event.pos
                if start_button.collidepoint(mousepos):
                    state = 'game'
                if practice_button.collidepoint(mousepos):
                    state = 'game'
                if test_button.collidepoint(mousepos):
                    state = 'game'

        if state == 'test':
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_BACKSPACE:
                    anstxt = anstxt[:-1]
                elif event.key == pg.K_RETURN:
                    ansinput = anstxt
                if event.unicode in numbers:
                    anstxt += event.unicode

    if state == 'test':
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

        for i in range(1,2):
            globals()[f"x{i}"] += globals()[f"xspd{i}"]
            globals()[f"y{i}"] += globals()[f"yspd{i}"]
            globals()[f"rect{i}"] = pg.Rect(globals()[f"x{i}"], globals()[f"y{i}"], 50, 50)
            pg.draw.rect(screen, [255,255,255], globals()[f"rect{i}"])
            question_surface = font.render(str(globals()[f"1num{i}"]) + " + " + str(globals()[f"2num{i}"]), True, (255, 255, 255))
            screen.blit(question_surface, (globals()[f"x{i}"], globals()[f"y{i}"]+55))
            if ansinput == str(globals()[f"1num{i}"] + globals()[f"2num{i}"]):
                anstxt = ''
                globals()[f"1num{i}"] = random.randint(0, 10)
                globals()[f"2num{i}"] = random.randint(0, 10)
                spawn = random.choice(spawnpos)
                if spawn == 'left' or spawn == 'right':
                    globals()[f"y{i}"] = random.randint(0, 500)
                    if spawn == 'left':
                        globals()[f"x{i}"] = -50
                    if spawn == 'right':
                        globals()[f"x{i}"] = 800
                if spawn == 'top' or spawn == 'bot':
                    globals()[f"x{i}"] = random.randint(0, 800)
                    if spawn == 'top':
                        globals()[f"y{i}"] = -50
                    if spawn == 'bot':
                        globals()[f"y{i}"] = 500
                globals()[f"xspd{i}"] = (375 - globals()[f"x{i}"]) / 1000
                globals()[f"yspd{i}"] = (225 - globals()[f"y{i}"]) / 1000

        ans_surface = font.render(anstxt, True, (255, 255, 255))
        screen.blit(ans_surface, (380, 200))
        pg.draw.rect(screen,[0,255,0],player)

    if state == 'settings':
        pg.draw.rect(screen, [255,255,255], start_button)
        pg.draw.rect(screen, [255,255,255], practice_button)
        pg.draw.rect(screen, [255, 255, 255], test_button)
        start = font2.render('Start', True, (0, 0, 0))
        test = font2.render('Test', True, (0, 0, 0))
        practice = font3.render('Practice', True, (0, 0, 0))
        screen.blit(start,(335,250))
        screen.blit(test, (115, 100))
        screen.blit(practice, (555, 110))

    if state == 'game':

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

        pg.draw.rect(screen, [255, 255, 255], back_button)
        back = font2.render('Back', True, (0, 0, 0))
        screen.blit(back, (55, 400))

        ans_surface = font.render(anstxt,True,(255,255,255))
        screen.blit(ans_surface,(380,200))

        question_surface = font.render(str(num1)+" "+op+" "+str(num2),True,(255,255,255))
        screen.blit(question_surface, (380,10))

        correct_surface = font.render(str("Correct: ") + str(correct), True, (255, 255, 255))
        screen.blit(correct_surface, (600, 10))

        incorrect_surface = font.render(str("Incorrect: ") + str(incorrect), True, (255, 255, 255))
        screen.blit(incorrect_surface, (600, 30))

    pg.display.flip()

    clock.tick(60)
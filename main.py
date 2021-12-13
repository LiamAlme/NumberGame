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
state = 'settings'

start_button = pg.Rect(300,250,200,50)
practice_button = pg.Rect(100,100,150,50)
test_button = pg.Rect(550,100,150,50)
back_button = pg.Rect(50,400,150,50)

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

        if state == 'game':
            if event.type == pg.MOUSEBUTTONDOWN:
                mousepos = event.pos
                if back_button.collidepoint(mousepos):
                    state = 'settings'
                    correct = 0
                    incorrect = 0
                    newproblem = True
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_BACKSPACE:
                    anstxt = anstxt[:-1]
                elif event.key == pg.K_RETURN:
                    if anstxt == str(ans):
                        correct += 1
                        newproblem = True
                    else:
                        incorrect += 1
                        newproblem = True
                    anstxt = ''
                else:
                    anstxt += event.unicode

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
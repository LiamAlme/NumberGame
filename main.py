import pygame as pg
import sys
import random

pg.init()
clock = pg.time.Clock()
screen = pg.display.set_mode([800,500])
font = pg.font.Font(None,35)
font2 = pg.font.Font(None,80)

anstxt = ''
newproblem = True
correct = 0
incorrect = 0
operation = ('+','-','*')
state = 'settings'

start_button = pg.Rect(300,250,200,50)
problem_amount_display = pg.Rect(325,120,150,50)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()

        if state == 'settings':
            if event.type == pg.MOUSEBUTTONDOWN:
                mousepos = event.pos
                if start_button.collidepoint(mousepos):
                    state = 'game'



        if state == 'game':
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
        pg.draw.rect(screen, [255,255,255], problem_amount_display)
        pg.draw.polygon(screen, [255,255,255], [(290, 145), (310, 125), (310, 165)])
        pg.draw.polygon(screen, [255, 255, 255], [(490, 125), (490, 165), (510, 145)])
        start = font2.render('Start', True, (0, 0, 0))
        screen.blit(start,(335,250))

    if state == 'game':
        if newproblem == True:
            num1 = random.randint(0,10)
            num2 = random.randint(0,10)
            op = random.choice(operation)
            if op == '+':
                ans = num1+num2
            if op == '-':
                ans = num1-num2
            if op == '*':
                ans = num1*num2
            newproblem = False

        screen.fill((0, 0, 0))

        ans_surface = font.render(anstxt,True,(255,255,255))
        screen.blit(ans_surface,(380,200))

        question_surface = font.render(str(num1)+" "+op+" "+str(num2),True,(255,255,255))
        screen.blit(question_surface, (380,10))

        correct_surface = font.render(str("Correct: ") + str(correct), True, (255, 255, 255))
        screen.blit(correct_surface, (650, 10))

        incorrect_surface = font.render(str("Incorrect: ") + str(incorrect), True, (255, 255, 255))
        screen.blit(incorrect_surface, (650, 30))

    pg.display.flip()

    clock.tick(60)
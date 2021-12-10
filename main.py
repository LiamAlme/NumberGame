import pygame as pg
import random

pg.init()
clock = pg.time.Clock()
screen = pg.display.set_mode([800,500])
font = pg.font.Font(None,32)
anstxt = ''
newproblem = True
correct = 0
incorrect = 0

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_BACKSPACE:
                anstxt = anstxt[:-1]
            elif event.key == pg.K_RETURN:
                anstxt = ''
                if anstxt == str(ans):
                    correct += 1
                    newproblem = True
                else:
                    incorrect += 1
                    newproblem = True
            else:
                anstxt += event.unicode


    if newproblem == True:
        num1 = random.randint(0,10)
        num2 = random.randint(0,10)
        ans = num1+num2
        newproblem = False

    screen.fill((0, 0, 0))

    ans_surface = font.render(anstxt,True,(255,255,255))
    screen.blit(ans_surface,(380,200))

    question_surface = font.render(str(num1)+str(' + ')+str(num2),True,(255,255,255))
    screen.blit(question_surface, (380,10))

    correct_surface = font.render(str("Correct: ") + str(correct), True, (255, 255, 255))
    screen.blit(correct_surface, (650, 10))

    incorrect_surface = font.render(str("Incorrect: ") + str(incorrect), True, (255, 255, 255))
    screen.blit(incorrect_surface, (650, 30))

    pg.display.flip()

    clock.tick(60)
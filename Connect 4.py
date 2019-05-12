import pygame
from pygame.locals import *
from pygame import gfxdraw
pygame.init()
#Defining constants
WHITE = (255, 219, 219)
LIGHTBLUE = (0, 102, 204)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
CADETBLUE = (95,158,160)
TURNCOLOURS = (RED, YELLOW)
players = ("Red", "Yellow")
pygame.display.set_caption("Connect 4")
display_width = 600
turn_number = 1 #Red's turn
display_height = int(display_width/7*6)
screen = pygame.display.set_mode((display_width, display_height + 100))
screen.fill(WHITE)
box_length = display_width/7
game_end = False
x_coord_list = [[int(display_width*x/7), int(display_width*(x+1)/7)] for x in range(7)]
y_coord_list = [[int((display_height*(x/6)) + 100), int((display_height*((x+1)/6))+ 100)] for x in range(6)][::-1]
#restart button
pygame.draw.rect(screen, CADETBLUE, pygame.Rect(530 ,0 , 70, 20))
myfont = pygame.font.SysFont('Comic Sans MS', 15)
textsurface = myfont.render('Restart', True, (0, 0, 0))
screen.blit(textsurface,(540,0))
done = False
game_state = [[0 for x in range(7)] for y in range(6)]
def drawCircle(x, y, r, colour):
    pygame.gfxdraw.aacircle(screen, x, y, r, colour)
    pygame.gfxdraw.filled_circle(screen, x, y, r, colour)
def resetPlayArea():
    pygame.draw.rect(screen, LIGHTBLUE, pygame.Rect(0, 100, display_width, display_height))
    for x in range(1, 8):
        for y in range(1, 7):
            drawCircle(int(display_width*x/7-box_length/2), int((display_height*y/6) +100 -box_length/2 ), 29, WHITE)

resetPlayArea()
def checkWin(lst):
   return lst == [1, 1, 1, 1] or lst == [2, 2, 2, 2]
print(game_state)
def checkWin2(x_pos, y_pos):
    check_win = [game_state[y_pos - y][x_pos] for y in range(4) if y_pos >=3] # check for win downwords
    if checkWin(check_win):
        return True
    for x in range(4): # check for win horizontally
        check_win = game_state[y_pos][x:x+4]
        #print(check_win)
        if checkWin(check_win):
            return True
    for y in range(4): # check for win diagonally negative gradient
        check_win = [game_state[y_pos+x-y][x_pos-x+y] for x in range(4) if y_pos+x-y <= 5 and y_pos+x-y>= 0 and x_pos-x+y>= 0 and x_pos-x+y<= 6]
        if checkWin(check_win):
            return True
    for y in range(4): # check for win diagonally positive gradient
        check_win = [game_state[y_pos+x-y][x_pos+x-y] for x in range(4) if y_pos+x+-y <= 5 and y_pos+x-y>= 0 and x_pos+x-y>= 0 and x_pos+x-y<= 6]
        #print(check_win)
        if checkWin(check_win):
            return True
def endGame(x):
    global game_end
    pygame.draw.rect(screen, WHITE, pygame.Rect(0, 25, display_width, 75))
    myfont = pygame.font.SysFont('Comic Sans MS', 25)
    if x == 'win':
        win_text = myfont.render('{player} wins'.format(player = players[turn_number - 1]), True, (0, 0, 0))
        screen.blit(win_text,(250,40))
    elif x == 'draw':
        win_text = myfont.render('Draw', True, (0, 0, 0))
        screen.blit(win_text,(275,40))
    game_end = True
while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        mos_x, mos_y = pygame.mouse.get_pos()
        for pos ,(x1, x2) in enumerate(x_coord_list):
            if mos_x>=x1 and mos_x<x2 and not game_end:
                x_pos = pos
                pygame.draw.rect(screen, WHITE, pygame.Rect(0, 25, display_width, 75))
                drawCircle(int((x1+x2)/2), int(100-(box_length/2)), 29, TURNCOLOURS[turn_number - 1])
                break #save a bit of time
        if event.type == MOUSEBUTTONDOWN :
            print(mos_x, mos_y)
            if mos_x>= 530 and mos_y<=20:
                resetPlayArea()
                game_end = False
                game_state = [[0 for x in range(7)] for y in range(6)]
                turn_number = 1
                continue
            if not game_end:
                for y_pos, y in enumerate(game_state):
                    if y[x_pos] == 0:
                        game_state[y_pos][x_pos] = turn_number
                        pygame.draw.rect(screen, WHITE, pygame.Rect(0, 25, display_width, 75))
                        for y_animation in range(5, y_pos, -1): #Animation
                            drawCircle(int((x_coord_list[x_pos][0]+x_coord_list[x_pos][1])/2 ), int((y_coord_list[y_animation][0]+y_coord_list[y_animation][1])/2 ), 29, TURNCOLOURS[turn_number - 1])
                            pygame.display.update()
                            pygame.time.wait(50)
                            drawCircle(int((x_coord_list[x_pos][0]+x_coord_list[x_pos][1])/2 ), int((y_coord_list[y_animation][0]+y_coord_list[y_animation][1])/2 ), 29, WHITE)
                            pygame.display.update()
                        #Draw actual placement
                        drawCircle(int((x_coord_list[x_pos][0]+x_coord_list[x_pos][1])/2 ), int((y_coord_list[y_pos][0]+y_coord_list[y_pos][1])/2 ), 30, TURNCOLOURS[turn_number - 1])
                        if checkWin2(x_pos, y_pos):
                            endGame('win')
                        if turn_number == 1:
                            turn_number = 2
                        elif turn_number ==2:
                            turn_number = 1
                        break
            #Draw detect
            pygame.event.clear(MOUSEBUTTONDOWN)
            raw_list = [x for y_set in game_state for x in y_set]
            if 0 not in raw_list:
                endGame('draw')

    pygame.display.update()
import pygame
from pygame.locals import *
import random # I copied this code from my snake game and edited abit of stuff
pygame.init()
done = False
BLACK = (0, 0, 0)
DARKGREEN = (0, 100, 0)
LAWNGREEN = (124, 252, 0)
RED = (255, 0, 0)
WHITE = (255, 219, 219)
SALMON = (250, 128, 114)
MAGENTA =  (255, 0, 255)
CYAN = (0,255,255)    
DEEPPINK = (255,20,147)
win_lose = [["Draw", 559], ["Cyan has lost", 495], ["Pink has lost", 505]] #Text and corresponding xcoords
pygame.display.set_caption("Tron")
display_width = 1200
display_height = 742
screen = pygame.display.set_mode((display_width, display_height))
screen.fill(BLACK)
pygame.draw.rect(screen, DARKGREEN, pygame.Rect(0, 0, display_width, 100))
grid_length = 10
grid_gap = 0
FPS = 30
clock = pygame.time.Clock()
x_coord_list = [x*(grid_length +grid_gap) + grid_gap for x in range(display_width//(grid_length + grid_gap))]
y_coord_list = [y*(grid_length +grid_gap) + grid_gap + 100 for y in range((display_height -100)//(grid_length + grid_gap))]
print(y_coord_list)
collide_value = 10101 # (can be any random number)works for all sides as the value will ref last value of x/y_coord_list exiting all sides
x_coord_list.append(collide_value) # holders so list index out of range error doesnt happen
y_coord_list.append(collide_value)
class Snake:
    def __init__(self, x, y, colour):
        self.x = x
        self.y = y
        self.colour = colour       
    def move(self):
        self.direction = [self.xchange, self.ychange]
        self.x += self.xchange
        self.y += self.ychange
        pygame.draw.rect(screen, self.colour, pygame.Rect(x_coord_list[self.x], y_coord_list[self.y], grid_length, grid_length))
print(y_coord_list)
def checkCollision():
    global lose
    draw = 0
    if stored_coords[-1] == stored_coords[-2]:
        lose = 0
        return True
    for x in stored_coords[:-3]: # check for collision with tail
        if [player1.x, player1.y] == x:
            lose = 1
            draw += 1
        if [player2.x, player2.y] == x:
            lose = 2
            draw += 1
        if lose != 3 and draw != 2:
            return True
        elif draw == 2:
            lose = 0
            return True
    draw = 0
    if x_coord_list[player1.x] == collide_value or y_coord_list[player1.y] == collide_value:
        lose = 1
        draw +=1
    if x_coord_list[player2.x] == collide_value or y_coord_list[player2.y] == collide_value:
        lose = 2
        draw += 1
    if lose != 3 and draw != 2:
            return True
    elif draw == 2:
        lose = 0
        return True
def loseWindow():
    pygame.draw.rect(screen, WHITE, pygame.Rect(445, 300, 300, 150))
    myfont = pygame.font.SysFont('Comic Sans MS', 30, True)
    textsurface = myfont.render(win_lose[lose][0], True, (0, 0, 0))
    screen.blit(textsurface,(win_lose[lose][1],340))
    pygame.draw.rect(screen, RED, pygame.Rect(560, 400, 75, 30))
    myfont = pygame.font.SysFont('Comic Sans MS', 15, True)
    textsurface = myfont.render('Restart', True, (0, 0, 0))
    screen.blit(textsurface,(570,405))
def buttonAnimationInit():
    pygame.draw.rect(screen, SALMON, pygame.Rect(560, 400, 75, 30))
    myfont = pygame.font.SysFont('Comic Sans MS', 15, True)
    textsurface = myfont.render('Restart', True, (0, 0, 0))
    screen.blit(textsurface,(570,405))
def buttonAnimationFinal():
    pygame.draw.rect(screen, RED, pygame.Rect(560, 400, 75, 30))
    myfont = pygame.font.SysFont('Comic Sans MS', 15, True)
    textsurface = myfont.render('Restart', True, (0, 0, 0))
    screen.blit(textsurface,(570,405))


def startGame():
    global stored_coords, lose, dt, game_end, player1, player2, start
    player1 = Snake((len(x_coord_list)-1)//8, (len(y_coord_list)-1)//2, CYAN)
    player2 = Snake(7*(len(x_coord_list)-1)//8, (len(y_coord_list)-1)//2, DEEPPINK)
    player1.xchange, player2.xchange, player1.ychange, player2.ychange = 1, -1, 0, 0
    lose = 3
    dt = 0
    player1.direction = [1,0]
    player2.direction = [-1,0]
    game_end = False
    start = False
    pygame.draw.rect(screen, BLACK, pygame.Rect(0, 100, display_width, display_height-100))
    myfont = pygame.font.SysFont('Comic Sans MS', 45, True)
    textsurface = myfont.render('Tron', True,  (146, 16, 0))
    screen.blit(textsurface,(545,30))
    player1.move()
    player2.move()
    stored_coords = [[player1.x, player1.y], [player2.x, player2.y]]

startGame()
while not done:
    dt += clock.tick(FPS)
    print(dt)
    if dt > 33 and start and not game_end:
        for player in [player1, player2]:
            player.move()
            stored_coords.append([player.x, player.y])
        
        if checkCollision():
            loseWindow()
            game_end = True
        dt = 0 
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        if game_end:
            mos_x, mos_y = pygame.mouse.get_pos()
            if mos_x > 560 and mos_x < 635 and mos_y < 430 and mos_y > 400:
                buttonAnimationInit()
                if event.type == MOUSEBUTTONDOWN:
                    startGame()
            else:
                buttonAnimationFinal()
        if event.type == pygame.KEYDOWN and not game_end:
            if event.key == K_SPACE:
                start = True
            if start:
                if event.key == K_LEFT and player2.direction[0] != 1:
                    player2.xchange = -1
                    player2.ychange = 0
                elif event.key == K_RIGHT and player2.direction[0] != -1:
                    player2.xchange = 1
                    player2.ychange = 0
                elif event.key == K_UP and player2.direction[1] != 1:
                    player2.ychange = -1
                    player2.xchange = 0
                elif event.key == K_DOWN and player2.direction[1] != -1:
                    player2.ychange = 1
                    player2.xchange = 0 
                if event.key == K_a and player1.direction[0] != 1:
                    player1.xchange = -1
                    player1.ychange = 0
                elif event.key == K_d and player1.direction[0] != -1:
                    player1.xchange = 1
                    player1.ychange = 0
                elif event.key == K_w and player1.direction[1] != 1:
                    player1.ychange = -1
                    player1.xchange = 0
                elif event.key == K_s and player1.direction[1] != -1:
                    player1.ychange = 1
                    player1.xchange = 0 
    pygame.display.update()
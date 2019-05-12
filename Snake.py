import pygame
from pygame.locals import *
import random
pygame.init()
done = False
BLACK = (0, 0, 0)
DARKGREEN = (0, 100, 0)
LAWNGREEN = (124, 252, 0)
RED = (255, 0, 0)
WHITE = (255, 219, 219)
SALMON = (250, 128, 114)
MAGENTA =  (255, 0, 255)
pygame.display.set_caption("Snake")
display_width = 962
display_height = 742 
screen = pygame.display.set_mode((display_width, display_height))
screen.fill(BLACK)
pygame.draw.rect(screen, DARKGREEN, pygame.Rect(0, 0, display_width, 100))
grid_length = 30
grid_gap = 2
FPS = 30
clock = pygame.time.Clock()
x_coord_list = [x*(grid_length +grid_gap) + grid_gap for x in range(display_width//(grid_length + grid_gap))]
y_coord_list = [y*(grid_length +grid_gap) + grid_gap + 100 for y in range((display_height -100)//(grid_length + grid_gap))]
print(y_coord_list)
collide_value = 10101 # (can be any random number)works for all sides as the value will ref last value of x/y_coord_list exiting all sides
x_coord_list.append(collide_value) # holders so list index out of range error doesnt happen
y_coord_list.append(collide_value)
class Snake:
    def __init__(self, x, y):
        self.x = x
        self.y = y       
    def move(self, x_change, y_change):
        self.x += x_change
        self.y += y_change
        pygame.draw.rect(screen, LAWNGREEN, pygame.Rect(x_coord_list[self.x], y_coord_list[self.y], grid_length, grid_length))
def drawInitialSnake(): 
    for x in range(0,len(stored_coords)):
        pygame.draw.rect(screen, LAWNGREEN, pygame.Rect(x_coord_list[stored_coords[x][0]], y_coord_list[stored_coords[x][1]], grid_length, grid_length))
def getRandomApple():
    valid = True
    while valid:
        x_apple = random.randint(0, len(x_coord_list)-2)
        y_apple = random.randint(0, len(y_coord_list)-2)
        if [x_apple, y_apple] not in stored_coords:
            valid = False
    return (x_apple, y_apple)
def drawApple(x, y):
    pygame.draw.rect(screen, RED, pygame.Rect(x_coord_list[x], y_coord_list[y], grid_length, grid_length))
print(y_coord_list)
def checkCollision():
    for x in stored_coords[1:]: # check for collision with tail
        if [snake_head.x, snake_head.y] == x:
            return True
    if x_coord_list[snake_head.x] == collide_value or y_coord_list[snake_head.y] == collide_value:
        return True 
def loseWindow():
    pygame.draw.rect(screen, WHITE, pygame.Rect(345, 300, 300, 150))
    myfont = pygame.font.SysFont('Comic Sans MS', 30, True)
    textsurface = myfont.render('You have lost', True, (0, 0, 0))
    screen.blit(textsurface,(400,340))
    pygame.draw.rect(screen, RED, pygame.Rect(460, 400, 75, 30))
    myfont = pygame.font.SysFont('Comic Sans MS', 15, True)
    textsurface = myfont.render('Restart', True, (0, 0, 0))
    screen.blit(textsurface,(470,405))
def buttonAnimationInit():
    pygame.draw.rect(screen, SALMON, pygame.Rect(460, 400, 75, 30))
    myfont = pygame.font.SysFont('Comic Sans MS', 15, True)
    textsurface = myfont.render('Restart', True, (0, 0, 0))
    screen.blit(textsurface,(470,405))
def buttonAnimationFinal():
    pygame.draw.rect(screen, RED, pygame.Rect(460, 400, 75, 30))
    myfont = pygame.font.SysFont('Comic Sans MS', 15, True)
    textsurface = myfont.render('Restart', True, (0, 0, 0))
    screen.blit(textsurface,(470,405))
def scoreBoard(score):
    pygame.draw.rect(screen, DARKGREEN, pygame.Rect(700, 0, display_width - 700, 100))
    myfont = pygame.font.SysFont('Comic Sans MS', 25, True)
    textsurface = myfont.render('Score: {}'.format(score), True, (30,144,255))
    screen.blit(textsurface,(800,30))

def startGame():
    global stored_coords, x_change, y_change, direction, dt, game_end, snake_head, x_apple, y_apple, score
    x_change = 0
    y_change = 0
    score = 0
    direction = [0, -1] # -1 cos its facing up at first
    dt = 0
    game_end = False
    pygame.draw.rect(screen, BLACK, pygame.Rect(0, 100, display_width, display_height-100))
    myfont = pygame.font.SysFont('Comic Sans MS', 45, True)
    textsurface = myfont.render('Snake', True,  (146, 16, 0))
    screen.blit(textsurface,(425,30))
    snake_head = Snake((len(x_coord_list)-1)//2, (len(y_coord_list)-1)//2)
    stored_coords = [[snake_head.x, snake_head.y], [snake_head.x, snake_head.y+ 1], [snake_head.x , snake_head.y+ 2]]
    x_apple, y_apple = getRandomApple()
    drawInitialSnake()
    scoreBoard(score)
startGame()
while not done:
    dt += clock.tick(FPS)
    if dt > 100 and (x_change or y_change) and not game_end:
        pygame.draw.rect(screen, BLACK, pygame.Rect(0, 100, display_width, display_height-100))
        drawApple(x_apple, y_apple) # apple needs to be drawn every loop
        direction = [x_change, y_change]
        snake_head.move(x_change, y_change)
        if (snake_head.x, snake_head.y) == (x_apple, y_apple): # check for eating the apple
            score += 10
            scoreBoard(score)
            for x in range(2):
                stored_coords.append(stored_coords[-1])
            x_apple, y_apple = getRandomApple() # if apple is eaten, creating new random coords for apple  
        for x in range(len(stored_coords) - 1, 0, -1): #moving coord down the stored_coords list
            stored_coords[x] = stored_coords[x- 1]
        for x in range(1,len(stored_coords)): # drawing the position of where the block ahead is one loop ago
            pygame.draw.rect(screen, LAWNGREEN, pygame.Rect(x_coord_list[stored_coords[x][0]], y_coord_list[stored_coords[x][1]], grid_length, grid_length))
        stored_coords[0] = [snake_head.x, snake_head.y]
        if checkCollision():
            loseWindow()
            game_end = True
        dt = 0 
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        if game_end:
            mos_x, mos_y = pygame.mouse.get_pos()
            if mos_x > 460 and mos_x < 535 and mos_y < 430 and mos_y > 400:
                buttonAnimationInit()
                if event.type == MOUSEBUTTONDOWN:
                    startGame()
            else:
                buttonAnimationFinal()
        if event.type == pygame.KEYDOWN and not game_end:
            if event.key == K_LEFT and direction[0] != 1:
                x_change = -1
                y_change = 0
            elif event.key == K_RIGHT and direction[0] != -1:
                x_change = 1
                y_change = 0
            elif event.key == K_UP and direction[1] != 1:
                y_change = -1
                x_change = 0
            elif event.key == K_DOWN and direction[1] != -1:
                y_change = 1
                x_change = 0 
    pygame.display.update()
from config import *
import pygame
from pygame.locals import *
from itertools import chain
import random
pygame.init()
done = False
pygame.display.set_caption("Tetris")
display_width = 550
display_height = 663
grid_length = 30
grid_border = 3
MOVEDOWN = USEREVENT + 1
MOVERIGHT = USEREVENT + 2
MOVELEFT = USEREVENT + 3
score_list = [40, 100, 300, 1200] #score u will get for 1/2/3/4 row clear(s)
screen = pygame.display.set_mode((display_width, display_height))
screen.fill(colour['DARKSLATEGRAY'])
pygame.draw.rect(screen, colour['GRAY'], pygame.Rect(333, 0, 10, 663)) # gray divider between game area and score board stuff
x_coords = [grid_border + (grid_length + grid_border)*n for n in range(10)]
x_coords_next = [(grid_border + (grid_length + grid_border)*n) + 350 for n in range(5)]
y_coords = [grid_border + (grid_length + grid_border)*n for n in range(20)]
x_coords.append('exceed')#values for when x coord exceeds the gridarea
y_coords.append('exceed')#values for when y coord exceeds the gridarea
print(y_coords)
for y in ([0, ' NEXT'], [230, 'SCORE'], [430, 'LINES']):# the three blue headers
    pygame.draw.rect(screen, colour['BLUE'], pygame.Rect(343, y[0], 550-343, 70))
    myfont = pygame.font.SysFont('Comic Sans MS', 35, True)
    text = myfont.render(y[1], True, (204,204,0))
    screen.blit(text,(385,y[0]+ 10))

class Block:
    def __init__(self, block_type):# initial x is 3, initial y is 0
        self.block_type = block_type
        self.x = 3
        self.y = 0
        self.rotation = 0
        self.colour = block_colours[block_type]
        self.stored_coord_values = []
    def moveDown(self):
        self.y += 1
    def moveLeft(self):
        self.x -= 1
    def moveRight(self):
        self.x += 1
    def rotate(self):
        if self.rotation < 3:
            self.rotation += 1
        else:
            self.rotation = 0
        self.relative_coord_check = list(chain(*[[(x, y) for (x, pos) in enumerate(row) if pos == 1] for (y, row) in enumerate(block[self.block_type][self.rotation])]))
        self.check_coords = [(x + self.x, y + self.y) for x, y in self.relative_coord_check]
        for x, y in self.check_coords:
            if y >= 20: # check for collision with ground
                if self.rotation == 0:
                    self.rotation = 3
                else:
                    self.rotation -= 1
                return False
            for y_pos, y_data in enumerate(game_state): #check for collision with other blocks
                for x_pos, x_data in enumerate(y_data):
                    if x_data[0] == 1 and y_pos == y and x_pos == x:
                        if self.rotation == 0:
                            self.rotation = 3
                        else:
                            self.rotation -= 1
                        return False
            #Push away from wall
            if self.block_type == 'i_block': #i block
                if x == -2:
                    self.moveRight()
                elif x == -1:
                    self.moveRight()             
                if x == 11:
                    self.moveLeft() 
                elif x == 10:
                    self.moveLeft()           
            else: # all the other blocks
                if x == -1:
                    self.moveRight()
                elif x == 10:
                    self.moveLeft()
            
        return True
    def draw(self):
        
        self.relative_coord = list(chain(*[[(x, y) for (x, pos) in enumerate(row) if pos == 1] for (y, row) in enumerate(block[self.block_type][self.rotation])])) # creating list of coords of block relative to top left corner of matrix
        self.coords = [(x + self.x, y + self.y) for x, y in self.relative_coord]
        
        #print(self.coords)
        self.coord_values = [(x_coords[x + self.x], y_coords[y + self.y]) for x, y in self.relative_coord]
        #print(self.coord_values)
        
        if 'exceed' in chain(*self.coord_values):

            return True # if it hits grid walls
        for x, y in self.coords:
            if game_state[y][x][0] == 1: #if it hits another block
                return True
        for coord in self.stored_coord_values: # remove previous area of block
             pygame.draw.rect(screen, colour['DARKSLATEGRAY'], pygame.Rect(coord[0] - grid_border, coord[1]- grid_border, grid_length + grid_border*2 , grid_length + grid_border*2))
        self.stored_coord_values = self.coord_values
        self.stored_coords = self.coords
        
        for coord in self.coord_values: # drawing the moving block
            drawTetrisBlocks(self.colour, coord[0], coord[1])
        drawGameBlocks()
def drawGameBlocks():        
    for y_pos, y in enumerate(game_state): #Redrawing game_state blocks
        for x_pos, x in enumerate(y):
            if x[0] == 1:
                drawTetrisBlocks(block_colours[x[1]], x_coords[x_pos], y_coords[y_pos])
                
def drawTetrisBlocks(block_colour, x, y):
    pygame.draw.rect(screen, colour['BLACK'], pygame.Rect(x - grid_border, y- grid_border, grid_length + grid_border*2 , grid_length + grid_border*2)) #Border
    pygame.draw.rect(screen, block_colour, pygame.Rect(x, y, grid_length, grid_length)) # Block

def createRandomBlock(block_list = [0, random.choice(list(block_colours.keys()))]):
    
    stored_random_block = random.choice(list(block_colours.keys()))
    block_list[0], block_list[1] = block_list[1], stored_random_block
    return block_list
def drawNextBlock(block_type_next):
    pygame.draw.rect(screen, colour['DARKSLATEGRAY'], pygame.Rect(343, 70, 550-343, 100)) # removing prevous 'next block'
    relative_coord = list(chain(*[[(x, y) for (x, pos) in enumerate(row) if pos == 1] for (y, row) in enumerate(block[block_type_next][0])]))
    if block_type_next == 'o_block' or block_type_next == 'i_block':
        coord_values = [(x_coords_next[x + 1], y_coords[y + 2]) for x, y in relative_coord]
    else:
        coord_values = [(x_coords_next[x + 1]+ 15, y_coords[y + 3]) for x, y in relative_coord]
    for coord in coord_values: # drawing the moving block
            drawTetrisBlocks(block_colours[block_type_next], coord[0], coord[1])
def checkLose():
    relative_coord = list(chain(*[[(x, y) for (x, pos) in enumerate(row) if pos == 1] for (y, row) in enumerate(block[block_test.block_type][0])])) # creating list of coords of block relative to top left corner of matrix
    coords = [(x + 3, y) for x, y in relative_coord]
    for x, y in coords:
        if game_state[y][x][0] == 1:
            return True
def moveRight():
    block_test.moveRight()
    if block_test.draw():
        block_test.coord_values =  block_test.stored_coord_values
        block_test.coords =  block_test.stored_coords
        block_test.x -= 1
def moveLeft():
    block_test.moveLeft()
    if block_test.draw():
        block_test.coord_values =  block_test.stored_coord_values
        block_test.coords =  block_test.stored_coords
        block_test.x += 1
def changeScore():
    pygame.draw.rect(screen, colour['DARKSLATEGRAY'], pygame.Rect(354, 310, 550-343, 100))
    pygame.draw.rect(screen, colour['DARKSLATEGRAY'], pygame.Rect(354, 515, 550-343, 100))
    myfont = pygame.font.SysFont('Comic Sans MS', 40, True)
    text = myfont.render(str(score), True, (255,255,255))
    screen.blit(text,(441 - len(str(score))* 11,320))
    myfont = pygame.font.SysFont('Comic Sans MS', 40, True)
    text = myfont.render(str(lines), True, (255,255,255))
    screen.blit(text,(441 - len(str(lines))* 11,525))
def loseWindow():
    pygame.draw.rect(screen, colour['WHITE'], pygame.Rect(100, 300, 150, 100))
    myfont = pygame.font.SysFont('Comic Sans MS', 20, True)
    textsurface = myfont.render('You have lost', True, (0, 0, 0))
    screen.blit(textsurface,(110,310))
def buttonAnimation(state):
    pygame.draw.rect(screen, colour[state], pygame.Rect(135, 350, 75, 30))
    myfont = pygame.font.SysFont('Comic Sans MS', 15, True)
    textsurface = myfont.render('Restart', True, (0, 0, 0))
    screen.blit(textsurface,(145,355))    
def startGame():
    global direction, past_left, past_right, lines, score, block_test, game_end, random_block, game_state
    direction = 0
    past_left = 0
    past_right = 0
    lines = 0
    score = 0   
    game_state = [[[0, 0] for y in range(10)] for x in range(20)]
    pygame.draw.rect(screen, colour['DARKSLATEGRAY'], pygame.Rect(0, 0, 10*(grid_length + grid_border) + grid_border, 20*(grid_length + grid_border) + grid_border))
    changeScore()
    random_block = createRandomBlock()
    block_test = Block(random_block[0])
    block_test.draw()
    drawNextBlock(random_block[1])
    game_end = False
    pygame.time.set_timer(MOVEDOWN, 700)
startGame()
while not done: #game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        if game_end:
            mos_x, mos_y = pygame.mouse.get_pos()
            if mos_x > 135 and mos_x < 210 and mos_y < 380 and mos_y > 350:
                buttonAnimation('SALMON')               
                if event.type == MOUSEBUTTONDOWN:
                    startGame()
                    print(mos_x, mos_y)
            else:
                buttonAnimation('RED')
        if event.type == MOVERIGHT:
            moveRight()
        if event.type == MOVELEFT:
            moveLeft()
        if event.type == MOVEDOWN:
            block_test.moveDown()
            if block_test.draw():
                for x , y in block_test.stored_coords:
                    game_state[y][x][0] = 1 #1 means there is a block there
                    game_state[y][x][1] = block_test.block_type # and its corresponding block tpye
                
                win_rows = []
                for y_row, y_data in enumerate(game_state):
                    win_counter = 0
                    for x_data, _ in y_data:
                        if x_data == 1:
                            win_counter += 1
                    if win_counter == 10:
                        win_rows.insert(0, y_row)
                first_loop = True # to prevent 200ms time wasting for first loop of animation
                if win_rows: # animation for row clear
                    for _ in range(3): # blinks 3 times
                        for y in win_rows:
                            for x_pos ,( _ , x_type) in enumerate(game_state[y]):
                                drawTetrisBlocks(block_colours[x_type], x_coords[x_pos], y_coords[y])
                        pygame.display.update()
                        if not first_loop:
                            pygame.time.wait(200)
                        first_loop = False
                        for y in win_rows:
                            for x in x_coords[:-1]:
                                drawTetrisBlocks(colour['WHITE'], x, y_coords[y])
                        pygame.display.update()
                        pygame.time.wait(200)

                    for row in win_rows:
                        for x in range(row, 0, -1):
                            game_state[x] = game_state[x - 1]

                    pygame.time.set_timer(MOVEDOWN, 700) # to reset keyboard input on new block
                    pygame.event.clear()
                    lines += len(win_rows)
                    score += score_list[len(win_rows) - 1]
                    changeScore()
                pygame.draw.rect(screen, colour['DARKSLATEGRAY'], pygame.Rect(0, 0, 10*(grid_length + grid_border) + grid_border, 20*(grid_length + grid_border) + grid_border))
                drawGameBlocks()
                random_block = createRandomBlock() 
                block_test = Block(random_block[0])
                block_test.draw()    
                drawNextBlock(random_block[1])

                if checkLose(): #Lose window
                    print('lose')
                    game_end = True
                    pygame.time.set_timer(MOVELEFT, 0)
                    pygame.time.set_timer(MOVEDOWN, 0)
                    pygame.time.set_timer(MOVERIGHT, 0)
                    loseWindow()
                    buttonAnimation('RED')

        if not game_end:
            if event.type == KEYDOWN:
                if event.key == K_DOWN:
                    pygame.time.set_timer(MOVEDOWN, 50)
                if event.key == K_RIGHT and past_left == 0:
                    pygame.time.set_timer(MOVELEFT, 0)
                    past_right = pygame.time.get_ticks() 
                    moveRight()
                if event.key == K_UP:
                    if block_test.rotate():
                        block_test.draw()
                if event.key == K_LEFT and past_right == 0:
                    pygame.time.set_timer(MOVERIGHT, 0)
                    past_left = pygame.time.get_ticks() 
                    moveLeft()
            if event.type == KEYUP:
                if event.key == K_DOWN:
                    pygame.time.set_timer(MOVEDOWN, 700)
                if event.key == K_RIGHT:
                    direction = 0
                    past_right = 0
                    pygame.time.set_timer(MOVERIGHT, 0)
                if event.key == K_LEFT:
                    direction = 0
                    past_left = 0
                    pygame.time.set_timer(MOVELEFT, 0)
        now = pygame.time.get_ticks() # All this is just to get that effect when u move left or right where it moves once then pauses for abit then continues moving
        if past_left and now - past_left >= 200:
            pygame.time.set_timer(MOVELEFT, 50)
            past_left = 0
        if past_right and now - past_right >= 200:
            pygame.time.set_timer(MOVERIGHT, 50)
            past_right = 0
    pygame.display.update()
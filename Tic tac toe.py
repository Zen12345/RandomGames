import pygame
from pygame.locals import *
pygame.init()
done = False
WHITE = (255, 219, 219)
BLACK = (0, 0, 0)
CADETBLUE = (95,158,160)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
SLATEGRAY = (112,128,144)
box_number = [0, 0]
y_value, x_value = False, False
game_end = False
win = [
    [
    1, 1, 1,
    0 ,0 ,0,
    0 ,0 ,0
    ],
    [
    0, 0, 0,
    1 ,1 ,1,
    0 ,0 ,0
    ],
    [
    0, 0, 0,
    0 ,0 ,0,
    1 ,1 ,1
    ],
    [
    1, 0, 0,
    1 ,0 ,0,
    1 ,0 ,0
    ],
    [
    0, 1, 0,
    0 ,1 ,0,
    0 ,1 ,0
    ],
    [
    0, 0, 1,
    0 ,0 ,1,
    0 ,0 ,1
    ],
    [
    1, 0, 0,
    0 ,1 ,0,
    0 ,0 ,1
    ],
    [
    0, 0, 1,
    0 ,1 ,0,
    1 ,0 ,0
    ],

]
game_state = [
    [0, 0, 0], 
    [0, 0, 0],
    [0, 0, 0]
]
turn_number = 1
pygame.display.set_caption("Tic Tac Toe")
display_width = 800
display_height = 600
screen = pygame.display.set_mode((display_width, display_height))
line_height = 420
line_width = 10
left_corner_x = 200
left_corner_y = 100
distance_apart = (line_height - 20)/3 
x_box = [
[left_corner_x, left_corner_x +distance_apart],
[left_corner_x + distance_apart + 10,left_corner_x + distance_apart*2 + 10],
[left_corner_x + distance_apart*2 + 20, left_corner_x + distance_apart*3 + 20]
]
y_box = [
[left_corner_y, left_corner_y +distance_apart],
[left_corner_y + distance_apart + 10,left_corner_y + distance_apart*2 + 10],
[left_corner_y + distance_apart*2 + 20, left_corner_y + distance_apart*3 + 20]
]
#Drawing the playarea
def play_area():
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, pygame.Rect(x_box[0][1], y_box[0][0], line_width, line_height))
    pygame.draw.rect(screen, BLACK, pygame.Rect(x_box[1][1], y_box[0][0], line_width, line_height))
    pygame.draw.rect(screen, BLACK, pygame.Rect(x_box[0][0], y_box[0][1], line_height, line_width))
    pygame.draw.rect(screen, BLACK, pygame.Rect(x_box[0][0], y_box[1][1], line_height, line_width))
    pygame.draw.rect(screen, CADETBLUE, pygame.Rect(680,0 , 120, 60))
    pygame.draw.rect(screen, SLATEGRAY, pygame.Rect(30,90 , 60, 110))
    pygame.draw.circle(screen, BLACK, (60,120), 20, 5)
    pygame.draw.line(screen, YELLOW, (42, 150), (42 + 35, 150 + 35), 7)
    pygame.draw.line(screen, YELLOW, (42, 150 + 35), (42 + 35, 150), 7)
    myfont = pygame.font.SysFont('Comic Sans MS', 25)
    textsurface = myfont.render('Restart', True, (0, 0, 0))
    screen.blit(textsurface,(695,10))
play_area() 

def draw_circle(x, y, colour):
    pygame.draw.circle(screen, colour, (x, y), 50, 10)
def draw_cross(x, y, colour):
    pygame.draw.line(screen, colour, (x, y), (x + 90, y + 90), 15)
    pygame.draw.line(screen, colour, (x, y + 90), (x + 90, y), 15)

while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        if event.type == MOUSEBUTTONDOWN: 
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if mouse_x > 680 and mouse_y < 60:
                #print('restart')
                game_state = [
                    [0, 0, 0], 
                    [0, 0, 0],
                    [0, 0, 0]
                ]
                play_area()
                turn_number = 1
                game_end = False
            if game_end == False:
                for coord, (a, b) in enumerate(x_box):
                    if mouse_x > a and mouse_x < b:
                        box_number[0] = coord
                        x_value = True
                for coord, (a, b) in enumerate(y_box):
                    if mouse_y > a and mouse_y < b:
                        box_number[1] = coord
                        y_value = True
                if game_state[box_number[1]][box_number[0]] != 0:
                    y_value, x_value = False, False 
                if y_value or x_value:
                    if y_value == False:
                        x_value = False
                    elif x_value == False:
                        y_value = False
                    else:
                        if turn_number == 1: #X's turn
                            draw_cross(int(x_box[box_number[0]][0] + (distance_apart - 90)/2), int(y_box[box_number[1]][0] + (distance_apart - 90)/2), BLACK)
                            game_state[box_number[1]][box_number[0]] = turn_number
                            temp_game_state = [1 if y==turn_number else 0 for row in game_state for y in row]
                            turn_number += 1
                            pygame.draw.line(screen, BLACK, (42, 150), (42 + 35, 150 + 35), 7)
                            pygame.draw.line(screen, BLACK, (42, 150 + 35), (42 + 35, 150), 7)
                            pygame.draw.circle(screen, YELLOW, (60,120), 20, 5)
                        elif turn_number == 2: # O's turn
                            draw_circle(int(x_box[box_number[0]][0] + distance_apart/2), int(y_box[box_number[1]][0] + distance_apart/2), BLACK)
                            game_state[box_number[1]][box_number[0]] = turn_number
                            temp_game_state = [1 if y==turn_number else 0 for row in game_state for y in row] 
                            turn_number -= 1
                            pygame.draw.circle(screen, BLACK, (60,120), 20, 5)
                            pygame.draw.line(screen, YELLOW, (42, 150), (42 + 35, 150 + 35), 7)
                            pygame.draw.line(screen, YELLOW, (42, 150 + 35), (42 + 35, 150), 7)
                        counter_win = 0
                       
                        
                        for x in win:
                            for y in range(9):
                                if x[y] == temp_game_state[y] and x[y] == 1:
                                    counter_win += 1
                            if counter_win == 3 and turn_number == 1: #O's turn is 1 now cos turn number got minused
                                #print(temp_game_state)
                                #print(x)
                                #print('O wins')
                                for pos, z in enumerate(x):
                                    x_pos = pos
                                    print(pos)
                                    if z == 1:
                                        while x_pos >= 3:
                                            x_pos -= 3
                                        y_pos = int(pos/3)
                                        draw_circle(int(x_box[x_pos][0] + distance_apart/2), int(y_box[y_pos][0] + distance_apart/2), RED)
                                myfont = pygame.font.SysFont('Comic Sans MS', 25)
                                win_text = myfont.render('O wins', True, (0, 0, 0))
                                screen.blit(win_text,(370,30))
                                game_end = True
                            elif counter_win == 3 and turn_number == 2: #X's turn is 2 now cos turn number got plused
                                #print(temp_game_state)
                                #print(x)
                                #print('X wins')
                                for pos, z in enumerate(x):
                                    x_pos = pos
                                    if z == 1:
                                        while x_pos >= 3:
                                            x_pos -= 3
                                        y_pos = int(pos/3)
                                        draw_cross(int(x_box[x_pos][0] + (distance_apart - 90)/2), int(y_box[y_pos][0] + (distance_apart - 90)/2), RED)
                                myfont = pygame.font.SysFont('Comic Sans MS', 25)
                                win_text = myfont.render('X wins', True, (0, 0, 0))
                                screen.blit(win_text,(370,30))
                                game_end = True
                            counter_win = 0
                        game_state_list = [x for row in game_state for x in row]
                        if 0 not in game_state_list and game_end == False:
                            myfont = pygame.font.SysFont('Comic Sans MS', 25)
                            win_text = myfont.render('Draw', True, (0, 0, 0))
                            screen.blit(win_text,(380,30))
                    y_value, x_value = False, False
    pygame.display.update()
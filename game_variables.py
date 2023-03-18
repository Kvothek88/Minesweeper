import numpy as np
import random as rn
import pygame

width = 480
height = 480
ht = 90
frame_width = 10
space = 30

game_type=0
difficulty=0
mines_list = [[12,17,30],
            [35,48,88],
            [103,159,266]]

fps = 15
gameover = False
win=False
play=False
options=False
mainmenu=True
images = {}
opened_squares=[]

def reset_game(difficulty,game_type,mines_list):
    if game_type==0:
        dimension = 9
    elif game_type==1:
        dimension=16
    elif game_type==2:
        dimension = 30
    game_mines_num = mines_list[game_type][difficulty]
    mines_count = game_mines_num
    board = np.empty((dimension,dimension),dtype='object')
    current_board = np.empty((dimension,dimension),dtype='object')
    for i in range(dimension):
        board[i] = "-"
    for i in range(dimension):
        current_board[i] = "-"
    game_mines = []
    while len(game_mines) < game_mines_num:
        row = rn.randint(0,dimension-1)
        col = rn.randint(0,dimension-1)
        if (row,col) not in game_mines:
            board[row][col]="m"
            game_mines.append((row,col))
    sq_size = width // dimension

    return board,current_board,game_mines, sq_size,dimension,mines_count,game_mines_num


board,current_board,game_mines,sq_size,dimension,mines_count,game_mines_num = reset_game(difficulty,game_type,mines_list)

empty_squares = (dimension**2)-game_mines_num

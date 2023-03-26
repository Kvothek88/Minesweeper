import pygame
import os
import numpy as np
import random as rn
from game_variables import *


def load_images():
    nums = ["0","1","2","3","4","5","6","7","8"]
    nums2 = ["b1","b2","b3"]
    for img in nums:
        images[img] = pygame.transform.scale(pygame.image.load(f'images/{img}.png'),(sq_size,sq_size))
    for img in nums2:
        images[img] = pygame.transform.scale(pygame.image.load(f'images/{img}.png'),(sq_size,sq_size))
    for img in range(3):
        images[f"difficulty{img}"] = pygame.transform.scale(pygame.image.load(f'images/difficulty{img}.png'),(160,40))
    for img in range(3):
        images[f"gametype{img}"] = pygame.transform.scale(pygame.image.load(f'images/gametype{img}.png'),(160,40))
    images["difficulty"] = pygame.transform.scale(pygame.image.load(os.path.join('images','difficulty.png')),(200,50))
    images["gametype"] = pygame.transform.scale(pygame.image.load(os.path.join('images','gametype.png')),(200,50))
    images["newgame"] = pygame.transform.scale(pygame.image.load(os.path.join('images','newgame.png')),(200,60))
    images["options"] = pygame.transform.scale(pygame.image.load(os.path.join('images','options.png')),(200,60))
    images["ok"] = pygame.transform.scale(pygame.image.load(os.path.join('images','ok.png')),(60,50))
    images["mainmenu"] = pygame.transform.scale(pygame.image.load(os.path.join('images','mainmenu.png')),(100,25))
    images["empty"] = pygame.transform.scale(pygame.image.load(os.path.join('images','empty.png')),(sq_size,sq_size))
    images["flag"] = pygame.transform.scale(pygame.image.load(os.path.join('images','flag.png')),(sq_size,sq_size))
    images["screen"] = pygame.transform.scale(pygame.image.load(os.path.join('images','screen.png')),(width,ht))
    images["play"] = pygame.transform.scale(pygame.image.load(os.path.join('images','play.png')),(ht-frame_width*2,ht-frame_width*2))
    images["win"] = pygame.transform.scale(pygame.image.load(os.path.join('images','win.png')),(ht-frame_width*2,ht-frame_width*2))
    images["lose"] = pygame.transform.scale(pygame.image.load(os.path.join('images','lose.png')),(ht-frame_width*2,ht-frame_width*2))


def draw_game(screen,text,text2,ones,tens,huds,mines_count,text3,secs):
    if play:
        screen.fill(pygame.Color("grey"))
        screen.blit(images["screen"],(space,space))
        screen.blit(images["mainmenu"],(2,2))
        if not gameover:
            screen.blit(images["play"],((screen.get_width()//2)-images["play"].get_width()//2, space+frame_width))
        if gameover:
            screen.blit(images["lose"],((screen.get_width()//2)-images["lose"].get_width()//2, space+frame_width))
        pygame.draw.rect(screen,pygame.Color("black"),(space+frame_width,space+frame_width,width//3.5,ht-frame_width*2))
        pygame.draw.rect(screen,pygame.Color("black"),(space+width-frame_width-width//3.5,space+frame_width,width//3.5,ht-frame_width*2))
        screen.blit(huds,(space+frame_width+18,space+frame_width+13))
        screen.blit(tens,(space+frame_width+tens.get_width()+28,space+frame_width+13))
        screen.blit(ones,(space+frame_width+2*tens.get_width()+38,space+frame_width+13))
        for r in range(len(current_board)):
            for c in range(len(current_board[r])):
                if current_board[r][c] == "-":
                    screen.blit(images["empty"],((space) + c * sq_size, (ht+2*space) + r * sq_size))
                if current_board[r][c] == "M":
                    screen.blit(images["b3"],((space) + c * sq_size, (ht+2*space) + r * sq_size))      
                if current_board[r][c] == "m":
                    screen.blit(images["b1"],((space) + c * sq_size, (ht+2*space) + r * sq_size))
                if current_board[r][c] == "flag":
                    screen.blit(images["flag"],((space) + c * sq_size, (ht+2*space) + r * sq_size))
                if current_board[r][c] == "0":
                    screen.blit(images["0"],((space) + c * sq_size, (ht+2*space) + r * sq_size))
                for i in range(1,8):
                    if current_board[r][c] == f"{i}":
                        screen.blit(images[str(i)],((space) + c * sq_size, (ht+2*space) + r * sq_size))
        if win:
            screen.blit(text,(screen.get_width()//2-text.get_width()//2,screen.get_height()//2))
            screen.blit(images["win"],((screen.get_width()//2)-images["win"].get_width()//2, space+frame_width))
        screen.blit(text3,(width-space-82,space+frame_width+13))
    if mainmenu and not options:
        screen.fill(pygame.Color("grey"))
        screen.blit(images["newgame"],(screen.get_width()//2-images["newgame"].get_width()//2,screen.get_height()//2-images["newgame"].get_height()))
        screen.blit(images["options"],(screen.get_width()//2-images["options"].get_width()//2,screen.get_height()//2+images["options"].get_height()))
        screen.blit(text2,(screen.get_width()//2-text2.get_width()//2,screen.get_height()//2-250))
    if options:
        screen.fill(pygame.Color("grey"))
        screen.blit(images["difficulty"],(screen.get_width()//2-images["difficulty"].get_width()-40,screen.get_height()//2-3*(images["difficulty"].get_height())))
        screen.blit(images["difficulty0"],(screen.get_width()//2-images["difficulty0"].get_width()-60,screen.get_height()//2-2*(images["difficulty0"].get_height())))
        screen.blit(images["difficulty1"],(screen.get_width()//2-images["difficulty1"].get_width()-60,screen.get_height()//2-images["difficulty1"].get_height()+20))
        screen.blit(images["difficulty2"],(screen.get_width()//2-images["difficulty2"].get_width()-60,screen.get_height()//2+40))
        if difficulty == 0:
            pygame.draw.rect(screen,pygame.Color("yellow"),(screen.get_width()//2-images["difficulty0"].get_width()-60,screen.get_height()//2-2*(images["difficulty0"].get_height()),160,40),2)
        if difficulty == 1:
            pygame.draw.rect(screen,pygame.Color("yellow"),(screen.get_width()//2-images["difficulty1"].get_width()-60,screen.get_height()//2-images["difficulty1"].get_height()+20,160,40),2)
        if difficulty == 2:
            pygame.draw.rect(screen,pygame.Color("yellow"),(screen.get_width()//2-images["difficulty2"].get_width()-60,screen.get_height()//2+40,160,40),2)
    
        screen.blit(images["gametype"],(screen.get_width()//2+40,screen.get_height()//2-3*(images["gametype"].get_height())))
        screen.blit(images["gametype0"],(screen.get_width()//2+60,screen.get_height()//2-2*(images["gametype0"].get_height())))
        screen.blit(images["gametype1"],(screen.get_width()//2+60,screen.get_height()//2-images["gametype1"].get_height()+20))
        screen.blit(images["gametype2"],(screen.get_width()//2+60,screen.get_height()//2+40))
        if game_type == 0:
            pygame.draw.rect(screen,pygame.Color("yellow"),(screen.get_width()//2+60,screen.get_height()//2-2*(images["gametype0"].get_height()),160,40),2)
        if game_type == 1:
            pygame.draw.rect(screen,pygame.Color("yellow"),(screen.get_width()//2+60,screen.get_height()//2-images["gametype1"].get_height()+20,160,40),2)
        if game_type == 2:
            pygame.draw.rect(screen,pygame.Color("yellow"),(screen.get_width()//2+60,screen.get_height()//2+40,160,40),2)

        screen.blit(images["ok"],(screen.get_width()//2-images["ok"].get_width()//2,screen.get_height()//2+5*(images["ok"].get_height())))


def search_mines(row,col,directions):
    mine_num = 0
    for i in range(8):
        r = row + directions[i][0]
        c = col + directions[i][1]
        if 0 <= r < dimension and 0 <= c < dimension: #within board
            if board[r][c] == "m":
                mine_num += 1
    return mine_num


def scan(direction, initial_sq, directions):
    scan_dir=[(0,1),(1,0),(0,-1),(-1,0)]
    mine = False
    dLeft = scan_dir[(direction+1)%4]
    dRight = scan_dir[(direction+3)%4]
    dL=scan_dir.index(dLeft)
    dR=scan_dir.index(dRight)
    d = scan_dir[direction]
    while not mine:
        mine_left=False
        mine_right=False
        go_left = False
        go_right = False    
        square = []
        for i in range(9):
            square.append([initial_sq[i][0]+d[0],initial_sq[i][1]+d[1]])
        for sq in square:
            if 0 <= sq[0] < dimension and 0 <= sq[1] < dimension:
                if board[sq[0]][sq[1]]=="m":
                    mine=True
                    break
        if not mine:
            initial_sq=square
            for sq in square:
                if 0 <= sq[0] < dimension and 0 <= sq[1] < dimension:
                    mine_num = search_mines(sq[0], sq[1], directions)
                    if current_board[sq[0]][sq[1]]=="-" and mine_num==0:
                        current_board[sq[0]][sq[1]] = "0"
                    elif current_board[sq[0]][sq[1]]=="-" and mine_num != 0:
                        current_board[sq[0]][sq[1]] = str(mine_num)
                else:
                    mine = True
            square=[]
            for i in range(9):
                square.append([initial_sq[i][0]+dLeft[0],initial_sq[i][1]+dLeft[1]])       
            for sq in square:
                if 0 <= sq[0] < dimension and 0 <= sq[1] < dimension:
                    if current_board[sq[0]][sq[1]]=="-":
                        go_left=True
                    if board[sq[0]][sq[1]]=="m":
                        mine_left=True
                        break
                else:
                    mine = True
            square=[]
            for i in range(9):
                square.append([initial_sq[i][0]+dRight[0],initial_sq[i][1]+dRight[1]])
            for sq in square:
                if 0 <= sq[0] < dimension and 0 <= sq[1] < dimension:
                    if current_board[sq[0]][sq[1]]=="-":
                        go_right=True                
                    if board[sq[0]][sq[1]]=="m":
                        mine_right=True
                        break
                else:
                    mine = True
            if not mine_left and go_left:
                scan(dL,initial_sq,directions)
            if not mine_right and go_right:
                scan(dR,initial_sq,directions)            
        else:
            square=[]
            for i in range(9):
                square.append([initial_sq[i][0]+dLeft[0],initial_sq[i][1]+dLeft[1]])       
            for sq in square:
                if 0 <= sq[0] < dimension and 0 <= sq[1] < dimension:
                    if current_board[sq[0]][sq[1]]=="-":
                        go_left=True
                    if board[sq[0]][sq[1]]=="m":
                        mine_left=True
                        break
                else:
                    mine = True
            square=[]
            for i in range(9):
                square.append([initial_sq[i][0]+dRight[0],initial_sq[i][1]+dRight[1]])
            for sq in square:
                if 0 <= sq[0] < dimension and 0 <= sq[1] < dimension:
                    if current_board[sq[0]][sq[1]]=="-":
                        go_right=True                
                    if board[sq[0]][sq[1]]=="m":
                        mine_right=True
                        break
                else:
                    mine = True
            if not mine_left and go_left:
                scan(dL,initial_sq,directions)
            if not mine_right and go_right:
                scan(dR,initial_sq,directions)

def win_condition(opened_squares,empty_squares):
    for r in range(len(current_board)):
        for c in range(len(current_board[r])):
            if current_board[r][c] != "-" and current_board[r][c] != "flag":
                if (r,c) not in opened_squares:
                    opened_squares.append((r,c))
    if len(opened_squares)!=0:
        if len(opened_squares)==empty_squares:
            return True


def main():
    pygame.init()
    screen = pygame.display.set_mode((width + 2 * space, height + ht + 3 * space))
    pygame.display.set_caption("Minesweeper")
    clock = pygame.time.Clock()
    screen.fill(pygame.Color("grey"))
    font = pygame.font.SysFont('Comic Sans MS', 60)
    text = font.render('You Won!', False, (255, 0, 0))
    font2 = pygame.font.SysFont('arial.ttf', 80)
    font3 = pygame.font.SysFont('arial.ttf', 75)
    font4 = pygame.font.SysFont('arial.ttf', 70)
    secs_count = 0
    secs = 0//12
    mins_count = 0
    mins = "%s" % str(mins_count) if mins_count >= 10 else "0%s" % str(mins_count)
    text3 = font4.render("{}:{}".format(mins,secs),True,(255,0,0),(0,0,0))
    text2 = font2.render('Minesweeper', False, (255, 0, 0))
    load_images()
    run = True
    global board
    global current_board
    global gameover
    global win
    global play
    global options
    global mainmenu
    global difficulty
    global game_type
    global mines_list
    global game_mines_num
    global dimension
    global sq_size
    global mines_count
    global empty_squares
    while run:
        if play:
            clock.tick(60)
            secs_count += 1
            secs = secs_count//12
            secs = "%s" % str(secs) if secs >= 10 else "0%s" % str(secs)
            if secs_count == 719:
                secs_count = 0
                mins_count += 1
                mins = "%s" % str(mins_count) if mins_count >= 10 else "0%s" % str(mins_count)
            text3 = font4.render("{}:{}".format(mins,secs),True,(255,0,0),(0,0,0))        
        for event in pygame.event.get():
            ones = font3.render(str(mines_count%10), False, (255, 0, 0))
            tens = font3.render(str(mines_count//10%10), False, (255, 0, 0))
            huds = font3.render(str(mines_count//100%10), False, (255, 0, 0))

            if event.type == pygame.QUIT:
                run = False

            if play:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    click = False
                    click2 = False
                    directions = ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1))
                    location = pygame.mouse.get_pos()
                    click_type = pygame.mouse.get_pressed()
                    if space < location[0] < space + width and (2*space + ht) < location [1] < (2*space + ht + height):
                        col = (location[0] - space) // sq_size
                        row = (location[1] - 2*space - ht) // sq_size
                        click = True
                    if screen.get_width()//2-images["play"].get_width()//2 < location[0] < screen.get_width()//2+images["play"].get_width()//2 \
                        and space+frame_width < location[1] < space+frame_width+images["play"].get_height() :
                        click2 = True
                    if click_type[0] and click and not gameover and not win: #left mouse button on board
                        click = False
                        if board[row][col] == "m" and current_board[row][col] != "flag": #if square is mine and not flagged
                            gameover = True
                            mines = []
                            for r in range(len(board)):
                                for c in range(len(board[r])):
                                    if board[r][c] == "m":
                                        mines.append((r,c))
                            for mine in mines:
                                current_board[mine[0]][mine[1]] = "m"
                            current_board[row][col] = "M"
                        elif board[row][col] == "-" and current_board[row][col] != "flag": #if square is empty and not flagged
                            if current_board[row][col] == "-":
                                mine_num = search_mines(row,col,directions)
                                if mine_num > 0:
                                    current_board[row][col] = str(mine_num)
                                else:
                                    initial_sq = []
                                    dir = ((-1,-1),(-1,0),(-1,1),(0,-1),(0,0),(0,1),(1,-1),(1,0),(1,1))
                                    for i in range(9):
                                        if i == 4:
                                            initial_sq.append([row,col])
                                        else:
                                            initial_sq.append([row+dir[i][0], col+dir[i][1]])
                                    for sq in initial_sq:
                                        if 0 <= sq[0] < dimension and 0 <= sq[1] < dimension: #within board
                                            mine_num = search_mines(sq[0],sq[1],directions)
                                            if current_board[sq[0]][sq[1]] == "-" and mine_num == 0:
                                                current_board[sq[0]][sq[1]] = "0"
                                            elif current_board[sq[0]][sq[1]] == "-" and mine_num != 0:
                                                current_board[sq[0]][sq[1]] = str(mine_num)
                                    #scan algorithm
                                    for i in range(4):
                                        scan(i,initial_sq,directions)
                    elif click_type[0] and click2: #left mouse button on faces
                        secs_count = 0
                        mins_count = 0
                        mins = "%s" % str(mins_count) if mins_count >= 10 else "0%s" % str(mins_count)
                        opened_squares.clear()
                        gameover = False
                        win = False
                        board,current_board,game_mines,sq_size,dimension,mines_count,game_mines_num,empty_squares = reset_game(difficulty,game_type,mines_list)
                        click2 = False
                    elif click_type[2] and click and not gameover and not win: #right mouse button
                        click = False
                        if current_board[row][col] == "-":
                            if mines_count > 0:
                                current_board[row][col] = "flag"
                                mines_count -= 1
                        elif current_board[row][col] == "flag":
                            if mines_count < game_mines_num:
                                current_board[row][col] = "-"
                                mines_count += 1
                    if 2 < location[0] < images["mainmenu"].get_width() and 2 < location[1] < images["mainmenu"].get_height():
                        play=False
                        mainmenu=True
                        opened_squares.clear()
                        board,current_board,game_mines,sq_size,dimension,mines_count,game_mines_num,empty_squares = reset_game(difficulty,game_type,mines_list)
                        gameover = False
                        win = False                     
            else:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    location = pygame.mouse.get_pos()
                    if mainmenu:
                        if screen.get_width()//2-images["newgame"].get_width()//2 < location[0] < screen.get_width()//2+images["newgame"].get_width()//2 \
                            and screen.get_height()//2-images["newgame"].get_height() < location[1] < screen.get_height()//2:
                            play=True
                            mainmenu=False
                            secs_count = 0
                            mins_count = 0
                        elif screen.get_width()//2-images["options"].get_width()//2 < location[0] < screen.get_width()//2+images["options"].get_width()//2 \
                            and screen.get_height()//2+images["options"].get_height() < location[1] < (screen.get_height()//2)+(2*images["options"].get_height()):
                            mainmenu=False
                            options=True
                    else:
                        if screen.get_width()//2-images["difficulty0"].get_width()-40 < location[0] < screen.get_width()//2-40 \
                            and screen.get_height()//2-2*images["difficulty0"].get_height() < location[1] < screen.get_height()//2-images["difficulty0"].get_height():
                            difficulty = 0
                        if screen.get_width()//2-images["difficulty1"].get_width()-40 < location[0] < screen.get_width()//2-40 \
                            and screen.get_height()//2-images["difficulty1"].get_height()+20 < location[1] < screen.get_height()//2+20:
                            difficulty = 1
                        if screen.get_width()//2-images["difficulty1"].get_width()-40 < location[0] < screen.get_width()//2-40 \
                            and screen.get_height()//2+40 < location[1] < screen.get_height()//2+images["difficulty2"].get_height()+40:
                            difficulty = 2
                        if screen.get_width()//2+60 < location[0] < screen.get_width()//2+images["gametype0"].get_width()+60 \
                            and screen.get_height()//2-2*images["gametype0"].get_height() < location[1] < screen.get_height()//2-images["gametype0"].get_height():
                            game_type = 0
                        if screen.get_width()//2+60 < location[0] < screen.get_width()//2+images["gametype1"].get_width()+60 \
                            and screen.get_height()//2-images["gametype1"].get_height()+20 < location[1] < screen.get_height()//2+20:
                            game_type = 1
                        if screen.get_width()//2+60 < location[0] < screen.get_width()//2+images["gametype2"].get_width()+60 \
                            and screen.get_height()//2+40 < location[1] < screen.get_height()//2+images["gametype2"].get_height()+40:
                            game_type = 2
                        if screen.get_width()//2-images["ok"].get_width()//2 < location[0] < screen.get_width()//2+images["ok"].get_width()//2 \
                            and (screen.get_height()//2)+(5*images["ok"].get_height()) < location[1] < (screen.get_height()//2)+(6*images["ok"].get_height()):
                            mainmenu=True
                            options=False

                        board,current_board,game_mines,sq_size,dimension,mines_count,game_mines_num,empty_squares = reset_game(difficulty,game_type,mines_list)
                        load_images()       

                                
        draw_game(screen,text,text2,ones,tens,huds,mines_count,text3,secs)
        clock.tick(fps)
        win=win_condition(opened_squares,empty_squares)
        pygame.display.update()

if __name__=="__main__":
    main()

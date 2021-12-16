'''
Johns Hopkins University
Department of Chemical and Biomolecular Engineering
Software Carpentry Project
Final Project Fall 2021
Authors: Dake Guo, Yu Xu

Welcome to our final project!
The goal of this project is to write a python code in order to
generate a playable puzzle game
The puzzle game is set to three levels, 3*3, 4*4, 5*5, press l/m/h to
enter either mode
you can you mouse or WASD to complete the puzzle.

In order to play the puzzle game, you will need this python file and .TTF file
and images can be found in our repository.
You can change any pictures you want to enjoy the game time.
You can also change the difficulty of the game any time you want.

The main idea of this file is to generate blocks that compose puzzle block,
break the picture into fragements and reshuffle it.
Thus far you can change the difficuly of the game anytime you want.

Hope you enjoy the game!
'''

import os
import sys
import random
import pygame
from pygame.constants import *


# check if puzzle worked
def ifend(screen, size):
    if isinstance(size, int):
        grid = size * size
        for i in range(grid - 1):
            if screen[i] != i:
                return False
        return True


# blank block move left
def Right(screen, void, col):
    if void % col == 0:
        return void
    screen[void - 1], screen[void] = screen[void], screen[void - 1]
    return void - 1


# blank block move right
def Left(screen, void, col):
    if (void + 1) % col == 0:
        return void
    screen[void + 1], screen[void] = screen[void], screen[void + 1]
    return void + 1


# blank block move up
def Down(screen, void, col):
    if void < col:
        return void
    screen[void - col], screen[void] = screen[void], screen[void - col]
    return void - col


# blank block move down
def Up(screen, void, row, col):
    if void >= (row - 1) * col:
        return void
    screen[void + col], screen[void] = screen[void], screen[void + col]
    return void + col


def Mix(row, col, grid):
    # Rearrange the blocks
    screen = []
    for i in range(grid):
        screen.append(i)
    # create a void block in the right corner
    void = grid - 1
    screen[void] = -1
    for i in range(10):
        direction = random.randint(0, 3)
        # move to the left
        if direction == 0:
            void = Left(screen, void, col)
        # move to the right
        elif direction == 1:
            void = Right(screen, void, col)
        # move up
        elif direction == 2:
            void = Up(screen, void, row, col)
        # move down
        elif direction == 3:
            void = Down(screen, void, col)
    return screen, void


# choose image randomly
def Chosepicture(picture_path):
    picturename = os.listdir(picture_path)
    # verify whether there is a picture
    # the image save path is same as the program path,
    # convenient to get the path
    # then get the image path
    if len(picturename) > 0:
        return os.path.join(picture_path, random.choice(picturename))


# interface at the end of the game
def Endpart(window, width, height):
    black = (255, 255, 255)
    red = (255, 0, 0)
    purple = (255, 0, 255)
    window.fill(black)

    # save fonts and graph into resources
    fontpath = os.path.join(os.getcwd(), 'resources/font/JDJYZHONG.TTF')
    # set the font size
    font1 = pygame.font.Font(fontpath, width // 10)
    font2 = pygame.font.Font(fontpath, width // 20)
    font3 = pygame.font.Font(fontpath, width // 20)

    # set the color and messages for the interface
    one = font1.render("You've succeeded!", True, purple)
    two = font2.render('Congratulations!', True, red)
    three = font3.render('Well Done!', True, red)

    # set the location of the wordings at the interface
    # location for You've succeeded!
    onerect = one.get_rect()
    onerect.midtop = (width / 2, height / 10)
    # location for Congratulations!
    tworect = two.get_rect()
    tworect.midtop = (width / 2, height / 2)
    # location for Well Done!
    threerect = three.get_rect()
    threerect.midtop = (width / 2, height / 1.5)

    # Display the messages
    window.blit(one, onerect)
    window.blit(two, tworect)
    window.blit(three, threerect)
    pygame.display.update()

    # See if the game should be ended
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        pygame.display.update()


# interface at the begining of the game
def Startpart(window, width, height):
    black = (255, 255, 255)
    red = (255, 0, 0)
    blue = (0, 0, 255)
    green = (0, 255, 255)
    window.fill(black)

    # set font size
    fontpath = os.path.join(os.getcwd(), 'resources/font/JDJYZHONG.TTF')
    font1 = pygame.font.Font(fontpath, width//10)
    font2 = pygame.font.Font(fontpath, width//22)

    # set the color and the messages
    one = font1.render('Game Starts!', True, red)
    two = font2.render('To select the mode, press H or M or L', True, blue)
    three = font2.render('H-5*5, M-4*4, L-3*3', True, green)

    # set the location of the messages
    # set the location for Game Starts!
    onerect = one.get_rect()
    onerect.midtop = (width/2, height/10)

    # set the location for To select the mode, press H or M or L
    tworect = two.get_rect()
    tworect.midtop = (width/2, height/2)

    # set the location for H-5*5, M-4*4, L-3*3
    threerect = three.get_rect()
    threerect.midtop = (width/2, height/1.5)

    # display the messages
    window.blit(one, onerect)
    window.blit(two, tworect)
    window.blit(three, threerect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == ord('l'):
                    return 3
                elif event.key == ord('m'):
                    return 4
                elif event.key == ord('h'):
                    return 5
        pygame.display.update()


# Main function
def main():
    # initalization
    pygame.init()
    clock = pygame.time.Clock()
    # load image
    picture_path = os.path.join(os.getcwd(), 'resources/pictures')
    picture = pygame.image.load(Chosepicture(picture_path))
    picture = pygame.transform.scale(picture, (600, 600))
    picture_rect = picture.get_rect()
    # setup window
    window = pygame.display.set_mode((600, 600))
    pygame.display.set_caption('PUZZLE GAME')
    # start up interface
    size = Startpart(window, picture_rect.width, picture_rect.height)
    assert isinstance(size, int)
    row, col = size, size
    grid = size * size
    # recognize the size of block
    blockwidth = picture_rect.width // col
    blockheight = picture_rect.height // row
    # verify if the initialization is correct
    while True:
        game_screen, void = Mix(row, col, grid)
        if not ifend(game_screen, size):
            break
    # set a boolean value to determine whether to exit the game
    bool = True
    while bool:
        # determine whether exit the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            # keyboard operation(WASD for up, down, left and right keys)
            elif event.type == pygame.KEYDOWN:
                # move left
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    void = Left(game_screen, void, col)
                # move right
                elif event.key == pygame.K_RIGHT or event.key == ord('d'):
                    void = Right(game_screen, void, col)
                # move up
                elif event.key == pygame.K_UP or event.key == ord('w'):
                    void = Up(game_screen, void, row, col)
                # move down
                elif event.key == pygame.K_DOWN or event.key == ord('s'):
                    void = Down(game_screen, void, col)

            # mouse operation
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = pygame.mouse.get_pos()
                x_pos = x // blockwidth
                y_pos = y // blockheight
                a = x_pos + y_pos * col
                # move left
                if a == void + 1:
                    void = Left(game_screen, void, col)
                # move right
                elif a == void - 1:
                    void = Right(game_screen, void, col)
                # move up
                elif a == void + col:
                    void = Up(game_screen, void, row, col)
                # move down
                elif a == void - col:
                    void = Down(game_screen, void, col)

        # verify if the game is end
        if ifend(game_screen, size):
            game_screen[void] = grid - 1
            bool = False
        # refresh the screem
        window.fill((255, 255, 255))

        for i in range(grid):
            if game_screen[i] == -1:
                continue
            x_pos = i // col
            y_pos = i % col
            gs = game_screen
            w = blockwidth
            h = blockheight
            rect = pygame.Rect(y_pos * w, x_pos * h, w, h)
            place = pygame.Rect((gs[i] % col) * w, (gs[i] // col) * h, w, h)
            window.blit(picture, rect, place)

        for i in range(col + 1):
            pr = picture_rect
            pygame.draw.line(window, (0, 0, 0), (i * w, 0), (i * w, pr.height))

        for i in range(row + 1):
            pr = picture_rect
            pygame.draw.line(window, (0, 0, 0), (0, i * h), (pr.width, i * h))

        pygame.display.update()
        clock.tick(10)

    # display the end interface
    Endpart(window, picture_rect.width, picture_rect.height)
main()

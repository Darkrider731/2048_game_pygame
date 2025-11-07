import pygame as pg

import brains
import interface
import recources

from tiles import Tile
from interface import key_pressed
from error import Error


pg.init()
pg.display.set_caption("2048")
pg.display.set_icon(recources.icon)
screen = pg.display.set_mode((330, 330))
screen.fill((80, 80, 80))

zero = recources.zero
two = recources.two
four = recources.four
eight = recources.eight
sixteen = recources.sixteen
thirty_two = recources.thirty_two
sixty_four = recources.sixty_four
one_twenty_eight = recources.one_twenty_eight
two_fifty_six = recources.two_fifty_six
five_twelve = recources.five_twelve

tiles_group = pg.sprite.Group()


def error(place):
    error_handle = Error(place)
    error_handle.handle_error()

#error(46)

def output(number, y, x, ):
    if x == 0:
        if y == 0:
            x_pos = 50
            y_pos = 50
        elif y == 1:
            x_pos = 50
            y_pos = 125
        elif y == 2:
            x_pos = 50
            y_pos = 200
        elif y == 3:
            x_pos = 50
            y_pos = 275
        else:
            error(1)

    elif x == 1:
        if y == 0:
            x_pos = 125
            y_pos = 50
        elif y == 1:
            x_pos = 125
            y_pos = 125
        elif y == 2:
            x_pos = 125
            y_pos = 200
        elif y == 3:
            x_pos = 125
            y_pos = 275
        else:
            error(2)

    elif x == 2:
        if y == 0:
            x_pos = 200
            y_pos = 50
        elif y == 1:
            x_pos = 200
            y_pos = 125
        elif y == 2:
            x_pos = 200
            y_pos = 200
        elif y == 3:
            x_pos = 200
            y_pos = 275
        else:
            error(3)

    else:
        if y == 0:
            x_pos = 275
            y_pos = 50
        elif y == 1:
            x_pos = 275
            y_pos = 125
        elif y == 2:
            x_pos = 275
            y_pos = 200
        elif y == 3:
            x_pos = 275
            y_pos = 275
        else:
            error(4)

    if number == 0:
        tile_image = zero

    elif number == 2:
        tile_image = two

    elif number == 4:
        tile_image = four

    elif number == 8:
        tile_image = eight

    elif number == 16:
        tile_image = sixteen

    elif number == 32:
        tile_image = thirty_two

    elif number == 64:
        tile_image = sixty_four

    elif number == 128:
        tile_image = one_twenty_eight

    elif number == 256:
        tile_image = two_fifty_six

    elif number == 512:
        tile_image = five_twelve

    else:
        error(5)

    title_tile = Tile((x_pos, y_pos), tile_image)
    tiles_group.add(title_tile)


def conversion(grid):
    for i in range(4):
        for j in range(4):
            value = (grid[i][j])
            output(value, i, j, )


def move(direction, mat):
    if direction == "RIGHT":
        mat, flag = brains.move_right(mat)
        brains.add_new_2(mat)
        return mat

    if direction == "LEFT":
        mat, flag = brains.move_left(mat)
        brains.add_new_2(mat)
        return mat

    if direction == "UP":
        mat, flag = brains.move_up(mat)
        brains.add_new_2(mat)
        return mat

    if direction == "DOWN":
        mat, flag = brains.move_down(mat)
        brains.add_new_2(mat)
        return mat


mat = brains.init()
conversion(mat)

tiles_group.draw(screen)
pg.display.flip()

not_out = True
waiting = "NULL"


def run_game(not_out, waiting, mat):
    while not_out:
        while waiting == "NULL":
            waiting = key_pressed()

        mat = move(waiting, mat)

        for tile in tiles_group:
            tiles_group.remove(tile)
        conversion(mat)
        screen.fill((80, 80, 80))
        tiles_group.draw(screen)
        pg.display.flip()
        not_out, status = brains.get_current_state(mat)
        waiting = "NULL"
    return status




def proceed():
    if status == 'WON':
        input_wait = True
        key = "NULL"
        while input_wait:
            screen.blit(recources.you_loose, (105, 150))
            pg.display.flip()
            input_wait = interface.key_pressed_is()


    elif status == 'LOST':
        input_wait = True
        while input_wait:
            screen.blit(recources.you_win, (80, 120))
            pg.display.flip()
            input_wait = interface.key_pressed_is()
status = 'LOST'




while True:
    status = run_game(not_out, waiting, mat)
    proceed()



else:
    error(9)

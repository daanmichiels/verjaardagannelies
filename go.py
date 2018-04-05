#!/usr/bin/env python3

import numpy as np
from scipy.ndimage import imread
from numpy.random import permutation

def main():
    perm_row = permutation(25)
    perm_col = permutation(25)

    im = imread('qr.png')
    qr = [[False for y in range(25)] for x in range(25)]

    hint = ['########         ########',
            '########         ########',
            '########         ########',
            '########         ########',
            '########         ########',
            '########         ########',
            '########         ########',
            '########         ########',
            '                         ',
            '                         ',
            '                         ',
            '                         ',
            '                         ',
            '                         ',
            '                         ',
            '                         ',
            '                #####    ',
            '########        #####    ',
            '########        #####    ',
            '########        #####    ',
            '########        #####    ',
            '########                 ',
            '########                 ',
            '########                 ',
            '########                 ']

    for i in range(25):
        y = int(120 / 25.0 * i + 1)
        for j in range(25):
            x = int(120 / 25.0 * j + 1)
            qr[j][i] = (im[y,x,0] < 128)

    for x in range(25):
        for y in range(25):
            if hint[y][x] is not '#':
                continue
            print('<div class="hint" style="left: ' + str(30*18 + 18*x) + 'px; top: ' + str(36 + 18*y) + 'px; background-color: ', end='');
            print('#000' if qr[x][y] else '#fff', end='')
            print('"></div>');

    for y in range(25):
        print('<div id="row' + str(y) +'" class="row" style="left: 36px; top: ' + str(36 + 18*y) + 'px;">');
        for x in range(25):
            print('<div id="item' + str(x) + '" class="item" style="background-color: ', end='');
            print('#000' if qr[x][perm_row[y]] else '#fff', end='')
            print(';"></div>');
        print('</div>')

    print('')

    for x in range(25):
        print('<div id="column' + str(x) +'" class="column" style="left: ' + str(18*58 + 18*x) + 'px; top: 36px;">');
        for y in range(25):
            print('<div id="item' + str(y) + '" class="item" style="background-color: ', end='');
            print('#000' if qr[perm_col[x]][y] else '#fff', end='')
            print(';"></div>');
        print('</div>')


if __name__ == '__main__':
    main()

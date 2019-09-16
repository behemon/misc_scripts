from collections import namedtuple
from fractions import Fraction
from copy import copy

Colour = namedtuple('Colour', 'r,g,b')
Colour.copy = lambda self: copy(self)

black = Colour(0, 0, 0)
white = Colour(255, 255, 255)  # Colour ranges are not enforced.


class Bitmap():
    def __init__(self, width=40, height=40, background=white):
        assert width > 0 and height > 0 and type(background) == Colour
        self.width = width
        self.height = height
        self.background = background
        self.map = [[background.copy() for w in range(width)] for h in range(height)]

    def fillrect(self, x, y, width, height, colour=black):
        assert x >= 0 and y >= 0 and width > 0 and height > 0 and type(colour) == Colour
        for h in range(height):
            for w in range(width):
                self.map[y + h][x + w] = colour.copy()

    def chardisplay(self):
        txt = [''.join(' ' if bit == self.background else '@'
                       for bit in row)
               for row in self.map]
        # Boxing
        txt = ['|' + row + '|' for row in txt]
        txt.insert(0, '+' + '-' * self.width + '+')
        txt.append('+' + '-' * self.width + '+')
        print('\n'.join(reversed(txt)))

    def set(self, x, y, colour=black):
        assert type(colour) == Colour
        self.map[y][x] = colour

    def get(self, x, y):
        return self.map[y][x]


# bitmap = Bitmap(20, 10)
# bitmap.fillrect(4, 5, 6, 3)
# assert bitmap.get(5, 5) == black
# assert bitmap.get(0, 1) == white
# bitmap.set(0, 1, black)
# assert bitmap.get(0, 1) == black
# bitmap.chardisplay()

def lines(self, x0, y0, x1, y1):
    "Bresenham's line algorithm"
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    x, y = x0, y0
    sx = -1 if x0 > x1 else 1
    sy = -1 if y0 > y1 else 1
    if dx > dy:
        err = dx / 2.0
        while x != x1:
            self.set(x, y)
            err -= dy
            if err < 0:
                y += sy
                err += dx
            x += sx
    else:
        err = dy / 2.0
        while y != y1:
            self.set(x, y)
            err -= dx
            if err < 0:
                x += sx
                err += dy
            y += sy
    self.set(x, y)


def line(self, x0, y0, x1, y1):
    rev = reversed
    if abs(y1 - y0) <= abs(x1 - x0):
        x0, y0, x1, y1 = y0, x0, y1, x1
        rev = lambda x: x
    if x1 < x0:
        x0, y0, x1, y1 = x1, y1, x0, y0
    leny = abs(y1 - y0)
    for i in range(leny + 1):
        self.set(*rev((round(Fraction(i, leny) * (x1 - x0)) + x0, (1 if y1 > y0 else -1) * i + y0)))


# Bitmap.line = line



Bitmap.line = line

bitmap = Bitmap(17, 17)
for points in ((1, 8, 8, 16), (8, 16, 16, 8), (16, 8, 8, 1), (8, 1, 1, 8)):
    bitmap.line(*points)
bitmap.chardisplay()

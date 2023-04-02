import pygame

pygame.init()
# setting the window size (weight and height):
size = (350, 250)
screen = pygame.display.set_mode(size)

# setting the name of the program:
name = "My first game"
pygame.display.set_caption(name)

# loading the image of shortcut (icon):
# the image must be placed in the same
# directory in advance
# img = pygame.image.load("image_file_name.png")

# setting the font:
# To list all system fonts, print next code:
# 1. a = pygame.font.get_fonts()
# 2. print(a)
font = pygame.font.SysFont('arialblack', 2)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
# setting the text: text, antialias, colour, background colour
follow1 = font.render("0000", True, (0, 255, 0), (0, 255, 0))
follow2 = font.render("0000", True, (255, 0, 0), (255, 0, 0))
follow3 = font.render("0000", True, (255, 255, 0), (255, 255, 0))
follow4 = font.render("0000", True, (0, 0, 255), (0, 0, 255))
# getting size of object: weight and height
w1, h1 = follow1.get_size()
w2, h2 = follow2.get_size()
w3, h3 = follow3.get_size()
w4, h4 = follow4.get_size()
x1, y1 = 10, 30
x2, y2 = 30, 50
x3, y3 = 50, 70
x4, y4 = 70, 90
dx1, dy1 = 1, 1
dx2, dy2 = 2, 1
dx3, dy3 = 1, 3
dx4, dy4 = 4, 2
# module pygame.time and class Clock -
# to adjust objects moving speed
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    # to adjust objects moving speed
    # (fps - frames per second)
    clock.tick(100)
    # to fill screen by black colour (to reset)
    # before the next move of the object
    screen.fill(BLACK)
    # displaying (rendering) text with coordinates (x, y)
    # over the black screen
    screen.blit(follow1, (x1, y1))
    screen.blit(follow2, (x2, y2))
    screen.blit(follow3, (x3, y3))
    screen.blit(follow4, (x4, y4))
    x1 += dx1
    y1 += dy1
    if x1 + w1 > 350 or x1 < 0:
        dx1 = -dx1
    if y1 + h1 > 250 or y1 < 0:
        dy1 = -dy1
    x2 += dx2
    y2 += dy2
    if x2 + w2 > 350 or x2 < 0:
        dx2 = - dx2
    if y2 + h2 > 250 or y2 < 0:
        dy2 = -dy2
    x3 += dx3
    y3 += dy3
    if x3 + w3 > 350 or x3 < 0:
        dx3 = -dx3
    if y3 + h3 > 250 or y3 < 0:
        dy3 = -dy3
    x4 += dx4
    y4 += dy4
    if x4 + w4 > 350 or x4 < 0:
        dx4 = -dx4
    if y4 + h4 > 250 or y4 < 0:
        dy4 = -dy4
    pygame.display.update()

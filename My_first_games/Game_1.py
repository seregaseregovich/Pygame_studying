import pygame

size = (350, 250)
name = "My program"
pygame.display.set_mode(size)
pygame.display.set_caption(name)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        else:
            pass

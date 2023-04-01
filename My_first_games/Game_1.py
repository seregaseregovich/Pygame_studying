import pygame

# setting the window size
size = (350, 250)
pygame.display.set_mode(size)

# setting the name of the program
name = "My first game"
pygame.display.set_caption(name)

# loading the image of shortcut
# the image must be placed in the same
# directory in advance
# img = pygame.image.load("image_file_name.png")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        else:
            pass

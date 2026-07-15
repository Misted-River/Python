import pygame
from pygame.locals import *

w = 1920
h = 1080


pygame.init()

canvas = pygame.display.set_mode((1920,1080)) # canvas size -> creates screen -> background 
background = pygame.image.load('placeholder_bg.png').convert() # initialise image -> surface2

# constants
position = (0,0)
bottom_line_height = 100 # move based on this height, which is centered

# set up objects
path = pygame.image.load('unnamed.png').convert_alpha() # patyhway moves -> surface2
player = pygame.image.load('player_placeholder.jpg').convert_alpha() # player image -> surface2
rocks = pygame.image.load('rocks.png').convert_alpha() # rocks on pathways, move same as path
path_rect = path.get_rect()

width_path = path_rect.width
height_path = path_rect.height

# resizing to fit
path = pygame.transform.smoothscale(path,(width_path*1.7, height_path*1.7)) 
rocks = pygame.transform.smoothscale(rocks,(width_path*1.7, height_path*1.7))
background = pygame.transform.smoothscale(background,(1920,1080)) # resizing image

path_mask = pygame.mask.from_surface(path)
path_rect = path.get_rect()

player_mask = pygame.mask.from_surface(player)
player_rect = player.get_rect() #  original player position (rect(0,0,300,180))

# rectangle -> rock
rocks_rect = path_rect # rocks is same rect as path's recxtangle

# extra for path
width_path = path_rect.width
height_path = path_rect.height

#----------------------------------------------------------------------------------
pygame.display.set_caption("Welcome to The Pathways") # name of game for window

exit = False
# mouse
#mouse_pos = pygame.mouse.get_pos()

pygame.event.get()
pygame.display.set_icon(background)

# player 
x = 800 # position x
y = 345 # position y

x_path = -365
y_path = 240

width = player.get_width()
height = player.get_height()



#----------------------------------------------------------------------------------
canvas.blit(background, dest=position) # render image onto surface, background
canvas.blit(player, player_rect) # render image onto surface, original position
canvas.blit(path, path_rect) # render image onto surface, path
canvas.blit(rocks, path_rect) # render image onto surface, rocks

hist = [] # history of last key pressed

while not exit:
    keys = pygame.key.get_pressed()
    w = keys[pygame.K_w]
    a = keys[pygame.K_a]
    s = keys[pygame.K_s]
    d = keys[pygame.K_d]

    

    offset = (x - x_path), (y - y_path)
    result = path_mask.overlap(player_mask,(offset))

    # variables for movement speed
    if result:
        velo = 2 # up down direction
        velo_path = 20 # up down direction
    else:
        velo = 3 # up down direction
        velo_path = 34 # up down direction

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True


    if w and y>0: # key = k_(the key) events 
        y -= velo*2
        hist.clear()
        hist.append("w")
        if w and y>0 and (not s) and (y_path<310) and w and y>0:
            y_path += velo_path
            hist.clear()
            hist.append("w")
    
    if result and hist[0] == "w" and s:
        y += velo*4
        y_path -= velo_path
        hist[0] == "none"
    if result and hist[0] == "s" and w:
        y -= velo*4
        y_path += velo_path
        hist[0] == "none"
    if result and hist[0] == "a" and d:
        x += velo*4
        x_path += velo_path
        hist[0] == "none"
    if result and hist[0] == "d" and a:
        x += velo*4
        x_path -= velo_path
        hist[0] == "none"
    

    if s and  y<1080-height:
        y += velo*2
        hist.clear()
        hist.append("s")

        if s and  y<1080-height and (not w) and y_path>-2525:
            y_path -= velo_path

            hist.clear()
            hist.append("s")

    if a and  x>0:
        x -= velo*2
        hist.clear()
        hist.append("a")

        if (not d) and x_path<-200:
            x_path += velo_path

            hist.clear()
            hist.append("a")


    if d and x<1920-width:
        x += velo*2
        hist.clear()
        hist.append("d")

        if (not a) and ( x<1920-width and x_path>-680):
            x_path -= velo_path
            hist.clear()
            hist.append("d")


    canvas.blit(background, dest=position) # render image onto surface, background
    canvas.blit(path, (x_path,y_path)) # render image onto surface, original position
    canvas.blit(rocks, (x_path,y_path)) # render image onto surface, rocks
    canvas.blit(player, (x,y)) # render image onto surface, original position
    pygame.display.update()
    
pygame.quit()



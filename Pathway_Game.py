import pygame
from pygame.locals import *

w = 1000
h = 1000


pygame.init()

canvas = pygame.display.set_mode((1000,1000)) # canvas size -> creates screen -> background 
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
background = pygame.transform.smoothscale(background,(1000,1000)) # resizing image

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

hist = ["none"] # history of last key pressed

def historyadd(lista,key):
    lista.clear()
    lista.append(key)

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
        velo = -3 # up down direction
        velo_path = -34 # up down direction
    else:
        velo = 3 # up down direction
        velo_path = 34 # up down direction

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

    if w and y>0: # key = k_(the key) events 
        y -= velo*2
                    
        if w and y>0 and (not s) and (y_path<310) and w and y>0:
            y_path += velo_path
            
        if hist[0] == "s":
            historyadd(hist,"s")
        elif hist[0] == "w":
            historyadd(hist,"w")

        if result and hist[0] == "w":
            y -= velo
            y_path += velo_path
            hist[0] ="w"
        if result and hist[0] == "s":
            y += velo
            y_path -= velo_path
            hist[0] ="s"


    if s and  y<1080-height:
        y += velo*2

        if s and  y<1080-height and (not w) and y_path>-2525:
            y_path -= velo_path

        if hist[0] == "w":
            historyadd(hist,"w")
        elif hist[0] == "s":
            historyadd(hist,"s")

        if result and hist[0] == "s":
            y -= velo
            y_path += velo_path
            hist[0] ="s"
        if result and hist[0] == "w":
            y += velo
            y_path -= velo_path
            hist[0] ="s"

            

    if a and  x>0:
        x -= velo*2
        historyadd(hist,"d")

        if (not d) and x_path<-200:
            x_path += velo_path
            historyadd(hist,"d")

        if result and hist[0] == "d":
            x += velo
            x_path -= velo_path
            hist[0] ="a"
            
            
        
    if d and x<1920-width:
        x += velo*2
        historyadd(hist,"a")

        if (not a) and ( x<1920-width and x_path>-680):
            x_path -= velo_path
            historyadd(hist,"a")

        if result and hist[0] == "a" and d:
            x += velo
            x_path += velo_path
            hist[0] ="d"
     

    

    print(hist[0])
    canvas.blit(background, dest=position) # render image onto surface, background
    canvas.blit(path, (x_path,y_path)) # render image onto surface, original position
    canvas.blit(rocks, (x_path,y_path)) # render image onto surface, rocks
    canvas.blit(player, (x,y)) # render image onto surface, original position
    pygame.display.update()
    
pygame.quit()



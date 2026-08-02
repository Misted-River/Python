import pygame
from pygame.locals import *


w = 1920
h = 1080

pygame.init()

canvas = pygame.display.set_mode((1920,1080)) # canvas size -> creates screen -> background 
background = pygame.image.load('place_holder.png').convert() # initialise image -> surface2
# constants
position = (0,0)
bottom_line_height = 100 # move based on this height, which is centered

# set up objects
path = pygame.image.load('pa_place.png').convert_alpha() # patyhway moves -> surface2
player = pygame.image.load('play_place.png').convert_alpha() # player image -> surface2
rocks = pygame.image.load('rocks.png').convert_alpha() # rocks on pathways, move same as path
dust = pygame.image.load('cosmic_dust.png').convert_alpha() # cosmic dust on pathways, move same as path
path_rect = path.get_rect()

width_path = path_rect.width
height_path = path_rect.height

# resizing to fit
path = pygame.transform.smoothscale(path,(width_path*1.7, height_path*1.7)) 
rocks = pygame.transform.smoothscale(rocks,(width_path*1.7, height_path*1.7))
dust = pygame.transform.smoothscale(dust,(width_path*1.7, height_path*1.7))
background = pygame.transform.smoothscale(background,(1920,1080)) # resizing image

player.set_colorkey((255,255,255))
dust.set_colorkey((255,255,255))

path_mask = pygame.mask.from_surface(path)
dust_mask = pygame.mask.from_surface(dust)
path_rect = path.get_rect()

player_mask = pygame.mask.from_surface(player)
player_rect = player.get_rect() #  original player position (rect(0,0,300,180))

# rectangle -> rock
rocks_rect = path_rect # rocks is same rect as path's recxtangle
dust_rect = path_rect # dust is same rect as path's recxtangle
# extra for path
width_path = path_rect.width
height_path = path_rect.height
#----------------------------------------------------------------------------------
pygame.display.set_caption("Welcome to The Pathways") # name of game for window

exit = False
# mouse
mx,my = pygame.mouse.get_pos()

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
canvas.blit(dust, path_rect) # render image onto surface, dust


hist = ["none","none"] # history of last key pressed

while not exit:

    keys = pygame.key.get_pressed()
    w = keys[pygame.K_w]
    a = keys[pygame.K_a]
    s = keys[pygame.K_s]
    d = keys[pygame.K_d]
    shift = keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]

    offset = (x - x_path), (y - y_path)
    poi = path_mask.overlap(player_mask,(offset)) 

    # variables for movement speed
    if poi: 
        velo = -3
        velo_path = -34 
    else:
        velo = 3 # up down direction
        velo_path = 34 # up down direction

    clicks = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: # left click
                click_position = event.pos
                clicks = True
            else:
                clicks = False

    if clicks:
        print("click")
    else:
        print("no click")

    if shift:
        velo = 6 # up down direction
        velo_path = 60 # up down direction

    if w and y>0: # key = k_(the key) events 
        if not poi and not a and not d:
            y -= velo*2
            hist[0] ="w"
            if not s and (y>0 and y_path<310)and x_path<-10:
                y_path += velo_path

        if poi and hist[0] == "s":
            y += velo
            hist[0] ="s"
        if poi and hist[0] == "d":
            x += velo
            hist[0] ="d"
        if poi and hist[0] == "a":
            x -= velo
            hist[0] ="a"

        if poi and hist[0] == "a" and hist[1] == "w":
            x -= velo
            y -= velo
            hist[0] ="a"
            hist[1] ="s"
        if poi and hist[0] == "d" and hist[1] == "w":
            x += velo
            y -= velo
            hist[0] ="d"
            hist[1] ="s"
    
    if  s and  y<1080-height:
        if not poi and not a and not d:
            y += velo*2
            hist[0] ="s"
            if (not w) and (y<1080-height and y_path>-2525):
                y_path -= velo_path

        if poi and hist[0] == "w":
            y -= velo
            hist[0] ="w" 
        if poi and hist[0] == "d":
            x += velo
            hist[0] ="d"
        if poi and hist[0] == "a":
            x -= velo
            hist[0] ="a"

    if a and  x>0:
        if not poi:
            x -= velo*2
            hist[0] ="a"
            if (not d) and x_path<-50:
                x_path += velo_path

        if poi and hist[0] == "d":
            x += velo
            hist[0] ="d"
        if poi and hist[0] == "w":
            y -= velo
            hist[0] ="w"
        if poi and hist[0] == "s":
            y += velo
            hist[0] ="s"
            
    if d and x<1920-width:
        if not poi:
            x += velo*2
            hist[0] ="d"
            if (not a) and (x<1920-width and x_path>-570):
                x_path -= velo_path

        if poi and hist[0] == "a":
            x -= velo
            hist[0] ="a" 
        if poi and hist[0] == "w":
            y -= velo
            hist[0] ="w"
        if poi and hist[0] == "s":
            y += velo
            hist[0] ="s"
    
    canvas.blit(background, dest=position) # render image onto surface, background
    canvas.blit(path, (x_path,y_path)) # render image onto surface, original position
    canvas.blit(rocks, (x_path,y_path)) # render image onto surface, rocks
    canvas.blit(dust, (x_path,y_path)) # render image onto surface, dust
    canvas.blit(player, (x,y)) # render image onto surface, original position
    pygame.display.update()
    
pygame.quit()

# more collision detection yayyyyy, but seriously I need to detect if a mouse clicks on some image masks /sarc
import pygame

pygame.init() 

canvas = pygame.display.set_mode((1920,1080)) # canvas size -> creates screen -> background 


# constants
position = (0,0)
bottom_line_height = 100 # move based on this height, which is centered

# set up objects
player = pygame.image.load('player_placeholder.jpg').convert_alpha() # player image -> surface2
path = pygame.image.load('pathways_place.png').convert_alpha() # patyhway moves -> surface2
rocks = pygame.image.load('rocks.png').convert_alpha() # rocks on pathways, move same as path

# masks
pa_mask = pygame.mask.from_surface(path)
path.set_colorkey((0,0,0))
pl_mask = pygame.mask.from_surface(player)
player.set_colorkey((0,0,0))

loc_player = (player.get_width(),player.get_height())
loc_path = (player.get_width(),player.get_height())




# rectangles
player_rect = player.get_rect() #  original player position (rect(0,0,300,180))
path_pos = path.get_rect()
rocks_pos = path_pos # rocks is same rect as path's recxtangle

width_path = path_pos.width
height_path = path_pos.height

# resizing to fit
path = pygame.transform.smoothscale(path,(width_path*1.7, height_path*1.7)) 
rocks = pygame.transform.smoothscale(rocks,(width_path*1.7, height_path*1.7))

#----------------------------------------------------------------------------------

background = pygame.image.load('placeholder_bg.png').convert() # initialise image -> surface2
background = pygame.transform.smoothscale(background,(1920,1080)) # resizing image

pygame.display.set_caption("Welcome to The Pathways") # name of game for window

exit = False
mouse = pygame.mouse.get_pos()
#objects = [] # gathering all players etc objects in game

pygame.event.get()
pygame.display.set_icon(background)

# player 
x = 800 # positioon x
y = 345 # position y

x_path = -365
y_path = 240

width = player.get_width()
height = player.get_height()

velo = 2 # up down direction
velo_path = 20 # up down direction

canvas.blit(background, dest=position) # render image onto surface, background
canvas.blit(player, player_rect) # render image onto surface, original position
canvas.blit(path, path_pos) # render image onto surface, path
canvas.blit(rocks, path_pos) # render image onto surface, rocks
#canvas.blit(pa_mask,path_pos)
pygame.display.update()

while not exit:
    pygame.display.update()

    keys = pygame.key.get_pressed()

    w = keys[pygame.K_w]
    a = keys[pygame.K_a]
    s = keys[pygame.K_s]
    d = keys[pygame.K_d]


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

    if w and y>0: # key = k_(the key) events 
        y -= velo*2

        if w and y>0 and (not s) and (y_path<310) and w and y>0:
            y_path += velo_path
                
        else:
            velo

    if s and  y<1080-height:
        y += velo*2
        
        if s and  y<1080-height and (not w) and y_path>-2525:
            y_path -= velo_path
                
        else:
            velo

    if a and  x>0:
        x -= velo*2
        if (not d) and x_path<-200:
            x_path += velo_path
        else:
            velo

    if d and x<1920-width:
        x += velo*2
        
        if (not a) and ( x<1920-width and x_path>-680) :
            x_path -= velo_path
        else:
            velo

    canvas.blit(background, dest=position) # render image onto surface, background
    canvas.blit(path, (x_path,y_path)) # render image onto surface, original position
    canvas.blit(rocks, (x_path,y_path)) # render image onto surface, rocks
    canvas.blit(player, (x,y)) # render image onto surface, original position
    
    pygame.display.update()

pygame.quit()

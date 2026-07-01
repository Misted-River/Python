import pygame

pygame.init() # initialise pygame module

position = (0,0)
clock = pygame.time.Clock()


# set up objects
player = pygame.image.load('player_placeholder.jpg')# player image -> surface2
path = pygame.image.load('pathways_place.png')# player image -> surface2

image_size = (1000, 1000)

bottom_line_height = 100 # move based on this height, which is centered



player_rect = player.get_rect() #  original player position (rect(0,0,300,180))

path_pos = path.get_rect()
width_path = path.get_rect().width
height_path = path.get_rect().height

path = pygame.transform.smoothscale(path,(width_path*1.7, height_path*1.7)) # 200,200 is default image size


#----------------------------------------------------------------------------------
canvas = pygame.display.set_mode((1920,1080),pygame.RESIZABLE) # canvas size -> creates screen -> background 
image = pygame.image.load('1.png').convert() # initialise image -> surface2

pygame.draw.line(canvas, 'Black', (0, canvas.get_height() - bottom_line_height), (canvas.get_width(), canvas.get_height() - bottom_line_height), 3) # thickness = 3



path_pos.midbottom = (canvas.get_width() // 2 + 150, canvas.get_height() - 450 - bottom_line_height - 15)
player_rect.midbottom = (canvas.get_width() // 2, canvas.get_height() - bottom_line_height - 15)


image = pygame.transform.smoothscale(image,(1920,1080)) # sizing image

pygame.display.set_caption("Welcome to The Pathways") # name of game for window

exit = False
#refresh = False
mouse = pygame.mouse.get_pos()

objects = [] # gathering all players etc objects in game


pygame.event.get()
pygame.display.set_icon(image)


# player 
x = 800 # positioon x
y = 345 # position y

x_path = -365
y_path = 240


width = player.get_width()
height = player.get_height()

width_path = path.get_width()
height_path = path.get_height()

velo = 5 # up down direction
velo_path = 45 # up down direction





canvas.blit(image, dest=position) # render image onto surface, background
canvas.blit(player, player_rect) # render image onto surface, original position
canvas.blit(path, path_pos) # render image onto surface, path
pygame.display.update()

while not exit:
    keys = pygame.key.get_pressed()

    w = keys[pygame.K_w]
    a = keys[pygame.K_a]
    s = keys[pygame.K_s]
    d = keys[pygame.K_d]
    print("x:",x_path,"y:",y_path )



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

    if w and y>0: # key = k_(the key) events 
        y -= velo
        if (not s) and ( y_path<310) :
             y_path += velo_path
        else:
            velo = 0

    if s and  y<1080-height:
        y += velo
        if (not w) and y_path>-2525:
            y_path -= velo_path
        else:
            velo = 0

    if a and  x>0:
        x -= velo
        if (not d) and x_path<-200:
            x_path += velo_path
        else:
            velo = 10
            x -= velo*2


    if d and x<1920-width:
        x += velo
    
        if (not a) and ( x<1920-width and x_path>-680) :
            x_path -= velo_path
        else:
            velo = 10
            x += velo*2

        

    canvas.blit(image, dest=position) # render image onto surface, background
    canvas.blit(path, (x_path,y_path)) # render image onto surface, original position
    canvas.blit(player, (x,y)) # render image onto surface, original position
    pygame.display.update()

            
        
        

pygame.quit()

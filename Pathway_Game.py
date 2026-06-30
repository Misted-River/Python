import pygame

pygame.init() # initialise pygame module

position = (0,0)



# set up objects
player = pygame.image.load('player_placeholder.jpg')# player image -> surface2
path = pygame.image.load('costume2.svg')# player image -> surface2

image_size = (1000, 1000)

bottom_line_height = 100 # move based on this height, which is centered



player_rect = player.get_rect() #  original player position (rect(0,0,300,180))

path_pos = path.get_rect()
width_path = path.get_rect().width
height_path = path.get_rect().height

path = pygame.transform.smoothscale(path,(width_path*3, height_path*3)) # 200,200 is default image size


#----------------------------------------------------------------------------------
canvas = pygame.display.set_mode((1920,1080),pygame.RESIZABLE) # canvas size -> creates screen -> background 
image = pygame.image.load('Untitled2186_20240824160114.png').convert() # initialise image -> surface2

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
x = 200 # positioon x
y = 200 # position y

x_path = 50
y_path = 50


width = player.get_width()
height = player.get_height()

width_path = path.get_width()
height_path = path.get_height()

velo = 5 # up down direction

velo_path = 15 # up down direction



canvas.blit(image, dest=position) # render image onto surface, background
canvas.blit(player, player_rect) # render image onto surface, original position
canvas.blit(path, path_pos) # render image onto surface, path
pygame.display.update()

while not exit:

    for event in pygame.event.get():
        
        keys = pygame.key.get_pressed()

        if event.type == pygame.QUIT:
            exit = True

        if keys[pygame.K_w] and y>0: # key = k_(the key) events 
            y -= velo
            y_path += velo_path
 
            print("Move the character up")

        if keys[pygame.K_s] and  y<1080-height:
            y += velo
            y_path -= velo_path
            print("Move the character down")

        if keys[pygame.K_a] and  x>0:
            x -= velo 
            x_path += velo_path
            print("Move the character left")

        if keys[pygame.K_d] and x<1920-width:
            x += velo
            x_path -= velo_path
            print("Move the character right")

    canvas.blit(image, dest=position) # render image onto surface, background

    canvas.blit(player, (x,y)) # render image onto surface, original position
    canvas.blit(path, (x_path,y_path)) # render image onto surface, original position

    pygame.display.update()

            
        
        

pygame.quit()

"""
import pygame

pygame.init() # initialise pygame module
img_position = (0,0)

FPS = 100
fps_clock = pygame.time.Clock()
time_counter = 0


# set up Fonts
fontObj = pygame.font.Font(None, 32)
textSufaceObj = fontObj.render('Welcome', True, 'White', None)
textRectObj = textSufaceObj.get_rect()

bottom_line_height = 10

#clock = pygame.time.Clock()
#----------------------------------------------------------------------------------
canvas= pygame.display.set_mode((1920,1080),pygame.RESIZABLE) # canvas size, resizable
image = pygame.image.load('Untitled2186_20240824160114.png').convert() # initialise image, covert to pixels, images are surfaces and change the colour of pixels already on screen

textRectObj.midbottom = (canvas.get_width() // 2, canvas.get_height() - bottom_line_height - 500) # for accurate placing


image= pygame.transform.smoothscale(image,(1920,1080)) # sizing image
pygame.display.set_caption("Welcome to The Pathways") # name

exit = False
mouse = pygame.mouse.get_pos()

refresh = False


pygame.event.get()
pygame.display.set_icon(image)




while exit != True:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w: # key = k_(the key) event
                print("Move the character forwards")
            elif event.key == pygame.K_s:
                print("Move the character backwards")
            elif event.key == pygame.K_a:
                print("Move the character left")
            elif event.key == pygame.K_d:
                print("Move the character right")
        if event.type == pygame.QUIT:
            exit = True
    canvas.fill((20,20,20))
    canvas.blit(image, dest = img_position) # render image onto surface
    canvas.blit(textSufaceObj, textRectObj) # render image onto surface
    pygame.display.update()
    print(mouse)

pygame.quit()

screen_originalvals = [0,0,1,1,1,0] # background

screen = [0]*6 # new list of 6 zeros
for i in range(6):
    screen[i]= screen_originalvals[i]


player_position = 3

while player_position > 1:
    screen[player_position] = screen_originalvals[player_position]
    player_position -= 1
    screen[player_position] = 8
    

    print(screen)

#fontObj = pygame.font.Font(None, 32)

# co-ordinates start from 0,0 in top left so (10,0) would move x to the right from the left (X,Y), when blitting the top left corner of the sourse is used to position the image on the screen

#textSufaceObj = fontObj.render('', True, 'BLack', None) # antialiasing is true
#textRectObj = textSufaceObj.get_rect()

#player_obj = game_object(player,10,3)

# multiple images use python classes

class game_object:
    def __init__(self,image,height,speed): # initialise object -> player, position, speed
        self.speed = speed
        self.image = image
        self.pos = image.get_rect().move(0,height)
 def move(self, up=False, down=False,left=False,right=False):
        if right:
            self.pos.right += self.speed
        if left:
            self.pos.right -= self.speed
        if down:
            self.pos.top += self.speed
        if up:
            self.pos.top -= self.speed
        if self.pos.right > canvas.get_width():
            self.pos.left = 0
        if self.pos.right < player.get_width():
            self.pos.left = 0
        if self.pos.top < 0:
            self.pos.top = canvas.get_height() -player.get_height()

import sys
import pygame
from pygame.locals import *

pygame.init()
pygame.display.set_caption("mask test")

screen = pygame.display.set_mode((500,500))

clock = pygame.time.Clock()

img = pygame.image.load('dot.png').convert_alpha()
img.set_colorkey((0,0,0))

img_2 = pygame.image.load('cosmic_dust.png').convert_alpha()

img_2 = pygame.transform.smoothscale(img_2, (500, 500))

img_2.set_colorkey((0,0,0))
img_loc = (50,50)

mask = pygame.mask.from_surface(img)
mask_2 = pygame.mask.from_surface(img_2)

show_masks = False

while True:
    screen.fill((255,0,0))

    if not show_masks:
        screen.blit(img,img_loc)
        screen.blit(img_2,(0,0))
    else:
        screen.blit(mask.to_surface(unsetcolor=(0,0,0,0),setcolor=(255,255,255,255)),img_loc)
        screen.blit(mask_2.to_surface(unsetcolor=(0,0,0,0),setcolor=(255,255,255,255)),(0,0))
        outline = [(p[0] + img_loc[0],p[1] + img_loc[1]) for p in mask.outline(every=2)] # list of points for outline of mask shape
        pygame.draw.lines(screen,(255,0,255),False,outline,3)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_m:
                show_masks = not show_masks


            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
    pygame.display.update()

#loc_player = (player.get_width(),player.get_height())
#loc_path = (player.get_width(),player.get_height())



def collide(self, mask, x= 0,y=0):
    pl_mask = pygame.mask.from_surface(self)
    offset= (self.x-x),int(player.y - y)
    poi = mask.overlap(pl_mask,offset)
    return poi


 if collide(player,pathborder_mask,0,0) != None:
        print('collide')
    else:
        print('no')

#canvas.blit(pa_mask.to_surface(unsetcolor=(0,0,0,0),setcolor=(255,255,255,255)),(x_path,y_path))

    #pygame.draw.lines(canvas,(255,0,255),False,outline,3)



      #poi_list = []
        #poi_list.append(poi)
        #print(poi_list)

"""
"""

import pygame
from pygame.locals import *
w = 600
h = 600
pygame.init()
canvas = pygame.display.set_mode((600,600)) # canvas size -> creates screen -> background 
# constants
position = (0,0)
bottom_line_height = 100 # move based on this height, which is centered
background = pygame.image.load('place_holder.png').convert() # initialise image -> surface2


# set up objects
dust = pygame.image.load('cosmic_dust.png').convert_alpha()  
dot = pygame.image.load('dot.png').convert_alpha() 

# resizing to fit
dust = pygame.transform.smoothscale(dust,(600,600))
#dust.set_colorkey((255,255,255))
dust_mask = pygame.mask.from_surface(dust)
dust_rect = dust.get_rect() # dust is same rect as path's recxtangle

dot.set_colorkey((255,255,255))
dot_mask = pygame.mask.from_surface(dot)
dot_rect = dot.get_rect()

#----------------------------------------------------------------------------------
pygame.display.set_caption("test") # name of game for window

exit = False

pygame.event.get()

# player 
x_path = -365
y_path = 240

mx,my = pygame.mouse.get_pos()


#----------------------------------------------------------------------------------
canvas.blit(background, dest=position) # render image onto surface, background
canvas.blit(dust, dust_rect) # render image onto surface, dust


hist = ["none","none"] # history of last key pressed

while not exit:
    mx,my = pygame.mouse.get_pos()

    keys = pygame.key.get_pressed()
    w = keys[pygame.K_w]
    a = keys[pygame.K_a]
    s = keys[pygame.K_s]
    d = keys[pygame.K_d]
    shift = keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]

    over_off = (mx - dust_rect.x), (my - dust_rect.y)
    poi_dust = dust_mask.overlap(dot_mask,(over_off))

    clicks = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: # left click
                click_position = event.pos # location mouse -> middle
                clicks = True
            else:
                clicks = False

    if clicks:
        print("click")
        if poi_dust:
            print("Mouse clicked on dust")
            print(poi_dust)

    if shift:
        velo = 12 # up down direction
        velo_path = 136 # up down direction

    canvas.blit(background, dest=position) # render image onto surface, background
    canvas.blit(dust, dust_rect) # render image onto surface, dust

    pygame.display.update()
    
pygame.quit()



import pygame
from pygame.locals import *

w = 500
h = 500

pygame.init()

canvas = pygame.display.set_mode((500,500)) # canvas size -> creates screen -> background 
background = pygame.image.load('place_holder.png').convert() # initialise image -> surface2

# constants
position = (0,0)
bottom_line_height = 100 # move based on this height, which is centered

# set up objects
rocks = pygame.image.load('rocks.png').convert_alpha() # rocks on pathways, move same as path
dust = pygame.image.load('cosmic_dust.png').convert_alpha() # cosmic dust on pathways, move same as path
dot = pygame.image.load('dot.png').convert_alpha() # cosmic dust on pathways, move same as path



# resizing to fit
rocks = pygame.transform.smoothscale(rocks,(500, 500))
dust = pygame.transform.smoothscale(dust,(500, 500))
background = pygame.transform.smoothscale(background,(500,500)) # resizing image
dot = pygame.transform.smoothscale(dot,(10,10)) # resizing image


dust_mask = pygame.mask.from_surface(dust)
dot_mask = pygame.mask.from_surface(dot) # create mask for circle



dot_rect = dot.get_rect() # original circle position (rect(0,0,10,10))
rocks_rect = rocks.get_rect() # rocks is same rect as path's recxtangle
dust_rect = dust.get_rect() # dust is same rect as path's recxtangle

# extra for path
#----------------------------------------------------------------------------------
pygame.display.set_caption("Welcome to The Pathways") # name of game for window

exit = False

pygame.event.get()
pygame.display.set_icon(background)


# player 
x = 800 # position x
y = 345 # position y

x_path = -365
y_path = 240

mx,my = pygame.mouse.get_pos()


#----------------------------------------------------------------------------------
canvas.blit(background, dest=position) # render image onto surface, background
canvas.blit(rocks, rocks_rect) # render image onto surface, rocks
canvas.blit(dust, dust_rect) # render image onto surface, dust
canvas.blit(dot, dot_rect) # render image onto surface, original position

hist = ["none","none"] # history of last key pressed

while not exit:
    mx,my = pygame.mouse.get_pos()

    keys = pygame.key.get_pressed()
    w = keys[pygame.K_w]
    a = keys[pygame.K_a]
    s = keys[pygame.K_s]
    d = keys[pygame.K_d]
    shift = keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]

    offset = (x - x_path), (y - y_path)
    over_off = (x_path - mx ), (y_path - my)

    poi_circl = dot_mask.overlap(dust_mask,(over_off))

    clicks = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: # left click
                click_position = event.pos # location mouse -> middle
                clicks = True
            else:
                clicks = False

    if clicks:
        print("click")
        if poi_circl:
            print("Mouse clicked on dust")
            print(poi_circl)


    canvas.blit(background, dest=position) # render image onto surface, background
    canvas.blit(rocks, (x_path,y_path)) # render image onto surface, rocks
    canvas.blit(dust, (x_path,y_path)) # render image onto surface, dust
    canvas.blit(dot, (mx,my)) # render image onto surface, original position

    pygame.display.update()
    
pygame.quit()

"""
"""
import pygame
from pygame.locals import *
w = 600
h = 600
pygame.init()
canvas = pygame.display.set_mode((600,600)) # canvas size -> creates screen -> background 
# constants
position = (0,0)
bottom_line_height = 100 # move based on this height, which is centered
background = pygame.image.load('place_holder.png').convert() # initialise image -> surface2




#----------------------------------------------------------------------------------
pygame.event.get()

# player 
x_path = -365
y_path = 240

mx,my = pygame.mouse.get_pos()


#----------------------------------------------------------------------------------
canvas.blit(background, dest=position) # render image onto surface, background


hist = ["none","none"] # history of last key pressed

while not exit:
    mx,my = pygame.mouse.get_pos()

    keys = pygame.key.get_pressed()
    w = keys[pygame.K_w]
    a = keys[pygame.K_a]
    s = keys[pygame.K_s]
    d = keys[pygame.K_d]
    shift = keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]

    over_off = (mx - dust_rect.x), (my - dust_rect.y)
    poi_dust = dust_mask.overlap(dot_mask,(over_off))

    clicks = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: # left click
                click_position = event.pos # location mouse -> middle
                clicks = True
            else:
                clicks = False

    if clicks:
        print("click")
        if poi_dust:
            print("Mouse clicked on dust")
            print(poi_dust)

    if shift:
        velo = 12 # up down direction
        velo_path = 136 # up down direction

    canvas.blit(background, dest=position) # render image onto surface, background
    canvas.blit(dust, dust_rect) # render image onto surface, dust

    pygame.display.update()
    
pygame.quit()



import pygame
from pygame.locals import *

w = 500
h = 500

pygame.init()

canvas = pygame.display.set_mode((500,500)) # canvas size -> creates screen -> background 
background = pygame.image.load('place_holder.png').convert() # initialise image -> surface2

# constants
position = (0,0)
bottom_line_height = 100 # move based on this height, which is centered

# set up objects
rocks = pygame.image.load('rocks.png').convert_alpha() # rocks on pathways, move same as path
dust = pygame.image.load('cosmic_dust.png').convert_alpha() # cosmic dust on pathways, move same as path
dot = pygame.image.load('dot.png').convert_alpha() # cosmic dust on pathways, move same as path



# resizing to fit
rocks = pygame.transform.smoothscale(rocks,(500, 500))
dust = pygame.transform.smoothscale(dust,(500, 500))
background = pygame.transform.smoothscale(background,(500,500)) # resizing image
dot = pygame.transform.smoothscale(dot,(10,10)) # resizing image


dust_mask = pygame.mask.from_surface(dust)
dot_mask = pygame.mask.from_surface(dot) # create mask for circle



dot_rect = dot.get_rect() # original circle position (rect(0,0,10,10))
rocks_rect = rocks.get_rect() # rocks is same rect as path's recxtangle
dust_rect = dust.get_rect() # dust is same rect as path's recxtangle

# extra for path
#----------------------------------------------------------------------------------
pygame.display.set_caption("Welcome to The Pathways") # name of game for window

exit = False

pygame.event.get()
pygame.display.set_icon(background)


# player 
x = 800 # position x
y = 345 # position y

x_path = -365
y_path = 240

mx,my = pygame.mouse.get_pos()


#----------------------------------------------------------------------------------
canvas.blit(background, dest=position) # render image onto surface, background
canvas.blit(rocks, rocks_rect) # render image onto surface, rocks
canvas.blit(dust, dust_rect) # render image onto surface, dust
canvas.blit(dot, dot_rect) # render image onto surface, original position

hist = ["none","none"] # history of last key pressed

while not exit:
    mx,my = pygame.mouse.get_pos()

    keys = pygame.key.get_pressed()
    w = keys[pygame.K_w]
    a = keys[pygame.K_a]
    s = keys[pygame.K_s]
    d = keys[pygame.K_d]
    shift = keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]

    offset = (x - x_path), (y - y_path)
    over_off = (x_path - mx ), (y_path - my)

    poi_circl = dot_mask.overlap(dust_mask,(over_off))

    clicks = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: # left click
                click_position = event.pos # location mouse -> middle
                clicks = True
            else:
                clicks = False

    if clicks:
        print("click")
        if poi_circl:
            print("Mouse clicked on dust")
            print(poi_circl)


    canvas.blit(background, dest=position) # render image onto surface, background
    canvas.blit(rocks, (x_path,y_path)) # render image onto surface, rocks
    canvas.blit(dust, (x_path,y_path)) # render image onto surface, dust
    canvas.blit(dot, (mx,my)) # render image onto surface, original position

    pygame.display.update()
    
pygame.quit()
"""


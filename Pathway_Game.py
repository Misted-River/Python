import pygame
from pygame.locals import *

w = 1920
h = 1080

timer = pygame.time.Clock()

pygame.init()

canvas = pygame.display.set_mode((1920,1080)) # canvas size -> creates screen -> background 
background = pygame.image.load('place_holder.png').convert() # initialise image -> surface2

# constants
position = (0,0)
bottom_line_height = 100 # move based on this height, which is centered

pygame.mixer.music.load('Walking The Pathways - Version 6.wav') # load music

# set up objects
path = pygame.image.load('pa_place.png').convert_alpha() # patyhway moves -> surface2
player = pygame.image.load('comet_stationary.png').convert_alpha() # player image -> surface2
rocks = pygame.image.load('rocks.png').convert_alpha() # rocks on pathways, move same as path
dust = pygame.image.load('cosmic_dust.png').convert_alpha() # cosmic dust on pathways, move same as path
dot = pygame.image.load('dot.png').convert_alpha() # cosmic dust on pathways, move same as path
scrap = pygame.image.load('city_scrap.png').convert_alpha() # cosmic dust on pathways, move same as path
cracks = pygame.image.load('cracks.png').convert_alpha() # cosmic dust on pathways, move same as path
line = pygame.image.load("line.png").convert_alpha() # line to go to next scene

# labels in scene 1
dust_label = pygame.image.load('dust_label.png').convert_alpha() # cosmic dust on pathways, move same as path
ring_label = pygame.image.load('ring_label.png').convert_alpha() # cosmic dust on pathways, move same as path
scrap_label = pygame.image.load('scrap_label.png').convert_alpha() # cosmic dust on pathways, move same as path

# comet costumes (anim frames for scene 1)
comet_1 = pygame.image.load('1.png').convert_alpha() # cosmic dust on pathways, move same as path
comet_2 = pygame.image.load('2.png').convert_alpha() # cosmic dust on pathways, move same as path
comet_3 = pygame.image.load('3.png').convert_alpha() # cosmic dust on pathways, move same as path
comet_4 = pygame.image.load('4.png').convert_alpha() # cosmic dust on pathways, move same as path
comet_5 = pygame.image.load('5.png').convert_alpha() # cosmic dust on pathways, move same as path


# right / left -> will be flipped
# top/ down will be flipped


# #----------------------------------------------------------------------------------

path_rect = path.get_rect()
width_path = path_rect.width
height_path = path_rect.height

# resizing to fit
path = pygame.transform.smoothscale(path,(width_path*1.7, height_path*1.7)) 

comet_1 = pygame.transform.smoothscale(comet_1,(500/1.5,343/1.5))
comet_2 = pygame.transform.smoothscale(comet_2,(500/1.5,343/1.5))
comet_3 = pygame.transform.smoothscale(comet_3,(500/1.5,343/1.5))
comet_4 = pygame.transform.smoothscale(comet_4,(500/1.5,343/1.5))
comet_5 = pygame.transform.smoothscale(comet_5,(500/1.5,343/1.5))

player = pygame.transform.smoothscale(player,(500/1.5,343/1.5))
rocks = pygame.transform.smoothscale(rocks,(width_path*1.7, height_path*1.7))
dust = pygame.transform.smoothscale(dust,(width_path*1.7, height_path*1.7))
scrap = pygame.transform.smoothscale(scrap,(width_path*1.7, height_path*1.7))
cracks = pygame.transform.smoothscale(cracks,(width_path*1.7, height_path*1.7))
line = pygame.transform.smoothscale(line,(width_path*1.7, height_path*1.7))
background = pygame.transform.smoothscale(background,(1920,1080)) # resizing image
dot = pygame.transform.smoothscale(dot,(15,10)) # resizing image

player.set_colorkey((255,255,255))
dot.set_colorkey((255,255,255))

path_mask = pygame.mask.from_surface(path)
dust_mask = pygame.mask.from_surface(dust)
player_mask = pygame.mask.from_surface(player)
dot_mask = pygame.mask.from_surface(dot) # create mask for circle
line_mask = pygame.mask.from_surface(line)
cracks_mask = pygame.mask.from_surface(cracks)
scrap_mask = pygame.mask.from_surface(scrap)


path_rect = path.get_rect()
player_rect = player.get_rect() #  original player position (rect(0,0,300,180))
dot_rect = dot.get_rect() # original circle position (rect(0,0,10,10))
rocks_rect = path_rect # rocks is same rect as path's recxtangle
dust_rect = path_rect # dust is same rect as path's recxtangle
scrap_rect = path_rect # scraps is same rect as path's recxtangle
cracks_rect = path_rect # cracks is same rect as path's recxtangle
line_rect = path_rect

# extra for path
width_path = path_rect.width
height_path = path_rect.height
#----------------------------------------------------------------------------------
pygame.display.set_caption("Welcome to The Pathways") # name of game for window

exit = False
scene = 1
frame = 0
right = "none"

pygame.event.get()
pygame.display.set_icon(background)

def canv_blit_rest():
    canvas.blit(scrap, (x_path,y_path)) # render image onto surface, scraps
    canvas.blit(cracks, (x_path,y_path)) # render image onto surface, cracks
    canvas.blit(dot, (mx,my)) # render image onto surface, original position
                

def canvas_blit_scene1(move):
    canvas.blit(background, dest=position) # render image onto surface, background
    canvas.blit(path, (x_path,y_path)) # render image onto surface, original position
    canvas.blit(rocks, (x_path,y_path)) # render image onto surface, rocks
    canvas.blit(dust, (x_path,y_path)) # render image onto surface, dust
    canvas.blit(line,(x_path,y_path))

    if move == True and frame == 1:
        player = comet_1
        if right == "yes":
            player = pygame.transform.flip(player, True, False)
            canvas.blit(player, (x,y)) # render image onto surface, original position
            timer.tick(10)
            canv_blit_rest()
        else:
            canvas.blit(player, (x,y)) # render image onto surface, original position
            timer.tick(10)
            canv_blit_rest()
        
    elif move == True and frame == 2:
        player = comet_2
        if right=="yes":
            player = pygame.transform.flip(player, True, False)
            canvas.blit(player, (x,y)) # render image onto surface, original position
            timer.tick(10)
            canv_blit_rest()
        else:
            canvas.blit(player, (x,y)) # render image onto surface, original position
            timer.tick(10)
            canv_blit_rest()
    elif move == True and frame == 3:
        player = comet_3
        if right=="yes":
            player = pygame.transform.flip(player, True, False)
            canvas.blit(player, (x,y)) # render image onto surface, original position
            timer.tick(10)
            canv_blit_rest()
        else:
            canvas.blit(player, (x,y)) # render image onto surface, original position
            timer.tick(10)
            canv_blit_rest()
    elif move == True and frame == 4:
        player = comet_4
        if right=="yes":
            player = pygame.transform.flip(player, True, False)
            canvas.blit(player, (x,y)) # render image onto surface, original position
            timer.tick(10)
            canv_blit_rest()
        else:
            canvas.blit(player, (x,y)) # render image onto surface, original position
            timer.tick(10)
            canv_blit_rest()
    elif move == True and frame == 5:
        player = comet_5
        if right=="yes":
            player = pygame.transform.flip(player, True, False)
            canvas.blit(player, (x,y)) # render image onto surface, original position
            timer.tick(10)
            canv_blit_rest()
        else:
            canvas.blit(player, (x,y)) # render image onto surface, original position
            timer.tick(10)
            canv_blit_rest()
    else:
        player = comet_3
        if hist_right[0] == "yes":
            player = pygame.transform.flip(player, True, False)
            canvas.blit(player, (x,y)) # render image onto surface, original position
            timer.tick(10)
            canv_blit_rest()
        else:
            canvas.blit(player, (x,y)) # render image onto surface, original position
            canv_blit_rest()
            
    
def canvas_blit_start():
    canvas.blit(background, dest=position) # render image onto surface, background
    canvas.blit(path, (x_path,y_path)) # render image onto surface, original position
    canvas.blit(rocks, (x_path,y_path)) # render image onto surface, rocks
    canvas.blit(dust, (x_path,y_path)) # render image onto surface, dust
    canvas.blit(line,(x_path,y_path))
    canvas.blit(player, (x,y)) # render image onto surface, original position
    canvas.blit(scrap, (x_path,y_path)) # render image onto surface, scraps
    canvas.blit(cracks, (x_path,y_path)) # render image onto surface, cracks
    canvas.blit(dot, (mx,my)) # render image onto surface, original position


def canvas_blit_labels(label):
    if label == "dust":
        canvas.blit(dust_label, (mx,my)) # render image onto surface, original position
    elif label == "ring":
        canvas.blit(ring_label, (mx,my)) # render image onto surface, original position
    elif label == "scrap":
        canvas.blit(scrap_label, (mx,my)) # render image onto surface, original position

def anim_walk_lr():
    print("images go here")

def anim_walk_td():
    print("images go here")

def direction_walk(direction):
    if direction == "left":
        print("insert walk anim here-> have picture and blit over each other as player moves")
    elif direction == "right":
        print("insert walk anim here-> have picture and blit over each other as player moves")
    elif direction == "top":
        print("insert walk anim here-> have picture and blit over each other as player moves")
    elif direction == "down":
        print("insert walk anim here-> have picture and blit over each other as player moves")


# player 
x = 800 # position x
y = 345 # position y

x_path = -365
y_path = 240

mx,my = pygame.mouse.get_pos()

width = player.get_width()
height = player.get_height()

#----------------------------------------------------------------------------------
canvas_blit_start()

hist = ["none","none"] # history of last key pressed
clicks = "none"
move = "none"

hist_right = [""]

pygame.mixer.music.play(4) # start music -> for 4 loops it plays and then it stops
pygame.mixer.music.set_volume(0.2)

while not exit:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # left click
            click_position = event.pos # location mouse -> middle
            clicks = True
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1: # left click
            click_position = event.pos # location mouse -> middle
            clicks = False

    if scene == 1:
        frame +=1
        if frame == 6:
            frame = 1

        mx,my = pygame.mouse.get_pos()

        keys = pygame.key.get_pressed()
        w = keys[pygame.K_w]
        a = keys[pygame.K_a]
        s = keys[pygame.K_s]
        d = keys[pygame.K_d]
        shift = keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]

        offset = (x - x_path), (y - y_path)
        over_off = (x_path - mx ), (y_path - my)

        poi = path_mask.overlap(player_mask,(offset)) 
        poi_next = line_mask.overlap(player_mask,(offset)) 

        poi_scraps = dot_mask.overlap(scrap_mask,(over_off))
        poi_cracks = dot_mask.overlap(cracks_mask,(over_off))
        poi_dot = dot_mask.overlap(dust_mask,(over_off))

        # variables for movement speed
        if poi:
            velo = -6
            velo_path = -68
        else:
            velo = 6 # up down direction
            velo_path = 68 # up down direction

        if move == True:
            print("anim walk")
        else:
            print("anim idle")
            move = False


        if not s and not d and not a and not w:
            move = False
            right = "none"


        canvas_blit_scene1(move)
        if clicks == True:  
            if poi_dot:
                canvas_blit_labels("dust")
            elif poi_scraps:
                if move == True:
                    canvas_blit_labels("scrap")   
            elif poi_cracks:
                    canvas_blit_labels("ring")


        if shift:
            velo = 12 # up down direction
            velo_path = 136 # up down direction

        if w and y>0: # key = k_(the key) events 
            move = True
            right = "none"
            hist_right[0] = "no"
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
            move = True
            right = "none"
            hist_right[0] = "no"
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
            move = True
            right = "none"
            hist_right[0] = "no"
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
            move = True
            right = "yes"
            hist_right[0] = "yes"
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
        if poi_next:
            scene = 2
            print(scene)
         
    if scene == 2:
        canvas.blit(background, dest=position) # render image onto surface, background
        pygame.mixer.music.stop

    pygame.display.update()

pygame.quit()



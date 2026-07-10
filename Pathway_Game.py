import pygame

pygame.init()

canvas = pygame.display.set_mode((1920,1080)) # canvas size -> creates screen -> background 
background = pygame.image.load('placeholder_bg.png').convert() # initialise image -> surface2

# constants
position = (0,0)
bottom_line_height = 100 # move based on this height, which is centered

# set up objects
player = pygame.image.load('player_placeholder.jpg').convert_alpha() # player image -> surface2
path = pygame.image.load('pathways_place.png').convert_alpha() # patyhway moves -> surface2
rocks = pygame.image.load('rocks.png').convert_alpha() # rocks on pathways, move same as path

# rectangles
player_rect = player.get_rect() #  original player position (rect(0,0,300,180))
path_rect = path.get_rect()
rocks_rect = path_rect # rocks is same rect as path's recxtangle

width_path = path_rect.width
height_path = path_rect.height

# resizing to fit
path = pygame.transform.smoothscale(path,(width_path*1.7, height_path*1.7)) 
rocks = pygame.transform.smoothscale(rocks,(width_path*1.7, height_path*1.7))
background = pygame.transform.smoothscale(background,(1920,1080)) # resizing image

# masks
pathborder_mask = pygame.mask.from_surface(path)
#path.set_colorkey((0,0,0))
#player.set_colorkey((0,0,0))
#----------------------------------------------------------------------------------
pygame.display.set_caption("Welcome to The Pathways") # name of game for window

exit = False
mouse_pos = pygame.mouse.get_pos()

pygame.event.get()
pygame.display.set_icon(background)

# player 
x = 800 # position x
y = 345 # position y

x_path = -365
y_path = 240

width = player.get_width()
height = player.get_height()

class Object:
    def _init(self):
        self.img = self.img
        self.x,self.y = self.START_POS
        
    def collide(self,mask,x=0,y=0):
        pl_mask = pygame.mask.from_surface(self)
        offset= (self.x-x),int(player.y - y)
        poi = mask.overlap(pl_mask,offset)
        return poi

# variables for movement speed

velo = 3 # up down direction
velo_path = 34 # up down direction
#----------------------------------------------------------------------------------
canvas.blit(background, dest=position) # render image onto surface, background
canvas.blit(player, player_rect) # render image onto surface, original position
canvas.blit(path, path_rect) # render image onto surface, path
canvas.blit(rocks, path_rect) # render image onto surface, rocks

while not exit:
    keys = pygame.key.get_pressed()
    w = keys[pygame.K_w]
    a = keys[pygame.K_a]
    s = keys[pygame.K_s]
    d = keys[pygame.K_d]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

    if player.collide(pathborder_mask) != None:
        print('collide')
    else:
        print('no')
            
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
        if (not a) and ( x<1920-width and x_path>-680):
            x_path -= velo_path
        else:
            velo

    canvas.blit(background, dest=position) # render image onto surface, background
    canvas.blit(path, (x_path,y_path)) # render image onto surface, original position
    canvas.blit(rocks, (x_path,y_path)) # render image onto surface, rocks
    canvas.blit(player, (x,y)) # render image onto surface, original position
    pygame.display.update()

pygame.quit()

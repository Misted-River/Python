import pygame

pygame.init() # initialise pygame module

position = (0,0)
clock = pygame.time.Clock()

bottom_line_height = 100 # move based on this height, which is centered

# set up objects
player = pygame.image.load('player_placeholder.jpg')# player image -> surface2
path = pygame.image.load('costume2.svg')# player image -> surface2

#fontObj = pygame.font.Font(None, 32)
image_size = (1000, 1000)


#textSufaceObj = fontObj.render('', True, 'BLack', None) # antialiasing is true
#textRectObj = textSufaceObj.get_rect()
player_pos = player.get_rect()

path_pos = path.get_rect()
width_path = path.get_rect().width
height_path = path.get_rect().height

path = pygame.transform.smoothscale(path,(width_path*3, height_path*3)) # 200,200 is default image size


clock = pygame.time.Clock()
#----------------------------------------------------------------------------------
canvas = pygame.display.set_mode((1920,1080),pygame.RESIZABLE) # canvas size -> creates screen -> background 
image = pygame.image.load('Untitled2186_20240824160114.png').convert() # initialise image -> surface2


path_pos.midbottom = (canvas.get_width() // 2 +150, canvas.get_height() -450 - bottom_line_height - 15)
player_pos.midbottom = (canvas.get_width() // 2, canvas.get_height() - bottom_line_height - 15)

image = pygame.transform.smoothscale(image,(1920,1080)) # sizing image

pygame.display.set_caption("Welcome to The Pathways") # name of game for window

exit = False
refresh = False
mouse = pygame.mouse.get_pos()

objects = [] # gathering all players etc objects in game

pygame.draw.line(canvas, 'Black', (0, canvas.get_height() - bottom_line_height), (canvas.get_width(), canvas.get_height() - bottom_line_height), 3)

pygame.event.get()
pygame.display.set_icon(image)

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

player_obj = game_object(player,10,3)

canvas.blit(image, dest=position) # render image onto surface, background
 
while not exit:
    canvas.blit(player, player_pos) # render image onto surface
    canvas.blit(path, path_pos) # render image onto surface, path
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w: # key = k_(the key) event
                player_obj.move(up=True)
                print("Move the character up")
            elif event.key == pygame.K_s:
                player_obj.move(down=True)
                print("Move the character down")
            elif event.key == pygame.K_a:
                player_obj.move(left=True)
                print("Move the character left")
            elif event.key == pygame.K_d:
                player_obj.move(right=True)
                print("Move the character right")
            
            
        if event.type == pygame.QUIT:
            exit = True
        canvas.blit(player_obj.image, player_obj.pos)
        pygame.display.update()
        clock.tick(60)
        

pygame.quit()

import pygame

pygame.init() # initialise pygame module

position = (0,0)
clock = pygame.time.Clock()
bottom_line_height = 10

# set up objects
player = pygame.image.load('comet_placeholder.png')# player image -> surface2
fontObj = pygame.font.Font(None, 32)

textSufaceObj = fontObj.render('Welcome', True, 'BLack', None) # antialiasing is true
textRectObj = textSufaceObj.get_rect()
player_pos = player.get_rect()

clock = pygame.time.Clock()
#----------------------------------------------------------------------------------
canvas= pygame.display.set_mode((1920,1080),pygame.RESIZABLE) # canvas size -> creates screen -> background 
image = pygame.image.load('Untitled2186_20240824160114.png').convert() # initialise image -> surface2

player_pos.midbottom = (canvas.get_width() // 2, canvas.get_height() - bottom_line_height - 15)

image= pygame.transform.smoothscale(image,(1920,1080)) # sizing image

pygame.display.set_caption("Welcome to The Pathways") # name

exit = False
run = True
refresh = False
mouse = pygame.mouse.get_pos()

objects = [] # gathering all players etc objects in game

pygame.draw.line(canvas, 'Black', (0, canvas.get_height() - bottom_line_height), (canvas.get_width(), canvas.get_height() - bottom_line_height), 3)

pygame.event.get()
pygame.display.set_icon(image)

# multiple images use python classes

class game_object:
    def __init__(self,image,height,speed):
        self.speed = speed
        self.image = image
        self.pos = image.get_rect().move(0,height)
    def move(self):
        self.pos = self.pos.move(self.speed,0)
        if self.pos.right > 600:
            self.pos.left = 0

while not exit:
    #canvas.blit(image, dest = position) # render image onto surface
    canvas.blit(image, dest=position) # render image onto surface, background
    canvas.blit(player, player_pos) # render image onto surface
    canvas.blit(textSufaceObj, textRectObj)
    pygame.display.update() 
    print (mouse)

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
    

pygame.quit()

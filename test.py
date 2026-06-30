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
"""
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
""" def move(self, up=False, down=False,left=False,right=False):
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
            self.pos.top = canvas.get_height() -player.get_height()"""

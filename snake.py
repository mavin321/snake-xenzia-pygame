import pygame
from pygame.locals import *
import time

pygame.init()#initializing the game
pygame.mixer.init() #initialize background music

#game speed
clock=pygame.time.Clock()
fps=60

#create game window
screen_height=700
screen_width=1000
screen=pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("snake xenzia")

# game variables
slither=False
game_over=False
score=0

#background 
WHITE=(0, 100, 0)
Black=(0, 0, 0)

#create a class for the snake object
class Snake(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load('assets/head_down.png')
        self.rect=self.image.get_rect()
        self.rect.center=[x,y]
        self.vel=2
        self.direction=''

    def update(self):
        if slither==True and game_over==False and 620>self.rect.top>60 and 900>self.rect.left>60:
            #movement
            keys=pygame.key.get_pressed()
            if keys[pygame.K_w] and self.direction!='down':
                self.image=pygame.image.load('assets/head_up.png')
                self.direction='up'
            elif keys[pygame.K_a] and self.direction!='right':             
                self.image=pygame.image.load('assets/head_left.png')
                self.direction='left'
            elif keys[pygame.K_d] and self.direction!='left':
                self.image=pygame.image.load('assets/head_right.png')
                self.direction='right'
            elif keys[pygame.K_s] and self.direction!='up':
                self.image=pygame.image.load('assets/head_down.png')
                self.direction='down'
        if self.direction=='up':
            self.rect.y-=self.vel
            self.rect.x+=0
        elif self.direction=='down':
            self.rect.y+=self.vel
            self.rect.x+=0
        elif self.direction=='right':
            self.rect.y+=0
            self.rect.x+=self.vel
        elif self.direction=='left':
            self.rect.y+=0
            self.rect.x-=self.vel
        



            
#creating groups
snake_group=pygame.sprite.Group()
#create an instance of the object
my_snake=Snake(screen_width//2,screen_height//2)
#adding to group
snake_group.add(my_snake)

#game loop
snake=True # true means its alive and false means its dead
while snake:

    clock.tick(fps)

    #loading the backgrounds
    screen.fill(WHITE)
    #placing the snake on the screen
    snake_group.draw(screen)
    snake_group.update()

    #CHECKING IF THE SNAKE IS WITHIN BOUNDS
    if my_snake.rect.top==60 or my_snake.rect.top==600 or my_snake.rect.left==60 or my_snake.rect.left==900:
        game_over=True
        slither=False
        my_snake.vel=0


    pygame.draw.rect(screen, Black, (50,50,900,600), 10)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            snake=False
        if event.type == pygame.MOUSEBUTTONDOWN and slither==False and game_over==False:
            slither=True
            my_snake.direction='down'
    

    pygame.display.update() #makes images work


pygame.quit()
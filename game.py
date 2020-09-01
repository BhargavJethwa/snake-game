import pygame
import time
import random as rd

pygame.init()

food_point=2
width = 600
height = 400
h1=470
dis = pygame.display.set_mode((width,h1))
pygame.display.set_caption("Snake Game")

def gen_food():
    global foodx,foody,food_point
    dis.fill(black)
    for a in range(width):
        pygame.draw.rect(dis,red,[a,height,snakeblock,snakeblock])
    font = pygame.font.SysFont("comicsansms",35)
    val = font.render("Score = "+str(snake_length-1), True, red)
    dis.blit(val,[snakeblock,height+snakeblock])
    if snake_length%10==1:
        food_point = 5
    else:
        food_point = 1
    foodx = round(rd.randrange(0,width-snakeblock)/snakeblock)*snakeblock
    foody = round(rd.randrange(0,height-snakeblock)/snakeblock)*snakeblock

def snake():
    global foodx,foody,snake_list,food_point
    for x1 in snake_list:
        pygame.draw.rect(dis,orange,[x1[0],x1[1],snakeblock,snakeblock])
    if food_point>1:
        font = pygame.font.SysFont("comicsansms",35)
        val = font.render("Bonus!!!", True, red)
        dis.blit(val,[width*3/7,height+snakeblock])
        pygame.draw.rect(dis,green,[foodx-snakeblock,foody-snakeblock,snakeblock*3,snakeblock*3])
    else:
        pygame.draw.rect(dis,green,[foodx,foody,snakeblock,snakeblock])       

    
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
black = (0,0,0)
orange = (240,50,0)
gameover=False
snakeblock = 10
snake_list = []
snake_length=1
x=width/2
x_change=0
y=height/2
y_change=0
dis.fill(black)
foodx=0
foody=0
clock = pygame.time.Clock()
speed= 10
gameend=False


while not gameover:
    while gameend:
        x_change=0
        y_change=0
        dis.fill(black)
        for a in range(width):
            pygame.draw.rect(dis,red,[a,height,snakeblock,snakeblock])
        score=snake_length-1
        font = pygame.font.SysFont("comicsansms",35)
        val = font.render("Score = "+str(score)+". Press 'r' to retry", True, red)
        dis.blit(val,[width/7,height+snakeblock])
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameend=False
                gameover = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    gen_food()
                    x_change=-snakeblock
                    gameend=False
                    dis.fill(black)
                    x=width/2
                    y=height/2
                    snake_length=1
                    snake_list = []
                    gen_food()
                    for a in range(width):
                         pygame.draw.rect(dis,red,[a,height,snakeblock,snakeblock])
        
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                print("space pressed")
                dis.fill(black)
                gen_food()
                for a in range(width):
                    pygame.draw.rect(dis,red,[a,height,snakeblock,snakeblock])
                x_change=-snakeblock
            if event.key==pygame.K_DOWN and x_change!=0:
                print("down pressed")
                x_change = 0
                y_change = snakeblock
            if event.key == pygame.K_UP and x_change!=0:
                print("up pressed")
                x_change = 0
                y_change = -snakeblock
            if event.key == pygame.K_RIGHT and y_change!=0:
                print("right pressed")
                x_change = snakeblock
                y_change = 0
            if event.key == pygame.K_LEFT and y_change!=0:
                print("left pressed")
                x_change = -snakeblock
                y_change = 0    
    
    
    head=[]
    x=x+x_change
    y=y+y_change
    x%=width
    y=y%height
    head.append(x)
    head.append(y)
    snake_list.append(head)
    if x>=width or x<0 or y>height or y<0:
        gameend=True
    if len(snake_list) > snake_length:
        #print("reduce",len(snake_list))
        pygame.draw.rect(dis,black,[snake_list[0][0],snake_list[0][1],snakeblock,snakeblock])
        del snake_list[0]
    if x_change==0 and y_change==0:
        font = pygame.font.SysFont("comicsansms",35)
        val = font.render("Press 's' to start", True, red)
        dis.blit(val,[width*2/7,height+snakeblock])
        pygame.display.update()
        continue;
    
    snake()
    for x1 in snake_list[0:-1]:
        if x1[0]==x and x1[1]==y:
            print("here")
            gameend=True
            
    if x==foodx and y==foody:
        snake_length+=food_point
        gen_food()
    
    clock.tick(speed)
    pygame.display.update()

pygame.quit()
# Hello From Prabas Gokarna Adhikari
# Thank you for visiting my YouTube
# If you have any inquiry feel free to reach me at: prabasruck@gmail.com
# You can change the speed of the snake altering the 'vel' value, the recommended value of vel is between 0.1 to 1.1
# Enjoy the game and add your own creativity to it



# Controls: Arrow keys or standard ASDW for movement 
#           Press 'ESC' to exit the game at any instant

#################################################################################################################################











import pygame 
from random import randint
   
pygame.init() 

width,height = 1200,700
  
window = pygame.display.set_mode((width, height))  # w * h
color = (255,0,0)
fcolor = (0,255,0)
running = True

xr, yr, size, vel = 50, 50, 20, 1.1
offsetx = offsety = size
xf, yf = 100, 100
scored, gameover = False, False
r,l,u,d = True, False, False, False
pos = []
score, highscore = 0, 0
f = 0.0

font = pygame.font.Font('freesansbold.ttf', 20)

def movement():
    global xr, yr
    if r and xr < width-offsetx:
        xr += vel
    elif l and xr > 0:
        xr -= vel
    elif d and yr < height-offsety:
        yr += vel
    elif u and yr > 0:
        yr -= vel

def check_key():
    global r,l,u,d
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and (not l or score == 0) :
        r = True 
        l = u = d = False
    elif (keys[pygame.K_LEFT] or keys[pygame.K_a]) and (not r or score == 0):
        l = True
        r = u = d = False
    elif (keys[pygame.K_DOWN] or keys[pygame.K_s]) and (not u or score == 0):
        d = True
        l = u = r = False
    elif (keys[pygame.K_UP] or keys[pygame.K_w]) and (not d or score == 0):
        u = True
        l = r = d = False



while(running):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running = False
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False

    if abs(xf-xr) < size and abs(yf-yr) < size:
        scored = True

    if scored:
        while(True):
            xf = randint(size*2, width-size*2)
            yf = randint(size*2, height-size*2)
            if [xf, yf] not in pos:
                break
        scored = False
        score += 1
        if highscore < score:
            highscore = score

    check_key()
    movement()

    window.fill((0, 0, 0)) 
    pygame.draw.rect(window, color, pygame.Rect(xr, yr, size, size)) 
    pos.append([xr, yr])
    
    for i in range(0, score):
        if len(pos) > size*(i+1):
            pygame.draw.rect(window, ( (i*5)%255, (i*2)%255, 255), pygame.Rect(pos[-size*(i+1)][0], pos[-size*(i+1)][1], size, size))
            if (len(pos) > size*score):
                del pos[0]
    pygame.draw.rect(window, fcolor, pygame.Rect(xf, yf, size, size))

    text = font.render(' Score: ' + str(score) +'   Current Highscore:' + str(highscore) + ' ', True, (0, 0, 0), (255, 255, 255))
    textRect = text.get_rect()
    textRect.center = (width - 300, 10)
    window.blit(text, textRect)

    if(size*0.5 > xr or xr > width-size*1.1 or size*0.5 > yr or yr > height-size*1.1 or ([xr, yr] in pos[:-3] and score > 5)):
        gameover = True
    if gameover:
        i = 0
        pos = []
        window.fill((0, 0, 0))
        text = font.render('YOU DIED!!      Final Score:' + str(score) + "  PRESS 'Space' to play again.", True, (0, 0, 0), (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (width/2-100, height/2)
        window.blit(text, textRect)
        xr = yr = 50 
        r = True
        l = u = d = False
        if keys[pygame.K_SPACE]:
            gameover = False
            score = 0
    pygame.display.update()

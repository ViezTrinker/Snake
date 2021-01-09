import pygame
import random
pygame.init()

height=510
width=510

# Set Up Display
win = pygame.display.set_mode( (height, width) )

# Titel
pygame.display.set_caption("Snake")

gameovermusic=pygame.mixer.Sound("gameover.wav")
hitmusic=pygame.mixer.Sound("hitsound.wav")
hitmusic.set_volume(0.15)

music = pygame.mixer.music.load('background.mp3')
pygame.mixer.music.play(-1)

vel=15
var=True
while var:
    xstart=random.randint(0,width)
    xstart=xstart-xstart%vel
    ystart=random.randint(0,height)
    ystart=ystart-ystart%vel
    if xstart<370 or ystart>10:
        var=False

heightsquare=15
widthsquare=15

UP=False
DOWN=False
LEFT=False
RIGHT=False

class square():
    def __init__(self,x,y,height,width,vel):
        self.x=x
        self.y=y
        self.height=height
        self.width=width
        self.vel=vel

class futter():
    def __init__(self, schlange):
        var=True
        self.schlange=schlange
        while var:
            isInSnake=False
            self.x=random.randint(0,width-15)
            self.x=self.x-self.x%vel
            self.y=random.randint(0,height-15)
            self.y=self.y-self.y%vel
            
            for square in self.schlange:
                if self.x==square.x and self.y==square.y:
                    isInSnake=True
            
            if not(self.x>370 and self.y<35) and not(isInSnake):
                var=False
        self.width=heightsquare
        self.height=widthsquare

def bewegung(schlange):

    class square():
        def __init__(self,x,y,height,width,vel):
            self.x=x
            self.y=y
            self.height=height
            self.width=width
            self.vel=vel    

    N=len(schlange)    
    #Futterkollision
    if schlange[0].x==essen.x and schlange[0].y==essen.y:
        kollisionessen()
        hitmusic.play()
        schwanzx=schlange[-1].x
        schwanzy=schlange[-1].y
        schwanz=square(schwanzx,schwanzy,heightsquare,widthsquare,vel)
        schlange.append(schwanz)
    
    
    
    for i in range(N-1,0,-1):
        schlange[i].x=schlange[i-1].x
        schlange[i].y=schlange[i-1].y
    
    if UP:
        schlange[0].y -=vel
    if DOWN:
        schlange[0].y +=vel
    if LEFT:
        schlange[0].x -=vel
    if RIGHT:
        schlange[0].x +=vel
    # Spiegelung, falls nötig
    for square in schlange:
        if square.x>=width:
            square.x=square.x-width
        if square.x<0:
            square.x=square.x+width
        if square.y>=height:
            square.y=square.y-height
        if square.y<0:
            square.y=square.y+height
      
    # Kollision mit sich selbst
    
    N=len(schlange)
    
    for i in range(1, N):
        if schlange[i].x==schlange[0].x and schlange[i].y==schlange[0].y:
            gameover()
    
    return schlange
    

def kollisionessen():
    global essen
    essen=futter(schlange)
    global punkte
    punkte += 1
    
def gameover():
    pygame.mixer.music.stop() 
    gameovermusic.play()
    text = font.render("GAME OVER", 1, (255, 255, 255))
    win.blit(text, (width/2-60, height/2-20))
    pygame.display.update()
    pygame.time.delay(10000)
    global run
    run=False
   
def redrawGameWindow():
    
    win = pygame.display.set_mode( (height, width))
    
    # Zeichne Schlange
    for quadr in schlange:
        pygame.draw.rect(win, (255,0,0), (quadr.x, quadr.y, quadr.height, quadr.width))
        
    # Zeichne Futter
    pygame.draw.rect(win, (0,255,0), (essen.x, essen.y, essen.height, essen.width))
    
    # Punkte
    text = font.render("Punkte: " + str(punkte), 1, (255, 255, 255))
    win.blit(text, (370, 10))
    
    pygame.display.update()

schlange=[square(xstart,ystart,heightsquare,widthsquare,vel)]
essen=futter(schlange)
punkte=0
font = pygame.font.SysFont('comicsans', 30, True)

clock = pygame.time.Clock()

run=True
while run:
    
    clock.tick(10)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and not(DOWN):
        UP=True
        DOWN=False
        LEFT=False
        RIGHT=False
    elif keys[pygame.K_DOWN] and not(UP):
        UP=False
        DOWN=True
        LEFT=False
        RIGHT=False
    elif keys[pygame.K_RIGHT] and not(LEFT):
        UP=False
        DOWN=False
        LEFT=False
        RIGHT=True
    elif keys[pygame.K_LEFT] and not(RIGHT):
        UP=False
        DOWN=False
        LEFT=True
        RIGHT=False
        
    schlange=bewegung(schlange)
    redrawGameWindow()

pygame.quit()
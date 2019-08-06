import pygame
import sys

pygame.init()

win = pygame.display.set_mode((500,500))

pygame.display.set_caption("Power of God")

class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpcount = 10
        self.left = False
        self.right = False
        self.walkcount = 0
    
    def draw(self,win):
        if self.walkcount + 1 >= 27:
            self.walkcount = 0

        if self.left:
            win.blit(walkleft[self.walkcount//3],(self.x,self.y))
            self.walkcount += 1
        
        elif self.right:
            win.blit(walkright[self.walkcount//3],(self.x,self.y))
            self.walkcount += 1
        
        else:
            win.blit(stand,(self.x,self.y))

walkleft = [pygame.image.load('L1.png'),pygame.image.load('L2.png'),pygame.image.load('L3.png'),pygame.image.load('L4.png'),pygame.image.load('L5.png'),pygame.image.load('L6.png'),pygame.image.load('L7.png'),pygame.image.load('L8.png'),pygame.image.load('L9.png')]
walkright = [pygame.image.load('R1.png'), pygame.image.load('R2.png'),pygame.image.load('R3.png'),pygame.image.load('R4.png'),pygame.image.load('R5.png'),pygame.image.load('R6.png'),pygame.image.load('R7.png'),pygame.image.load('R8.png'),pygame.image.load('R9.png')]
background = pygame.image.load('bg.jpg')
stand = pygame.image.load('standing.png')

clock = pygame.time.Clock()

pygame.mixer.init()
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play(-1,0.0)



man = player(300, 419, 64, 64)

def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
        win.fill((255,255,255))
        font1 = pygame.font.Font('freesansbold.ttf', 50)
        font2 = pygame.font.Font('freesansbold.ttf',32)
        text1 = font1.render("Power of God",True,(80,225,100),(255,255,255))
        text2 = font2.render("Press P to Start.",True,(80,225,100),(255,255,255))
        win.blit(text1,(100,155))
        win.blit(text2,(100,220))
        # pygame.display.flip()
        pygame.display.update()
        clock.tick(15)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_p]:
            intro = False
            pygame.mixer.music.stop()


    

def redrawWindow():
    global walkcount
    win.blit(background,(0,0))
    man.draw(win)
    pygame.display.update()

# mainloop


def gameloop():
    run = True
    while run:
        clock.tick(27)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit(0)
        
        keys = pygame.key.get_pressed()

        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and man.x > man.vel:
            man.x -= man.vel
            man.left = True
            man.right = False
        elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and man.x < 500 - man.width - man.vel:
            man.x += man.vel
            man.left = False
            man.right = True
        else:
            man.right = False
            man.left = False
            man.walkcount = 0
        
        if not(man.isJump):
            # if keys[pygame.K_UP] and y > vel:
            #     y -= vel
            # if keys[pygame.K_DOWN] and y < 500 - height - vel:
            #     y += vel
            if keys[pygame.K_UP] or keys[pygame.K_w]:
                man.isJump = True
                man.right = False
                man.left = False
                man.walkcount = 0
                pygame.mixer.music.load("jump1.wav")
                pygame.mixer.music.play(0,0.0)
        else:
            if man.jumpcount >= -10:
                neg = 1
                if man.jumpcount < 0:
                    neg = -1
                man.y -= (man.jumpcount ** 2) * 0.5 * neg
                man.jumpcount -= 1
            else:
                man.isJump = False
                man.jumpcount = 10
        
        redrawWindow()
        
        win.fill((0,0,0))

    # pygame.draw.rect(win,(120,230,40),(x,y,width,height))
    # pygame.display.update()
game_intro()
gameloop()
pygame.quit()

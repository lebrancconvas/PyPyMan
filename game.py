import pygame

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

walkleft = [pygame.image.load('L1.png'),pygame.image.load('L2.png'),pygame.image.load('L3.png'),pygame.image.load('L4.png'),pygame.image.load('L5.png'),pygame.image.load('L6.png'),pygame.image.load('L7.png'),pygame.image.load('L8.png'),pygame.image.load('L9.png')]
walkright = [pygame.image.load('R1.png'), pygame.image.load('R2.png'),pygame.image.load('R3.png'),pygame.image.load('R4.png'),pygame.image.load('R5.png'),pygame.image.load('R6.png'),pygame.image.load('R7.png'),pygame.image.load('R8.png'),pygame.image.load('R9.png')]
background = pygame.image.load('bg.jpg')
stand = pygame.image.load('standing.png')

clock = pygame.time.Clock()

pygame.mixer.init()
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play(-1,0.0)


    

def redrawWindow():
    global walkcount
    win.blit(background,(0,0))
    if man.walkcount + 1 >= 27:
        man.walkcount = 0

    if man.left:
        win.blit(walkleft[man.walkcount//3],(man.x,man.y))
        man.walkcount += 1
    elif man.right:
        win.blit(walkright[man.walkcount//3],(man.x,man.y))
        man.walkcount += 1
    else:
        win.blit(stand,(man.x,man.y))
    pygame.display.update()

# mainloop
run = True
man = player(300,419,64,64)
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
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

pygame.quit()

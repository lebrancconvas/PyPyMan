import pygame

pygame.init()

win = pygame.display.set_mode((500,500))

pygame.display.set_caption("Power of God")

x = 50
y = 419
width = 30
height = 30
vel = 10
isJump = False
jumpcount = 10
walkleft = [pygame.image.load('L1.png'),pygame.image.load('L2.png'),pygame.image.load('L3.png'),pygame.image.load('L4.png'),pygame.image.load('L5.png'),pygame.image.load('L6.png'),pygame.image.load('L7.png'),pygame.image.load('L8.png'),pygame.image.load('L9.png')]
walkright = [pygame.image.load('R1.png'), pygame.image.load('R2.png'),pygame.image.load('R3.png'),pygame.image.load('R4.png'),pygame.image.load('R5.png'),pygame.image.load('R6.png'),pygame.image.load('R7.png'),pygame.image.load('R8.png'),pygame.image.load('R9.png')]
background = pygame.image.load('bg.jpg')
stand = pygame.image.load('standing.png')

clock = pygame.time.Clock()

left = False
right = False
walkcount = 0

run = True

sound = pygame.mixer
sound.init()
music = sound.music
music.load("music.mp3")
music.play(-1,0.0)

# pygame.mixer.init()
# pygame.mixer.music.load("music.mp3")
# pygame.mixer.music.play(-1,0.0)

def redrawWindow():
    global walkcount
    win.blit(background,(0,0))
    if walkcount + 1 >= 27:
        walkcount = 0

    if left:
        win.blit(walkleft[walkcount//3],(x,y))
        walkcount += 1
    elif right:
        win.blit(walkright[walkcount//3],(x,y))
        walkcount += 1
    else:
        win.blit(stand,(x,y))
    pygame.display.update()

# mainloop
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()

    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and x > vel:
        x -= vel
        left = True
        right = False
    elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and x < 500 - width - vel:
        x += vel
        left = False
        right = True
    else:
        right = False
        left = False
        walkcount = 0
    
    if not(isJump):
        # if keys[pygame.K_UP] and y > vel:
        #     y -= vel
        # if keys[pygame.K_DOWN] and y < 500 - height - vel:
        #     y += vel
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            isJump = True
            right = False
            left = False
            walkcount = 0
    else:
        if jumpcount >= -10:
            neg = 1
            if jumpcount < 0:
                neg = -1
            y -= (jumpcount ** 2) * 0.5 * neg
            jumpcount -= 1
        else:
            isJump = False
            jumpcount = 10
    
    redrawWindow()
    
    win.fill((0,0,0))

    # pygame.draw.rect(win,(120,230,40),(x,y,width,height))
    # pygame.display.update()

pygame.quit()

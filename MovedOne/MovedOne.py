import pygame 

width = 1000
height = 600

window = pygame.display.set_mode((width, height)) 
pygame.display.set_caption("Moved One") 

screen = pygame.Surface((width, height))
screen.fill((50, 50, 50))

pygame.font.init()
text = pygame.font.Font(None, 32)
txt = "This is so amazing Word as tiger when eating its prey"
txt = "Just Word"

x = int(width / 2 - (len(txt) * text.get_height() / 4))
y = int(height / 2 - 10)
step = 2

RCol = 0
GCol = 0
BCol = 0

rift = False

done = True 
#pygame.key.set_repeat(50, 50)
while done: 
    #pygame.time.delay(10)
    for e in pygame.event.get(): 
        if e.type == pygame.QUIT: 
            done = False 
        if e.type == pygame.KEYDOWN:
            #if e.key == pygame.K_r:
            #    if RCol < 255: RCol += 1
            #    else: RCol = 0
            #if e.key == pygame.K_g:
            #    if GCol < 255: GCol += 1
            #    else: GCol = 0
            #if e.key == pygame.K_b:
            #    if BCol < 255: BCol += 1
            #    else: BCol = 0
            if e.key == pygame.K_SPACE:
                rift = not(rift)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if x > 0:
            x -= step
        elif rift:
            x = width - (len(txt) * text.get_height() / 2)
    if keys[pygame.K_RIGHT]:
        if x < width - (len(txt) * text.get_height() / 2):
            x += step
        elif rift:
            x = 0
    if keys[pygame.K_UP]:
        if y > 0:
            y -= step
        elif rift:
            y = height - text.get_height()
    if keys[pygame.K_DOWN]:
        if y < height - text.get_height():
            y += step
        elif rift:
            y = 0
    if keys[pygame.K_r]:
        if RCol < 255: RCol += 1
        else: RCol = 0
    if keys[pygame.K_g]:
        if GCol < 255: GCol += 1
        else: GCol = 0
    if keys[pygame.K_b]:
        if BCol < 255: BCol += 1
        else: BCol = 0

    pygame.display.set_caption(f"Moved One: {RCol} {GCol} {BCol}, {rift}") 

    screen.fill((50, 50, 50))
    screen.blit(text.render(txt, 1, (RCol, GCol, BCol)), (x , y))
    window.blit(screen, (0, 0)) 
    pygame.display.flip()
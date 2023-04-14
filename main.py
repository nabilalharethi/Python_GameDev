import pygame
import random
import sys
import pygame.mixer

pygame.init()

fps = 60
fps_clock = pygame.time.Clock()
window_width = 600
window_height = 600



font = pygame.font.Font(None, 30)


bullet_width = 5
bullet_height = 10
bullet_speed = 10



score = 0

window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Asteroid")
pygame.mixer.music.set_volume(0.5)  # sets the volume to 50%


pygame.mixer.music.load("brute_force.mp3")
pygame.mixer.music.play(-1)  # -1 indicates that the music will loop indefinitely


background = pygame.image.load("space.png").convert_alpha()

background = pygame.image.load("space.png").convert_alpha()
background_width, background_hieght = 600,600

background = pygame.transform.scale(background,(background_width,background_hieght))


asteroid_image = pygame.image.load("asteroid.png").convert_alpha()
asteroid_width, asteroid_hieght = 50,50



asteroid_image = pygame.transform.scale(asteroid_image,(asteroid_width,asteroid_hieght))
player = pygame.Rect(window_width/2, window_height/2, 20, 20)

jet_image =  pygame.image.load("jet.png").convert_alpha()
jet_width, jet_hieght = 50,50
jet_image = pygame.transform.scale(jet_image,(jet_width,jet_hieght))



bullets = []

asteroids = []
for i in range(5):
    x = random.randint(0, window_width)
    y = random.randint(0, window_height)
    asteroids.append(pygame.Rect(x, y, 50, 50))

run = True
i=0
while run:
    window.blit(background,(0,0))
    i-=1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bullet = pygame.Rect(player.centerx + 13,player.top,bullet_width,bullet_height)
            bullets.append(bullet)
 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= 5
    if keys[pygame.K_RIGHT]:
        player.x += 5
    if keys[pygame.K_UP]:
        player.y -= 5
    if keys[pygame.K_DOWN]:
        player.y += 5

    player.clamp_ip(pygame.Rect(0, 0, window_width, window_height))
    
    for bullet in bullets:
        bullet.y -=5
        if bullet.y <0:
            bullets.remove(bullet)

    for asteroid in asteroids:
        asteroid.y += 5
        if asteroid.y > window_height:
            asteroid.y = 0
            asteroid.x = random.randint(0, window_width)
            
        for bullet in bullets:
            if asteroid.colliderect(bullet):
                score+=1
                bullets.remove(bullet)
                asteroid.x = random.randint(0,window_width)
                asteroid.y=0
                

        if player.colliderect(asteroid):
            score -= 1
            asteroid.x = random.randint(0, window_width)
            asteroid.y = 0

    
    for asteroid in asteroids:
        #pygame.draw.rect(window, (255, 255, 255), asteroid)
        window.blit(asteroid_image,(asteroid.x,asteroid.y))
    window.blit(jet_image,player)
    #pygame.draw.rect(window, (255, 0, 0), player)
    
    for bullet in bullets:
        pygame.draw.rect(window, (255, 255, 255), bullet)
        

    text = font.render(f"Score: {score}", True, (255, 255, 255))
    window.blit(text, (10, 10))
    pygame.display.update()
    fps_clock.tick(fps)

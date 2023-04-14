import pygame
from datetime import datetime

pygame.init()

pygame.display.set_caption('clock')
screen = pygame.display.set_mode((800, 600))

fps = pygame.time.Clock()

background = pygame.image.load("/Users/willki/Documents/PP2/7lab/images/mickieClock.jpeg")
minHand = pygame.image.load("/Users/willki/Documents/PP2/7lab/images/min.png")
secHand = pygame.image.load("/Users/willki/Documents/PP2/7lab/images/sec.png")

def time(t):
    return 360 - t * 6

def rotate(surface, image, left_pos, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = left_pos).center)

    surface.blit(rotated_image, new_rect)

done = False

while done is not True:
    fps.tick(45)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.blit(background, (0,0))
    t = datetime.now()
    angle_sec = time(t.second)
    angle_min = time(t.minute)
    rotate(screen, secHand, (253, 155), angle_sec)
    rotate(screen, minHand, (253, 150), angle_min)

    pygame.display.flip()

pygame.quit()
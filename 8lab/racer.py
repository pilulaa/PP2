import pygame , sys
import random, time
from pygame.locals import *

pygame.init()

#Colors
BLACK = pygame.Color(0, 0, 0)
RED = pygame.Color(255, 0, 0)

#Set FPS
fps = pygame.time.Clock()
FPS = 60

#Variables
WIDTH = 400
HEIGHT = 600
SPEED = 5
SPEED_COIN = 2
COIN_SCORE = 0

#Setting up fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 25)
game_over = font.render("Game Over", True, BLACK)

#Screen Creation
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer")
background = pygame.image.load("/Users/willki/Documents/PP2/8lab/images_racer/AnimatedStreet.png")

#Classes for objects
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("/Users/willki/Documents/PP2/8lab/images_racer/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, WIDTH - 40), 0)

    def move(self):
        self.rect.move_ip(0, SPEED)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, WIDTH - 40), 0)

    def new(self):
        self.rect.center = (random.randint(40, WIDTH- 40), 0)
        self.rect.move_ip(0, SPEED)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("/Users/willki/Documents/PP2/8lab/images_racer/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.top > 0:
            if pressed_keys[K_UP]:
                self.rect.move_ip(0, -5)
        if self.rect.bottom < HEIGHT:
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0,5)
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("/Users/willki/Documents/PP2/8lab/images_racer/coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(30, WIDTH - 30), 0)

    def move(self):
        self.rect.move_ip(0, SPEED_COIN)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(30, WIDTH - 30), 0)

    def new(self):
        screen.blit(self.image, self.rect)
        self.rect.top = 0
        self.rect.center = (random.randint(30, WIDTH - 30), 0)
        self.rect.move_ip(0, SPEED_COIN)

#Setting up sprites
p1 = Player()
e1 = Enemy() 
c1 = Coin()

#Creating sprite groups
enemies = pygame.sprite.Group()
enemies.add(e1)
all_sprites = pygame.sprite.Group()
all_sprites.add(e1)
all_sprites.add(p1)
coins = pygame.sprite.Group()
coins.add(c1)

#Adding userevent 
inc_speed = pygame.USEREVENT + 1
pygame.time.set_timer(inc_speed, 1000)

#Game Loop
while True:
    #Cycles through all events occurring
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == inc_speed:
            SPEED += 0.2

    #Background, text settings 
    screen.blit(background, (0, 0))
    coin_score_text = font_small.render(str(COIN_SCORE), True, BLACK)
    screen.blit(coin_score_text, (375, 10))

    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()
    for entity in coins:
        screen.blit(entity.image, entity.rect)
        entity.move()

    #Collect coins
    if pygame.sprite.spritecollideany(p1, coins):
        pygame.mixer.Sound("/Users/willki/Documents/PP2/8lab/images_racer/coin_collect.wav").play()
        for entity in coins:
            COIN_SCORE += 1
            entity.kill()
        c2 = Coin()
        coins.add(c2)
        c2.new()

    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(p1, enemies):
        pygame.mixer.Sound("/Users/willki/Documents/PP2/8lab/images_racer/crash.wav").play()
        time.sleep(0.5)

        screen.fill(RED)
        screen.blit(game_over, (30, 250))
        pygame.display.update()
        for entity in enemies:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    fps.tick(FPS)
import pygame
import os

pygame.init()

WIDTH = 500
HEIGHT = 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))

fps = pygame.time.Clock()

music_dir = "./7lab/music/"
music_files = os.listdir(music_dir)
current_music = 0
pygame.mixer.music.load(music_dir + music_files[current_music])

font = pygame.font.SysFont(None, 24)

key_play = pygame.K_SPACE
key_stop = pygame.K_ESCAPE
key_next = pygame.K_RIGHT
key_prev = pygame.K_LEFT

pygame.mixer.music.play()

done = False

while not done:
    fps.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == key_play:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()

            elif event.key == key_stop:
                pygame.mixer.music.stop()
                done = True

            elif event.key == key_next:
                current_music = (current_music + 1) % len(music_files)
                pygame.mixer.music.load(music_dir + music_files[current_music])
                pygame.mixer.music.play()
                
            elif event.key == key_prev:
                current_music = (current_music - 1) % len(music_files)
                pygame.mixer.music.load(music_dir + music_files[current_music])
                pygame.mixer.music.play()

    pygame.display.update()
pygame.quit()
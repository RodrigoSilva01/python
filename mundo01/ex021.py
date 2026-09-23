import time
import pygame

pygame.mixer.init()
pygame.mixer.music.load('sigmamusicart.mp3')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    time.sleep(1)
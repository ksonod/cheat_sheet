import pygame
import time

pygame.mixer.init()# initialization
pygame.mixer.music.load( "440Hz.wav") # load a file

# -1 means loop
pygame.mixer.music.play(-1) # number of playing
time.sleep(2)
pygame.mixer.music.stop() # finish

import pygame
import time
import os

pygame.mixer.init()# initialization
pygame.mixer.music.load( "440Hz.wav") # load a file
# 音楽再生、および再生回数の設定(-1はループ再生)
pygame.mixer.music.play(-1) # number of playing
time.sleep(2)
pygame.mixer.music.stop() # finish

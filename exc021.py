# Faça um programa em python que abra e reproduza um arquivo MP3

import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer_music.load('exc021.mp3')
pygame.mixer_music.play(loops=0, start=0.0)
pygame.event.wait()
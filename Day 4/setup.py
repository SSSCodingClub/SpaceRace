import pygame
import random

pygame.init()
pygame.font.init()
pygame.mixer.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720

DEFAULT_FONT = pygame.font.Font("font.ttf", 100)
TITLE_FONT = pygame.font.Font("font.ttf", 140)
SMALL_FONT = pygame.font.Font("font.ttf", 60)

SOUND_MUSIC = pygame.mixer.Sound("music.mp3")
SOUND_SELECT = pygame.mixer.Sound("select.mp3")
SOUND_EXPLOSION = pygame.mixer.Sound("explosion.mp3")

SOUND_MUSIC.set_volume(0.01)
SOUND_SELECT.set_volume(0.05)
SOUND_EXPLOSION.set_volume(0.05)
#! /bin/env python3

import sys

import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    #  Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
      (ai_settings.screen_width, ai_settings.screen_height))  # 1200, 800 is a tuple that defines dimensions of game window
    pygame.display.set_caption("Alien Invasion")

    # Make a ship
    ship = Ship(ai_settings, screen)

    # ?????????
    bullets = Group()


    # Set the background color:
    bg_color = (230, 230, 230)

    # Start the main loop for the game
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_screen(ai_settings, screen, ship, bullets)

        
run_game()

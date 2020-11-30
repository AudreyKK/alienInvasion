import pygame
from pygame.sprite import Sprite
import random

class Star(Sprite):
    '''A class to manage stars rushing by'''

    def __init__(self, ai_settings, screen):
        '''Create a star object at a 'random' point along the right edge of screen.'''
        super(Star, self).__init__()
        self.screen = screen

        # Create a star rect at (0,0) and then set correct position.
        self.rect = pygame.Rect(0, 0, ai_settings.star_width,
        ai_settings.star_height)
        self.rect.centerx = random.randrange(ai_settings.screen_width)
        self.rect.centery = 0

        # Store the star's position as a decimal value.
        self.y = float(self.rect.y)

        self.color = ai_settings.star_color
        self.speed_factor = ai_settings.star_speed_factor

    def update(self):
        '''Move the star down.'''
        # Update the decimal position of the stars.
        self.y += self.speed_factor
        # Update the rect position
        self.rect.y = self.y

    def draw_star(self):
        '''Draw the star to the screen.'''
        pygame.draw.rect(self.screen, self.color, self.rect)

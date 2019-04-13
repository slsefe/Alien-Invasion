import pygame

class Ship():

    def __init__(self, ai_settings, screen):

        self.screen = screen
        self.ai_settings = ai_settings

        # load ship image
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # set the initial position of ship
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

        # moving flag
        self.moving_right = False
        self.moving_left = False


    def update(self):
        """change position of ship according to moving flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        
        self.rect.centerx = self.center
    

    def blitme(self):
        """display ship in screen"""
        self.screen.blit(self.image, self.rect)
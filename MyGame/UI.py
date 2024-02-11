#Import Modules
from typing import Any
import pygame

#Initiate pygame
pygame.init()

class User_Int(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        ui_top = pygame.image.load("MyGame\\Assets\\UI\\UI_Top.gif").convert_alpha()
        self.ui_panes = [ui_top]
        self.image = self.ui_panes[0]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.mask_rect = self.mask.get_rect()
        self.mask_image = self.mask.to_surface()

    def update(self):
        x = 1

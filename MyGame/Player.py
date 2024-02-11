#Import Module
import pygame
from Global import SCREEN_WIDTH, SCREEN_HEIGHT
import UI
pygame.init()

#Player Class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.images = []

        img = pygame.image.load(
            "MyGame\Assets\Plane\RedPlane.gif").convert_alpha()
        #pygame.transform.scale2x(img, img)
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect(center = (300, 700))
        self.mask = pygame.mask.from_surface(self.image)
        self.mask_rect = self.mask.get_rect(center = (300,700))
        self.mask_image = self.mask.to_surface()
        
        
    
    #Movement
    def movement(self, object):
        keys = pygame.key.get_pressed()
        self.movement_speed = 5
        collided = self.mask.overlap(object.mask, (object.rect.x 
                                                   - self.rect.x, 
                                                   object.rect.y 
                                                   - self.rect.y))
        if collided:
            self.rect.y +=10
            print(object.rect.center)
        else:
            if keys[pygame.K_d] and self.rect.right <= SCREEN_WIDTH: 
                self.rect.x += self.movement_speed
                self.mask_rect.x += self.movement_speed
            if keys[pygame.K_a] and self.rect.left >=0:
                self.rect.x -= self.movement_speed
                self.mask_rect.x -= self.movement_speed
            if keys[pygame.K_w] and self.rect.top >=0:
                self.rect.y -= self.movement_speed
                self.mask_rect.x -= self.movement_speed
            if keys[pygame.K_s] and self.rect.bottom <= SCREEN_HEIGHT:
                self.rect.y += self.movement_speed
                self.mask_rect.x += self.movement_speed



    # def enviro_collision(self, object):
    #     collided = self.mask.overlap(object.mask, (object.rect.x 
    #                                                - self.rect.x, 
    #                                                object.rect.y 
    #                                                - self.rect.y))
    #     if collided:
    #         self.rect.x += 1
    #         self.rect.top += object.rect.top

        

    def update(self, object):
        self.movement(object)
        #self.enviro_collision(object)
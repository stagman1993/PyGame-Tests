#Import Modules
import pygame
import logging
import Player
from UI import User_Int
from Global import SCREEN_WIDTH, SCREEN_HEIGHT

#Initiate Pygame
pygame.init()

#Main Code
def main():
    
    #Sys Variables
    Running = True
    Game_Active = False

    #Setup System 
    Clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #Initialise Ui
    ui = User_Int()
    ui_list = pygame.sprite.Group()
    ui_list.add(ui)
    ui_sprites = []
    #Initialise player
    player = Player.Player()
    player_list = pygame.sprite.Group()
    player_list.add(player)
    
    #Game Loop
    while Running:
        keys = pygame.key.get_pressed()
        
        #Fill Screen
        screen.fill("#7a97cc")

        #Draw UI
        ui_list.update()
        ui_list.draw(screen)

        #Update Player
        player_list.draw(screen)
        player_list.update(object = ui)

        #Debug Masks
        # if keys[pygame.K_t]:
        #     screen.blit(player.mask_image, (player.rect))
        #     print(player_list.spritedict[player].x)
        # if keys[pygame.K_y]:
        #     screen.blit(ui.mask_image, (0,0))
        

        # hits = player.mask.overlap(ui.mask, (ui_list.spritedict[ui].x 
        #                                     - player.rect.x,
        #                                     ui_list.spritedict[ui].y 
        #                                     - player.rect.y))
        # if hits:
        #     player_list.spritedict[player].x += 6
        #     player_list.spritedict[player].y += 6
        #     Collided = True
        #     print(Collided)

        
        #Quit Game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                Running = False
    
        pygame.display.update() #Refresh Screen
        Clock.tick(60) #Set Tickrate

if __name__ == "__main__":
    main()
#Import Modules
from cmath import rect
import pygame
from Player import Player
import Map_Loader
import pytmx
from Camera import *

#Initilize PyGame
pygame.init()
pygame.font.init()

#Main Code
def main():

    #System Variables
    screen_width = 1920
    screen_height = 1080
    running = True
    game_active = False
    clock = pygame.time.Clock()

    #Screen Initialisation
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Test Game!")

    map = Map_Loader.TiledMap("OwnGame\Assets\Test_map2.tmx")
    map_image = map.make_map()
    
    map_rect = map_image.get_rect()

    #Player Initilisation
    player = pygame.sprite.GroupSingle()
    player.add(Player())

    for sprite in player:
        player_rect = sprite.image

    #Camera Setup
    camera = Camera(player_rect)
    follow = Follow(camera, player_rect)
    border = Border(camera, player_rect)
    auto = Auto(camera, player_rect)
    camera.setmethod(follow)

    


    #Game Running Loop
    while running:

         #Game Feature Init
        keys = pygame.key.get_pressed()

        if game_active:      
            screen.fill("#607cb1")
            screen.blit(map_image, (0,0))
            player.draw(screen)
            player.update()
            camera.scroll()
            
            
        else:
            #keys = pygame.key.get_pressed()
            screen.fill("#607cb1")
            if keys[pygame.K_r]:
                game_active = True
                
        #Update Screen
        pygame.display.update()
        clock.tick(60)

        #System Keys
        if keys[pygame.K_p]:
            pygame.display.toggle_fullscreen()     
        if keys[pygame.K_ESCAPE]:
            running = False
            print("Program Exiting") 

        #Quit Game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False



if __name__ == "__main__":
        main()
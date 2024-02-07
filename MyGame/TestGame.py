from tkinter import CENTER
from turtle import window_height, window_width
import pygame
import time
import Movement
from random import randint

pygame.init()
pygame.font.init()

"""System Variables"""
screen_width = 800
screen_height = 400
test_font = pygame.font.FontType("Assets/font/Pixeltype.ttf", 50)

"""Player Variables"""
player_speed = 2
boost_multiplier = 2

"""Start Code"""
window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Test Game")
program_icon = pygame.image.load("Assets\ICON.png")
pygame.display.set_icon(program_icon)

"""System Surface"""
bg_surface = pygame.image.load("Assets\graphics\Sky.png").convert_alpha()
ground_surface = pygame.image.load(
    "Assets\graphics\ground.png").convert_alpha()
ground_rect = ground_surface.get_rect(top = 300)

"""Enemy Details"""
snail_surface = pygame.image.load(
    "Assets\graphics\snail\snail1.png").convert_alpha()
snail_rect = snail_surface.get_rect(bottomleft = (820, 300))
fly_surface = pygame.image.load("Assets\graphics\Fly\Fly1.png").convert_alpha()
fly_rect = fly_surface.get_rect(center = (800, 150))

"""Player Details"""
player_surface = pygame.image.load(
    "Assets\graphics\Player\player_walk_1.png").convert_alpha()
player_rect = player_surface.get_rect(midbottom = (100, 300))

"""Start Screen"""
player_stand = pygame.image.load(
    "Assets\graphics\Player\player_stand.png").convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(
    center= (screen_width/2, screen_height/2))

"""Game Over"""
game_over_surface = test_font.render("Press R to Start", False, 
                                    (64, 64, 64))
game_over_rect = game_over_surface.get_rect(midbottom = 
                                    (screen_width/2, screen_height-25))

"""Game Title"""
game_name_surface = test_font.render("Pixel Jumper", False, 
                                    (64, 64, 64))
game_name_Rect = game_name_surface.get_rect(midtop = (screen_width/2, 25))


def update_score(score, colour):
    score_surface = test_font.render(f"Score: {score}", False, 
                                             (64, 64, 64))
    score_rect = score_surface.get_rect(center = (screen_width/2, 50))
    pygame.draw.rect(window, colour, score_rect)
    pygame.draw.rect(window, colour, score_rect, 50)
    window.blit(score_surface, score_rect)
    

def enemy_movement(enemy_list):
    if enemy_list:
        for enemy_rect in enemy_list:
            enemy_rect.x -= 2

            window.blit(snail_surface, enemy_rect)

        return enemy_list
    else: return []
        

def main():
    
    running = True
    game_active = False
    clock = pygame.time.Clock()
    player_gravity = 0
    score = 0
    enemy_rect_list = []

    #Timer
    obstacle_timer = pygame.USEREVENT + 1
    timer = pygame.time.set_timer(obstacle_timer, 1000)

    while running:
        

        if game_active:
            keys = pygame.key.get_pressed()

            print(timer)

            """Environment"""
            window.blit(bg_surface, (0, 0))
            window.blit(ground_surface, (0, 300))

            """Score"""
            update_score(score, "#c0e8ec")

            """Obstacle Movement"""
            enemy_rect_list = enemy_movement(enemy_rect_list)

            # """Snail"""
            # snail_rect.x -= 5 #Snail Movement
            # if snail_rect.right <= 0: 
            #     snail_rect.left = screen_width
            #     score += 1
            # window.blit(snail_surface, snail_rect)

            """Player"""
            player_gravity += 1
            player_rect.y += player_gravity
            if player_rect.bottom >= ground_rect.top:
                player_rect.bottom = ground_rect.top
            if player_rect.left <=0:
                player_rect.left = 0
            if player_rect.right >= screen_width:
                player_rect.right = screen_width
            window.blit(player_surface, player_rect)
            if player_rect.colliderect(snail_rect):
                game_active = False

            if event.type == obstacle_timer:
                print("Test")
        

            """Mouse Test Code"""
            # pygame.mouse.set_visible(1)
            # mouse_pos = pygame.mouse.get_pos()
            # if player_rect.collidepoint(mouse_pos):
            #      print(pygame.mouse.get_pressed())
            
            if keys[pygame.K_d]:
                player_rect.x += 5
            if keys[pygame.K_a]:
                player_rect.x -= 5 
            if keys[pygame.K_SPACE] and player_rect.bottom >= ground_rect.top:
                player_gravity = -20
            

        else:
            keys = pygame.key.get_pressed()
            window.fill((94, 129, 162))
            if score > 0:
                update_score(score, (94, 129, 162))
            else:
                window.blit(game_name_surface, game_name_Rect)

            window.blit(game_over_surface, game_over_rect)
            window.blit(player_stand, player_stand_rect)
            
            if keys[pygame.K_r]:
                score = 0
                player_rect.midbottom = (100, 300)
                snail_rect.left = screen_width
                game_active = True
            

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        pygame.display.update() #Updates Display
        clock.tick(60)

        """Debug Keys"""
        if keys[pygame.K_p]:
            pygame.display.toggle_fullscreen()     
        if keys[pygame.K_ESCAPE]:
            running = False
            print("Program Exiting")

    pygame.quit()
        
if __name__ == "__main__":
        main()
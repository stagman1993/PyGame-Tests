from turtle import window_height, window_width
import pygame
import time
import Movement

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

def update_score(score, colour):
    score_surface = test_font.render(f"Score: {score}", False, 
                                             (64, 64, 64))
    score_rect = score_surface.get_rect(center = (screen_width/2, 50))
    pygame.draw.rect(window, colour, score_rect)
    pygame.draw.rect(window, colour, score_rect, 50)
    window.blit(score_surface, score_rect)

def main():

    running = True
    game_active = False
    clock = pygame.time.Clock()
    player_gravity = 0
    score = 0

    while running:

        if game_active:
            clock.tick(60)
            keys = pygame.key.get_pressed()
            
            """Environment"""
            window.blit(bg_surface, (0, 0))
            window.blit(ground_surface, (0, 300))

            """Score"""
            update_score(score, "#c0e8ec")

            """Snail"""
            snail_rect.x -= 5 #Snail Movement
            if snail_rect.right <= 0: 
                snail_rect.left = screen_width
                score += 1
        
            window.blit(snail_surface, snail_rect)

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
            update_score(score, (94, 129, 162))
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

        """Debug Keys"""
        if keys[pygame.K_p]:
            pygame.display.toggle_fullscreen()     
        if keys[pygame.K_ESCAPE]:
            running = False
            print("Program Exiting")

    pygame.quit()
        
if __name__ == "__main__":
        main()
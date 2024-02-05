import pygame

def movement(player_pos, player_speed, boost_multiplier):
    boost_speed = 1
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= player_speed * boost_speed
    if keys[pygame.K_s]:
        player_pos.y += player_speed * boost_speed
    if keys[pygame.K_a]:
        player_pos.x -= player_speed * boost_speed
    if keys[pygame.K_d]:
        player_pos.x += player_speed * boost_speed
    if keys[pygame.K_LSHIFT]:
        boost_speed = boost_multiplier
    
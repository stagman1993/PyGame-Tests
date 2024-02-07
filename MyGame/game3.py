from numpy import true_divide
import pygame as pg
import time
import random
pg.font.init()

"""System Variables"""
WIDTH, HEIGHT = 1920, 1080
FPS = 120
BG = pg.transform.scale(pg.image.load("Assets\Background.jpg"), (WIDTH, HEIGHT))
FONT = pg.font.SysFont("Ariel", 30)
FONT2 = pg.font.SysFont("Ariel", 100)

"""Player Variables"""
PLAYER_HEIGHT = 60
PLAYER_WIDTH = 40
PLAYER_VELOCITY = 5
BOOST_FACTOR = 2

"""Projectile Variables"""
PROJECTILE_WIDTH = 25
PROJECTILE_HEIGHT = 25
PROJECTILE_VELOCITY = 10

"""System start Code"""
WIN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Test")

"""Draw Items Code"""
def draw(player, elasped_time, projectiles, sprite_group):
    WIN.fill([255, 255, 255])# Fills Background fixes flicker
    WIN.blit(BG,(0,0))  #Sets Background

    time_text = FONT.render(f"Time: {round(elasped_time)}s", 1, "white") #Defines Time Display
    WIN.blit(time_text, (10, 10)) #Draws Time Display

    for projectile in projectiles:
        pg.draw.rect(WIN, "white", projectile)

    #pg.draw.rect(WIN, "red", player)
    
    sprite_group.draw(WIN)
    pg.display.update()


"""Player Movement Code"""
def player_movement(player):
    BOOST_SPEED = 1

    keys = pg.key.get_pressed()
    if keys[pg.K_LSHIFT]:
        BOOST_SPEED = BOOST_FACTOR
    if keys[pg.K_a] and player.rect.x - PLAYER_VELOCITY >= 0:
        player.rect.x -= PLAYER_VELOCITY * BOOST_SPEED
    if keys[pg.K_d] and player.rect.x + PLAYER_VELOCITY + player.width <= WIDTH:
        player.rect.x += PLAYER_VELOCITY * BOOST_SPEED
    if keys[pg.K_w] and player.rect.y - PLAYER_VELOCITY >= 0:
        player.rect.y -= PLAYER_VELOCITY * BOOST_SPEED
    if keys[pg.K_s] and player.rect.y + PLAYER_VELOCITY + player.height <= HEIGHT:
        player.rect.y += PLAYER_VELOCITY * BOOST_SPEED    

class Player(pg.sprite.Sprite):
    def __init__(self, player_image, pos_x, pos_y):
        super().__init__()
        self.image = pg.image.load(player_image)
        self.rect = self.image.get_rect()
        self.height = self.image.get_height()
        self.width = self.image.get_width()
        self.rect.x = pos_x
        self.rect.y = pos_y

"""Main Code"""
def main():
    run = True

    clock = pg.time.Clock()
    start_time = time.time()
    elapsed_time = 0

    player = Player("Assets\F5S4.png", 200, HEIGHT - 300)
    sprite_group = pg.sprite.Group()
    sprite_group.add(player)

    projectile_add_increment = 2000
    projectile_count = 0

    projectiles = []
    hit = False

    while run:
        projectile_count += clock.tick(FPS)
        elapsed_time = time.time() - start_time

        if projectile_count > projectile_add_increment:
            for _ in range(3):
                projectile_x = random.randint(0, WIDTH - PROJECTILE_WIDTH)  #Gives projectile a random x location
                projectile = pg.Rect(projectile_x, -PROJECTILE_HEIGHT, PROJECTILE_WIDTH, PROJECTILE_HEIGHT) #Creates projectile off screen
                projectiles.append(projectile)

            projectile_add_increment = max(1000, projectile_add_increment - 25)
            projectile_count = 0    
                #projectile_y = random.randint(0, HEIGHT - PROJECTILE_HEIGHT)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                break
        keys = pg.key.get_pressed()
        if keys[pg.K_p]:
            pg.display.toggle_fullscreen()     
        if keys[pg.K_ESCAPE]:
            pg.quit()

        for projectile in projectiles[:]:
            projectile.y += random.randint(0, PROJECTILE_VELOCITY)
            if projectile.y > HEIGHT:
                projectiles.remove(projectile)
            elif projectile.y + PROJECTILE_HEIGHT >= player.rect.y and projectile.colliderect(player):
                projectiles.remove(projectile)
                hit = True
                break

        if hit:
            lost_text = FONT2.render("You Lost!", 1, "white")
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            pg.display.update()
            pg.time.delay(4000)
            break

        player_movement(player)
        draw(player, elapsed_time, projectiles, sprite_group)
    pg.quit()

if __name__ == "__main__":
    main()
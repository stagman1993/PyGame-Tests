import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_walk_1 = pygame.image.load(
            "OwnGame\Assets\Character_Static_Roll_1.png"
            ).convert_alpha()
        player_walk_2 = pygame.image.load(
            "OwnGame\Assets\Character_Static_Roll_2.png"
            ).convert_alpha()
        player_walk_3 = pygame.image.load(
            "OwnGame\Assets\Character_Static_Roll_3.png"
            ).convert_alpha()
        player_walk_4 = pygame.image.load(
            "OwnGame\Assets\Character_Static_Roll_4.png"
            ).convert_alpha()
        player_walk_5 = pygame.image.load(
            "OwnGame\Assets\Character_Static_Roll_5.png"
            ).convert_alpha()
        player_walk_6 = pygame.image.load(
            "OwnGame\Assets\Character_Static_Roll_6.png"
            ).convert_alpha()
        player_walk_7 = pygame.image.load(
            "OwnGame\Assets\Character_Static_Roll_7.png"
            ).convert_alpha()
        player_walk_8 = pygame.image.load(
            "OwnGame\Assets\Character_Static_Roll_8.png"
            ).convert_alpha()
        self.player_walk = [player_walk_1, player_walk_2, player_walk_3,
                            player_walk_4, player_walk_5, player_walk_6,
                            player_walk_7, player_walk_8
                            ]
        self.player_index = 0
        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom = (150, 850))
        self.gravity = 0

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d] and self.rect.right <= 1920:
            self.rect.x += 5
        if keys[pygame.K_a] and self.rect.left >= 0:
            self.rect.x -= 5
        if keys[pygame.K_w]:
            self.rect.y -= 5
        if keys[pygame.K_s]:
            self.rect.y += 5
        if keys[pygame.K_SPACE] and self.rect.bottom >= 850:
            self.gravity -200
            print(self.rect.y)

    # def apply_gravity(self):
    #     self.gravity += 1
    #     self.rect.y += self.gravity
    #     if self.rect.bottom >= 850:
    #         self.rect.bottom = 850

    def animation_state(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d] and self.rect.right <= 1920:
            self.player_index += 0.3
            if self.player_index >= len(self.player_walk): self.player_index =0
            self.image = self.player_walk[int(self.player_index)]
        if keys[pygame.K_a] and self.rect.left >= 0:
            self.player_index -= 0.3
            if self.player_index <= -len(self.player_walk): self.player_index =0
            self.image = self.player_walk[int(self.player_index)]
            
            



    def update(self):
        self.player_input()
        # self.apply_gravity()
        self.animation_state()
            
            
        
import pygame
import pytmx

class TiledMap():
    def __init__(self, filepath):
        tm = pytmx.load_pygame(filepath, pixelalpha=False)
        self.width = tm.width * tm.tilewidth
        self.height = tm.height * tm.tileheight
        self.tmxdata = tm

    def render(self, surface):
        ti_get_gid = self.tmxdata.get_tile_image_by_gid
        for layer in self.tmxdata.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid, in layer:
                    tile = ti_get_gid(gid)
                    if tile:
                        surface.blit(tile, (x * self.tmxdata.tilewidth, 
                                           y * self.tmxdata.tileheight))
    def make_map(self):
        temp_surface = pygame.Surface((self.width, self.height))
        temp_surface.convert_alpha()
        self.render(temp_surface)
        return temp_surface
    
import pyxel

from src.Settings.settings import Settings

class Player:
    def __init__(self, game_map):
        self.map = game_map

        # Position de départ
        self.x = 16
        self.y = 16

        # Vitesse
        self.speed = 1.5

        # Sprite actuel
        self.current_sprite = Settings.sprite_player["down"]

    def is_wall(self, x, y):
        # Coins du joueur
        left = x
        right = x + Settings.PLAYER_SIZE - 1
        top = y
        bottom = y + Settings.PLAYER_SIZE - 1

        points = [
            (left, top),
            (right, top),
            (left, bottom),
            (right, bottom)
        ]

        # Vérifie chaque coin
        for px, py in points:
            tile_x = int(px // Settings.TILE_SIZE)
            tile_y = int(py // Settings.TILE_SIZE)

            tile = self.map.get_tile(tile_x, tile_y)

            if self.map.is_solid(tile):
                return True

        return False

    def move(self, dx, dy):
        # Déplacement horizontal
        new_x = self.x + dx

        if not self.is_wall(new_x, self.y):
            self.x = new_x

        # Déplacement vertical
        new_y = self.y + dy

        if not self.is_wall(self.x, new_y):
            self.y = new_y

    def update(self):

        # Déplacement vers le bas
        if pyxel.btn(pyxel.KEY_S):
            self.move(0, self.speed)
            self.current_sprite = Settings.sprite_player["down"]

        # Déplacement vers le haut
        if pyxel.btn(pyxel.KEY_Z):
            self.move(0, -self.speed)
            self.current_sprite = Settings.sprite_player["up"]

        # Déplacement vers la gauche
        if pyxel.btn(pyxel.KEY_Q):
            self.move(-self.speed, 0)
            self.current_sprite = Settings.sprite_player["left"]

        # Déplacement vers la droite
        if pyxel.btn(pyxel.KEY_D):
            self.move(self.speed, 0)
            self.current_sprite = Settings.sprite_player["right"]

    def draw(self):
        sprite_x, sprite_y = self.current_sprite

        pyxel.blt(
            int(self.x),
            int(self.y),
            Settings.PLAYER_IMAGE_BANK,
            sprite_x,
            sprite_y,
            Settings.PLAYER_SIZE,
            Settings.PLAYER_SIZE,
            Settings.PLAYER_TRANSPARENT_COLOR
        )
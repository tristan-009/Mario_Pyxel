import pyxel

from src.Settings.settings import Settings
from src.Game.map import Map
from src.Game.player import Player

class Main:

    def __init__(self):
        pyxel.init(Settings.width, Settings.height, title=Settings.title, fps=Settings.fps)
        pyxel.load("U3a.pyxres")

        self.state = "menu"

        self.map = Map()
        self.player = Player(self.map)

        pyxel.run(self.update, self.draw)

    def update(self):
        if self.state == "menu":
            self.update_menu()

        elif self.state == "game":
            self.update_game()

    def update_menu(self):
        if pyxel.btnp(pyxel.KEY_O):
            self.state = "game"

    def update_game(self):
        self.player.update()

    def draw(self):
        if self.state == "menu":
            self.draw_menu()

        elif self.state == "game":
            self.draw_game()

    def draw_menu(self):
        pyxel.cls(3)

        pyxel.text(
            Settings.width // 2 - 45,
            Settings.height // 2,
            "O pour jouer",
            7
        )

    def draw_game(self):
        pyxel.cls(0)

        self.map.draw()
        self.player.draw()

if __name__ == "__main__":
    Main()

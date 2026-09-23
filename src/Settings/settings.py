class Settings:

    # Fenêtre
    width = 528
    height = 240
    fps = 60
    title = "Mario 67"

    # Map
    TILE_SIZE = 8

    # Joueur
    PLAYER_SIZE = 16
    PLAYER_IMAGE_BANK = 0
    PLAYER_TRANSPARENT_COLOR = 1

    sprite_player = {
        "right": (48, 112),
        "left": (0, 112),
        "up": (32, 112),
        "down": (16, 112),
    }

    # Blocs
    bloc = {
        "normal": (48, 64)
    }

    # Éléments de décor
    scale = {
        "up": (80, 32),
        "down": (95, 63)
    }
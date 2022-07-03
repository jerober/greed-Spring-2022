import random
from game.casting.actor import Actor
from game.shared.color import Color
from game.shared.point import Point

class Artifact(Actor):
    """
    An item of cultural or historical interest. 
    
    The responsibility of an Artifact is to provide a message about itself.

    Attributes:
        _message (string): A short description about the artifact.
    """
    def __init__(self, COLS, ROWS, CELL_SIZE, FONT_SIZE):
        super().__init__()
        gem_or_rock = [79, 42]
        text = chr(random.choice(gem_or_rock))

        x = random.randint(1, COLS - 1)
        y = random.randint(1, ROWS - 1)
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        
        self.set_text(text)
        self.set_font_size(FONT_SIZE)
        self.set_color(color)
        self.set_position(position)
        self.set_velocity(Point(0,5))




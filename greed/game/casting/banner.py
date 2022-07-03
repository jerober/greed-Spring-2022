from game.casting.actor import Actor

class Banner(Actor):
    """
    An item of cultural or historical interest. 
    
    The responsibility of an Artifact is to provide a message about itself.

    Attributes:
        _message (string): A short description about the artifact.
    """
    def __init__(self):
        super().__init__()
        self._score = 0

    def update_score(self, score_change):
        self._score += score_change
        self._text = "Score: " + str(self._score)
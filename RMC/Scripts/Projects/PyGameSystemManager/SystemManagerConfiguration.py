"""---------------------------------------------------------------------------------------
    CONTRIBUTORS
        NAME - EMAIL
---------------------------------------------------------------------------------------"""

# Imports --------------------------------------------------------------------------------
from pygame.rect import Rect

# Namespace ------------------------------------------------------------------------------

# Class ----------------------------------------------------------------------------------

class SystemManagerConfiguration (object):

    # Fields -----------------------------------------------------------------------------
    frameRate = 60
    screenRect = Rect(0, 0, 800, 600)
    gameTitle = "Game Title"
    projectPath = None

    # Initialization ---------------------------------------------------------------------
    def __init__(self):
        pass

    # Methods ----------------------------------------------------------------------------

    # Event Handlers ---------------------------------------------------------------------



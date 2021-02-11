"""---------------------------------------------------------------------------------------
    CONTRIBUTORS
        NAME - EMAIL
---------------------------------------------------------------------------------------"""

# Imports --------------------------------------------------------------------------------
import pygame
from pygame.color import Color
from pygame.rect import Rect

from RMC.Scripts.Projects.PyGameSystemManager.Entities.Entity import Entity

# Namespace ------------------------------------------------------------------------------

# Class ----------------------------------------------------------------------------------

class RectEntity (Entity):

    # Fields -----------------------------------------------------------------------------
    color = None


    # Initialization ---------------------------------------------------------------------
    def __init__(self, x, y, width, height, color=Color(255, 255, 255, 255)):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        pass

    # Methods ----------------------------------------------------------------------------
    def Blit (self, screen):
        pygame.draw.rect(screen,
                          self.color,
                          pygame.Rect(self.x, self.y, self.width, self.height))
        pass

    def __Refresh(self):
        pass
    # Event Handlers ---------------------------------------------------------------------




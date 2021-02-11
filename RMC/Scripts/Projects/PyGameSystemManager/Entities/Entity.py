"""---------------------------------------------------------------------------------------
    CONTRIBUTORS
        NAME - EMAIL
---------------------------------------------------------------------------------------"""

# Imports --------------------------------------------------------------------------------

# Namespace ------------------------------------------------------------------------------

# Class ----------------------------------------------------------------------------------
from pygame.rect import Rect


class Entity (object):

    # Fields -----------------------------------------------------------------------------
    x = 0
    y = 0
    __width = None
    __height = None
    blittable = None

    # Properties -------------------------------------------------------------------------
    def GetBoundsRect(self):
        return Rect(self.x, self.y, self.GetWidth(), self.GetHeight())
        pass

    def SetWidth(self, width):
        self.__width = width

    def GetWidth(self):
        return self.__width

    def SetHeight(self, height):
        self.__height = height
        pass

    def GetHeight(self):
        return self.__height

    # Initialization ---------------------------------------------------------------------
    def __init__(self, blittable=None):
        if type(self) == Entity:
            raise Exception("<Entity> class must be subclassed before use.")

        if blittable is not None:
            self.SetBlittable(blittable)
        pass

    # Methods ----------------------------------------------------------------------------
    def SetBlittable(self, blittable):
        self.blittable = blittable
        self.SetWidth(self.blittable.get_width())
        self.SetHeight(self.blittable.get_height())
        pass

    def Blit(self):
        if type(self) == Entity:
            raise Exception("Blit() method must overridden before use.")
        pass

    def SetPosition(self, x, y):
        self.x = x
        self.y = y
        pass

    # Event Handlers ---------------------------------------------------------------------



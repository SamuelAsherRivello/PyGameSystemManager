"""---------------------------------------------------------------------------------------
    CONTRIBUTORS
        NAME - EMAIL
---------------------------------------------------------------------------------------"""

# Imports --------------------------------------------------------------------------------
import pygame

# Namespace ------------------------------------------------------------------------------
_asset__library_images = {}
_asset__library_sounds = {}

# Class ----------------------------------------------------------------------------------

# Keep previously loaded assets in arrays
# A recommended best practice from https://nerdparadise.com/programming/pygame/part2
class AssetLibrary (object):

    # Fields -----------------------------------------------------------------------------

    # Initialization ---------------------------------------------------------------------
    def __init__(self):
        pass

    # Methods ---------------------------)-------------------------------------------------
    @staticmethod
    def LoadImage (fullPath):

        global _asset__library_images

        image = _asset__library_images.get(fullPath)

        if image is None:
            image = pygame.image.load(fullPath)
            _asset__library_images[fullPath] = image

        return image
        pass

    @staticmethod
    def LoadSound (fullPath):

        global _asset__library_sounds

        sound = _asset__library_sounds.get(fullPath)

        if sound is None:
            sound = pygame.mixer.Sound(fullPath)
            _asset__library_sounds[fullPath] = sound

        return sound
        pass

    # Event Handlers ---------------------------------------------------------------------





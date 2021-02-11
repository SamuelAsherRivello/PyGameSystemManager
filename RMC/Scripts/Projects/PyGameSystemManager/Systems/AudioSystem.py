"""---------------------------------------------------------------------------------------
    CONTRIBUTORS
        NAME - EMAIL
---------------------------------------------------------------------------------------"""

# Imports --------------------------------------------------------------------------------
import os

from RMC.Scripts.Projects.Core.AssetLibrary import AssetLibrary
from RMC.Scripts.Projects.EventDispatcher.EventDispatcher import EventDispatcher
from RMC.Scripts.Projects.PyGameSystemManager.Systems.System import System

# Namespace ------------------------------------------------------------------------------

# Class ----------------------------------------------------------------------------------

class AudioSystem (System):

    # Fields -----------------------------------------------------------------------------
    inputPressed = None
    OnInput = EventDispatcher()

    # Initialization ---------------------------------------------------------------------
    def __init__(self):
        pass

    # Methods ----------------------------------------------------------------------------
    def OnAdded(self, systemManager):
        super(AudioSystem, self).OnAdded(systemManager)
        pass

    def OnInitialize(self):
        pass

    def OnStart(self):
        pass

    def OnUpdate(self, deltaTime):
        pass

    def OnRemoved(self):
        pass

    def PlaySound(self, relativePath):

        fullPath = os.path.join(self.systemManager.configuration.projectPath, relativePath)
        effect = AssetLibrary.LoadSound(fullPath)
        effect.play()
        pass

    # Event Handlers ---------------------------------------------------------------------



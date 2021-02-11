"""---------------------------------------------------------------------------------------
    CONTRIBUTORS
        NAME - EMAIL
---------------------------------------------------------------------------------------"""

# Imports --------------------------------------------------------------------------------
from RMC.Scripts.Projects.EventDispatcher.EventDispatcher import EventDispatcher
from RMC.Scripts.Projects.PyGameSystemManager.Systems.System import System

# Namespace ------------------------------------------------------------------------------

# Class ----------------------------------------------------------------------------------

class InputSystem (System):

    # Fields -----------------------------------------------------------------------------
    inputPressed = None
    OnInput = EventDispatcher()

    # Initialization ---------------------------------------------------------------------
    def __init__(self):
        pass

    # Methods ----------------------------------------------------------------------------
    def OnAdded(self, systemManager):
        super(InputSystem, self).OnAdded(systemManager)
        pass

    def OnInitialize(self):
        pass

    def OnStart(self):
        pass

    def OnUpdate(self, deltaTime):
        for event in self.systemManager.inputEvents:
            self.OnInput.DispatchEvent(event)
        pass

    def OnRemoved(self):
        pass

    # Event Handlers ---------------------------------------------------------------------



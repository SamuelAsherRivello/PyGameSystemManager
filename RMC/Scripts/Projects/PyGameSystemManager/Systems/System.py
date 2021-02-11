"""---------------------------------------------------------------------------------------
    CONTRIBUTORS
        NAME - EMAIL
---------------------------------------------------------------------------------------"""

# Imports --------------------------------------------------------------------------------

# Namespace ------------------------------------------------------------------------------

# Class ----------------------------------------------------------------------------------
class System (object):

    # Fields -----------------------------------------------------------------------------
    systemManager = None
    PG = None

    # Initialization ---------------------------------------------------------------------
    def __init__(self):
        if type(self) == System:
            raise Exception("<System> class must be subclassed before use.")
        pass

    # Methods ----------------------------------------------------------------------------
    def OnAdded (self, systemManager):
        self.systemManager = systemManager
        self.PG = self.systemManager.PG
        pass

    def OnInitialize(self):
        pass

    def OnStart(self):
        pass

    def OnUpdate(self, deltaTime):
        pass

    def OnRemoved(self):
        pass
    # Event Handlers ---------------------------------------------------------------------



"""---------------------------------------------------------------------------------------
    CONTRIBUTORS
        NAME - EMAIL
---------------------------------------------------------------------------------------"""

# Imports --------------------------------------------------------------------------------

# Namespace ------------------------------------------------------------------------------

# Class ----------------------------------------------------------------------------------
class EventDispatcher (object):

    # Fields -----------------------------------------------------------------------------
    __handlers = None

    # Initialization ---------------------------------------------------------------------
    def __init__(self):
        self.__handlers = []

    # Methods ----------------------------------------------------------------------------
    def __iadd__(self, handler):
        self.__handlers.append(handler)
        return self

    def __isub__(self, handler):
        self.__handlers.remove(handler)
        return self

    def DispatchEvent(self, *args, **keywargs):
        for handler in self.__handlers:
            handler(*args, **keywargs)

    def RemoveAllEventListeners(self, inObject):
        for theHandler in self.__handlers:
            if theHandler.im_self == inObject:
                self -= theHandler

    # Event Handlers ---------------------------------------------------------------------



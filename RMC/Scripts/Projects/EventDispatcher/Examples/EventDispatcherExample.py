from RMC.Scripts.Projects.EventDispatcher.EventDispatcher import EventDispatcher

class MyBroadcaster():
    def __init__(self):
        self.OnChange = EventDispatcher()

def OnChangeHandler (*argv):
    for arg in argv:
        print(arg)
    pass

theBroadcaster = MyBroadcaster()

# add a listener to the event
theBroadcaster.OnChange += OnChangeHandler
theBroadcaster.OnChange.DispatchEvent("what01", 10)

# remove listener from the event
theBroadcaster.OnChange -= OnChangeHandler
theBroadcaster.OnChange.DispatchEvent("what02", 10)


"""---------------------------------------------------------------------------------------
    CONTRIBUTORS
        NAME - EMAIL
---------------------------------------------------------------------------------------"""

# Imports --------------------------------------------------------------------------------
from RMC.Scripts.Projects.PyGameSystemManager.Entities.AnimatedImageEntity import AnimatedImageEntity

# Namespace ------------------------------------------------------------------------------

# Class ----------------------------------------------------------------------------------


class CustomCharacterEntity (AnimatedImageEntity):

    # Fields -----------------------------------------------------------------------------
    __velocity = [0, 0]
    __velocityMin = [-10, -30]
    __velocityMax = [10, 30]

    speed = [5, 5]

    isOnGround = False
    __gravity = [0, 1]
    __friction = [20, 0]

    # Properties -------------------------------------------------------------------------
    def SetVelocity(self, velocity):
        self.__velocity[0] = velocity[0]
        self.__velocity[1] = velocity[1]
        pass

    def GetVelocity(self):
        return self.__velocity;
        pass

    def SetVelocityBy(self, deltaV):
        self.__velocity[0] = self.__velocity[0] + deltaV[0]
        self.__velocity[1] = self.__velocity[1] + deltaV[1]
        pass

    # Initialization ---------------------------------------------------------------------
    def __init__(self):
        x = 0
        y = 0
        width = 50
        height = 52
        relativePath = "RMC/Images/Hero.png"
        super(CustomCharacterEntity, self).__init__(x, y, width, height, relativePath, 0, 4)
        pass

    # Methods ----------------------------------------------------------------------------
    def OnUpdate(self, deltaTime):

        # Handle X  Friction
        velocityXNew = float(self.GetVelocity()[0])

        if velocityXNew > 0.5 or velocityXNew < -0.5:
            if self.isOnGround is False:
                velocityXNew *= 0.7
            else:
                velocityXNew *= 0.9
        else:
            velocityXNew=0

        # Sometimes handle falling
        if self.isOnGround is False:
            self.SetVelocityBy(self.__gravity)
        else:

            # Animate only when 'walking'
            if velocityXNew != 0:
                super(CustomCharacterEntity, self).OnUpdate(deltaTime)

            # When grounded, keep the X, and set Y to 0
            self.SetVelocity((0, 0))

        self.SetVelocity((velocityXNew, self.__velocity[1]))

        self.__velocity[0] = self.Clamp(self.__velocity[0], self.__velocityMin[0], self.__velocityMax[0])
        self.__velocity[1] = self.Clamp(self.__velocity[1], self.__velocityMin[1], self.__velocityMax[1])

        self.x = self.x + self.__velocity[0]
        self.y = self.y + self.__velocity[1]
        pass

    # Event Handlers ---------------------------------------------------------------------
    def Clamp(self, value, minValue, maxValue):
        return max(min(value, maxValue), minValue)
        pass

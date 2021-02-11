"""---------------------------------------------------------------------------------------
    CONTRIBUTORS
        NAME - EMAIL
---------------------------------------------------------------------------------------"""

# Imports --------------------------------------------------------------------------------
import random

from RMC.Scripts.Projects.EventDispatcher.EventDispatcher import EventDispatcher
from RMC.Scripts.Projects.PyGameSystemManager.Examples.CustomCharacterEntity import CustomCharacterEntity
from RMC.Scripts.Projects.PyGameSystemManager.Systems.AudioSystem import AudioSystem
from RMC.Scripts.Projects.PyGameSystemManager.Systems.InputSystem import InputSystem
from RMC.Scripts.Projects.PyGameSystemManager.Systems.RenderSystem import RenderSystem
from RMC.Scripts.Projects.PyGameSystemManager.Systems.System import System

# Namespace ------------------------------------------------------------------------------

# Class ----------------------------------------------------------------------------------

class CustomGameSystem (System):

    # Fields -----------------------------------------------------------------------------
    inputSystem = None
    renderSystem = None
    audioSystem = None
    guiSystem = None

    scoreTextEntity = None
    restartTextEntity = None

    isInputPressedUp = False
    isInputPressedLeft = False
    isInputPressedRight = False

    coins = []
    floor = []
    customCharacter = None
    characterHeightFromBottom = 500
    floorHeightFromBottom = 32
    coinsHeightFromBottom = 300
    characterYFloor = None
    background = None

    score = 0
    isPlaying = False

    OnScoreChanged = EventDispatcher()
    OnGameStarted = EventDispatcher()
    OnGameCompleted = EventDispatcher()

    # Properties -------------------------------------------------------------------------
    def SetScore(self, value):
        self.score = value
        self.OnScoreChanged.DispatchEvent(self.score)
        pass

    def GetScore(self):
        return self.score

    # Initialization ---------------------------------------------------------------------
    def __init__(self):
        pass

    # Methods ----------------------------------------------------------------------------
    def OnAdded(self, systemManager):
        super(CustomGameSystem, self).OnAdded(systemManager)
        pass

    def OnInitialize(self):

        # Input
        self.inputSystem = self.systemManager.GetSystem(InputSystem)
        self.inputSystem.OnInput += self.InputSystem_OnInput

        # Render
        self.renderSystem = self.systemManager.GetSystem(RenderSystem)

        # Audio
        self.audioSystem = self.systemManager.GetSystem(AudioSystem)

        pass

    def OnStart(self):
        self.StartGame()
        pass

    def OnUpdate(self, deltaTime):

        # Gravity
        self.DoCharacterFloorDetection()

        if self.isPlaying is False:
            return

        deltaVelocityX = 0
        deltaVelocityY = 0
        deltaPositionY = 0

        # Use Keys
        if self.isInputPressedLeft is True:
            deltaVelocityX = -1
        if self.isInputPressedRight is True:
            deltaVelocityX = 1

        if self.isInputPressedUp is True:
            # Only allow jumps from ground
            if self.customCharacter.isOnGround:

                deltaPositionY = -1
                deltaVelocityY = self.customCharacter.speed[1]
                self.customCharacter.isOnGround = False

                # Play Sound
                self.audioSystem.PlaySound("RMC/Audio/CharacterJump.wav")


        # Handle Wall Collision
        left = 0
        right = self.systemManager.configuration.screenRect[2]

        wallBumpX = 0;
        if self.customCharacter.x < left:
            deltaVelocityX = 0
            self.customCharacter.x = left
            wallBumpX = 5
        elif self.customCharacter.x + self.customCharacter.GetWidth() > right:
            deltaVelocityX = 0
            self.customCharacter.x = right - self.customCharacter.GetWidth()
            wallBumpX = -5

        if wallBumpX != 0:
            # Play Sound
            self.audioSystem.PlaySound("RMC/Audio/CharacterHitGround.wav")
            self.customCharacter.SetVelocity((0, self.customCharacter.GetVelocity()[1]))

        # Move
        self.customCharacter.SetVelocityBy((deltaVelocityX * self.customCharacter.speed[0],
                                            -deltaVelocityY * self.customCharacter.speed[1]))

        self.MoveCharacterBy(wallBumpX, deltaPositionY)

        # Coins
        for coin in self.coins[:]:
            if coin.GetBoundsRect().colliderect(self.customCharacter.GetBoundsRect()):
                # Reward points
                self.SetScore(self.GetScore() + 10)

                # Play Sound
                self.audioSystem.PlaySound("RMC/Audio/CoinCollected.wav")

                # Remove coin from rendering list
                self.renderSystem.DestroyEntity(coin)

                # Remove coin from my list
                self.coins.remove(coin)

        if self.coins.__len__() == 0:
            self.CompleteGame()

        pass

    def OnRemoved(self):
        pass

    def StartGame(self):

        self.renderSystem.DestroyAllEntities()

        # Background
        self.background = self.renderSystem.CreateImage(0, 0, 600, 400, "RMC/Images/Background.png")
        self.background.SetPosition(0, 0)

        # Main Character
        self.customCharacter = self.renderSystem.AddEntity(CustomCharacterEntity())
        self.customCharacter.SetPosition(100, self.systemManager.configuration.screenRect[2] - self.characterHeightFromBottom)

        # Gold Coins
        self.coins = []
        for row in range(2):
            for column in range(5):
                coin = self.renderSystem.CreateAnimatedImage(0, 0, 32, 32, "RMC/Images/Coin.png", 0, 7)
                coin.SetPosition(150 + column * 75,
                                 self.systemManager.configuration.screenRect[3] - self.coinsHeightFromBottom + row * 100)
                self.coins.append(coin)

        # Floor
        floorY = self.systemManager.configuration.screenRect[3] - self.floorHeightFromBottom
        self.characterYFloor = floorY + 10
        blocksToCreate = 1 + int(self.systemManager.configuration.screenRect[2] / 32)
        for i in range(blocksToCreate):
            floor = self.renderSystem.CreateImage(0, 0, 32, 32, "RMC/Images/Block.png")
            floor.SetPosition(i * 32, floorY)

        grassToCreate = 3
        grassX = 0
        for i in range(grassToCreate):
            grass = self.renderSystem.CreateImage(0, 0, 32, 32, "RMC/Images/Grass.png")
            grassX = grassX + random.randint(100, 250)
            grass.SetPosition(grassX, floorY - 30)

        self.isPlaying = True
        self.OnGameStarted.DispatchEvent(None)
        pass

    def CompleteGame(self):

        self.audioSystem.PlaySound("RMC/Audio/GameCompleted.wav")
        self.OnGameCompleted.DispatchEvent(None)
        self.isPlaying = False
        pass

    def RestartGame(self):
        self.audioSystem.PlaySound("RMC/Audio/GameRestarted.wav")
        self.StartGame()
        pass

    # Event Handlers ---------------------------------------------------------------------
    def InputSystem_OnInput(self, event):

        if self.isPlaying == False:
            return

        # Key DOWN
        if event.type == self.systemManager.PG.KEYDOWN:
            if event.key == self.systemManager.PG.K_UP:
                self.isInputPressedUp = True

            if event.key == self.systemManager.PG.K_RIGHT:
                self.isInputPressedRight = True
            elif event.key == self.systemManager.PG.K_LEFT:
                self.isInputPressedLeft = True

        # Key UP
        if event.type == self.systemManager.PG.KEYUP:
            if event.key == self.systemManager.PG.K_UP:
                self.isInputPressedUp = False

            if event.key == self.systemManager.PG.K_RIGHT:
                self.isInputPressedRight = False
            elif event.key == self.systemManager.PG.K_LEFT:
                self.isInputPressedLeft = False


    def DoCharacterFloorDetection(self):

        if self.customCharacter.y > self.characterYFloor - self.customCharacter.GetHeight():

            if self.customCharacter.isOnGround == False:
                self.customCharacter.y = self.characterYFloor - self.customCharacter.GetHeight()
                self.customCharacter.isOnGround = True
            self.audioSystem.PlaySound("RMC/Audio/CharacterHitGround.wav")
        pass


    def MoveCharacterBy(self, deltaX, deltaY):

        if deltaX == 0 and deltaY == 0:
            return;

        # Move
        self.customCharacter.x += deltaX
        self.customCharacter.y += deltaY
        pass

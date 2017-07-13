import sys
from afiBotBrain import *
from afiBotManager import *
from afiBotPlayer import *
from idPlayer import *
from idActor import *
from idEntity import *
from idVec3 import *
class test(afiBotBrain):
 def Think(self , deltaTimeMS):
  botInput = aiInput_t()
  botInput.moveFlag = aiMoveFlag_t.NULLMOVE
  if afiBotManager.GetFlagStatus(self.enemyTeam) == flagStatus_t.FLAGSTATUS_INBASE:
    self.enemyFlag = afiBotManager.GetFlag(self.enemyTeam)
    self.body.MoveToPosition(self.enemyFlag.GetPosition(), 8)
  return botInput
 def Spawn(self,spawnDict):
  self.spawnDict = spawnDict
  self.enemyTeam = 0
  self.myTeam = self.body.team
  if self.myTeam == 0:
    self.enemyTeam = 1
  return
 def Restart(self):
  return
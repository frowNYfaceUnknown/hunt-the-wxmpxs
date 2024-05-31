import random
from utils import Event
from typing import Any, Callable

from agent import Agent
from grid import GridObjects
from .GridObjects import getWumpus, getPit, getGold, getWall

class Grid:

    def __init__(
            self,
            size: tuple[int, int],
            playerPos: tuple[int, int] = (1, 1),
            wumpi: int = 1,
            pits: int = 2,
            gold: int = 1
        ) -> None:
        
        self.size = size
        self.playerPos = playerPos
        self.grid: list[list["GridObjects.GridObject"]] = [ [ None for i in range(size[0] + 2) ] for j in range(size[1] + 2) ]    ## so while iterating, you iterate over y first, then x
        
        self.movePlayer = Event()
        self.movePlayer += self._move_player

        self._populate_with_GridObjects(wumpi=wumpi, pits=pits, gold=gold)
        self.disp_grid()

    def _populate_with_GridObjects(self, **gameObjDict: int) -> None:
        
        ## make sure number of wumpi and number of pits are less than y*x.
        try:
            if gameObjDict["wumpi"] + gameObjDict["pits"] > self.size[0] * self.size[1]:
                raise OverflowError("The number of wumpi and pits combined exceed the total number of cells in the grid.")
        
        except KeyError:
            raise KeyError("Missing Parameter: Values for `wumpi` and/or `pits` not found in gameOjbjDict.")

        for y in range(self.size[1] + 2):
            for x in range(self.size[0] + 2):

                if y == 0 or y == self.size[1] + 1 or x == 0 or x == self.size[0] + 1:
                    self.grid[y][x] = getWall()
                    self.grid[y][x].initGridObject((x, y), self)
        
        xrange = (1, self.size[0])      ## inclusive, inclusive
        yrange = (1, self.size[0])      ## inclusive, inclusive
        exclude = [self.playerPos]      ## exclude player spawn position
        for gameObj in gameObjDict.keys():

            totalGenerated = 0
            if gameObj == "wumpi" or gameObj == "pits":
                
                while totalGenerated < gameObjDict[gameObj]:
                    
                    genX = random.randint(xrange[0], xrange[1])
                    genY = random.randint(yrange[0], yrange[1])
                    if (genX, genY) not in exclude:
                        
                        self.grid[genY][genX] = getWumpus() if gameObj == "wumpi" else getPit()
                        self.grid[genY][genX].initGridObject((genX, genY), self)
                        totalGenerated += 1
                        exclude.append((genX, genY))    ## exclude this point from further on
            
            elif gameObj == "gold":
                pass ## for now
    
    def _move_player(self, **kwds) -> None:

        dom = kwds.get("dom")
        if dom == None:
            raise KeyError("Missing Parameter: No direction of movement provided.")
        
        agentObj: "Agent.Agent" = kwds.get("agentObj")
        if agentObj == None:
            raise KeyError("Missing Parameter: No Agent Object provided.")
        
        tempPos = (self.playerPos[0] + dom[0], self.playerPos[1] + dom[1])
        if self.grid[tempPos[1]][tempPos[0]] != None:
            self.grid[tempPos[1]][tempPos[0]](
                agentObj = agentObj,
                newPos = tempPos
            )
        else:
            self.playerPos = tempPos
            agentObj.pos = tempPos

    def disp_grid(self) -> None:

        for y in range(self.size[1] + 1, -1, -1):
            print("+-----" * (self.size[0] + 2) + "+")
            for x in range(self.size[0] + 2):
                info = ""
                if str(self.grid[y][x]) == "wumpus":
                    info += "W"
                if str(self.grid[y][x]) == "pit":
                    info += "P"
                if str(self.grid[y][x]) == "gold":
                    info += "G"
                if str(self.grid[y][x]) == "wall":
                    info = "#"
                if (x, y) == self.playerPos:
                    info += "Pl"
                x = int(((5 - len(info))/2))
                print("|" + " " * x + info + " " * (5 - x - len(info)), end="")
            print("|")
        print("+-----" * (self.size[0] + 2) + "+")
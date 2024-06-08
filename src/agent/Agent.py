from grid import Grid
from utils import DoA, Percept

from typing import Any, Callable

class Agent:

    def __init__(self, parentGrid: "Grid.Grid") -> None:
        
        self.grid = parentGrid
        self.pos = self.grid.playerPos
        self.entryPos = self.grid.playerPos
        self.dir = DoA.Up
        self.isPerceiving = [Percept.Nothing]
        self.isAlive = True
        self.hasExited = False

        self.perceive()     ## perceive the initial position
    
    def perceive(self) -> Percept:
        
        self.isPerceiving = self.grid.perceive(self.pos)

    def decipher_input(self, inp: str):
        
        if inp == "w":
            self.move()
        
        elif inp == "a":
            self.rotate(reverse=True)
        
        elif inp == "s":
            self.move(reverse=True)
        
        elif inp == "d":
            self.rotate()
        
        elif inp == "e":
            self.shoot()
        
        elif inp == "q":
            self.exit()
        
        elif inp == "H":
            print()
        
        else:
            print("Invalid input. Try H for Help.\n\nCustom Inputs can be configured via running utils.\n\n\tpy utils.py --customise_inps")    ## TODO: 

    def disp_perception(self):
        
        print("The agent perceives: ", end="")
        for idx in range(len(self.isPerceiving)):
            if idx != len(self.isPerceiving) - 1:
                print(self.isPerceiving[idx], end=", ")
            else:
                print(self.isPerceiving[idx])

    def move(self, reverse = False) -> None:       ## dom -- direction of movement

        if reverse == True:
            
            self.grid.movePlayer(
                dom = -self.dir,
                agentObj = self
            )
        
        else:

            self.grid.movePlayer(
                dom = self.dir,
                agentObj = self
            )
    
    def moveTo(self, pos: tuple[int, int]) -> None:

        self.pos = pos
        self.grid.playerPos = pos

    def rotate(self, reverse: DoA = False) -> None:

        if reverse == True:

            if self.dir == DoA.Up:
                self.rotateTo(DoA.Left)
            
            elif self.dir == DoA.Left:
                self.rotateTo(DoA.Down)
            
            elif self.dir == DoA.Down:
                self.rotateTo(DoA.Right)
            
            elif self.dir == DoA.Right:
                self.rotateTo(DoA.Up)
        
        else:

            if self.dir == DoA.Up:
                self.rotateTo(DoA.Right)
            
            elif self.dir == DoA.Right:
                self.rotateTo(DoA.Down)
            
            elif self.dir == DoA.Down:
                self.rotateTo(DoA.Left)
            
            elif self.dir == DoA.Left:
                self.rotateTo(DoA.Up)
    
    def rotateTo(self, newDir: DoA) -> None:

        self.dir = newDir
        self.grid.playerDir = newDir

    def shoot(self, dos: DoA) -> None:      ## dos -- direction of shooting     TODO: implement shooting     [!!]
        pass

    def killPlayer(self) -> None:

        self.isAlive = False
        self.grid.playerAlive = False

    def exit(self):
        pass

    def hunt(self) -> None:
        """
            Override this function. This function is supposed to contain the main loop of the agent until either the agent is dead or wins.
        """
        raise NotImplementedError("Please use Manual, Propositional, Hybrid, or any other self-implemented Agent.")
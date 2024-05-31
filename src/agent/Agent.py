from grid import Grid
from utils import DoA, Percept

from typing import Any, Callable

class Agent:

    def __init__(self, parentGrid: "Grid.Grid") -> None:
        
        self.grid = parentGrid
        self.pos = self.grid.playerPos
        self.isPerceiving = Percept.Nothing
        self.alive = True

        self.perceive()     ## perceive the initial position
    
    def perceive(self) -> Percept:          ##                                  TODO: implement perception   [!!!]
        pass

    def move(self, dom: DoA) -> None:       ## dom -- direction of movement

        self.grid.movePlayer(
            dom = dom,
            agentObj = self
        )
    
    def shoot(self, dos: DoA) -> None:      ## dos -- direction of shooting     TODO: implement shooting     [!!]
        pass

    def hunt(self) -> None:
        """
            Override this function. This function is supposed to contain the main loop of the agent until either the agent is dead or wins.
        """
        raise NotImplementedError("Please use Manual, Propositional, Hybrid, or any other self-implemented Agent.")
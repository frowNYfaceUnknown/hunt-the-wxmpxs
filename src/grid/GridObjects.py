from typing import Callable, Any

from grid import Grid
from agent import Agent
from utils import Percept

class GridObject:

    def __init__(
            self,
            name: str,
            func: Callable
    ) -> None:
        
        self.name = name
        self.func = func
    
    def __str__(self) -> str:
        
        return self.name

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        
        return self.func(*args, **kwds)
    
    def initGridObject(
            self,
            pos: tuple[int, int],
            parentGrid: "Grid.Grid"
    ) -> None:
        
        self.pos = pos
        self.parentGrid = parentGrid

def getWumpus() -> GridObject:

    def wumpusFunc(*args, **kwds):
        
        agentObj: "Agent.Agent" = kwds.get("agentObj")
        if agentObj == None:
            raise KeyError("Missing Parameter: No Agent Object provided.")
        
        newPos = kwds.get("newPos")
        if newPos == None:
            raise KeyError("Missing Parameter: No position provided. (Likely due to an internal argument-passing error)")

        ## move the player to new position
        agentObj.moveTo(newPos)
        
        ## un-alive the agent
        print("GAME OVER: Wumpus ate the Agent. Agent Died.")
        agentObj.killPlayer()

    return GridObject(name="wumpus", func=wumpusFunc)

def getPit() -> GridObject:
    
    def pitFunc(*args, **kwds):
        
        agentObj: "Agent.Agent" = kwds.get("agentObj")
        if agentObj == None:
            raise KeyError("Missing Parameter: No Agent Object provided.")
        
        newPos = kwds.get("newPos")
        if newPos == None:
            raise KeyError("Missing Parameter: No position provided. (Likely due to an internal argument-passing error)")

        ## move the player to new position
        agentObj.moveTo(newPos)

        ## un-alive the agent
        print("GAME OVER: Agent fell into the pit. Agent Died.")
        agentObj.killPlayer()

    return GridObject(name="pit", func=pitFunc)

def getGold() -> GridObject:
    
    def goldFunc(*args, **kwds):
        
        agentObj: "Agent.Agent" = kwds.get("agentObj")
        if agentObj == None:
            raise KeyError("Missing Parameter: No Agent Object provided.")
        
        newPos = kwds.get("newPos")
        if newPos == None:
            raise KeyError("Missing Parameter: No position provided. (Likely due to an internal argument-passing error)")
        
        ## move the player to new position
        agentObj.moveTo(newPos)

    return GridObject(name="gold", func=goldFunc)

def getWall() -> GridObject:
    
    def wallFunc(*args, **kwds):
        
        agentObj: "Agent.Agent" = kwds.get("agentObj")
        if agentObj == None:
            raise KeyError("Missing Parameter: No Agent Object provided.")
        
        ## perceive bump and nothing else
        agentObj.isPerceiving = Percept.Bump

    return GridObject(name="wall", func=wallFunc)
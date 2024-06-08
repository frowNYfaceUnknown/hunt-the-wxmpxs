## basic utils for the project
from enum import Enum
from typing import Any, Callable

class DoA(Enum):        ## DoM -- Direction of Action

    Up      = (0, 1)
    Right   = (1, 0)
    Left    = (-1, 0)
    Down    = (0, -1)

    @classmethod
    def fromVals(cls, val: tuple[int, int]) -> "DoA":

        if val == (0, 1):
            return DoA.Up
        
        elif val == (1, 0):
            return DoA.Right
        
        elif val == (-1, 0):
            return DoA.Left
        
        elif val == (0, -1):
            return DoA.Down
    
    def __getitem__(self, key: int) -> "DoA":
        
        if -1 < key < 2:
            return self.value[key]
        
        else:
            raise IndexError(f"DoA has only two elements. But {key}th element was tried to access.")

    def __neg__(self) -> "DoA":
        return DoA.fromVals((-self.value[0], -self.value[1]))

class Percept(Enum):

    Nothing = 0
    Stench  = 1
    Breeze  = 2
    Scream  = 3
    Glitter = 4
    Bump    = 5

    def __str__(self) -> str:
        return self.name

class Event:

    def __init__(self) -> None:
        """
            Custom Event class. An event is an object that can at once trigger multiple different similar actions.\n
            This is achieved by subscribing a function or a method to an event.\n
            NOTE: An event can take multiple arguments, but cannot return values returned by the subscribers.
        """
        self.subscribers: list[Callable] = []
    
    def __iadd__(self, other: Callable) -> None:
        
        if isinstance(other, Callable):
            self.subscribers.append(other)
            return self
        
        else:
            raise TypeError(f"{other} is not a function.")
    
    def __isub__(self, other: Callable) -> bool:

        try:
            self.subscribers.remove(other)
            return True
        except:
            return False
    
    def __call__(self, *args: Any, **kwds: Any) -> None:    ## only kwds used so as to remove ambiguity of args during execution
        
        for subscriber in self.subscribers:
            subscriber(*args, **kwds)
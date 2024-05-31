## basic utils for the project
from enum import Enum
from typing import Any, Callable

class DoA(Enum):        ## DoM -- Direction of Action

    Up      = (0, 1)
    Right   = (1, 0)
    Left    = (-1, 0)
    Down    = (0, -1)

class Percept(Enum):

    Nothing = 0
    Stench  = 1
    Breeze  = 2
    Scream  = 3
    Glitter = 4
    Bump    = 5

class Event:

    def __init__(self) -> None:
        """
            Custom Event class. An event is an object that can at once trigger multiple different similar actions.\n
            This is achieved by subscribing a function or a method to an event.\n
            NOTE: An event can take multiple arguments, but cannot return values returned by the subscribers.
        """
        self.subscribers: list[Callable] = []
    
    def __iadd__(self, other: Callable) -> bool:
        
        try:
            if other.isinstance(Callable):
                self.subscribers.append(other)
                return True
            else:
                return False
        except:
            return False
    
    def __isub__(self, other: Callable) -> bool:

        try:
            self.subscribers.remove(other)
            return True
        except:
            return False
    
    def __call__(self, *args: Any, **kwds: Any) -> None:    ## only kwds used so as to remove ambiguity of args during execution
        
        for subscriber in self.subscribers:
            subscriber(*args, **kwds)
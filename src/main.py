import getopt
from grid.Grid import Grid
from agent.Agent import Agent

def main(mode: int) -> int:
    grid = Grid((5, 5))
    player = Agent(grid)

    player.hunt()

if __name__ == "__main__":
    
    ## parse command line arguments for mode - manual, automatic, hybrid
    main(0)
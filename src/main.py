import getopt
from grid.Grid import Grid
from agent.ManualAgent import ManualAgent

def main(mode: int) -> int:
    grid = Grid((5, 5))
    player = ManualAgent(grid)

    player.hunt()

if __name__ == "__main__":
    
    ## parse command line arguments for mode - manual, automatic, hybrid
    main(0)
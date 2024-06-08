from .Agent import Agent

class ManualAgent(Agent):

    def hunt(self) -> None:
        
        while self.isAlive and not self.hasExited:
            
            ## display the grid first
            self.grid.disp_grid()

            ## perceive the environment and then display the perception
            self.perceive()
            self.disp_perception()
            
            ## ask user what to do
            mov = input("What does the agent do next? (W | A | S | D | E | Q | H):").casefold()
            self.decipher_input(mov)

            ## display the grid one last time if the player died.
            if not self.isAlive:
                self.grid.disp_grid()
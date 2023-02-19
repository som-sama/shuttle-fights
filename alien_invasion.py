import sys

import pygame

#overall class to manage game bheaviour and assests.
class AlienInvasion:
    
    def __init__(self):
        #creating game resources.
        pygame.init()
        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")

    #lets start the main loop for the game

    def run_game(Self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
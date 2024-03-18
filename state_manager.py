# state manager 
## contains game states
import pygame 

class StateManager():

    def __init__(self, game):
        self.states = []
        self.current_state = None 
        self.game = game
        
    def set_state(self, state):
        """Sets the current statet"""
        self.current_state = state 
    
    def handle_events(self):
        """Handles all the events of the game"""
        if self.current_state:
            for  event in pygame.event.get():
                if event.type == pygame.QUT:
                    pygame.quit()
                else:
                    self.current_state.handle_event(event)
    
    def update(self, events):
        if self.current_state:
            self.current_state.update(events)
    
    def render(self, screen):
        if self.current_state:
            self.current_state.render(screen)


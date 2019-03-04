import game
import pygame
from character import *
from pygame.locals import *
from constants import *


class ControlledCharacter(Character):

    def update_events(self, events):
         # Y movement
        if not self.land and self.jump:
            self.jump= False
        return
   
    def on_left(self):
        self.direction = True
        self.right = True
        self.left = False

    def on_right(self):
        self.direction = False        
        self.right = False
        self.left = True

    def on_bullet_hit(self):
        self.jump = True
    
    
    def on_start(self):
        self.direction = True
        self.right = True

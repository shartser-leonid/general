import numpy as np
import game
import pygame
from character import *
from pygame.locals import *
from constants import *


class FlyingBullet(Character):
    def __init__(self, x, y, direction , collider, resources,actors_list):  
        self._actors_list = actors_list
        self._direction = direction
        Character.__init__(self,x,y,collider,resources)
        self.vy=0
        self.gravity_factor=0

    def update_events(self, events):
        # check against actors and call on_bullet_hit
        for a in self._actors_list:
            col = a.collider
            if np.abs(col.x-self.x)<3:
                a.on_bullet_hit()


        return

    def on_left(self):
        l=self._actors_list
        if (self in l): l.remove(self)
    def on_right(self):
        l=self._actors_list
        if (self in l): l.remove(self)

    def on_start(self):
        self.direction = self._direction
        self.right = self._direction
        self.left = not self.right
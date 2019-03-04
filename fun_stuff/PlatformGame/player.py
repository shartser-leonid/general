import game
import pygame
from character import *
from pygame.locals import *
from constants import *
from flying_bullet import *
from resources import *

class Player(Character):
    def __init__(self, x, y, collider, resources,actors_list):  
        self.quit=False
        self._actors_list = actors_list
        self._resources = resources
        Character.__init__(self,x,y,collider,resources)
        self._Res = Resources()
        self.on_deadly=False

    def on_deadly_stuff(self):
        if (not self.is_dying):
            self.frame=0
        self.on_deadly=True
        self.is_dying = True
        
    def off_deadly_stuff(self):
        if (self.on_deadly):
            self.on_deadly=False
            self.jump = False
            self.is_dying=False
            self.frame=0

    def update_events(self, events):
        if K_RIGHT in events:
            if not self.right:
                self.direction = True
                self.frame = 0
            self.right = events[K_RIGHT]
            
        if K_LEFT in events:
            if not self.left:
                self.direction = False
                self.frame = 0
            self.left = events[K_LEFT]
            
        if K_UP in events:
            self.jump = events[K_UP]
            self.frame = 0

        if K_SPACE in events:
            fb=FlyingBullet(self.x, int(self.y-self.collider.h/2), self.direction, pygame.Rect(0,0,15,35), self._Res.ball,self._actors_list)
            fb.on_start()
            self._actors_list.append(fb)
        
        if K_ESCAPE in events:
            self.quit = True

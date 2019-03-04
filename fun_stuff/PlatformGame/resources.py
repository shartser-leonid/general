import game
import pygame
from pygame.locals import *


class Shifting:
    def __init__(self,x=0,w=0,y=0,h=0):
        self.x=x
        self.w=w
        self.y=y
        self.h=h

def build_sprite_manager(sheet_name,w,h,flip=False,blank_color=(0,0,0),scale=1.0,shifting=Shifting()):
    sheet = game.load_image(sheet_name,blank_color,scale=scale)
    size = sheet.get_size()
    sheet = pygame.transform.scale(sheet, (int(size[0]*scale), int(size[1]*scale)))
    s=shifting
    s5 = SpriteManager(int(w*scale),int(h*scale),sheet,flip,shift_x=s.x,shift_w=s.w,shift_y=s.y,shift_h=s.h)
    return s5


class SpriteManager:
    def __init__(self,w,h,sheet,flip=False,shift_x=0,shift_w=0,shift_y=0,shift_h=0):
        self._W=w
        self._H=h
        self._sheet=sheet
        self._flip = flip
        #self._shift = shift
        self.shift_x,self.shift_w,self.shift_y,self.shift_h=shift_x,shift_w,shift_y,shift_h

    def get_by_coords(self,x,y,w,h,n):
        rects = [pygame.Rect(x,y,w,h)]*n
        sprites = game.load_sprites(self._sheet, rects, (0,0,0))
        sprites_flipped = game.flip_sprites(sprites)
        return [sprites_flipped,sprites]    

    def get_ij(self,list_ijs):
        flip= self._flip
        sheet = self._sheet
        rects = [pygame.Rect(ind[1]*self._W + self.shift_x,ind[0]*self._H+self.shift_y, self._W-self.shift_w,self._H-self.shift_h) for ind in list_ijs]
        sprites = game.load_sprites(sheet, rects, (0,0,0))
        sprites_flipped = game.flip_sprites(sprites)
        if not flip:
            return [sprites,sprites_flipped]
        else:
            return [sprites_flipped,sprites]    

class Resources:
    def __init__(self):
        # Carga de imagenes
        sheet = game.load_image('graphics/arc22.png')
        sheet2 = game.load_image('graphics/arc2.png')
        elan_pic = game.load_image('graphics/elan_mod.png')
        adam_pic = game.load_image('graphics/adam_mod.png')
        self._sheet2=sheet2
        self._sheet3= game.load_image('graphics/blocks2.png')
        

        #rects = [#pygame.Rect(514,8,24,34),
        #        pygame.Rect(550,8,30,34),
        #         pygame.Rect(582,8,28,34),
        #         pygame.Rect(550,8,30,34)]
        rects = [pygame.Rect(112,2,26,40),
                 pygame.Rect(112,2,26,40),
                 pygame.Rect(112,2,26,40),
                 pygame.Rect(4,4,30,38),
                 pygame.Rect(4,4,30,38),
                 pygame.Rect(4,4,30,38)]

        self._W=34
        self._H=42

        


        caminando_der = game.load_sprites(sheet, rects, (0,0,0))
        caminando_izq = game.flip_sprites(caminando_der)

        rects = [pygame.Rect(76,2,26,40),
                 pygame.Rect(112,2,24,40)]
        quieto_der = game.load_sprites(sheet, rects, (0,0,0))
        quieto_izq = game.flip_sprites(quieto_der)

        rects = [pygame.Rect(4,4,30,38),
                 pygame.Rect(38,4,30,36)]
        saltando_der = game.load_sprites(sheet, rects, (0,0,0))
        saltando_izq = game.flip_sprites(saltando_der)
        self.player = [
            [quieto_der, quieto_izq], #idle 
            [caminando_der,caminando_izq],  #walking          
            [saltando_der, saltando_izq]] #jumping


        rects = [pygame.Rect(105,335,33,46),pygame.Rect(105,335,33,46)]
        ninja_idle = game.load_sprites(sheet2, rects, (0,0,0))
        ninja_idle_flipped = game.flip_sprites(ninja_idle)

        rects = [pygame.Rect(105,335,33,46),
                pygame.Rect(140,339,32,41), pygame.Rect(172,338,31,42)]
        ninja_walking = game.load_sprites(sheet2, rects, (0,0,0))
        ninja_walking_flipped = game.flip_sprites(ninja_walking)

        rects = [pygame.Rect(311,338,33,40), 
                 pygame.Rect (343,336,35,37)]
        ninja_jumping = game.load_sprites(sheet2, rects, (0,0,0))
        ninja_jumping_flipped = game.flip_sprites(ninja_jumping)

        self.ninja1 = [
            [ninja_idle,ninja_idle_flipped],
            [ninja_walking,ninja_walking_flipped],
            [ninja_jumping,ninja_jumping_flipped],
        ]    


        s1 = SpriteManager(34,42,sheet2,True,0)
        #s2 = SpriteManager(34,42,sheet2,False,4)
        s3 = SpriteManager(34,34,self._sheet3,False,4,4,2,2)

        s2 = build_sprite_manager('graphics/arc2.png',34,42,False,scale=2,shifting=Shifting(x=4))

        self.ninja = [
            s1.get_ij([(1,8),(1,8)]),
            s1.get_ij([(1,8),(1,9)]),
            s1.get_ij([(1,13),(1,14)])
        ]

        self.blue_guy = [
            s2.get_ij([(6,16),(6,16)]),
            s2.get_ij([(6,16),(6,17)]),
            s2.get_ij([(6,17),(6,17)])
        ]

        x=s3.get_ij([(8,6),(8,6)])
        s7 = build_sprite_manager('graphics/single_fire.png',391,131,flip=True,blank_color=(0,0,0),scale=0.15,shifting=Shifting(0,0,0,0))
        x=s7.get_ij([(0,0)])
        self.ball = [x,x,x]

        s4=SpriteManager(331,41,elan_pic,False)
        x1=s4.get_by_coords(0,0,78,149,2)
        x2=s4.get_by_coords(0,0,78,149,2)
        self.elan = [x1,x1,x2]

        s4=SpriteManager(0,0,adam_pic,False)
        x11=s4.get_by_coords(0,0,74,141,2)
        x21=s4.get_by_coords(0,0,74,141,2)
        self.adam = [x11,x11,x21]

        '''
        self._funky_ninja_sheet = game.load_image('graphics/knight2.png',(255,255,255),1)
        size = self._funky_ninja_sheet.get_size()
        # create a 2x bigger image than self.image
        scale=0.25
        self._funky_ninja_sheet = pygame.transform.scale(self._funky_ninja_sheet, (int(size[0]*scale), int(size[1]*scale)))
        s5 = SpriteManager(300/4,320/4,self._funky_ninja_sheet,False)
        '''
        s5 = build_sprite_manager('graphics/knight2.png',300,320,flip=False,blank_color=(255,255,255),scale=0.25)
        #self.funky_ninja = [s5.get_ij([(0,0),(0,0)]),s5.get_ij([(1,0),(1,1),(1,2)]),s5.get_ij([(3,1),(3,2)])]

        s8 = build_sprite_manager('graphics/gorgle_dying.png',65,40,flip=False,blank_color=(255,255,255),scale=1.5,shifting=Shifting(0,0,5,5))
        #self.dying = [s7.get_ij([(0,0),(0,0)]),s7.get_ij([(1,0),(2,0),(3,0),(4,0),(5,0),(6,0)]),s7.get_ij([(0,0),(0,0)])]
        
        s6 = build_sprite_manager('graphics/gorgle_walking_h.png',40,45,flip=False,blank_color=(255,255,255),scale=1.5,shifting=Shifting(0,0,5,5))
        self.funky_ninja = [s6.get_ij([(0,0),(0,0)]),s6.get_ij([(1,0),(2,0),(3,0),(4,0),(5,0),(6,0)]),s6.get_ij([(0,0),(0,0)]),s8.get_ij([(0,0),(1,0),(2,0),(3,0),(4,0)])]



        
        

        sheet = game.load_image('graphics/blocks11.png')
        suelo = game.load_sprite(sheet, pygame.Rect(444,104,32,32))
        subsuelo = game.load_sprite(sheet, pygame.Rect(172,138,32,32))
        self.tiles = [suelo, subsuelo]
    




    
        

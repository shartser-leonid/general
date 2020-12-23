import game
import pygame
from constants import *
from resources import *
from player import *
from tile import *
from tilemap import *
from tileset import *
from camera import *
from gamelogic import *
from controlled_character import *
# just a comment another one

# Game starts!
game.start(DISP_W*2, DISP_H*2)

resources = Resources()

moving_actors=[]

player = Player(40, 40, pygame.Rect(0,0,15,35), resources.funky_ninja,moving_actors)
ai = ControlledCharacter(100, 40, pygame.Rect(0,0,15,35), resources.ninja1)
ai2 = ControlledCharacter(120, 40, pygame.Rect(0,0,15,35), resources.ninja)
ai10 = ControlledCharacter(40, 40, pygame.Rect(0,0,15,35), resources.blue_guy)
#blue_guy1 = ControlledCharacter(80, 40, pygame.Rect(0,0,15,35), resources.blue_guy)

tilemap = Tilemap() 
tilemap.load_tilesets('map1.json')
tilemap.load_map('map1.json')

moving_actors.extend([player,ai,ai2,ai10])

camera = Camera(0, 0, player,moving_actors, tilemap, True, 0.25)
gamelogic = Gamelogic(moving_actors, tilemap)

clock = game.clock()

pygame.mixer.init()
pygame.mixer.music.load("sound/hyperfun.mp3")
pygame.mixer.music.play(100)

#sheet = game.load_image('graphics/blocks1.png')
#sheet2 = game.load_image('graphics/blocks2.png')

# Gameloop
gamelogic.start()

while True:
    events = game.get_events()
    if 'QUIT' in events or player.quit:
        game.quit_game()
        break
    
    game.clear()

    gamelogic.update(events)
    camera.update()
    camera.draw()

    clock.tick(30)
    game.debug_txt('FPS: '+str(clock.get_fps())[:4], (540,380),RED) 
    
    game.update()
    
    

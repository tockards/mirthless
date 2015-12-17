import pygame
from pygame.locals import *
from messages import messages
from util import debug

class AnimatedSprite(pygame.sprite.DirtySprite):
    animations = {
        "stand": ['Aquatic0.png:4:1:0','Aquatic0.png:5:1:90','Aquatic0.png:4:1:180','Aquatic0.png:5:1:270'],
        'walkleft': [],
        'walkright': [],
        'walkup': [],
        'walkdown': []
    }
    def __init__(self, tilemaps, rect, animations={}, layer=2, fps=60):
        self._layer = layer
        self.framerate = 60/fps
        self.counter = 0
        super(pygame.sprite.DirtySprite, self).__init__()
        self.setanimation('stand')
        self.tilemaps = tilemaps
        if animations:
            self.animations = animations
        self.rect = rect
        self.image = self.tilemaps.get_by_path(self.currentframe())

    def setanimation(self, newanimation):
        self.animation = newanimation
        self.frame =0

    def currentframe(self):
        try:
            return self.animations[self.animation][self.frame]
        except:
            self.frame = 0
            return self.animations['stand'][self.frame]

    def update(self):
        self.counter += 1
        if self.counter%self.framerate == 0:
            if self.frame < len(self.animations[self.animation]) -1:
                self.frame += 1
            else:
                self.frame = 0
            self.image = self.tilemaps.get_by_path(self.currentframe())
            self.image = pygame.transform.smoothscale(self.image, (self.rect.w, self.rect.h))

    def delete(self):
        self.kill()


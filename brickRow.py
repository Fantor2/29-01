from config import *
import pygame
from brick import Brick

class BrickRow:
    def __init__(self):
        self.row = []
        color = RED
        y = 80
        for i in range(20):
            x = 0 + i*BRICK_WIDTH
            brick=Brick(x,y,color)
            self.row.append(brick)
    def update(self):
        pass

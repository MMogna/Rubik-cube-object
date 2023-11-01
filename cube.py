#!env Python3.11

from icecream import ic
import numpy as np


# face based description of the cube
class Cube3x3:
    def __init__(self) -> None:
        self.top_layer = {}
        self.mid_layer = {}
        self.bot_layer = {}

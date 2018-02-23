import Pizza
import numpy as np
import math
from random import randint

class Ga:
    # population of pizzas
    pizzas = None
    
    r = None
    c = None
    l = None
    h = None
    
    def __init__(r, c, l, h):
        pizzas = np.empty((50))
        self.r = r
        self.c = c
        self.l = l
        self.h = h
        
        self.init_pop()
        
    def init_pop(self):
        width = randint(1, self.h)
        height = randint(math.ceil(2*l/width), int(self.h/width))
        
        
    
    def selection(self):
        
        
        
    def crossover(self):
        
    def mutate(self):

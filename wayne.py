#!/usr/bin/env python3
from wheel import Wheel
from vehicle import Vehicle

class Pinto(Vehicle):
    def __init__(self, color):
        self.wheel = Wheel(25) 
        self.engine = Engine(2.8)
        self.speed = 0.0
        self.color = color

    def start(self):
        self.engine.turn_on()

    def stop(self): 
        self.engine.turn_off()
    
    def accelerate(self):
        if self.speed < 55:
            self.speed += 1.0
        else:
            self.speed = 55

    def brake(self):
        if self.speed > 0.0:
            self.speed -= 1.0
        else:
            self.speed = 0.0


    def print_speed(self):
        print(f"Current Speed: {self.speed}")

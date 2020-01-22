#!/usr/bin/env python3
from wheel import Wheel
from vehicle import Vehicle

class BMX(Vehicle):

    def __init__(self,u_color):
        self.front_wheel = Wheel(16)
        self.rear_wheel = Wheel(16)
        self.pedal = True
        self.handlebars = True
        self.frame = True
        self.brakes = True
        self.color = u_color
        self.speed = 0


    def pedal(self):
        if self.front_wheel and self.rear_wheel and self.pedal and self.frame and ( not self.speed > 30 ):
            self.speed += 1


    def brake(self):
        if self.handlebars and self.front_wheel and self.rear_wheel and self.brakes and self.frame and (not self.speed < 0 ):
            self.speed -= 1


    def paint(self, color):
        self.color = color


    def print_speed(self):
        print(f"Current Speed: {self.speed}")

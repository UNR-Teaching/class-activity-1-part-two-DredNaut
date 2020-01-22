#!/usr/bin/env python3
class Engine:

    def __init__(self, displacement):
        self.displacement = displacement
        self.engine_on = False
        

    def turn_on(self):
        self.engine_on = True


    def turn_off(self):
        self.engine_on = False

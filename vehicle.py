#!/usr/bin/env python3
from abc import ABC, abstractmethod

class Vehicle(ABC):

    def __init__(self, color, num_wheels):
        self.speed = 0
        self.number_of_wheels = num_wheels

    
    @abstractmethod
    def print_speed(self):
        pass

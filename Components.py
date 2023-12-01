#!/usr/bin/env python3


from Utils import *


class Pad:
    def __init__(self, x, y, radius, width=1):
        self.x = x
        self.y = y
        self.width = width
        self.radius = radius


    def draw(self, color=(1, 1, 1)):
        Line(x0=self.x, y0=self.y+self.radius, x1=self.x, y1=self.y-self.radius, size=self.width, color=color)

    def reset(self, x, y):
        self.x = x
        self.y = y


class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def draw(self):
        Circle(x=self.x, y=self.y, radius=4, weight=6)

    def reset(self, x, y):
        self.x = x
        self.y = y



class Arrow:
    def __init__(self, x=320, y=650, d=25, width=3, color=(0, 0.705, 0.705)):
        self.x = x
        self.y = y
        self.d = d
        self.width = width
        self.color = color
        self.vertex_x =  self.x - self.d
        self.vertex_y = self.y


    def draw(self):
        Line(self.x, self.y, self.x + self.d, self.y, self.width, self.color)
        Line(self.x, self.y, self.vertex_x, self.vertex_y, self.width, self.color)
        Line(self.vertex_x, self.vertex_y, self.x, self.y + self.d, self.width, self.color)
        Line(self.vertex_x, self.vertex_y, self.x, self.y - self.d, self.width, self.color)
        


class Pause:
    def __init__(self, x=445, y=650, d=25, width=3, color=(0.125, 0.660, 0.286)):
        self.x = x
        self.y = y
        self.d = d
        self.width = width
        self.space = 15
        self.color = color


    def draw(self):
        Line(self.x + self.space, self.y + self.d, self.x + self.space, self.y - self.d, self.width, self.color)
        Line(self.x - self.space, self.y + self.d, self.x - self.space, self.y - self.d, self.width, self.color)



class Play:
    def __init__(self, x=435, y=650, d=25, width=3, color=(0.125, 0.660, 0.286)):
        self.x = x
        self.y = y
        self.d = d
        self.width = width
        self.color = color
        self.vertex_x =  self.x + self.d
        self.vertex_y = self.y


    def draw(self):
        Line(self.x, self.y + self.d, self.x, self.y - self.d, self.width, self.color)
        Line(self.vertex_x, self.y, self.x, self.y + self.d, self.width, self.color)
        Line(self.vertex_x, self.y, self.x, self.y - self.d, self.width, self.color)



class Cross:
    def __init__(self, x=580, y=650, d=25, width=3, color=(0.840, 0.0924, 0.0924)):
        self.x = x
        self.y = y
        self.d = d
        self.width = width
        self.color = color


    def draw(self):
        Line(self.x, self.y, self.x + self.d, self.y + self.d, self.width, self.color)
        Line(self.x, self.y, self.x + self.d, self.y - self.d, self.width, self.color)
        Line(self.x, self.y, self.x - self.d, self.y + self.d, self.width, self.color)
        Line(self.x, self.y, self.x - self.d, self.y - self.d, self.width, self.color)


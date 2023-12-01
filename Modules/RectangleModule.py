#!/usr/bin/env python3


from .ImportGL import *
from .LineModule import Line

class Rectangle:
    def __init__(self, x0, y0, w, h, fill=False, color=(1, 1, 1)):
        self.x0 = x0
        self.y0 = y0
        self.w = w
        self.h = h
        self.color=color

        if fill:
            self.drawFillRect()
        else:
            self.drawRect()


    def drawRect(self):
        x1 = self.x0 + self.w
        y1 = self.y0

        x2 = x1
        y2 = y1 - self.h

        x3 = self.x0
        y3 = y2

        Line(self.x0, self.y0, x1, y1, size=2, color=self.color)
        Line(x1, y1, x2, y2, size=2, color=self.color)
        Line(x2, y2, x3, y3, size=2, color=self.color)
        Line(x3, y3, self.x0, self.y0, size=2, color=self.color)


    def drawFillRect(self):
        x1 = self.x0 + self.w
        y1 = self.y0

        for i in range(self.h, 0, -2):
            Line(self.x0, self.y0-i, x1, y1-i, size=2, color=self.color)




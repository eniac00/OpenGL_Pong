
from Utils import *

def drawText(x, y, text, color=(1, 1, 1)):
    glColor3f(color[0], color[1], color[2])
    glRasterPos2f(x, y)
    for character in text:
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(character))


def drawTextSmall(x, y, text, color=(1, 1, 1)):
    glColor3f(color[0], color[1], color[2])
    glRasterPos2f(x, y)
    for character in text:
        glutBitmapCharacter(GLUT_BITMAP_9_BY_15, ord(character))


def drawPauseText(x=430, y=300):
    Line(x0=x-10, y0=y-20, x1=x+90, y1=y-20)
    Line(x0=x-10, y0=y+35, x1=x+90, y1=y+35)
    drawText(x, y, "Paused!")


def drawGOText(x=400, y=350, winner=None):
    if winner:
        Line(x0=x-10, y0=y+35, x1=x+135, y1=y+35)
        drawText(x, y, "GameOver!!!")
        drawText(x, y-50, f"Player {winner} won!")
        Line(x0=x-10, y0=y-70, x1=x+140, y1=y-70)
    else:
        print("error")


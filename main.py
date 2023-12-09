#!/usr/bin/env python3


from Utils import *

class Menu:
    def __init__(self):
        self.width = 500  # screen width
        self.height = 700 # screen height

        self.hover = None

    def drawTitle(self):
        Rectangle(50, 630, 70, 70, fill=True)
        Rectangle(50, 560, 20, 50, fill=True)

        Rectangle(151, 590, 60, 60, fill=True)

        Rectangle(255, 601, 15, 70, fill=True)
        Rectangle(270, 600, 50, 15, fill=True)
        Rectangle(320, 601, 15, 70, fill=True)

        Rectangle(370, 630, 15, 100, fill=True)
        Rectangle(385, 630, 60, 20, fill=True)
        Rectangle(370, 530, 80, 15, fill=True)
        Rectangle(450, 580, 15, 50, fill=True)

    
    def drawComponents(self):
        self.drawTitle()

        if self.hover:
            if self.hover == 1:
                Rectangle(90, 440, 320, 80, fill=True)
                Rectangle(90, 320, 320, 80)
                Rectangle(90, 200, 320, 80)

                drawText(200, 390, "P1 vs P2", color=(0, 0, 0))
                drawText(200, 270, "P2 vs AI")
                drawText(220, 150, "Quit")

            if self.hover == 2:
                Rectangle(90, 440, 320, 80)
                Rectangle(90, 320, 320, 80, fill=True)
                Rectangle(90, 200, 320, 80)

                drawText(200, 390, "P1 vs P2")
                drawText(200, 270, "P2 vs AI", color=(0, 0, 0))
                drawText(220, 150, "Quit")

            if self.hover == 3:
                Rectangle(90, 440, 320, 80)
                Rectangle(90, 320, 320, 80)
                Rectangle(90, 200, 320, 80, fill=True, color=(1, 0, 0))

                drawText(200, 390, "P1 vs P2")
                drawText(200, 270, "P2 vs AI")
                drawText(220, 150, "Quit")
        else:
            Rectangle(90, 440, 320, 80)
            drawText(200, 390, "P1 vs P2")
            Rectangle(90, 320, 320, 80)
            drawText(200, 270, "P2 vs AI")
            Rectangle(90, 200, 320, 80)
            drawText(220, 150, "Quit")

        drawTextSmall(170, 40, "created by eniac00")

            
    def iterate(self):
        glViewport(0, 0, self.width, self.height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0.0, self.width, 0.0, self.height, 0.0, 1.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()


    def showScreen(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        self.iterate()
        glClearColor(0, 0, 0, 1.0)
        self.drawComponents()
        glutSwapBuffers()


    def checkButtonClick(self, x, y):
        if self.height-y >= 360 and self.height-y <= 440:
            if x >= 90 and x <= 410:
                subprocess.Popen(["python", "Game.py"])
                glutLeaveMainLoop()
        elif self.height-y >= 240 and self.height-y <= 320:
            if x >= 90 and x <= 410:
                print("Coming soon ...")
        elif self.height-y >= 120 and self.height-y <= 200:
            if x >= 90 and x <= 410:
                glutLeaveMainLoop()
        else:
            pass

        glutPostRedisplay()


    def checkButtonHover(self, x, y):
        if self.height-y >= 360 and self.height-y <= 440:
            if x >= 90 and x <= 410:
                self.hover = 1
        elif self.height-y >= 240 and self.height-y <= 320:
            if x >= 90 and x <= 410:
                self.hover = 2
        elif self.height-y >= 120 and self.height-y <= 200:
            if x >= 90 and x <= 410:
                self.hover = 3
        else:
            self.hover = None

        glutPostRedisplay()
        

    def animate(self):
        glutPostRedisplay()


    def keyboardListener(self, key, x, y):
        if key == b"w":
            pass
        glutPostRedisplay()


    def mouseListener(self, button, state, x, y):
        if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
            self.checkButtonClick(x, y)
        glutPostRedisplay()


    def specialKeyListener(self, key, x, y):
        if key == GLUT_KEY_UP:
            if not self.hover:
                self.hover = 1
            else:
                if self.hover == 1:
                    self.hover = 3
                else:
                    self.hover = (abs(self.hover-2) % 3) + 1

        if key == GLUT_KEY_DOWN:
            if not self.hover:
                self.hover = 3
            else:
                self.hover = ((self.hover) % 3)  + 1
        glutPostRedisplay()


    def run(self):
        glutInit()
        glutInitDisplayMode(GLUT_RGBA)
        glutInitWindowSize(self.width, self.height)
        glutInitWindowPosition(0, 0)
        glutCreateWindow(b"OpenGL Pong")
        glutDisplayFunc(self.showScreen)
        glutIdleFunc(self.animate)
        glutKeyboardFunc(self.keyboardListener)
        glutPassiveMotionFunc(self.checkButtonHover)
        glutMouseFunc(self.mouseListener)
        glutSpecialFunc(self.specialKeyListener)
        glutMainLoop()



if __name__ == "__main__":
    Menu().run()


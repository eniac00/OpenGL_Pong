#!/usr/bin/env python3

from Utils import *

class Game:
    def __init__(self):
        self.width = 900  # screen width
        self.height = 700 # screen height
        self.upper_bound = self.height-100   # real height in which ball can move
                                             # leaving 100 pixel from the top side for showing buttons(pause, exit, retry, point) 

        self.pad_height = 60 # pad length
        self.pad1 = Pad(30, 300, self.pad_height//2, 8) # initializing left pad
        self.pad2 = Pad(870, 300, self.pad_height//2, 8) # initializing right pad
        self.pad_y_vel = 80  # pad vertical movement

        self.ball = Ball(self.width//2, self.height//2) # initializing the ball
        self.MAX_VEL = 10  # ball max velocity possible
        self.ball_x_vel = self.MAX_VEL * int(sample([1, -1], 1)[0])  # ball x direction velocity
        self.ball_y_vel = 0  # ball y direction velocity

        self.p1_point = 0   # player_1/left_pad point
        self.p2_point = 0   # player_2/right_pad point

        self.freeze = True     # tracking if the pause button is been pressed or not
        self.gameOver = False   # tracking if gameOver happened (if any of the paddle misses 3 ball this means gameover)
        self.winner = None      # after gameOver who is the winner

        pygame.init()
        pygame.mixer.init()
        self.boink_sound = pygame.mixer.Sound("./Sound/boink2.wav")  # sound when ball hits the pad
        self.gameover_sound = pygame.mixer.Sound("./Sound/heehee.mp3") # game over sound jardinains laughing
        self.pad_break_sound = pygame.mixer.Sound("./Sound/paddleBreak.wav") # paddle missing the incoming ball 
        self.hello_sound = pygame.mixer.Sound("./Sound/hello.mp3")  # game start sound
        self.boundary_sound = pygame.mixer.Sound("./Sound/twang.wav") # ball hits the boundary

        self.hello_sound.play()  # game starts so playing 

        self.prev_time = time.time()  # necessary for calculating time delta
        self.dt = 0      # necessary for calculating time delta
        self.fps = 30    # necessary for calculating time delta

    

    def calcDeltaTime(self):
        self.dt = time.time() - self.prev_time
        self.prev_time = time.time()
        self.dt *= self.fps


    def drawComponents(self):
        Line(250, 700, 250, 600, size=1)
        Line(380, 700, 380, 600, size=1)
        Line(510, 700, 510, 600, size=1)
        Line(650, 700, 650, 600, size=1)

        Line(0, self.upper_bound, self.width, self.upper_bound, size=2) # Boundary Line

        drawText(70, 645, f"Player_1: {self.p1_point:02}")
        drawText(720, 645, f"Player_2: {self.p2_point:02}")

        self.pad1.draw()
        self.pad2.draw()
        self.ball.draw()

        Arrow().draw()
        Pause().draw() if not self.freeze else Play().draw()
        Cross().draw()

        drawPauseText() if self.freeze and not self.gameOver else None
        drawGOText(winner=self.winner) if self.gameOver else None


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
        self.calcDeltaTime()
        self.drawComponents()
        self.checkBallBoundaryCollision()
        self.checkBallPadCollision()
        glutSwapBuffers()


    def checkBallPadCollision(self):
        if self.ball.x < -20 or self.ball.x > self.width+20:
            if self.ball.x < 0:
                if self.p2_point == 2:
                    self.gameOver = True
                    self.gameover_sound.play()
                    self.p2_point += 1
                    self.winner = 2
                else:
                    self.p2_point += 1
                    self.pad_break_sound.play()
                self.ball.reset(self.width//2+randint(10, 50), self.height//2+randint(20, 100))
                self.ball_x_vel *= 1
                self.ball_y_vel *= int(sample([1, -1], 1)[0])

            if self.ball.x > self.width:
                if self.p1_point == 2:
                    self.gameOver = True
                    self.gameover_sound.play()
                    self.p1_point += 1
                    self.winner = 1
                else:
                    self.p1_point += 1
                    self.pad_break_sound.play()
                self.ball.reset(self.width//2+randint(10, 50), self.height//2+randint(20, 100))
                self.ball_x_vel *= -1
                self.ball_y_vel *= int(sample([1, -1], 1)[0])

        if self.ball.y <= self.pad1.y+30 and self.ball.y >= self.pad1.y-30:
            if self.ball.x-8 <= self.pad1.x:
                self.boink_sound.play()
                self.ball_x_vel *= -1

                difference_in_y = self.pad1.y - self.ball.y
                reduction_factor = (self.pad_height/2)/self.MAX_VEL
                y_vel = difference_in_y / reduction_factor
                self.ball_y_vel = -1 * y_vel

        if self.ball.y <= self.pad2.y+30 and self.ball.y >= self.pad2.y-30:
            if self.ball.x+8 >= self.pad2.x:
                self.boink_sound.play()
                self.ball_x_vel *= -1

                difference_in_y = self.pad2.y - self.ball.y
                reduction_factor = (self.pad_height/2)/self.MAX_VEL
                y_vel = difference_in_y / reduction_factor
                self.ball_y_vel = -1 * y_vel


    def checkBallBoundaryCollision(self):
        if  self.ball.y+5 >= self.upper_bound:
            self.ball_y_vel *= -1
            self.boundary_sound.play()
        elif self.ball.y-5 <= 0:
            self.ball_y_vel *= -1
            self.boundary_sound.play()

        
    def resetEverything(self):
        self.p1_point = 0
        self.p2_point = 0
        self.ball.reset(self.width//2, self.height//2)
        self.pad1.reset(30, 300)
        self.pad2.reset(870, 300)
        self.gameOver = False
        self.ball_x_vel = self.MAX_VEL * int(sample([1, -1], 1)[0])
        self.ball_y_vel = 0
        self.hello_sound.play()


    def checkButton(self, x, y):
        if y <= self.height and y >= self.upper_bound:
            if x >= 250 and x <= 380:
                self.resetEverything()
            elif x >= 380 and x <= 510:
                self.freeze = True if not self.freeze else False
            elif x >= 510 and x <= 650:
                subprocess.Popen(["python", "main.py"])
                glutLeaveMainLoop()

    def animate(self):
        if not self.freeze and not self.gameOver:
            self.ball.x += self.ball_x_vel * self.dt
            self.ball.y += self.ball_y_vel * self.dt
        glutPostRedisplay()


    def keyboardListener(self, key, x, y):
        if key == b" ":
            self.freeze = True if not self.freeze else False
            
        if not self.freeze and not self.gameOver:
            if key == b"w":
                if not self.pad1.y >= self.upper_bound-45:
                    self.pad1.y += self.pad_y_vel * self.dt
            if key == b"s":
                if not self.pad1.y <= 0+45:
                    self.pad1.y -= self.pad_y_vel * self.dt

        glutPostRedisplay()


    def mouseListener(self, button, state, x, y):
        if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
            self.checkButton(x, self.height-y)
        glutPostRedisplay()


    def specialKeyListener(self, key, x, y):
        if not self.freeze and not self.gameOver:
            if key == GLUT_KEY_UP:
                if not self.pad2.y >= self.upper_bound-45:
                    self.pad2.y += self.pad_y_vel * self.dt
            if key == GLUT_KEY_DOWN:
                if not self.pad2.y <= 0+45:
                    self.pad2.y -= self.pad_y_vel * self.dt
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
        glutMouseFunc(self.mouseListener)
        glutSpecialFunc(self.specialKeyListener)
        glutMainLoop()



if __name__ == "__main__":
    Game().run()


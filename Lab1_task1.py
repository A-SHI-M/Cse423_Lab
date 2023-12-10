from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import math
import random

W_Width, W_Height = 500,500


ballx = bally = 0
speed = 0.01
ball_size = 2
create_new = False


class point:
    def __init__(self):
        self.x=0
        self.y=0
        self.z=0


def crossProduct(a, b):
    result=point()
    result.x = a.y * b.z - a.z * b.y
    result.y = a.z * b.x - a.x * b.z
    result.z = a.x * b.y - a.y * b.x

    return result

def convert_coordinate(x,y):
    global W_Width, W_Height
    a = x - (W_Width/2)
    b = (W_Height/2) - y 
    return a,b

def draw_points(x, y, s):
    glPointSize(s) #pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glVertex2f(x,y) #jekhane show korbe pixel
    glEnd()

def drawAxes():
    glLineWidth(1)
    glBegin(GL_LINES)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(250,0)
    glVertex2f(-250,0)
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(0,250)
    glVertex2f(0,-250)
    glEnd()

    glPointSize(5)
    glBegin(GL_POINTS)
    glColor3f(0, 1.0, 0.0)
    glVertex2f(0,0)
 
    glEnd()


def drawShapes():
    glBegin(GL_TRIANGLES)
    glVertex2d(-170,170)
    glColor3f(0, 1.0, 0.0)
    glVertex2d(-180,150)
    glColor3f(1,0, 0.0)
    glVertex2d(-160,150)
    glEnd()

    glBegin(GL_QUADS)
    glVertex2d(-170,120)
    glColor3f(1,0, 1)
    glVertex2d(-150,120)
    glColor3f(0,0, 1)
    glVertex2d(-150,140)
    glColor3f(0,1,0)
    glVertex2d(-170,140)
    glEnd()

def drawHouse():
    glBegin(GL_TRIANGLES)
    glColor3f(0.5,0.5, 1)
    glVertex2d(0,20)
    glVertex2d(-100,-50)
    glVertex2d(100,-50)
    glEnd()

    glLineWidth(3)
    glBegin(GL_LINES)
    glColor3f(0.5,0.5, 1)
    glVertex2f(-90,-50)
    glVertex2f(-90,-200)
    
    glVertex2f(-90,-199)
    glVertex2f(90,-199)

    glVertex2f(90,-200)
    glVertex2f(90,-50)

    glVertex2f(-65,-200)
    glVertex2f(-65,-100)

    glVertex2f(-40,-200)
    glVertex2f(-40,-100)

    glVertex2f(-65,-101)
    glVertex2f(-40, -101)

    glVertex2f(65,-140)
    glVertex2f(65,-100)

    glVertex2f(40,-140)
    glVertex2f(40,-100)
    
    glVertex2f(52.5,-140)
    glVertex2f(52.5,-100)
    
    glVertex2f(40,-139)
    glVertex2f(65,-139)

    glVertex2f(40,-101)
    glVertex2f(65,-101)

    glVertex2f(40,-120)
    glVertex2f(65,-120)
    glEnd()

    draw_points(-45, -150 , 5)

    





r, g, b, a = 0, 0, 0, 0
def keyboardListener(key, x, y):

    global r, g, b, a
    if key==b'd':
        r += 0.1
        g += 0.1
        b += 0.1
        a += 0.1
        print("Night to Day")
    if key==b'n':
        r -= 0.1
        g -= 0.1
        b -= 0.1
        a -= 0.1
        print("Day to Night")
    # if key==b's':
    #    print(3)
    # if key==b'd':
    #     print(4)

    glutPostRedisplay()
left = False
right = False
straight = True
def specialKeyListener(key, x, y):
    global rainPoints, left, right, straight
    if key=='w':
        print(1)
    if key==GLUT_KEY_LEFT:
        if straight == True:
            left = True
            straight = False
            for i in rainPoints:
                i[2] -= i[1]-i[3]
            print("Left")
        elif right == True:
            straight = True
            right = False
            for i in rainPoints:
                i[2] -= i[1]-i[3]
            print('Straight')
        elif left == True:
            print('Already Left')
    if key== GLUT_KEY_RIGHT:		#// up arrow key
        if left == True:
            straight = True
            left = False
            for i in rainPoints:
                i[2] += i[1]-i[3]
            print('Straight')
        elif straight == True:
            right = True
            straight = False
            for i in rainPoints:
                i[2] += i[1]-i[3]
            print('Right')
        elif right == True:
            print('Already Right')
    print(left, straight, right)
    glutPostRedisplay()

def mouseListener(button, state, x, y):	#/#/x, y is the x-y of the screen (2D)
    global ballx, bally, create_new
    if button==GLUT_LEFT_BUTTON:
        if(state == GLUT_DOWN):    # 		// 2 times?? in ONE click? -- solution is checking DOWN or UP
            
            c_X, c_y = convert_coordinate(x,y)
            ballx, bally = c_X, c_y
            print(ballx,bally)
        
    if button==GLUT_RIGHT_BUTTON:
        if state == GLUT_DOWN: 	
            create_new = convert_coordinate(x,y)
    glutPostRedisplay()

rainPoints = []

for x in range(-500, 500, 10):
    y1 = 250 + random.randrange(10,30)
    y2 = y1-random.randrange(10, 30)
    while True:
        rainPoints += [[x, y1, x, y2]]
        y1 = y2 - 20
        y2 = y1-random.randrange(10, 30)
        if y2 <= -50:
            break
            


def display():
    global r, g, b, a, rainPoints
    #//clear the display
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(r, g, b, a);	#//color black
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    #//load the correct matrix -- MODEL-VIEW matrix
    glMatrixMode(GL_MODELVIEW)
    #//initialize the matrix
    glLoadIdentity()
    #//now give three info
    #//1. where is the camera (viewer)?
    #//2. where is the camera looking?
    #//3. Which direction is the camera's UP direction?
    gluLookAt(0,0,200,	0,0,0,	0,1,0)
    glMatrixMode(GL_MODELVIEW)
    drawHouse()
    glLineWidth(1)
    glBegin(GL_LINES)
    for i in rainPoints:
        glVertex2f(i[0], i[1])
        glVertex2f(i[2], i[3])
    glEnd()
    
    

    

    if(create_new):
        m,n = create_new
        glBegin(GL_POINTS)
        glColor3f(0.7, 0.8, 0.6)
        glVertex2f(m,n)
        glEnd()


    glutSwapBuffers()


def animate():
    #//codes for any changes in Models, Camera
    glutPostRedisplay()
    global ballx, bally,speed, rainPoints, left, right, straight

    for i in range(len(rainPoints)):
        if rainPoints[i][1] >= -20:
            if straight == True:
                rainPoints[i][1] -= 0.1
                rainPoints[i][3] -= 0.1
            if left == True:
                rainPoints[i][0] -= 0.1
                rainPoints[i][1] -= 0.1
                rainPoints[i][2] -= 0.1
                rainPoints[i][3] -= 0.1
            if right == True:
                rainPoints[i][0] += 0.1
                rainPoints[i][1] -= 0.1
                rainPoints[i][2] += 0.1
                rainPoints[i][3] -= 0.1
        else:
            if straight == True:
                rainPoints[i][1] += 300
                rainPoints[i][3] += 300
            if left == True:
                rainPoints[i][0] += 300
                rainPoints[i][1] += 300
                rainPoints[i][2] += 300
                rainPoints[i][3] += 300
            if right == True:
                rainPoints[i][0] -= 300
                rainPoints[i][1] += 300
                rainPoints[i][2] -= 300
                rainPoints[i][3] += 300


   

    
    

def init():
    #//clear the screen
    glClearColor(0,0,0,0)
    #//load the PROJECTION matrix
    glMatrixMode(GL_PROJECTION)
    #//initialize the matrix
    glLoadIdentity()
    #//give PERSPECTIVE parameters
    gluPerspective(104,	1,	1,	1000.0)
    # **(important)**aspect ratio that determines the field of view in the X direction (horizontally). The bigger this angle is, the more you can see of the world - but at the same time, the objects you can see will become smaller.
    #//near distance
    #//far distance


glutInit()
glutInitWindowSize(W_Width, W_Height)
glutInitWindowPosition(0, 0)
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB) #	//Depth, Double buffer, RGB color

# glutCreateWindow("My OpenGL Program")
wind = glutCreateWindow(b"OpenGL Coding Practice")
init()

glutDisplayFunc(display)	#display callback function
glutIdleFunc(animate)	#what you want to do in the idle time (when no drawing is occuring)

glutKeyboardFunc(keyboardListener)
glutSpecialFunc(specialKeyListener)
glutMouseFunc(mouseListener)
glutMainLoop()		#The main loop of OpenGL

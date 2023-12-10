from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import math, random

W_Width, W_Height = 500,500


ballx = bally = 0
speed = 0.01
ball_size = 4
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

pause = False
def keyboardListener(key, x, y):

    global ball_size, pause
    if pause != True:
        if key==b'w':
            ball_size+=1
            print("Size Increased")
        if key==b's':
            ball_size-=1
            print("Size Decreased")
    if key==b' ':
        if pause == True:
            pause = False
        else:
            pause = True
    # if key==b's':
    #    print(3)
    # if key==b'd':
    #     print(4)

    glutPostRedisplay()

def specialKeyListener(key, x, y):
    global speed, pause
    if pause != True:
        if key=='w':
            print(1)
        if key==GLUT_KEY_UP:
            speed *= 2
            print("Speed Increased")
        if key== GLUT_KEY_DOWN:		#// up arrow key
            speed /= 2
            print("Speed Decreased")
    glutPostRedisplay()
    # if key==GLUT_KEY_RIGHT:
        
    # if key==GLUT_KEY_LEFT:
        

    # if key==GLUT_KEY_PAGE_UP:
       
    # if key==GLUT_KEY_PAGE_DOWN:
        
    # case GLUT_KEY_INSERT:
    #   
    #
    # case GLUT_KEY_HOME:
    #     
    # case GLUT_KEY_END:
    #   

balls = []
yessball = False
allBallColor = []
def mouseListener(button, state, x, y):	#/#/x, y is the x-y of the screen (2D)
    global ballx, bally, create_new, yessball, balls, allBallColor, pause
    if pause != True:
        if button==GLUT_LEFT_BUTTON:
            if(state == GLUT_DOWN):    # 		// 2 times?? in ONE click? -- solution is checking DOWN or UP
                for i in balls:
                    i[2] = [0,0,0]
            if (state == GLUT_UP):
                for i in range(len(balls)):
                    balls[i][2] = allBallColor[i]
        if button==GLUT_RIGHT_BUTTON:
            if state == GLUT_DOWN:
                yessball = True	
                ballx, bally = convert_coordinate(x,y)
                if ballx >= 0 and ballx <= 180 and bally >= 0 and bally <= 180:
                    ballcolor = [random.random(), random.random(), random.random()]
                    allBallColor += [ballcolor]
                    direction = [random.choice('+-'), random.choice('+-')]
                    balls += [[ballx, bally, ballcolor, direction]]
                
    # case GLUT_MIDDLE_BUTTON:
    #     //........

    glutPostRedisplay()

def display():
    #//clear the display
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0,0,0,0);	#//color black
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

    #drawAxes() 
    global ballx, bally, ball_size, balls
    for i in balls:
        glColor3f(i[2][0], i[2][1], i[2][2])
        draw_points(i[0], i[1], ball_size)
        

    #draw_points(ballx, bally, ball_size)
    #drawShapes()
    glColor3f(0,0,1)
    glLineWidth(4)
    glBegin(GL_LINES)
    glVertex2d(180,0)
    glVertex2d(180,180)
    glVertex2d(180,180)
    glVertex2d(0,180)
    glVertex2d(0,180)
    glVertex2d(0,0)
    glVertex2d(0,0)
    glVertex2d(180,0)

    glEnd()

    if(create_new):
        m,n = create_new
        glBegin(GL_POINTS)
        glColor3f(0.7, 0.8, 0.6)
        glVertex2f(m,n)
        glEnd()
    glutSwapBuffers()

notation = ['+', '+']
def animate():
    #//codes for any changes in Models, Camera
    glutPostRedisplay()
    global balls, speed
    for i in range(len(balls)):
        if balls[i][0] < 180 and balls[i][1] >= 180:
            balls[i][3][1] = '-'
        if balls[i][0] >= 180 and balls[i][1] < 180:
            balls[i][3][0] = '-'
        if balls[i][0] > 0 and balls[i][1] <= 0:
            balls[i][3][1] = '+'
        if balls[i][0] <= 0 and balls[i][1] > 0:
            balls[i][3][0] = '+'
        if balls[i][0] >= 180 and balls[i][1] >= 180:
            balls[i][3][0] = '-'
            balls[i][3][1] = '-'
        if balls[i][0] <= 0 and balls[i][1] <= 0:
            balls[i][3][0] = '+'
            balls[i][3][1] = '+'
        if balls[i][0] <= 0 and balls[i][1] >= 180:
            balls[i][3][0] = '+'
            balls[i][3][1] = '-'
        if balls[i][0] >= 180 and balls[i][1] <= 0:
            balls[i][3][0] = '-'
            balls[i][3][1] = '+'
        if pause != True:
            if balls[i][3][0] == '+':
                balls[i][0] += speed
            else: 
                balls[i][0] -= speed
            if balls[i][3][1] == '+':
                balls[i][1] += speed
            else:
                balls[i][1] -= speed
    #print(ballx,bally)

    



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

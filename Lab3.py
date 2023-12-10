from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math


W_Width, W_Height = 500,500
ballx = bally = 0
speed = 0.02
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


def circle():
    global centers
    for p in range(len(centers)):
        #c_x, c_y, radius = centers[p][0], centers[p][1], centers[p][2]
        c_x, c_y, radius = centers[p]
        d_init = 1 - radius
        x, y, d = 0, radius, d_init
        pixels = []
        while True:
            pixels += [[x, y]]
            if d < 0:
                direc = 'E'
            else:
                direc = 'SE'
            if direc == 'E':
                d = d + 2*x + 3
                x += 1
            elif direc == 'SE':
                d = d + 2*x - 2*y + 5
                x += 1
                y -= 1
            if x > y:
                break
        circle_points = []
        for x, y in pixels:
            circle_points += [[c_x+x, c_y+y], [c_x+y, c_y+x], [c_x+y, c_y-x], [c_x+x, c_y-y], 
                       [c_x-x, c_y-y], [c_x-y, c_y-x], [c_x-y, c_y+x], [c_x-x, c_y+y]]
        count = 0
        while True:
            x, y = circle_points[count][0], circle_points[count][1]
            if x >= -250 and x <= 250 and y >= -250 and y <= 250:
                draw = True
            else:
                draw = False
                break
            count += 1
            if count == len(circle_points):
                break
        glColor(1,0,0)
        if draw == True:
            for x, y in circle_points:
                draw_points(x, y, 3)


pause = False
def keyboardListener(key, x, y):
    global ball_size, pause
    if key==b'w':
        ball_size+=1
        print("Size Increased")
    if key==b's':
        ball_size-=1
        print("Size Decreased")
    if key==b' ':
        if pause == False:
            pause = True
        else:
            pause = False
    # if key==b's':
    #    print(3)
    # if key==b'd':
    #     print(4)

    glutPostRedisplay()

def specialKeyListener(key, x, y):
    global speed
    if key=='w':
        print(1)
    if key==GLUT_KEY_LEFT:
        speed *= 2
        print("Speed Increased")
    if key== GLUT_KEY_RIGHT:		#// up arrow key
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

centers = []
def mouseListener(button, state, x, y):	#/#/x, y is the x-y of the screen (2D)
    global centers
    if button==GLUT_LEFT_BUTTON:
        if(state == GLUT_DOWN):    # 		// 2 times?? in ONE click? -- solution is checking DOWN or UP
            pass
            
        
    if button==GLUT_RIGHT_BUTTON:
        if state == GLUT_DOWN: 	
            c_x, c_y = convert_coordinate(x,y)
            print(x, y)
            if pause == False:
                centers += [[c_x, c_y, 25]]
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
    global centers
    if len(centers) != 0:
        circle()

    

    

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
    global centers, speed
    for i in centers:
        if pause == False:
            i[2] += speed
    

def init():
    #//clear the screen
    glClearColor(0,0,0,0)
    #//load the PROJECTION matrix
    glMatrixMode(GL_PROJECTION)
    #//initialize the matrix
    glLoadIdentity()
    #//give PERSPECTIVE parameters
    gluPerspective(104,	1,	1,	1000.0)
    # **(important)**aspect ratio that determines the field of view in the X direction (horizontally). 
    # The bigger this angle is, the more you can see of the world - but at the same time, 
    # the objects you can see will become smaller.
    #//near distance
    #//far distance


glutInit()
glutInitWindowSize(W_Width, W_Height)
glutInitWindowPosition(450, 0)
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB) #	//Depth, Double buffer, RGB color

# glutCreateWindow("My OpenGL Program")
wind = glutCreateWindow(b"Assignment-3 - Circle - 20201042")
init()

glutDisplayFunc(display)	#display callback function
glutIdleFunc(animate)	#what you want to do in the idle time (when no drawing is occuring)

glutKeyboardFunc(keyboardListener)
glutSpecialFunc(specialKeyListener)
glutMouseFunc(mouseListener)

glutMainLoop()		#The main loop of OpenGL

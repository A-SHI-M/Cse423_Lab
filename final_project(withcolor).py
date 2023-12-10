from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

player = None
import math
import time
import random 
game_over = False
start_time1 = time.time()
start_time2 = time.time()+3

tor_time1 = time.time()-2
tor_time2 = time.time()-2

W_Width, W_Height = 1366,768

speed_rain = 0.2
speed_sub = 6
speed_sub1 = 4.5
submarines = []
bubbles = []

speed_rad = 0.015
torpedo1 = []
torpedo2 = []
speed_tor = 4.5

class torpedo:
    def __init__(self,list1,x,y):
        self.body = {"bp1":list1[0],'bp2':list1[1],'bp3':list1[2],'bp4':list1[3],'bp5':list1[4]}
        self.p1 = [list1[1][0],list1[4][1]]
        self.inc_x = x
        self.inc_y = y
        self.active = True

def draw_torpedo1():
    global torpedo1
    for tor in torpedo1:
        if tor.active == True:

            color = (0.0, 0.0, 0.0)
            draw_filled_polygon([(tor.body["bp1"][0],tor.body["bp1"][1]),
                               (tor.body["bp2"][0],tor.body["bp2"][1]),
                              (tor.body["bp3"][0],tor.body["bp3"][1]),
                              (tor.body["bp4"][0],tor.body["bp4"][1])], color)
            color = (2.0, 1.0, 0.0)
            draw_filled_polygon([(tor.body["bp4"][0],tor.body["bp4"][1]),
                                 (tor.body["bp5"][0],tor.body["bp5"][1]),
                                 (tor.body["bp1"][0],tor.body["bp1"][1])],color)

def draw_torpedo2():
    global torpedo2
    for tor in torpedo2:
        if tor.active == True:
            color = (0.0, 0.0, 0.0)
            draw_filled_polygon([(tor.body["bp1"][0],tor.body["bp1"][1]),
                               (tor.body["bp2"][0],tor.body["bp2"][1]),
                              (tor.body["bp3"][0],tor.body["bp3"][1]),
                              (tor.body["bp4"][0],tor.body["bp4"][1])], color)
            color = (2.0, 1.0, 0.0)
            draw_filled_polygon([(tor.body["bp4"][0],tor.body["bp4"][1]),
                                 (tor.body["bp5"][0],tor.body["bp5"][1]),
                                 (tor.body["bp1"][0],tor.body["bp1"][1])],color)


class bubble:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.rad = 10
        self.flag = True

class submarine:
    def __init__(self,list1,list2,list3,list4,list5,list6,circle1,circle2,num):
        self.num = num
        self.main_body = {"mp1":list1[0],"mp2":list1[1],"mp3":list1[2],"mp4":list1[3]}
        self.propeller = {'pp1':list2[0],'pp2':list2[1],'pp3':list2[2],'pp4':list2[3],'pp5':list2[4]}
        self.top_body = {"tp1":list3[0],"tp2":list3[1],"tp3":list3[2],"tp4":list3[3]}
        self.air_duct = {"ap1":list4[0],"ap2":list4[1],"ap3":list4[2],"ap4":list4[3]}
        self.door = {"dp1":list5[0],"dp2":list5[1],"dp3":list5[2],"dp4":list5[3]}
        self.lower_body =  {'lp1':list6[0],'lp2':list6[1],'lp3':list6[2],'lp4':list6[3],'lp5':list6[4]}
        self.circle1 = circle1
        self.circle2 = circle2
        self.gear = False
        self.control = True
        self.life = 3

#submarine 11 :
list1 = [[-530,180],[-630,180],[-630,130],[-530,130]]
list2 = [[-660,165],[-680,165],[-680,145],[-660,145],[-655,155]]
list3 = [[-550,200],[-580,200],[-610,180],[-550,180]]
list4 = [[-560,215],[-570,215],[-570,200],[-560,200]]
list5 = [[-540,165],[-560,165],[-560,145],[-540,145]]
list6 = [[-570,130],[-610,130],[-610,115],[-570,115],[-555,122.5]]
circle1 = [-580,155]
circle2 = [-615,155]

sub11 = submarine(list1,list2,list3,list4,list5,list6,circle1,circle2,1)
submarines.append(sub11)

#submarine 22 :
list11 = [[530,180],[630,180],[630,130],[530,130]]
list22 = [[660,165],[680,165],[680,145],[660,145],[655,155]]
list33 = [[550,200],[580,200],[610,180],[550,180]]
list44 = [[560,215],[570,215],[570,200],[560,200]]
list55 = [[540,165],[560,165],[560,145],[540,145]]
list66 = [[570,130],[610,130],[610,115],[570,115],[555,122.5]]
circle11 = [580,155]
circle22 = [615,155]

sub22 = submarine(list11,list22,list33,list44,list55,list66,circle11,circle22,2)
submarines.append(sub22)



class rain:
    def __init__(self,x,y):
        self.x1 =  x
        self.y1 = y
        self.x2 = x
        self.y2 = y+15

rains = []
def draw_rain():
    global rains
    for j in range(len(rains)):
        for k in rains[j]:
            if -160 < k.x1 <130 :
                if 60 < k.x1 < 120:
                    pass
                elif k.y1 > 310:
                    draw_lines(k.x1,k.y1,k.x2,k.y2)                  
            else:
                draw_lines(k.x1,k.y1,k.x2,k.y2)


def rr(p,y):
    rain1 = []
    for j in range(p):
        x = random.uniform(-680,680)
        k = rain(x,y)
        rain1.append(k)
    return rain1

rain1 = rr(40,380)
rain2 = rr(30,405)
rain4 = rr(40,425)
rain5 = rr(40,450)
rain3 = rr(25,480)
rains.append(rain1)
rains.append(rain2)
rains.append(rain4)
rains.append(rain5)
rains.append(rain3)


def draw_bubble():
    global bubbles
    for i in bubbles:
        if i.flag == True:
            points = circle_maker(i.rad)
            all_points = zone_converter(i.x,i.y,points)
            for j in all_points[1]:
                if j[1] > 230 :
                    i.flag = False
            for j in all_points:
                for k in j:
                    draw_points(k[0],k[1],2)

def draw_submarine(submarines):
    for sub in submarines:

        points = circle_maker(25)
        px1 = sub.main_body["mp1"][0]
        py1 = (sub.main_body['mp1'][1] +  sub.main_body['mp4'][1])/2
        px2 = sub.main_body['mp2'][0]
        py2 = (sub.main_body['mp2'][1] +  sub.main_body['mp3'][1])/2

        color = (0.0, 0.5, 0.0)
        draw_filled_circle(color, (px1, py1), 25, 32)
        draw_filled_circle(color, (px2, py2), 25, 32)


        color = (0.541, 0.247, 0.169)
        draw_filled_polygon([(sub.main_body["mp1"][0], sub.main_body["mp1"][1]),
                             (sub.main_body["mp2"][0], sub.main_body["mp2"][1]),
                              (sub.main_body["mp3"][0], sub.main_body["mp3"][1]),
                              (sub.main_body["mp4"][0], sub.main_body["mp4"][1])], color)
        

        color =(0.804, 0.522, 0.247) 
        draw_filled_polygon([(sub.top_body["tp1"][0], sub.top_body["tp1"][1]), 
                             (sub.top_body["tp2"][0], sub.top_body["tp2"][1]),
                             (sub.top_body["tp3"][0], sub.top_body["tp3"][1]), 
                             (sub.top_body["tp4"][0], sub.top_body["tp4"][1])], color)


        color =  (0.0, 0.0, 0.0) 
        draw_filled_polygon([(sub.propeller["pp1"][0], sub.propeller["pp1"][1]), 
                             (sub.propeller["pp2"][0], sub.propeller["pp2"][1]),
                             (sub.propeller["pp3"][0], sub.propeller["pp3"][1]), 
                             (sub.propeller["pp4"][0], sub.propeller["pp4"][1]),
                             (sub.propeller["pp5"][0], sub.propeller["pp5"][1])], color)


        color = (0.0, 0.0, 0.0)     
        draw_filled_polygon([(sub.air_duct["ap1"][0], sub.air_duct["ap1"][1]), 
                             (sub.air_duct["ap2"][0], sub.air_duct["ap2"][1]),
                             (sub.air_duct["ap3"][0], sub.air_duct["ap3"][1]), 
                             (sub.air_duct["ap4"][0], sub.air_duct["ap4"][1])], color)

    

        color = (0.0, 0.0, 0.0)
        draw_filled_polygon([(sub.lower_body["lp1"][0],sub.lower_body["lp1"][1]), 
                             (sub.lower_body["lp2"][0],sub.lower_body["lp2"][1]),
                             (sub.lower_body["lp3"][0],sub.lower_body["lp3"][1]), 
                             (sub.lower_body["lp4"][0],sub.lower_body["lp4"][1])], color)
        color = (2.0,1.0,0.0)
        draw_filled_polygon([(sub.lower_body["lp4"][0],sub.lower_body["lp4"][1]),
                             (sub.lower_body["lp5"][0],sub.lower_body["lp5"][1]),
                             (sub.lower_body["lp1"][0],sub.lower_body["lp1"][1])],color)


        color = (1.0, 0.843, 0.0)
        draw_filled_circle(color, (sub.circle1[0], sub.circle1[1]), 10, 32) #Drawing Full-Circle
        draw_filled_circle(color, (sub.circle2[0], sub.circle2[1]), 10, 32)  

        color = (0.8, 0.8, 0.8)
        draw_filled_polygon([(sub.door["dp1"][0], sub.door["dp1"][1]), 
                             (sub.door["dp2"][0], sub.door["dp2"][1]),
                             (sub.door["dp3"][0], sub.door["dp3"][1]), 
                             (sub.door["dp4"][0], sub.door["dp4"][1])], color)


def boatMaker():
    boatx = 80
    boaty = 233
    boat_x1, boat_x2 = -boatx, boatx
    boat_y1, boat_y2 = boaty, boaty

    color = (0.545, 0.396, 0.275)
    draw_filled_polygon([(boat_x1 , boat_y1), (boat_x2, boat_y2),(boat_x1 , boat_y1), (boat_x1-40, boat_y1+40),(boat_x1-40, boat_y1+40),(boat_x1-90,boat_y1+70),
                     (boat_x1-90, boat_y1+70),(boat_x1-87,boat_y1+75),(boat_x1-87, boat_y1+75),(boat_x1-40,boat_y1+55),(boat_x1-40, boat_y1+55),(boat_x1,boat_y1+55),
                     (boat_x1, boat_y1+55),(boat_x1+15,boat_y1+40),(boat_x1+15,boat_y1+40),(boat_x1+90,boat_y1+40),(boat_x1+90,boat_y1+40),(boat_x1+110,boat_y1+55),
                     (boat_x1+110,boat_y1+55),(boat_x1+180,boat_y1+55),(boat_x1+180,boat_y1+55),(boat_x1+180,boat_y1+30),(boat_x1+180,boat_y1+30),(boat_x2,boat_y2)],color)

    color = (1.0, 0.862, 0.345)
    draw_filled_polygon([(boatx-20, boaty+55), (boatx-20, boaty+140),(boatx-20, boaty+140), (boatx+40, boaty+70),(boatx+40, boaty+70), (boatx-10, boaty+70),
                     (boatx-10, boaty+70), (boatx-10, boaty+55),(59.0 , 288.0),(69.0 , 288.0)],color)
    
  
    color = (0.333, 0.420, 0.184)
    draw_filled_polygon([(boatx-108, boaty+40), (boatx-108, boaty+65),(boatx-70, boaty+40), (boatx-70, boaty+65),(boatx-108, boaty+65), (boatx-70, boaty+65),
                     (boatx-108, boaty+50), (boatx-154, boaty+77),(boatx-108, boaty+57), (boatx-150, boaty+82),(-74.0 , 309.0),(-69.0 , 315.0),(-29.0 , 273.0),
                     (9.0 , 274.0)],color)
    
    color =(0.0, 0.392, 0.0)
    circleMaker(-boatx+15,boaty+20, 10, color)
    circleMaker(-boatx+55,boaty+20, 10, color)
    circleMaker(-boatx+95,boaty+20, 10, color)
    circleMaker(-boatx+135,boaty+20, 10, color)

    color = (0,0,0)
    circleMaker(-boatx+2,boaty+83, 7, color)
    circleMaker(-boatx+2,boaty+83, 4, color)




    global bombs, bombN
    idx = 0
    for i in bombs:
        if -420 <= i[0] <= 420 and -318 <= i[1] <= -213:
            bombN[idx] = False
        else:
            if bombN[idx] == True:
                color = (1.0, 1.0, 0.0)
                circleMaker(i[0], i[1], 5, color)
                color = (0.0, 0.0, 0.0)
                circleMaker(i[0], i[1], 10, color)
        idx += 1


bombs = [[0,233], [0,233], [0,233], [0,233]]
bombN = [True, True, True, True]
def convert_coordinate(x,y):
    global W_Width, W_Height
    a = x - (W_Width/2)
    b = (W_Height/2) - y 
    return a,b


def draw_points(x, y, s):
    glPointSize(s) 
    glBegin(GL_POINTS)
    glColor4f(0.678, 0.847, 0.902, 0.5)
    glVertex2f(x,y) 
    glEnd()

def draw_lines(x,y,a,b):
    glPointSize(2)
    glBegin(GL_LINES)
    glColor3f(1.0,1.0,1.0)
    glVertex2f(x,y)
    glVertex2f(a,b)
    glEnd()

##---------------------Midpoint Line Algorithm---------------------------#
def MidPointLine(x1, y1, x2, y2):
    points = []
    dx = x2 - x1
    dy = y2 - y1
    d  = 2*dy - dx
    incE  = 2*dy
    incNE = 2*dy - 2*dx
    x = x1
    y = y1
    for i in range(x, x2+1):
        points += [[i, y]]
        if d > 0:
            d += incNE
            y += 1
        else:
            d += incE
    return points

def findZone(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    if dx>0 and dy>=0:
        if abs(dx) > abs(dy):
            return 0
        else:
            return 1
    elif dx<=0 and dy>=0:
        if abs(dx) > abs(dy):
            return 3
        else:
            return 2
    elif dx<0 and dy<0:
        if abs(dx) > abs(dy):
            return 4
        else:
            return 5
    elif dx>=0 and dy<0:
        if abs(dx) > abs(dy):
            return 7
        else:
            return 6
        
def convertToZone0(zone, x1, y1, x2, y2):
    if zone == 1:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
    elif zone == 2:
        x1, y1 = y1, -x1
        x2, y2 = y2, -x2
    elif zone == 3:
        x1, y1 = -x1, y1
        x2, y2 = -x2, y2
    elif zone == 4:
        x1, y1 = -x1, -y1
        x2, y2 = -x2, -y2
    elif zone == 5:
        x1, y1 = -y1, -x1
        x2, y2 = -y2, -x2
    elif zone == 6:
        x1, y1 = -y1, x1
        x2, y2 = -y2, x2
    elif zone == 7:
        x1, y1 = x1, -y1
        x2, y2 = x2, -y2
    return x1, y1, x2, y2


def convertToZoneM(color, zone, points):
    s = 2
    glColor3f(color[0], color[1], color[2])
    if zone ==0:
        for x, y in points:
            draw_points(x, y, s)
    elif zone == 1:
        for x, y in points:
            draw_points(y, x, s)
    elif zone == 2:
        for x, y in points:
            draw_points(-y, x, s)
    elif zone == 3:
        for x, y in points:
            draw_points(-x, y, s)
    elif zone == 4:
        for x, y in points:
            draw_points(-x, -y, s)
    elif zone == 5:
        for x, y in points:
            draw_points(-y, -x, s)
    elif zone == 6:
        for x, y in points:
            draw_points(y, -x, s)
    elif zone == 7:
        for x, y in points:
            draw_points(x, -y, s)

def drawLines(color, x1, y1, x2, y2):
    zone = findZone(x1, y1, x2, y2)
    x1, y1, x2, y2 = convertToZone0(zone, x1, y1, x2, y2)
    points = MidPointLine(x1, y1, x2, y2)
    convertToZoneM(color, zone, points)
#=========================================================================#

#---------------Midpoint Circle Algorithm---------------------------#
def circle_maker(rad):
    zone0 = []
    d_init = 1 - rad
    x_temp = 0
    while x_temp < rad :
        if d_init >= 0 :
            d_init = d_init + 2 * x_temp - 2* rad + 5 
            zone0.append((x_temp,rad))
            x_temp+=1
            rad -= 1
        else:
            d_init = d_init + 2 * x_temp +  3 
            zone0.append((x_temp,rad))
            x_temp+=1
    return zone0


def zone_converter(x,y,arr):
    all_points = [[],[],[],[],[],[],[],[]]
    for i in range(0,len(arr)):
        m = arr[i]
        for j in range(8):
            if j == 0 :
                all_points[j].append((m[1]+x,m[0]+y))
            elif j == 1:
                all_points[j].append((m[0]+x,m[1]+y))
            elif j == 2:
                all_points[j].append((-m[0]+x,m[1]+y))
            elif j == 3:
                all_points[j].append((-m[1]+x,m[0]+y))
            elif j == 4:
                all_points[j].append((-m[1]+x,-m[0]+y))
            elif j == 5:
                all_points[j].append((-m[0]+x,-m[1]+y))
            elif j == 6:
                all_points[j].append((m[0]+x,-m[1]+y))
            elif j == 7:
                all_points[j].append((m[1]+x,-m[0]+y))

    return all_points
#================================================================================#


def keyboardListener(key, x, y):
    global sub22,sub11, submarines, speed_sub, torpedo1, torpedo2, tor_time1, tor_time2,game_over,speed_sub1,speed_tor
    if key==b'o':
        if sub22.gear:
            sub22.gear = False
        else:
            sub22.gear = True
    if key==b's':
        if sub11.gear:
            sub11.gear = False
        else:
            sub11.gear = True
    if key == b'n':
        sub11.life = 0
        game_over = True
    if key == b'm':
        sub22.life = 0
        game_over = True

    if key == b'c':
        if game_over == False:
            m = sub22.circle1[0] - sub11.circle1[0] 
            n = sub22.circle1[1] - sub11.circle1[1] 
            n1 = (n/m)*speed_tor
            time_int1 = time.time() - tor_time1
            if time_int1 > 1.5:
                list1 = []
                for i in sub11.lower_body.keys():
                    k = sub11.lower_body[i]
                    list3 = [k[0],k[1]]
                    list1.append(list3)
                tor = torpedo(list1,speed_tor,n1)
                torpedo1.append(tor)
                tor_time1 = time.time()

    if key == b'p':
        if game_over == False:
            m = sub11.circle1[0] - sub22.circle1[0] 
            n = sub11.circle1[1] - sub22.circle1[1] 
            n1 = (n/m)*speed_tor
            time_int2 = time.time() - tor_time2
            if time_int2 > 1.5:
                list1 = []
                for i in sub22.lower_body.keys():
                    k = sub22.lower_body[i]
                    list3 = [k[0],k[1]]
                    list1.append(list3)
                tor = torpedo(list1,speed_tor,n1)
                torpedo2.append(tor)
                tor_time2 = time.time()

    if key==b'x':
        if game_over == False:
            for sub in submarines:
                if sub.num == 1:
                    if sub.control == True:
                        if sub.main_body['mp3'][1] > -320 :  
                            if sub.gear == False:
                                if -270<sub.main_body['mp3'][0]<250 and  sub.main_body['mp3'][1] < -240 :
                                    pass
                                else:
                                    for j in sub.main_body:
                                        sub.main_body[j][1] = sub.main_body[j][1]-speed_sub
                                    for j in sub.propeller:
                                        sub.propeller[j][1] = sub.propeller[j][1]-speed_sub
                                    for j in sub.top_body:
                                        sub.top_body[j][1] = sub.top_body[j][1]-speed_sub
                                    for j in sub.air_duct:
                                        sub.air_duct[j][1] = sub.air_duct[j][1]-speed_sub
                                    for j in sub.door:
                                        sub.door[j][1] = sub.door[j][1]-speed_sub
                                    for j in sub.lower_body:
                                        sub.lower_body[j][1] = sub.lower_body[j][1]-speed_sub                    
                                    sub.circle1 = [sub.circle1[0], sub.circle1[1]-speed_sub]
                                    sub.circle2 = [sub.circle2[0], sub.circle2[1]-speed_sub]
                            else:
                                if (sub.main_body['mp3'][0] -50) > -680 and  ((sub.main_body['mp1'][1] +sub.main_body['mp3'][1]) / 2) <= 225 :              
                                    for j in sub.main_body:
                                        sub.main_body[j][1] = sub.main_body[j][1]+speed_sub1
                                        sub.main_body[j][0] = sub.main_body[j][0]-speed_sub1
                                    for j in sub.propeller:
                                        sub.propeller[j][1] = sub.propeller[j][1]+speed_sub1
                                        sub.propeller[j][0] = sub.propeller[j][0]-speed_sub1
                                    for j in sub.top_body:
                                        sub.top_body[j][1] = sub.top_body[j][1]+speed_sub1
                                        sub.top_body[j][0] = sub.top_body[j][0]-speed_sub1
                                    for j in sub.air_duct:
                                        sub.air_duct[j][1] = sub.air_duct[j][1]+speed_sub1
                                        sub.air_duct[j][0] = sub.air_duct[j][0]-speed_sub1
                                    for j in sub.door:
                                        sub.door[j][1] = sub.door[j][1]+speed_sub1
                                        sub.door[j][0] = sub.door[j][0]-speed_sub1
                                    for j in sub.lower_body:
                                        sub.lower_body[j][1] = sub.lower_body[j][1]+speed_sub1
                                        sub.lower_body[j][0] = sub.lower_body[j][0]-speed_sub1         

                                    sub.circle1 = [sub.circle1[0], sub.circle1[1]+speed_sub1]
                                    sub.circle2 = [sub.circle2[0], sub.circle2[1]+speed_sub1]
                                    sub.circle1 = [sub.circle1[0]-speed_sub1, sub.circle1[1]]
                                    sub.circle2 = [sub.circle2[0]-speed_sub1, sub.circle2[1]]                          

    if key== b'f':
        if game_over == False:		
            for sub in submarines:
                if sub.num == 1:
                    if sub.control == True:
                        if ((sub.main_body['mp1'][1] +sub.main_body['mp3'][1]) / 2) <= 225:  
                            if sub.gear == False:
                                for j in sub.main_body:
                                    sub.main_body[j][1] = sub.main_body[j][1]+speed_sub
                                for j in sub.propeller:
                                    sub.propeller[j][1] = sub.propeller[j][1]+speed_sub
                                for j in sub.top_body:
                                    sub.top_body[j][1] = sub.top_body[j][1]+speed_sub
                                for j in sub.air_duct:
                                    sub.air_duct[j][1] = sub.air_duct[j][1]+speed_sub
                                for j in sub.door:
                                    sub.door[j][1] = sub.door[j][1]+speed_sub
                                for j in sub.lower_body:
                                    sub.lower_body[j][1] = sub.lower_body[j][1]+speed_sub
                                
                                sub.circle1 = [sub.circle1[0], sub.circle1[1]+speed_sub]
                                sub.circle2 = [sub.circle2[0], sub.circle2[1]+speed_sub]  
                            else:
                                if sub.main_body['mp1'][0] + 35 < 680: 
                                    for j in sub.main_body:
                                        sub.main_body[j][1] = sub.main_body[j][1]+speed_sub1
                                        sub.main_body[j][0] = sub.main_body[j][0]+speed_sub1
                                    for j in sub.propeller:
                                        sub.propeller[j][1] = sub.propeller[j][1]+speed_sub1
                                        sub.propeller[j][0] = sub.propeller[j][0]+speed_sub1
                                    for j in sub.top_body:
                                        sub.top_body[j][1] = sub.top_body[j][1]+speed_sub1
                                        sub.top_body[j][0] = sub.top_body[j][0]+speed_sub1
                                    for j in sub.air_duct:
                                        sub.air_duct[j][1] = sub.air_duct[j][1]+speed_sub1
                                        sub.air_duct[j][0] = sub.air_duct[j][0]+speed_sub1
                                    for j in sub.door:
                                        sub.door[j][1] = sub.door[j][1]+speed_sub1
                                        sub.door[j][0] = sub.door[j][0]+speed_sub1
                                    for j in sub.lower_body:
                                        sub.lower_body[j][1] = sub.lower_body[j][1]+speed_sub1
                                        sub.lower_body[j][0] = sub.lower_body[j][0]+speed_sub1    

                                    sub.circle1 = [sub.circle1[0], sub.circle1[1]+speed_sub1]
                                    sub.circle2 = [sub.circle2[0], sub.circle2[1]+speed_sub1]
                                    sub.circle1 = [sub.circle1[0]+speed_sub1, sub.circle1[1]]
                                    sub.circle2 = [sub.circle2[0]+speed_sub1, sub.circle2[1]]
                
    if key==b'g':
        if game_over == False:
            for sub in submarines:
                if sub.num == 1:
                    if sub.control == True:
                        if sub.main_body['mp1'][0] + 35 < 680:  
                            if sub.gear == False:
                                if sub.main_body['mp3'][1] < -240:
                                    pass
                                else:
                                    for j in sub.main_body:
                                        sub.main_body[j][0] = sub.main_body[j][0]+speed_sub
                                    for j in sub.propeller:
                                        sub.propeller[j][0] = sub.propeller[j][0]+speed_sub
                                    for j in sub.top_body:
                                        sub.top_body[j][0] = sub.top_body[j][0]+speed_sub
                                    for j in sub.air_duct:
                                        sub.air_duct[j][0] = sub.air_duct[j][0]+speed_sub
                                    for j in sub.door:
                                        sub.door[j][0] = sub.door[j][0]+speed_sub
                                    for j in sub.lower_body:
                                        sub.lower_body[j][0] = sub.lower_body[j][0]+speed_sub      

                                    sub.circle1 = [sub.circle1[0]+speed_sub, sub.circle1[1]]
                                    sub.circle2 = [sub.circle2[0]+speed_sub, sub.circle2[1]]
                            else:
                                if sub.main_body['mp3'][1] > -320 :  
                                    for j in sub.main_body:
                                        sub.main_body[j][1] = sub.main_body[j][1]-speed_sub1
                                        sub.main_body[j][0] = sub.main_body[j][0]+speed_sub1
                                    for j in sub.propeller:
                                        sub.propeller[j][1] = sub.propeller[j][1]-speed_sub1
                                        sub.propeller[j][0] = sub.propeller[j][0]+speed_sub1
                                    for j in sub.top_body:
                                        sub.top_body[j][1] = sub.top_body[j][1]-speed_sub1
                                        sub.top_body[j][0] = sub.top_body[j][0]+speed_sub1
                                    for j in sub.air_duct:
                                        sub.air_duct[j][1] = sub.air_duct[j][1]-speed_sub1
                                        sub.air_duct[j][0] = sub.air_duct[j][0]+speed_sub1
                                    for j in sub.door:
                                        sub.door[j][1] = sub.door[j][1]-speed_sub1
                                        sub.door[j][0] = sub.door[j][0]+speed_sub1
                                    for j in sub.lower_body:
                                        sub.lower_body[j][1] = sub.lower_body[j][1]-speed_sub1
                                        sub.lower_body[j][0] = sub.lower_body[j][0]+speed_sub1        

                                    sub.circle1 = [sub.circle1[0], sub.circle1[1]-speed_sub1]
                                    sub.circle2 = [sub.circle2[0], sub.circle2[1]-speed_sub1]
                                    sub.circle1 = [sub.circle1[0]+speed_sub1, sub.circle1[1]]
                                    sub.circle2 = [sub.circle2[0]+speed_sub1, sub.circle2[1]]  
    if key==b'a':
        if game_over == False:
            for sub in submarines:
                if sub.num == 1:
                    if sub.control == True:
                        if (sub.main_body['mp3'][0] -50) > -680:  
                            if sub.gear == False:
                                for j in sub.main_body:
                                    sub.main_body[j][0] = sub.main_body[j][0]-speed_sub
                                for j in sub.propeller:
                                    sub.propeller[j][0] = sub.propeller[j][0]-speed_sub
                                for j in sub.top_body:
                                    sub.top_body[j][0] = sub.top_body[j][0]-speed_sub
                                for j in sub.air_duct:
                                    sub.air_duct[j][0] = sub.air_duct[j][0]-speed_sub
                                for j in sub.door:
                                    sub.door[j][0] = sub.door[j][0]-speed_sub
                                for j in sub.lower_body:
                                    sub.lower_body[j][0] = sub.lower_body[j][0]-speed_sub        
                                sub.circle1 = [sub.circle1[0]-speed_sub, sub.circle1[1]]
                                sub.circle2 = [sub.circle2[0]-speed_sub, sub.circle2[1]]
                            else:
                                if sub.main_body['mp3'][1] > -320 :  
                                    for j in sub.main_body:
                                        sub.main_body[j][1] = sub.main_body[j][1]-speed_sub1
                                        sub.main_body[j][0] = sub.main_body[j][0]-speed_sub1
                                    for j in sub.propeller:
                                        sub.propeller[j][1] = sub.propeller[j][1]-speed_sub1
                                        sub.propeller[j][0] = sub.propeller[j][0]-speed_sub1
                                    for j in sub.top_body:
                                        sub.top_body[j][1] = sub.top_body[j][1]-speed_sub1
                                        sub.top_body[j][0] = sub.top_body[j][0]-speed_sub1
                                    for j in sub.air_duct:
                                        sub.air_duct[j][1] = sub.air_duct[j][1]-speed_sub1
                                        sub.air_duct[j][0] = sub.air_duct[j][0]-speed_sub1
                                    for j in sub.door:
                                        sub.door[j][1] = sub.door[j][1]-speed_sub1
                                        sub.door[j][0] = sub.door[j][0]-speed_sub1
                                    for j in sub.lower_body:
                                        sub.lower_body[j][1] = sub.lower_body[j][1]-speed_sub1
                                        sub.lower_body[j][0] = sub.lower_body[j][0]-speed_sub1   

                                    sub.circle1 = [sub.circle1[0], sub.circle1[1]-speed_sub1]
                                    sub.circle2 = [sub.circle2[0], sub.circle2[1]-speed_sub1]
                                    sub.circle1 = [sub.circle1[0]-speed_sub1, sub.circle1[1]]
                                    sub.circle2 = [sub.circle2[0]-speed_sub1, sub.circle2[1]]      

        glutPostRedisplay()

def specialKeyListener(key, x, y):
    global submarines, speed_sub, game_over
    if key==GLUT_KEY_UP:
        if game_over == False:
            for sub in submarines:
                if sub.num == 2:
                    if sub.control == True:
                        if ((sub.main_body['mp1'][1] +sub.main_body['mp3'][1]) / 2) <= 225:  
                            if sub.gear == False:
                                for j in sub.main_body:
                                    sub.main_body[j][1] = sub.main_body[j][1]+speed_sub
                                for j in sub.propeller:
                                    sub.propeller[j][1] = sub.propeller[j][1]+speed_sub
                                for j in sub.top_body:
                                    sub.top_body[j][1] = sub.top_body[j][1]+speed_sub
                                for j in sub.air_duct:
                                    sub.air_duct[j][1] = sub.air_duct[j][1]+speed_sub
                                for j in sub.door:
                                    sub.door[j][1] = sub.door[j][1]+speed_sub
                                for j in sub.lower_body:
                                    sub.lower_body[j][1] = sub.lower_body[j][1]+speed_sub
                                
                            
                                sub.circle1 = [sub.circle1[0], sub.circle1[1]+speed_sub]
                                sub.circle2 = [sub.circle2[0], sub.circle2[1]+speed_sub]
                            else:
                                if sub.main_body['mp1'][0] - 35 > -680: 
                                    for j in sub.main_body:
                                        sub.main_body[j][1] = sub.main_body[j][1]+speed_sub1
                                        sub.main_body[j][0] = sub.main_body[j][0]-speed_sub1
                                    for j in sub.propeller:
                                        sub.propeller[j][1] = sub.propeller[j][1]+speed_sub1
                                        sub.propeller[j][0] = sub.propeller[j][0]-speed_sub1
                                    for j in sub.top_body:
                                        sub.top_body[j][1] = sub.top_body[j][1]+speed_sub1
                                        sub.top_body[j][0] = sub.top_body[j][0]-speed_sub1
                                    for j in sub.air_duct:
                                        sub.air_duct[j][1] = sub.air_duct[j][1]+speed_sub1
                                        sub.air_duct[j][0] = sub.air_duct[j][0]-speed_sub1
                                    for j in sub.door:
                                        sub.door[j][1] = sub.door[j][1]+speed_sub1
                                        sub.door[j][0] = sub.door[j][0]-speed_sub1
                                    for j in sub.lower_body:
                                        sub.lower_body[j][1] = sub.lower_body[j][1]+speed_sub1
                                        sub.lower_body[j][0] = sub.lower_body[j][0]-speed_sub1  

                                    sub.circle1 = [sub.circle1[0], sub.circle1[1]+speed_sub1]
                                    sub.circle2 = [sub.circle2[0], sub.circle2[1]+speed_sub1]
                                    sub.circle1 = [sub.circle1[0]-speed_sub1, sub.circle1[1]]
                                    sub.circle2 = [sub.circle2[0]-speed_sub1, sub.circle2[1]]                          
    
    if key== GLUT_KEY_DOWN:		
        for sub in submarines:
            if game_over == False:
                    if sub.num == 2:
                        if sub.control == True:
                            if sub.main_body['mp3'][1] > -320 :  
                                if sub.gear == False:
                                    if -270<sub.main_body['mp3'][0]<250 and  sub.main_body['mp3'][1] < -240 :
                                        pass
                                    else:
                                        for j in sub.main_body:
                                            sub.main_body[j][1] = sub.main_body[j][1]-speed_sub
                                        for j in sub.propeller:
                                            sub.propeller[j][1] = sub.propeller[j][1]-speed_sub
                                        for j in sub.top_body:
                                            sub.top_body[j][1] = sub.top_body[j][1]-speed_sub
                                        for j in sub.air_duct:
                                            sub.air_duct[j][1] = sub.air_duct[j][1]-speed_sub
                                        for j in sub.door:
                                            sub.door[j][1] = sub.door[j][1]-speed_sub
                                        for j in sub.lower_body:
                                            sub.lower_body[j][1] = sub.lower_body[j][1]-speed_sub
                                        sub.circle1 = [sub.circle1[0], sub.circle1[1]-speed_sub]
                                        sub.circle2 = [sub.circle2[0], sub.circle2[1]-speed_sub]  
                                else:
                                    if (sub.main_body['mp3'][0] +50) < 680 and  ((sub.main_body['mp1'][1] +sub.main_body['mp3'][1]) / 2) <= 225 :   
                                        for j in sub.main_body:
                                            sub.main_body[j][1] = sub.main_body[j][1]+speed_sub1
                                            sub.main_body[j][0] = sub.main_body[j][0]+speed_sub1
                                        for j in sub.propeller:
                                            sub.propeller[j][1] = sub.propeller[j][1]+speed_sub1
                                            sub.propeller[j][0] = sub.propeller[j][0]+speed_sub1
                                        for j in sub.top_body:
                                            sub.top_body[j][1] = sub.top_body[j][1]+speed_sub1
                                            sub.top_body[j][0] = sub.top_body[j][0]+speed_sub1
                                        for j in sub.air_duct:
                                            sub.air_duct[j][1] = sub.air_duct[j][1]+speed_sub1
                                            sub.air_duct[j][0] = sub.air_duct[j][0]+speed_sub1
                                        for j in sub.door:
                                            sub.door[j][1] = sub.door[j][1]+speed_sub1
                                            sub.door[j][0] = sub.door[j][0]+speed_sub1
                                        for j in sub.lower_body:
                                            sub.lower_body[j][1] = sub.lower_body[j][1]+speed_sub1
                                            sub.lower_body[j][0] = sub.lower_body[j][0]+speed_sub1         

                                        sub.circle1 = [sub.circle1[0], sub.circle1[1]+speed_sub1]
                                        sub.circle2 = [sub.circle2[0], sub.circle2[1]+speed_sub1]
                                        sub.circle1 = [sub.circle1[0]+speed_sub1, sub.circle1[1]]
                                        sub.circle2 = [sub.circle2[0]+speed_sub1, sub.circle2[1]]
                    
    if key==GLUT_KEY_RIGHT:
        if game_over == False:
            for sub in submarines:
                if sub.num == 2:
                    if sub.control == True:
                        if sub.main_body['mp3'][0] + 50 < 680:  
                            if sub.gear == False:
                                for j in sub.main_body:
                                    sub.main_body[j][0] = sub.main_body[j][0]+speed_sub
                                for j in sub.propeller:
                                    sub.propeller[j][0] = sub.propeller[j][0]+speed_sub
                                for j in sub.top_body:
                                    sub.top_body[j][0] = sub.top_body[j][0]+speed_sub
                                for j in sub.air_duct:
                                    sub.air_duct[j][0] = sub.air_duct[j][0]+speed_sub
                                for j in sub.door:
                                    sub.door[j][0] = sub.door[j][0]+speed_sub
                                for j in sub.lower_body:
                                    sub.lower_body[j][0] = sub.lower_body[j][0]+speed_sub    
                                sub.circle1 = [sub.circle1[0]+speed_sub, sub.circle1[1]]
                                sub.circle2 = [sub.circle2[0]+speed_sub, sub.circle2[1]]
                            else:
                                if sub.main_body['mp3'][1] > -350 :  
                                    for j in sub.main_body:
                                        sub.main_body[j][1] = sub.main_body[j][1]-speed_sub1
                                        sub.main_body[j][0] = sub.main_body[j][0]+speed_sub1
                                    for j in sub.propeller:
                                        sub.propeller[j][1] = sub.propeller[j][1]-speed_sub1
                                        sub.propeller[j][0] = sub.propeller[j][0]+speed_sub1
                                    for j in sub.top_body:
                                        sub.top_body[j][1] = sub.top_body[j][1]-speed_sub1
                                        sub.top_body[j][0] = sub.top_body[j][0]+speed_sub1
                                    for j in sub.air_duct:
                                        sub.air_duct[j][1] = sub.air_duct[j][1]-speed_sub1
                                        sub.air_duct[j][0] = sub.air_duct[j][0]+speed_sub1
                                    for j in sub.door:
                                        sub.door[j][1] = sub.door[j][1]-speed_sub1
                                        sub.door[j][0] = sub.door[j][0]+speed_sub1
                                    for j in sub.lower_body:
                                        sub.lower_body[j][1] = sub.lower_body[j][1]-speed_sub1
                                        sub.lower_body[j][0] = sub.lower_body[j][0]+speed_sub1     
                                    sub.circle1 = [sub.circle1[0], sub.circle1[1]-speed_sub1]
                                    sub.circle2 = [sub.circle2[0], sub.circle2[1]-speed_sub1]
                                    sub.circle1 = [sub.circle1[0]+speed_sub1, sub.circle1[1]]
                                    sub.circle2 = [sub.circle2[0]+speed_sub1, sub.circle2[1]]  
    if key==GLUT_KEY_LEFT:
        if game_over == False:
            for sub in submarines:
                if sub.num == 2:
                    if sub.control == True:
                        if (sub.main_body['mp1'][0] -35) > -680:  
                            if sub.gear == False:
                                if sub.main_body['mp3'][1] < -240 and sub.main_body['mp3'][0] < 450:
                                    pass
                                else:
                                    for j in sub.main_body:
                                        sub.main_body[j][0] = sub.main_body[j][0]-speed_sub
                                    for j in sub.propeller:
                                        sub.propeller[j][0] = sub.propeller[j][0]-speed_sub
                                    for j in sub.top_body:
                                        sub.top_body[j][0] = sub.top_body[j][0]-speed_sub
                                    for j in sub.air_duct:
                                        sub.air_duct[j][0] = sub.air_duct[j][0]-speed_sub
                                    for j in sub.door:
                                        sub.door[j][0] = sub.door[j][0]-speed_sub
                                    for j in sub.lower_body:
                                        sub.lower_body[j][0] = sub.lower_body[j][0]-speed_sub   
                                    sub.circle1 = [sub.circle1[0]-speed_sub, sub.circle1[1]]
                                    sub.circle2 = [sub.circle2[0]-speed_sub, sub.circle2[1]]
                            else:
                                if sub.main_body['mp3'][1] > -320 :  
                                    for j in sub.main_body:
                                        sub.main_body[j][1] = sub.main_body[j][1]-speed_sub1
                                        sub.main_body[j][0] = sub.main_body[j][0]-speed_sub1
                                    for j in sub.propeller:
                                        sub.propeller[j][1] = sub.propeller[j][1]-speed_sub1
                                        sub.propeller[j][0] = sub.propeller[j][0]-speed_sub1
                                    for j in sub.top_body:
                                        sub.top_body[j][1] = sub.top_body[j][1]-speed_sub1
                                        sub.top_body[j][0] = sub.top_body[j][0]-speed_sub1
                                    for j in sub.air_duct:
                                        sub.air_duct[j][1] = sub.air_duct[j][1]-speed_sub1
                                        sub.air_duct[j][0] = sub.air_duct[j][0]-speed_sub1
                                    for j in sub.door:
                                        sub.door[j][1] = sub.door[j][1]-speed_sub1
                                        sub.door[j][0] = sub.door[j][0]-speed_sub1
                                    for j in sub.lower_body:
                                        sub.lower_body[j][1] = sub.lower_body[j][1]-speed_sub1
                                        sub.lower_body[j][0] = sub.lower_body[j][0]-speed_sub1      
                                    sub.circle1 = [sub.circle1[0], sub.circle1[1]-speed_sub1]
                                    sub.circle2 = [sub.circle2[0], sub.circle2[1]-speed_sub1]
                                    sub.circle1 = [sub.circle1[0]-speed_sub1, sub.circle1[1]]
                                    sub.circle2 = [sub.circle2[0]-speed_sub1, sub.circle2[1]]                    
    
    # if key==GLUT_KEY_PAGE_UP:
       
    # if key==GLUT_KEY_PAGE_DOWN:
        
    # case GLUT_KEY_INSERT:
    #   
    #
    # case GLUT_KEY_HOME:
    #     
    # case GLUT_KEY_END:
    #   
    glutPostRedisplay()

def draw_filled_polygon(vertices, color):
    glPointSize(2)
    glBegin(GL_POLYGON)
    glColor3f(*color) 
    for vertex in vertices:
        glVertex2f(*vertex) 
    glEnd()

def draw_filled_circle( color, center, radius, num_segments, start_angle=0, arc_length=2 * math.pi):
    end_angle = start_angle + arc_length
    angle_step = arc_length / num_segments
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(*color)
    for i in range(num_segments + 1):
        angle = start_angle + i * angle_step
        x = center[0] + math.cos(angle) * radius
        y = center[1] + math.sin(angle) * radius
        glVertex2f(x, y)

    glEnd()

def fill_color_circle(x,y,rad, color):
    triangle_amount = 20  
    two_pi = 2.0 * math.pi
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x, y)  
    glColor3f(*color)
    for i in range(triangle_amount + 1):
        glVertex2f(
            x + (rad * math.cos(i * two_pi / triangle_amount)),
            y + (rad * math.sin(i * two_pi / triangle_amount))
        )
    glEnd()


def circleMaker(x, y, rad, color):
    point = circle_maker(rad)
    allpoint = zone_converter(x, y, point)
    for i in allpoint:
        for j in i:
            draw_points(j[0], j[1], 1.2)
    fill_color_circle(x,y,rad, color)




def draw_titanic():
    #leftside
    color=(0.333, 0.333, 0.333)
    draw_filled_polygon([(-300, -318), (-100, -318), (-300, -318), (-370, -233),(-370, -233), (-300, -250), (-300, -250), 
                         (-100, -250), (-100, -250), (-120, -270), (-120, -270), (-80, -280), (-80, -280), (-110, -290), 
                         (-110, -290), (-100, -318)],color) #body
    #red color part start
    color=(0.647, 0.165, 0.165)
    draw_filled_polygon([(-287, -260), (-245, -260),(-287, -260), (-287, -250),(-245, -260), (-245, -250),(-283, -245), 
    (-249, -245),(-283, -245), (-283, -250),(-249, -245), (-249, -250),(-288.0 , -250.0),(-285.0 , -250.0),
    (-251.0 , -250.0),(-249.0 , -250.0)],color)
    color = (0.647, 0.165, 0.165)
    draw_filled_polygon([(-231, -260), (-189, -260),(-231, -260), (-231, -250),(-189, -260), (-189, -250),(-227, -245), (-227, -250),
    (-227, -245), (-193, -245),(-193, -245), (-193, -250),(-231.0 , -249.0), (-228.0 , -250.0), (-194.0 , -250.0), 
    (-190.0 , -250.0)],color)
    color = (0.647, 0.165, 0.165)
    draw_filled_polygon([(-175, -260), (-133, -260),(-175, -260), (-175, -250),(-133, -260), (-133, -250),(-171, -245), 
    (-171, -250),(-171, -245), (-137, -245),(-137, -245), (-137, -250),(-176.0 , -250.0),(-172.0 , -250.0),
    (-139.0 , -250.0),(-134.0 , -250.0)],color)
    color = (0.129, 0.141, 0.141)
    draw_filled_polygon([(-260, -245), (-260, -200),(-272, -245), (-272, -200),(-274.0 , -200.0),(-262.0 , -200.0),(-273.0 , -243.0),(-261.0 , -244.0)],color)
    
    draw_filled_polygon([(-216, -245), (-216, -200),(-204, -245), (-204, -200),(-218.0 , -199.0),(-206.0 , -200.0),(-217.0 , -244.0),(-205.0 , -243.0)],color)

    draw_filled_polygon([(-160, -245), (-160, -200),(-148, -245), (-148, -200),(-161.0 , -201.0),(-149.0 , -200.0),(-161.0 , -247.0),(-149.0 , -246.0)],color)

    draw_filled_polygon([(260, -245), (260, -200),(272, -245), (272, -200),(260.0 , -245.0),(271.0 , -245.0),(259.0 , -200.0),(270.0 , -199.0)],color)

    draw_filled_polygon([(216, -245), (216, -200),(204, -245), (204, -200),(203.0 , -245.0),(214.0 , -243.0),(203.0 , -200.0),(214.0 , -200.0)],color)

    draw_filled_polygon([(160, -245), (160, -200),(148, -245), (148, -200),(147.0 , -244.0),(159.0 , -243.0),(147.0 , -201.0),(159.0 , -200.0)],color)


    
    circleMaker(-267, -200, 6, color)
    circleMaker(-267, -289, 10, color)
    circleMaker(-211, -200, 6, color)
    circleMaker(-211, -289, 10, color)
    circleMaker(-155, -200, 6, color)
    circleMaker(-155, -289, 10, color)
    #red color part end


    #rightside
    color=(0.333, 0.333, 0.333)
    draw_filled_polygon([(300, -318), (100, -318),(300, -318), (370, -233),(370, -233), (300, -250),(300, -250), (100, -250),(100, -250), (120, -270),
                         (120, -270), (80, -280),(80, -280), (110, -290),(110, -290), (100, -318)],color)
    
    #red color part start
    color=(0.647, 0.165, 0.165)
    draw_filled_polygon([(287, -260),(245, -260),(287, -260), (287, -250),(245, -260), (245, -250),(283, -245), (249, -245),(283, -245), (283, -250),(249, -245),
                         (249, -250),(244.0 , -250.0),(247.0 , -250.0),(282.0 , -250.0),(286.0 , -249.0)],color)
    

    draw_filled_polygon([(231, -260), (189, -260),(231, -260), (231, -250),(189, -260), (189, -250),(227, -245), (227, -250),(227, -245), (193, -245),(193, -245),
                         (193, -250),(188.0 , -250.0),(192.0 , -249.0),(225.0 , -249.0),(230.0 , -250.0)],color)

    draw_filled_polygon([(175, -260), (133, -260),(175, -260), (175, -250),(133, -260), (133, -250),(171, -245), (171, -250),(171, -245),
                         (137, -245),(137, -245), (137, -250),(132.0 , -250.0),(135.0 , -249.0),(170.0 , -249.0),(173.0 , -249.0)],color)
    color = (0.129, 0.141, 0.141)
    circleMaker(265, -200, 6, color)
    circleMaker(265, -289, 10, color)
    circleMaker(209, -200, 6, color)
    circleMaker(209, -289, 10, color)
    circleMaker(153, -200, 6, color)
    circleMaker(153, -289, 10, color)
    #red color part end
  
    #-----Khajana------#
    color = (1.0, 1.0, 0.0)
    for i in range(-45, 46, 10):
        circleMaker(i, -290, 5, color)
    for i in range(-40, 41, 10):
        circleMaker(i, -280, 5, color)
    for i in range(-25, 26, 10):
        circleMaker(i, -270, 5, color)

    color=(0.647, 0.322, 0.176)
    draw_filled_polygon([(-30, -318), (30, -318),(-50, -290), (-30, -318),(50, -290), (30, -318),(-47.0 , -296.0),(45.0 , -296.0)],color)

def auto_fall(sub): 
    if  (sub.main_body['mp3'][1] > -300):
        for j in sub.main_body:
            sub.main_body[j][1] = sub.main_body[j][1]-0.3
        for j in sub.propeller:
            sub.propeller[j][1] = sub.propeller[j][1]-0.3
        for j in sub.top_body:
            sub.top_body[j][1] = sub.top_body[j][1]-0.3
        for j in sub.air_duct:
            sub.air_duct[j][1] = sub.air_duct[j][1]-0.3
        for j in sub.door:
            sub.door[j][1] = sub.door[j][1]-0.3
        for j in sub.lower_body:
            sub.lower_body[j][1] = sub.lower_body[j][1]-0.3
        sub.circle1 = [sub.circle1[0], sub.circle1[1]-0.3]
        sub.circle2 = [sub.circle2[0], sub.circle2[1]-0.3] 


def mouseListener(button, state, x, y):	#/#/x, y is the x-y of the screen (2D)
    if button==GLUT_LEFT_BUTTON:
        if(state == GLUT_DOWN):    # 		// 2 times?? in ONE click? -- solution is checking DOWN or UP
            #print(x,y)
            c_X, c_y = convert_coordinate(x,y)
            print(c_X, c_y)
            ballx, bally = c_X, c_y
        
    if button==GLUT_RIGHT_BUTTON:
        if state == GLUT_DOWN: 	
            create_new = convert_coordinate(x,y)
    # case GLUT_MIDDLE_BUTTON:
    #     //........

    glutPostRedisplay()

def render_text(text, x, y, font, color):
    glColor3f(color[0], color[1], color[2])
    glRasterPos2f(x, y)

    for char in text:
        glutBitmapCharacter(font, ord(char))

def display():
    global submarines , bubbles , player
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0,0,0,0);	
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-683, 683, -384, 384, -1, 1)


    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


    #main code

    color=(0.0, 0.5, 1.0)
    draw_filled_polygon([(-680 , 285.0), (680 , 285.0), (690 , -300.0), (-690 , -300.0)],color)

    color=(0.53, 0.81, 0.98)
    draw_filled_polygon([(-680, 230), (680, 230), (690, 380), (-690, 380)],color)


    color=(0.36, 0.25, 0.20)
    
    draw_filled_polygon([(685 ,-300), (-685 ,-300), (-685, -380), (685, -380)],color)



    color =(0.502, 0.6, 0.667)
    draw_filled_circle(color, (-392,350), 30, 32)
    draw_filled_circle(color, (-410.0, 337.0), 25, 32)
    draw_filled_circle(color, (-375.0 , 338.0), 25, 32)
    
    
    draw_filled_circle(color, (239.0 , 294.0), 35, 32)
    draw_filled_circle(color, (215.0 , 285.0), 25, 32)
    draw_filled_circle(color, (260.0 , 285.0), 25, 32)

    draw_filled_circle(color, (580.0 , 320.0), 35, 32)
    draw_filled_circle(color, (555.0 , 310.0), 25, 32)
    draw_filled_circle(color, (605.0 , 310.0), 25, 32)


    draw_filled_circle(color, (-680.0 , 290.0), 25, 32)
    draw_filled_circle(color, (-665.0 , 285.0), 19, 32)




    draw_submarine(submarines)
    
    draw_bubble()

    boatMaker()

    draw_rain()
    
    if game_over == False:
        draw_torpedo1()
        draw_torpedo2()

    draw_titanic()


    font = GLUT_BITMAP_TIMES_ROMAN_24
    text_color = (1.0, 0.7, 0.2)
     
    txt1 = "GAME OVER"
    txt2 = "LEFT SUBMARINE(MARKAVA) HAS WON THE GAME"
    txt3 = "RIGHT SUBMARINE(DESTROYER) HAS WON THE GAME"
    txt4 = 'NOBODY SUBMARINE HAS WON. RESULT : DRAW'
    txt5 = "Markava life : " + str(sub11.life)
    txt6 = "Destroyer life : " + str(sub22.life)
    render_text(txt5, -650, -360, font, text_color)
    render_text(txt6, 500, -360, font, text_color)    
    # if sub22.control == False:
    #     render_text(txt1, -100, 50, font, text_color)
    #     render_text(txt2, -280, -50, font, text_color)
    # elif sub11.control == False:
    #     render_text(txt1, -100, 50, font, text_color)
    #     render_text(txt3, -280, -50, font, text_color)

    text_color = (0.0, 0.0, 0.0)
    font = GLUT_BITMAP_TIMES_ROMAN_24
    if game_over:
        if player == 1:
            render_text(txt1, -100, 50, font, text_color)
            render_text(txt2, -280, -50, font, text_color)
        elif player == 2 :
            render_text(txt1, -100, 50, font, text_color)
            render_text(txt3, -280, -50, font, text_color)
        else:
            render_text(txt1, -100, 50, font, text_color)
            render_text(txt4, -280, -50, font, text_color)           
    glutSwapBuffers()


from math import tan, pi
theta = random.randrange(-10, 20)
bomb_left = [tan((225+theta)*(pi/180)), tan((225+theta+20)*(pi/180))]
bomb_right = [tan((315-theta)*(pi/180)), tan((315-theta-20)*(pi/180))]





def direction():
    global theta, bomb_left, bomb_right
    theta = random.randrange(-10, 16)
    bomb_left = [tan((225+theta)*(pi/180)), tan((225+theta+20)*(pi/180))]
    bomb_right = [tan((315-theta)*(pi/180)), tan((315-theta-20)*(pi/180))]


def animate():
    global bubbles, speed_rad, sub11, sub22, bubbles ,start_time1,start_time2, rains, speed_rain, torpedo1, torpedo2, speed_tor, game_over,player
    global bomb_left, bomb_right, bombs, bombN 
    if game_over == False:
        elapsed_time1 = time.time()-start_time1
        elapsed_time2 = time.time()- start_time2
        if elapsed_time1 > 2 :
            if sub11.control == True:
                x1 = (sub11.air_duct['ap1'][0]+sub11.air_duct['ap2'][0] ) / 2
                y1 = (sub11.air_duct['ap1'][1]+ 5)
                bub1 = bubble(x1,y1)
                bubbles.append(bub1)
                start_time1 = time.time()
        if elapsed_time2 > 2 :
            if sub22.control == True:
                x1 = (sub22.air_duct['ap1'][0]+sub22.air_duct['ap2'][0] ) / 2
                y1 = (sub22.air_duct['ap1'][1]+ 5)
                bub2 = bubble(x1,y1)
                bubbles.append(bub2)
                start_time2 = time.time()+3
        for i in bubbles:
            i.y += 0.3
            i.rad += speed_rad

        
        for j in range(len(rains)):
            for k in rains[j]:
                k.y1 -= speed_rain
                k.y2 -= speed_rain
                if k.y1 < 230:
                    if j == 0:
                        k.y1 = 380
                        k.y2 = 395
                    if j == 1:
                        k.y1 = 405
                        k.y2 = 420
                    if j == 2:
                        k.y1 = 425
                        k.y2 = 440
                    if j == 3:
                        k.y1 = 450
                        k.y2 = 465
                    if j== 4:
                        k.y1 = 470
                        k.y2 = 485



        if sub11.control == False:
            auto_fall(sub11)
        if sub22.control == False:
            auto_fall(sub22)

        for tor in torpedo1:
            if tor.active == True:
                # m = sub22.circle1[0] - tor.body['bp5'][0]
                # n = sub22.circle1[1] - tor.body['bp5'][1]
                # print(m,n)
                for j in tor.body:
                    tor.body[j][0] = tor.body[j][0]+ speed_tor
                    tor.body[j][1] = tor.body[j][1] + tor.inc_y
                    if tor.body["bp4"][0]> 680 :
                        tor.active = False
                if sub22.main_body['mp1'][0] < tor.body['bp5'][0] < sub22.main_body['mp3'][0] :
                    if sub22.main_body['mp1'][1]+15 > tor.body['bp5'][1] > sub22.main_body['mp3'][1]-8:
                        sub22.control = False
                        tor.active = False
                        sub22.life = 0
        for tor in torpedo2:
            if tor.active == True:
                for j in tor.body:
                    tor.body[j][0] = tor.body[j][0]-speed_tor
                    tor.body[j][1] = tor.body[j][1] - tor.inc_y
                    if tor.body["bp4"][0] < -680 :
                        tor.active = False
                if sub11.main_body['mp1'][0] > tor.body['bp5'][0] > sub11.main_body['mp3'][0] :
                    if sub11.main_body['mp1'][1]+15 > tor.body['bp5'][1] > sub11.main_body['mp3'][1]-8:
                        sub11.control = False
                        tor.active = False  
                        sub11.life = 0      
        if -270<sub11.main_body['mp3'][0]<250 and  sub11.main_body['mp3'][1] < -240 and sub11.control == True:
            player = 1
            game_over = True
        if -270<sub22.main_body['mp3'][0]<250 and  sub22.main_body['mp3'][1] < -240 and sub22.control == True:
            player = 2
            game_over = True
        if sub11.control == False and sub22.control == False:
            game_over = True


        dx = [1/bomb_left[0], 1/bomb_left[1], 1/bomb_right[0], 1/bomb_right[1]]
        for i in range(len(bombs)):
            bombs[i][0] -= dx[i]
            bombs[i][1] -= 1
        flag = False
        for i in bombs:
            if -318 <= i[1]:
                flag = True
        if flag == False:
            bombs = [[0,233], [0,233], [0,233], [0,233]]
            bombN = [True, True, True, True]
            direction()
        left_p1 = sub11.main_body["mp1"]
        left_p2 = sub11.main_body["mp2"]
        left_p3 = sub11.main_body["mp3"]
        left_p4 = sub11.main_body["mp4"]
        extra = 20
        left_p1 = [sub11.main_body["mp1"][0]+extra, sub11.main_body["mp1"][1]+extra]
        left_p2 = [sub11.main_body["mp2"][0]-extra, sub11.main_body["mp2"][1]+extra]
        left_p3 = [sub11.main_body["mp3"][0]-extra, sub11.main_body["mp3"][1]-extra]
        left_p4 = [sub11.main_body["mp4"][0]+extra, sub11.main_body["mp4"][1]-extra]
        count = 0
        for i in bombs:
            if (left_p2[0] <= i[0] <= left_p1[0]) and (left_p4[1] <= i[1] <= left_p1[1]):
                if bombN[count] == True and sub11.life > 0:
                    sub11.life -= 1
                    bombN[count] = False
            count += 1
        right_p1 = [sub22.main_body["mp1"][0]-extra, sub22.main_body["mp1"][1]+extra]
        right_p2 = [sub22.main_body["mp2"][0]+extra, sub22.main_body["mp2"][1]+extra]
        right_p3 = [sub22.main_body["mp3"][0]+extra, sub22.main_body["mp3"][1]-extra]
        right_p4 = [sub22.main_body["mp4"][0]-extra, sub22.main_body["mp4"][1]-extra]
        count = 0
        for i in bombs:
            if (right_p1[0] <= i[0] <= right_p2[0]) and (right_p4[1] <= i[1] <= right_p1[1]):
                if bombN[count] == True and sub22.life > 0:
                    sub22.life  -= 1
                    bombN[count] = False
            count += 1
        if sub11.life == 0 :
            sub11.control = False
        if sub22.life == 0:
            sub22.control = False
    #//codes for any changes in Models, Camera
    glutPostRedisplay()

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

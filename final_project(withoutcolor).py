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

speed_rain = 0.15
speed_sub = 6
speed_sub1 = 4.5
submarines = []
bubbles = []

speed_rad = 0.015
torpedo1 = []
torpedo2 = []
speed_tor = 2.5

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
            draw_lines(tor.body["bp1"][0],tor.body["bp1"][1],tor.body["bp2"][0],tor.body["bp2"][1])
            draw_lines(tor.body["bp2"][0],tor.body["bp2"][1],tor.body["bp3"][0],tor.body["bp3"][1])
            draw_lines(tor.body["bp3"][0],tor.body["bp3"][1],tor.body["bp4"][0],tor.body["bp4"][1])
            draw_lines(tor.body["bp4"][0],tor.body["bp4"][1],tor.body["bp5"][0],tor.body["bp5"][1])
            draw_lines(tor.body["bp5"][0],tor.body["bp5"][1],tor.body["bp1"][0],tor.body["bp1"][1])

def draw_torpedo2():
    global torpedo2
    for tor in torpedo2:
        if tor.active == True:
            draw_lines(tor.body["bp1"][0],tor.body["bp1"][1],tor.body["bp2"][0],tor.body["bp2"][1])
            draw_lines(tor.body["bp2"][0],tor.body["bp2"][1],tor.body["bp3"][0],tor.body["bp3"][1])
            draw_lines(tor.body["bp3"][0],tor.body["bp3"][1],tor.body["bp4"][0],tor.body["bp4"][1])
            draw_lines(tor.body["bp4"][0],tor.body["bp4"][1],tor.body["bp5"][0],tor.body["bp5"][1])
            draw_lines(tor.body["bp5"][0],tor.body["bp5"][1],tor.body["bp1"][0],tor.body["bp1"][1])


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
list5 = [[-530,165],[-550,165],[-550,145],[-530,145]]
list6 = [[-570,130],[-610,130],[-610,115],[-570,115],[-555,122.5]]
circle1 = [-580,155]
circle2 = [-620,155]

sub11 = submarine(list1,list2,list3,list4,list5,list6,circle1,circle2,1)
submarines.append(sub11)

#submarine 22 :
list11 = [[530,180],[630,180],[630,130],[530,130]]
list22 = [[660,165],[680,165],[680,145],[660,145],[655,155]]
list33 = [[550,200],[580,200],[610,180],[550,180]]
list44 = [[560,215],[570,215],[570,200],[560,200]]
list55 = [[530,165],[550,165],[550,145],[530,145]]
list66 = [[570,130],[610,130],[610,115],[570,115],[555,122.5]]
circle11 = [580,155]
circle22 = [620,155]

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
                    draw_points(k[0],k[1],1)

def draw_submarine(submarines):
    for sub in submarines:
        draw_lines(sub.main_body["mp1"][0],sub.main_body["mp1"][1],sub.main_body["mp2"][0],sub.main_body["mp2"][1])
        draw_lines(sub.main_body["mp3"][0],sub.main_body["mp3"][1],sub.main_body["mp4"][0],sub.main_body["mp4"][1])
        

        draw_lines(sub.top_body["tp1"][0],sub.top_body["tp1"][1],sub.top_body["tp2"][0],sub.top_body["tp2"][1])
        draw_lines(sub.top_body["tp2"][0],sub.top_body["tp2"][1],sub.top_body["tp3"][0],sub.top_body["tp3"][1])     
        draw_lines(sub.top_body["tp4"][0],sub.top_body["tp4"][1],sub.top_body["tp1"][0],sub.top_body["tp1"][1])


        draw_lines(sub.propeller["pp1"][0],sub.propeller["pp1"][1],sub.propeller["pp2"][0],sub.propeller["pp2"][1])
        draw_lines(sub.propeller["pp2"][0],sub.propeller["pp2"][1],sub.propeller["pp3"][0],sub.propeller["pp3"][1])
        draw_lines(sub.propeller["pp3"][0],sub.propeller["pp3"][1],sub.propeller["pp4"][0],sub.propeller["pp4"][1])
        draw_lines(sub.propeller["pp4"][0],sub.propeller["pp4"][1],sub.propeller["pp5"][0],sub.propeller["pp5"][1])
        draw_lines(sub.propeller["pp5"][0],sub.propeller["pp5"][1],sub.propeller["pp1"][0],sub.propeller["pp1"][1])


        draw_lines(sub.air_duct["ap1"][0],sub.air_duct["ap1"][1],sub.air_duct["ap2"][0],sub.air_duct["ap2"][1])
        draw_lines(sub.air_duct["ap2"][0],sub.air_duct["ap2"][1],sub.air_duct["ap3"][0],sub.air_duct["ap3"][1])     
        draw_lines(sub.air_duct["ap4"][0],sub.air_duct["ap4"][1],sub.air_duct["ap1"][0],sub.air_duct["ap1"][1])

        draw_lines(sub.door["dp1"][0],sub.door["dp1"][1],sub.door["dp2"][0],sub.door["dp2"][1])
        draw_lines(sub.door["dp2"][0],sub.door["dp2"][1],sub.door["dp3"][0],sub.door["dp3"][1])
        draw_lines(sub.door["dp3"][0],sub.door["dp3"][1],sub.door["dp4"][0],sub.door["dp4"][1])
        draw_lines(sub.door["dp4"][0],sub.door["dp4"][1],sub.door["dp1"][0],sub.door["dp1"][1])



        draw_lines(sub.lower_body["lp1"][0],sub.lower_body["lp1"][1],sub.lower_body["lp2"][0],sub.lower_body["lp2"][1])
        draw_lines(sub.lower_body["lp2"][0],sub.lower_body["lp2"][1],sub.lower_body["lp3"][0],sub.lower_body["lp3"][1])
        draw_lines(sub.lower_body["lp3"][0],sub.lower_body["lp3"][1],sub.lower_body["lp4"][0],sub.lower_body["lp4"][1])
        draw_lines(sub.lower_body["lp4"][0],sub.lower_body["lp4"][1],sub.lower_body["lp5"][0],sub.lower_body["lp5"][1])
        draw_lines(sub.lower_body["lp5"][0],sub.lower_body["lp5"][1],sub.lower_body["lp1"][0],sub.lower_body["lp1"][1])


        points = circle_maker(25)
        px1 = sub.main_body["mp1"][0]
        py1 = (sub.main_body['mp1'][1] +  sub.main_body['mp4'][1])/2
        px2 = sub.main_body['mp2'][0]
        py2 = (sub.main_body['mp2'][1] +  sub.main_body['mp3'][1])/2
        all_points11 = zone_converter(px1,py1,points)
        all_points22 = zone_converter(px2,py2,points)

        if sub.num == 1:
            for i in range(len(all_points11)):
                if i in [0,1,6,7]:
                    for j in all_points11[i]:
                        draw_points(j[0],j[1],1)

            for i in range(len(all_points22)):
                if i in [2,3,4,5]:
                    for j in all_points22[i]:
                        draw_points(j[0],j[1],1)
        if sub.num == 2:
            for i in range(len(all_points11)):
                if i in [2,3,4,5]:
                    for j in all_points11[i]:
                        draw_points(j[0],j[1],1)

            for i in range(len(all_points22)):
                if i in [0,1,6,7]:
                    for j in all_points22[i]:
                        draw_points(j[0],j[1],1)            

        points11 = circle_maker(10)
        all_circle11 = zone_converter(sub.circle1[0],sub.circle1[1],points11)
        for i in range(len(all_circle11)):
            for j in all_circle11[i]:
                draw_points(j[0],j[1],1)

        all_circle22 = zone_converter(sub.circle2[0],sub.circle2[1],points11)
        for i in range(len(all_circle22)):
            for j in all_circle22[i]:
                draw_points(j[0],j[1],1)

def boatMaker():
    boatx = 80
    boaty = 233
    boat_x1, boat_x2 = -boatx, boatx
    boat_y1, boat_y2 = boaty, boaty

    draw_lines(boat_x1 , boat_y1, boat_x2, boat_y2)
    draw_lines(boat_x1 , boat_y1, boat_x1-40, boat_y1+40)
    draw_lines(boat_x1-40, boat_y1+40,boat_x1-90,boat_y1+70)
    draw_lines(boat_x1-90, boat_y1+70,boat_x1-87,boat_y1+75)
    draw_lines(boat_x1-87, boat_y1+75,boat_x1-40,boat_y1+55)
    draw_lines(boat_x1-40, boat_y1+55,boat_x1,boat_y1+55)
    draw_lines(boat_x1, boat_y1+55,boat_x1+15,boat_y1+40)
    draw_lines(boat_x1+15,boat_y1+40,boat_x1+90,boat_y1+40)
    draw_lines(boat_x1+90,boat_y1+40,boat_x1+110,boat_y1+55)
    draw_lines(boat_x1+110,boat_y1+55,boat_x1+180,boat_y1+55)
    draw_lines(boat_x1+180,boat_y1+55,boat_x1+180,boat_y1+30)
    draw_lines(boat_x1+180,boat_y1+30,boat_x2,boat_y2)
    point = circle_maker(10)
    allpoint1 = zone_converter(-boatx+15,boaty+20, point)
    allpoint2 = zone_converter(-boatx+55,boaty+20, point)
    allpoint3 = zone_converter(-boatx+95,boaty+20, point)
    allpoint4 = zone_converter(-boatx+135,boaty+20, point)
    allpoint  = [allpoint1, allpoint2, allpoint3, allpoint4]
    for i in allpoint:
        for j in i:
            for k in j:
                draw_points(k[0], k[1], 1.5)
    draw_lines(boatx-20, boaty+55, boatx-20, boaty+140)
    draw_lines(boatx-20, boaty+140, boatx+40, boaty+70)
    draw_lines(boatx+40, boaty+70, boatx-10, boaty+70)
    draw_lines(boatx-10, boaty+70, boatx-10, boaty+55)
    """ draw_lines(boatx-10, boaty+80, boatx-10, boaty+115)
    draw_lines(boatx-10, boaty+115, boatx+20, boaty+80)
    draw_lines(boatx-10, boaty+80, boatx+20, boaty+80) """
    draw_lines(boatx-108, boaty+40, boatx-108, boaty+65)
    draw_lines(boatx-70, boaty+40, boatx-70, boaty+65)
    draw_lines(boatx-108, boaty+65, boatx-70, boaty+65)
    draw_lines(boatx-108, boaty+50, boatx-154, boaty+77)
    draw_lines(boatx-108, boaty+57, boatx-150, boaty+82)
    point = circle_maker(7)
    allpoint111 = zone_converter(-boatx+2,boaty+83, point)
    for i in allpoint111:
        for j in i:
            draw_points(j[0], j[1], 1.2)
    point = circle_maker(4)
    allpoint111 = zone_converter(-boatx+2,boaty+83, point)
    for i in allpoint111:
        for j in i:
            draw_points(j[0], j[1], 1.2)
    global bombs, bombN
    idx = 0
    for i in bombs:
        if -435 <= i[0] <= 435 and -318 <= i[1] <= -213:
            pass
        else:
            if bombN[idx] == True:
                circleMaker(i[0], i[1], 5)
                circleMaker(i[0], i[1], 10)
        idx += 1


bombs = [[0,233], [0,233], [0,233], [0,233]]
bombN = [True, True, True, True]
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

def draw_lines(x,y,a,b):
    glPointSize(2)
    glBegin(GL_LINES)
    glColor3f(1.0,1.0,1.0)
    glVertex2f(x,y)
    glVertex2f(a,b)
    glEnd()

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
            if time_int1 > 2:
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
            if time_int2 > 2:
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

def circleMaker(x, y, rad):
    point = circle_maker(rad)
    allpoint = zone_converter(x, y, point)
    for i in allpoint:
        for j in i:
            draw_points(j[0], j[1], 1.2)
def draw_titanic():
    #leftside
    draw_lines(-300, -318, -100, -318)
    draw_lines(-300, -318, -370, -233)
    draw_lines(-370, -233, -300, -250)
    draw_lines(-300, -250, -100, -250)
    draw_lines(-287, -260, -245, -260)
    draw_lines(-287, -260, -287, -250)
    draw_lines(-245, -260, -245, -250)
    draw_lines(-231, -260, -189, -260)
    draw_lines(-231, -260, -231, -250)
    draw_lines(-189, -260, -189, -250)
    draw_lines(-175, -260, -133, -260)
    draw_lines(-175, -260, -175, -250)
    draw_lines(-133, -260, -133, -250)
    draw_lines(-283, -245, -249, -245)
    draw_lines(-283, -245, -283, -250)
    draw_lines(-249, -245, -249, -250)
    draw_lines(-260, -245, -260, -200)
    draw_lines(-272, -245, -272, -200)
    circleMaker(-267, -200, 6)
    circleMaker(-267, -289, 10)
    draw_lines(-227, -245, -227, -250)
    draw_lines(-227, -245, -193, -245)
    draw_lines(-193, -245, -193, -250)
    draw_lines(-216, -245, -216, -200)
    draw_lines(-204, -245, -204, -200)
    circleMaker(-211, -200, 6)
    circleMaker(-211, -289, 10)
    draw_lines(-171, -245, -171, -250)
    draw_lines(-171, -245, -137, -245)
    draw_lines(-137, -245, -137, -250)
    draw_lines(-160, -245, -160, -200)
    draw_lines(-148, -245, -148, -200)
    circleMaker(-155, -200, 6)
    circleMaker(-155, -289, 10)
    #ridges
    draw_lines(-100, -250, -120, -270)
    draw_lines(-120, -270, -80, -280)
    draw_lines(-80, -280, -110, -290)
    draw_lines(-110, -290, -100, -318)
    #rightside
    draw_lines(300, -318, 100, -318)
    draw_lines(300, -318, 370, -233)
    draw_lines(370, -233, 300, -250)
    draw_lines(300, -250, 100, -250)
    draw_lines(287, -260, 245, -260)
    draw_lines(287, -260, 287, -250)
    draw_lines(245, -260, 245, -250)
    draw_lines(231, -260, 189, -260)
    draw_lines(231, -260, 231, -250)
    draw_lines(189, -260, 189, -250)
    draw_lines(175, -260, 133, -260)
    draw_lines(175, -260, 175, -250)
    draw_lines(133, -260, 133, -250)
    draw_lines(283, -245, 249, -245)
    draw_lines(283, -245, 283, -250)
    draw_lines(249, -245, 249, -250)
    draw_lines(260, -245, 260, -200)
    draw_lines(272, -245, 272, -200)
    circleMaker(265, -200, 6)
    circleMaker(265, -289, 10)
    draw_lines(227, -245, 227, -250)
    draw_lines(227, -245, 193, -245)
    draw_lines(193, -245, 193, -250)
    draw_lines(216, -245, 216, -200)
    draw_lines(204, -245, 204, -200)
    circleMaker(209, -200, 6)
    circleMaker(209, -289, 10)
    draw_lines(171, -245, 171, -250)
    draw_lines(171, -245, 137, -245)
    draw_lines(137, -245, 137, -250)
    draw_lines(160, -245, 160, -200)
    draw_lines(148, -245, 148, -200)
    circleMaker(153, -200, 6)
    circleMaker(153, -289, 10)
    #ridges
    draw_lines(100, -250, 120, -270)
    draw_lines(120, -270, 80, -280)
    draw_lines(80, -280, 110, -290)
    draw_lines(110, -290, 100, -318)
    #-----Khajana------#
    draw_lines(-30, -318, 30, -318)
    draw_lines(-50, -290, -30, -318)
    draw_lines(50, -290, 30, -318)
    for i in range(-45, 46, 10):
        circleMaker(i, -290, 5)
    for i in range(-40, 41, 10):
        circleMaker(i, -280, 5)
    for i in range(-25, 26, 10):
        circleMaker(i, -270, 5)


def auto_fall(sub):
    if sub.main_body['mp3'][1] > -300 :  
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
            print(x,y)
            c_X, c_y = convert_coordinate(x,y)
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
    

    draw_lines(-680,230,680,230)
    draw_lines(-680, -320, 680, -320)


    # draw_lines(-630,180,-530,180)
    # draw_lines(-630,130,-530,130)
    draw_submarine(submarines)
    
    draw_bubble()

    boatMaker()

    draw_rain()
    
    if game_over == False:
        draw_torpedo1()
        draw_torpedo2()

    draw_titanic()


    font = GLUT_BITMAP_TIMES_ROMAN_24
    text_color = (1.0, 0.5, 0.0) 
     
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
        if elapsed_time1 > 3 :
            if sub11.control == True:
                x1 = (sub11.air_duct['ap1'][0]+sub11.air_duct['ap2'][0] ) / 2
                y1 = (sub11.air_duct['ap1'][1]+ 5)
                bub1 = bubble(x1,y1)
                bubbles.append(bub1)
                start_time1 = time.time()
        if elapsed_time2 > 3 :
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
                    if sub22.main_body['mp1'][1]+5 > tor.body['bp5'][1] > sub22.main_body['mp3'][1]-5:
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
                    if sub11.main_body['mp1'][1]+5 > tor.body['bp5'][1] > sub11.main_body['mp3'][1]-5:
                        sub11.control = False
                        tor.active = False  
                        sub11.life = 0      
        if -270<sub11.main_body['mp3'][0]<250 and  sub11.main_body['mp3'][1] < -240 :
            player = 1
            game_over = True
        if -270<sub22.main_body['mp3'][0]<250 and  sub22.main_body['mp3'][1] < -240 :
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
        extra = 20
        left_p1 = [sub11.main_body["mp1"][0]+extra, sub11.main_body["mp1"][1]+extra]
        left_p2 = [sub11.main_body["mp2"][0]-extra, sub11.main_body["mp2"][1]+extra]
        left_p3 = [sub11.main_body["mp3"][0]-extra, sub11.main_body["mp3"][1]-extra]
        left_p4 = [sub11.main_body["mp4"][0]+extra, sub11.main_body["mp4"][1]-extra]
        count = 0
        for i in bombs:
            if (left_p2[0] <= i[0] <= left_p1[0]) and (left_p4[1] <= i[1] <= left_p1[1]):
                if bombN[count] == True:
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
                if bombN[count] == True:
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

from subprocess import check_output
from picamera import PiCamera
from time import sleep
from PIL import Image
import calibrate
import logging
import colors
import serial
import time
import cv2

global Down, Medium1, Medium2, Up, FlUp, FlDown, coord, l

l = []
coord = []

log = logging.getLogger(__name__)

Down=True
Medium1=False
medium=False
Medium2=False
Up=False

FlUp=True
FlDown=False

def prepare():
    global s1, camera
    print("Conectarea la Arduino Mega...")
    s1 = serial.Serial('/dev/ttyACM0', 9600)
    print("Conectat! - MegaA")
    print(" ")

    camera = PiCamera(resolution=(200, 200), framerate=30)
    camera.zoom = (0.1,0.1,0.74,0.74)
    camera.start_preview(fullscreen = False, window = (680,380,400,400))
    sleep(1)
    camera.shutter_speed = camera.exposure_speed
    camera.exposure_mode = 'off'
    g = camera.awb_gains
    camera.awb_mode = 'off'
    camera.awb_gains = g    
    
    sleep(1)
    print("Gata! Introdu un cub 4x4x4 amestecat iar apoi apasa 'Solve' pentru a rezolva cubul!") 

def slow():    
    global delayElevatorG,delayElevatorD,delayElevatorg,delayElevatorScanD,delayElevatord,delayElevatorDown,delayFlipperf,delayElevatorn,delayElevatorJ,delayElevatorN,delayElevatorO,delayElevatorP,delayElevatorUp,delayRotator1,delayRotator2,delayFlipper,delayElevatorScan    
    delayElevatorG = 0.47
    delayElevatorD = 0.55
    delayElevatorN = 0.51
    delayElevatorJ = 0.19
    delayElevatorP = 0.28
    delayElevatorO = 0.34
    delayElevatorUp = 0.58
    delayRotator1 = 0.56
    delayRotator2 = 0.69
    delayFlipper = 0.15
    delayElevatorg = 0.3
    delayElevatorn = 0.33
    delayElevatord = 0.36
    delayElevatorDown = 0.39
    delayFlipperf = 0.11
    delayElevatorScanD = 0.23
    delayElevatorScan = 0.36
    s1.write(b'4')
    s1.write(b'7')

def medium():
    global delayElevatorG,delayElevatorD,delayElevatorJ,delayElevatorScanD,delayElevatorg,delayElevatord,delayElevatorDown,delayFlipperf,delayElevatorn,delayElevatorN,delayElevatorO,delayElevatorP,delayElevatorUp,delayRotator1,delayRotator2,delayFlipper,delayElevatorScan    
    delayElevatorG = 0.41
    delayElevatorD = 0.48
    delayElevatorN = 0.44
    delayElevatorJ = 0.17
    delayElevatorP = 0.24
    delayElevatorO = 0.3
    delayElevatorUp = 0.51
    delayRotator1 = 0.49
    delayRotator2 = 0.6
    delayFlipper = 0.15
    delayElevatorg = 0.3
    delayElevatorn = 0.33
    delayElevatord = 0.36
    delayElevatorDown = 0.39
    delayFlipperf = 0.11
    delayElevatorScanD = 0.23
    delayElevatorScan = 0.31
    s1.write(b'4')
    s1.write(b'8')

def fast():
    global delayElevatorG,delayElevatorD,delayElevatorJ,delayElevatorScanD,delayElevatorg,delayElevatord,delayElevatorDown,delayFlipperf,delayElevatorn,delayElevatorN,delayElevatorO,delayElevatorP,delayElevatorUp,delayRotator1,delayRotator2,delayFlipper,delayElevatorScan    
    delayElevatorG = 0.31
    delayElevatorD = 0.37
    delayElevatorN = 0.34
    delayElevatorJ = 0.13
    delayElevatorP = 0.19
    delayElevatorO = 0.23
    delayElevatorUp = 0.4
    delayRotator1 = 0.35
    delayRotator2 = 0.44
    delayFlipper = 0.15
    delayElevatorg = 0.3
    delayElevatorn = 0.33
    delayElevatord = 0.36
    delayElevatorDown = 0.39
    delayFlipperf = 0.11
    delayElevatorScanD = 0.23
    delayElevatorScan = 0.24
    s1.write(b'4')
    s1.write(b'9')

def ElevatorDown():
    global Down, Medium1, medium, Medium2, Up
    
    if Down:
        pass
    
    elif Medium1:
        s1.write(b'g')
        sleep(delayElevatorg)
    
    elif medium:
        s1.write(b'n')
        sleep(delayElevatorn)
        
    elif Medium2:
        s1.write(b'd')
        sleep(delayElevatord)
        
    elif Up:
        s1.write(b'e')
        sleep(delayElevatorDown)
        
    if Down==False:    
        Down=True
        Medium1=False
        medium=False
        Medium2=False
        Up=False
    
def Elevator1():
    global Down, Medium1, medium, Medium2,Up
    
    if Down:
        s1.write(b'G')
        sleep(delayElevatorG)
    
    elif Medium1:
        pass
    
    elif medium:
        s1.write(b'j')
        sleep(delayElevatorJ)
        
    elif Medium2:
        s1.write(b'p')
        sleep(delayElevatorP)
        
    elif Up:
        s1.write(b'o')
        sleep(delayElevatorO)
        
    if Medium1==False:
        Down=False
        Medium1=True
        medium=False
        Medium2=False
        Up=False
        
def ElevatorMedium():
    global Down, Medium1, medium, Medium2,Up
    
    if Down:
        s1.write(b'N')
        sleep(delayElevatorN)
    
    elif Medium1:
        s1.write(b'J')
        sleep(delayElevatorJ)
    
    elif medium:
        pass
        
    elif Medium2:
        s1.write(b'j')
        sleep(delayElevatorJ)
        
    elif Up:
        s1.write(b'p')
        sleep(delayElevatorP)
        
    if medium==False:
        Down=False
        Medium1=False
        medium=True
        Medium2=False
        Up=False
    
def Elevator2():
    global Down, Medium1, medium, Medium2,Up
    
    if Down:
        s1.write(b'D')
        sleep(delayElevatorD)
    
    elif Medium1:
        s1.write(b'P')
        sleep(delayElevatorP)
    
    elif medium:
        s1.write(b'J')
        sleep(delayElevatorJ)
        
    elif Medium2:
        pass
        
    elif Up:
        s1.write(b'j')
        sleep(delayElevatorJ)
        
    if Medium2==False:
        Down=False
        Medium1=False
        medium=False
        Medium2=True
        Up=False
    
def ElevatorUp():
    global Down, Medium1, medium, Medium2,Up
    
    if Down:
        s1.write(b'E')
        sleep(delayElevatorUp)
    
    elif Medium1:
        s1.write(b'O')
        sleep(delayElevatorO)
    
    elif medium:
        s1.write(b'P')
        sleep(delayElevatorP)
        
    elif Medium2:
        s1.write(b'J')
        sleep(delayElevatorJ)
        
    elif Up:
        pass
    
    if Up==False:
        Down=False
        Medium1=False
        medium=False
        Medium2=False
        Up=True

   
def ElevatorUpScan():
    s1.write(b'S')
    sleep(delayElevatorScan)
    
def ElevatorDownScan():
    s1.write(b's')
    sleep(delayElevatorScanD)
    
def RotatorPositive():
    s1.write(b'R')
    sleep(delayRotator1)
    
    if Medium2 or Up or (medium and (l[0]=='D' or l[0]=='B')):
        
        for n, i in enumerate(l):
            if i=='F':
                l[n]='L'
                
            elif i=='L':
                l[n]='B'
                
            elif i=='B':
                l[n]='R'
                
            elif i=='R':
                l[n]='F'
    
def RotatorNegative():
    s1.write(b'r')
    sleep(delayRotator1)
    
    if Medium2 or Up or (medium and (l[0]=='D' or l[0]=='B')):
        
        for n, i in enumerate(l):
            if i=='F':
                l[n]='R'
                
            elif i=='L':
                l[n]='F'
                
            elif i=='B':
                l[n]='L'
                
            elif i=='R':
                l[n]='B'      
    
def RotatorDouble():
    s1.write(b'B')
    sleep(delayRotator2)
    
    if Medium2 or Up or (medium and (l[0]=='D' or l[0]=='B')):
        
        for n, i in enumerate(l):
            if i=='F':
                l[n]='B'
                
            elif i=='L':
                l[n]='R'
                
            elif i=='B':
                l[n]='F'
                
            elif i=='R':
                l[n]='L'

def FlipperUp():
    global FlUp, FlDown
    
    if FlDown:                     
        if Down:
            s1.write(b'F')
            sleep(delayFlipper)
            for n, i in enumerate(l):
                
                if i=='F':
                    l[n]='U'
                elif i=='U':
                    l[n]='B'
                elif i=='B':
                    l[n]='D'
                elif i=='D':
                    l[n]='F'
                    
        elif Down==False:
            s1.write(b'6')
            s1.write(b'F')
            sleep(delayFlipperf)
                
    elif FlUp:
        pass
    
    FlUp = True
    FlDown = False
    
def FlipperDown():
    global FlUp, FlDown
    
    if FlUp:        
        if Down:
            s1.write(b'f')
            sleep(delayFlipper)
            for n, i in enumerate(l):
                
                if i=='F':
                    l[n]='D'
                elif i=='U':
                    l[n]='F'
                elif i=='B':
                    l[n]='U'
                elif i=='D':
                    l[n]='B'
        
        elif Down==False:
            s1.write(b'6')
            s1.write(b'f')
            sleep(delayFlipperf)
    
    elif FlDown:
        pass
    
    FlDown = True
    FlUp = False
    
def close():
    s1.write(b'H')
    FlipperUp()
    sleep(0.2)
    s1.write(b'h')
    camera.close()
    s1.write(b'Q')
            
def solver():
    
    global l,coord
    a1 = time.time()
    s1.write(b'H')
    FlipperDown()
    camera.capture('/home/pi/MultiCuber/CubeScan/rubiks-side-U.png')
    im = Image.open('/home/pi/MultiCuber/CubeScan/rubiks-side-U.png')
    rotated = im.rotate(270)
    rotated.save('/home/pi/MultiCuber/CubeScan/rubiks-side-U.png')
    
    ElevatorUpScan()
    FlipperUp()
    ElevatorDownScan()
    FlipperDown()    
    
    camera.capture('/home/pi/MultiCuber/CubeScan/rubiks-side-R.png')
    im = Image.open('/home/pi/MultiCuber/CubeScan/rubiks-side-R.png')
    rotated = im.rotate(180)
    rotated.save('/home/pi/MultiCuber/CubeScan/rubiks-side-R.png')
    
    ElevatorUpScan()
    FlipperUp()
    ElevatorDownScan()
    FlipperDown()    
    
    camera.capture('/home/pi/MultiCuber/CubeScan/rubiks-side-D.png')
    im = Image.open('/home/pi/MultiCuber/CubeScan/rubiks-side-D.png')
    rotated = im.rotate(90)
    rotated.save('/home/pi/MultiCuber/CubeScan/rubiks-side-D.png')
    
    ElevatorUpScan()
    FlipperUp()
    ElevatorDownScan()
    FlipperDown()    
    
    camera.capture('/home/pi/MultiCuber/CubeScan/rubiks-side-L.png')
    
    ElevatorUp()
    RotatorNegative()
    ElevatorDown()
    FlipperUp()
    FlipperDown()
    
    camera.capture('/home/pi/MultiCuber/CubeScan/rubiks-side-B.png')
    
    ElevatorUp()
    RotatorDouble()
    ElevatorDown()
    FlipperUp()
    FlipperDown()
    
    camera.capture('/home/pi/MultiCuber/CubeScan/rubiks-side-F.png')
    
    
    s1.write(b'h')
    
    b1 = time.time()
    a2 = time.time()
    
    cmd1 = "cd /home/pi/MultiCuber/rubiks-cube-tracker/usr/bin; python rubiks-cube-tracker.py --directory /home/pi/MultiCuber/CubeScan"
    log.info(cmd1)
    output1 = check_output(cmd1, shell=True)
    
    output1 = str(output1)
    output1 = output1[2:]
    output1 = output1.rstrip(output1[-1])
    output1 = output1.rstrip(output1[-1])
    output1 = output1.rstrip(output1[-1])
        
    cmd2 = ("rubiks-color-resolver.py --json --rgb" + " " + "'" + output1 + "'")
    log.info(cmd2)
    output2 = check_output(cmd2, shell=True)
    
    fo = open("ouput.txt", "w+")
    fo.write(str(output2))
    fo.close()
    fo = open("ouput.txt", "r")
    fo.seek(22)
    contents = fo.read(118-22)
    print(contents)
    
    b2 = time.time()
    a3= time.time()
    
    cmd = ("cd /home/pi/MultiCuber/TPR-4x4x4-Solver-master; java -cp .:threephase.jar:twophase.jar solver " + contents)
    output = check_output(cmd, shell=True)
    #print(output)
    output = str(output)
    l = list(output)
    del l[:124]
    l = [ele for ele in l if ele.strip()]
    l.pop()
    l.pop()
    l.pop()
   
    l.append('Terminat!')
    print(l)
    print("Scanarea si gasirea algoritmului s-a finlizat!")

    print("Incepem sa rezolvam cubul!")
    c1 = l.count("w")
    print("Mutari pentru stratul mijlociu (w):")
    print(c1)       
    c2 = l.count("'")
    print("Mutari prime ('):")
    print(c2)       
    c3 = l.count('2')
    print("Mutari duble:")
    print(c3)       
    c4 = len(l)      
    q = c4 - c3 - c2 - c1
    print("Mutari totale:")
    print(q)
    
    b3 = time.time()
    a4 = time.time()
    
    s1.write(b'H')
    
    for x in range(q):
        
        if l[0]=="F" and l[1]=="w" and l[2]=="'":
            
            FlipperDown()
            ElevatorDown()
            FlipperUp()
            ElevatorMedium()
            RotatorNegative()
            del l[0]
            del l[0]
            del l[0]

        elif l[0]=="F" and l[1]=="w" and l[2]=="2":
            
            FlipperDown()
            ElevatorDown()
            FlipperUp()
            ElevatorMedium()
            RotatorDouble()
            del l[0]
            del l[0]
            del l[0]

        elif l[0]=="R" and l[1]=="w" and l[2]=="'":
            
            ElevatorUp()
            RotatorPositive()
            FlipperDown()
            ElevatorDown()
            FlipperUp()
            ElevatorMedium()
            RotatorNegative()
            del l[0]
            del l[0]
            del l[0]

        elif l[0]=="R" and l[1]=="w" and l[2]=="2":
            
            ElevatorUp()
            RotatorPositive()
            FlipperDown()
            ElevatorDown()
            FlipperUp()
            ElevatorMedium()
            RotatorDouble()
            del l[0]
            del l[0]
            del l[0]

        elif l[0]=="U" and l[1]=="w" and l[2]=="'":
            ElevatorMedium()
            RotatorNegative()
            del l[0]
            del l[0]
            del l[0]

        elif l[0]=="U" and l[1]=="w" and l[2]=="2":
            ElevatorMedium()
            RotatorDouble()
            del l[0]
            del l[0]
            del l[0]

        elif l[0]=="B" and l[1]=="w" and l[2]=="'":
            
            FlipperDown()
            ElevatorDown()
            FlipperUp()
            ElevatorMedium()
            RotatorNegative()
            del l[0]
            del l[0]
            del l[0]

        elif l[0]=="B" and l[1]=="w" and l[2]=="2":
            
            FlipperDown()
            ElevatorDown()
            FlipperUp()
            ElevatorMedium()
            RotatorDouble()
            del l[0]
            del l[0]
            del l[0]

        elif l[0]=="D" and l[1]=="w" and l[2]=="'":
            
            ElevatorMedium()
            RotatorNegative()
            del l[0]
            del l[0]
            del l[0]

        elif l[0]=="D" and l[1]=="w" and l[2]=="2":
            
            ElevatorMedium()
            RotatorDouble()
            del l[0]
            del l[0]
            del l[0]

        elif l[0]=="L" and l[1]=="w" and l[2]=="'":
            
            ElevatorUp()
            RotatorNegative()
            FlipperDown()
            ElevatorDown()
            FlipperUp()
            ElevatorMedium()
            RotatorNegative()
            del l[0]
            del l[0]
            del l[0]

        elif l[0]=="L" and l[1]=="w" and l[2]=="2":
            
            ElevatorUp()
            RotatorNegative()
            FlipperDown()
            ElevatorDown()
            FlipperUp()
            ElevatorMedium()
            RotatorDouble()
            del l[0]
            del l[0]
            del l[0]

        elif l[0]=="F" and l[1]=="w":
            
            FlipperDown()
            ElevatorDown()
            FlipperUp()
            ElevatorMedium()
            RotatorPositive()
            del l[0]
            del l[0]

        elif l[0]=="R" and l[1]=="w":
            
            ElevatorUp()
            RotatorPositive()
            FlipperDown()
            ElevatorDown()
            FlipperUp()
            ElevatorMedium()
            RotatorPositive()
            del l[0]
            del l[0]

        elif l[0]=="U" and l[1]=="w":
            ElevatorMedium()
            RotatorPositive()
            del l[0]
            del l[0]

        elif l[0]=="B" and l[1]=="w":
            
            FlipperDown()
            ElevatorDown()
            FlipperUp()
            ElevatorMedium()
            RotatorPositive()
            del l[0]
            del l[0]

        elif l[0]=="D" and l[1]=="w":
            
            ElevatorMedium()
            RotatorPositive()
            del l[0]
            del l[0]

        elif l[0]=="L" and l[1]=="w":
            
            ElevatorUp()
            RotatorNegative()
            FlipperDown()
            ElevatorDown()
            FlipperUp()
            ElevatorMedium()
            RotatorPositive()
            del l[0]
            del l[0]        
        
        elif l[0]=="F" and l[1]=="'":
            
            FlipperDown()
            ElevatorDown()
            FlipperUp()
            Elevator1()
            RotatorNegative()
            del l[0]
            del l[0]

        elif l[0]=="F" and l[1]=="2":
            
            FlipperDown()
            ElevatorDown()
            FlipperUp()
            Elevator1()
            RotatorDouble()
            del l[0]
            del l[0]

        elif l[0]=="R" and l[1]=="'":
            
            ElevatorUp()
            RotatorPositive()
            FlipperDown()
            ElevatorDown()
            FlipperUp()
            Elevator1()
            RotatorNegative()
            del l[0]
            del l[0]

        elif l[0]=="R" and l[1]=="2":
            
            ElevatorUp()
            RotatorPositive()
            FlipperDown()
            ElevatorDown()
            FlipperUp()
            Elevator1()
            RotatorDouble()
            del l[0]
            del l[0]

        elif l[0]=="U" and l[1]=="'":
            Elevator1()
            RotatorNegative()
            del l[0]
            del l[0]

        elif l[0]=="U" and l[1]=="2":
            Elevator1()
            RotatorDouble()
            del l[0]
            del l[0]

        elif l[0]=="B" and l[1]=="'":
            
            FlipperDown()
            ElevatorDown()
            FlipperUp()
            Elevator2()
            RotatorNegative()
            del l[0]
            del l[0]

        elif l[0]=="B" and l[1]=="2":
            
            FlipperDown()
            ElevatorDown()
            FlipperUp()
            Elevator2()
            RotatorDouble()
            del l[0]
            del l[0]

        elif l[0]=="D" and l[1]=="'":
            
            Elevator2()
            RotatorNegative()
            del l[0]
            del l[0]

        elif l[0]=="D" and l[1]=="2":
            
            Elevator2()
            RotatorDouble()
            del l[0]
            del l[0]

        elif l[0]=="L" and l[1]=="'":
            
            ElevatorUp()
            RotatorNegative()
            FlipperDown()
            ElevatorDown()
            FlipperUp()
            Elevator1()
            RotatorNegative()
            del l[0]
            del l[0]

        elif l[0]=="L" and l[1]=="2":
            
            ElevatorUp()
            RotatorNegative()
            FlipperDown()
            ElevatorDown()
            FlipperUp()
            Elevator1()
            RotatorDouble()
            del l[0]
            del l[0]

        elif l[0]=="F":
            
            FlipperDown()
            ElevatorDown()
            FlipperUp()
            Elevator1()
            RotatorPositive()
            del l[0]

        elif l[0]=="R":
            
            ElevatorUp()
            RotatorPositive()
            FlipperDown()
            ElevatorDown()
            FlipperUp()
            Elevator1()
            RotatorPositive()
            del l[0]

        elif l[0]=="U":
            Elevator1()
            RotatorPositive()
            del l[0]

        elif l[0]=="B":
            
            FlipperDown()
            ElevatorDown()
            FlipperUp()
            Elevator2()
            RotatorPositive()
            del l[0]

        elif l[0]=="D":
            
            Elevator2()
            RotatorPositive()
            del l[0]

        elif l[0]=="L":
            
            ElevatorUp()
            RotatorNegative()
            FlipperDown()
            ElevatorDown()
            FlipperUp()
            Elevator1()
            RotatorPositive()
            del l[0]

        elif l[0]=="x" and l[1]=="'":
            del l[0]
            del l[0]
            for n, i in enumerate(l):
                if i=='F':
                    l[n]='D'
                elif i=='U':
                    l[n]='F'
                elif i=='D':
                    l[n]='B'
                elif i=='B':
                    l[n]='U'

        elif l[0]=="x" and l[1]=="2":
            del l[0]
            del l[0]
            for n, i in enumerate(l):
                if i=='F':
                    l[n]='B'
                elif i=='U':
                    l[n]='D'
                elif i=='D':
                    l[n]='U'
                elif i=='B':
                    l[n]='F'

        elif l[0]=="x":
            del l[0]
            for n, i in enumerate(l):
                if i=='F':
                    l[n]='U'
                elif i=='U':
                    l[n]='B'
                elif i=='D':
                    l[n]='F'
                elif i=='B':
                    l[n]='D'

        elif l[0]=="y" and l[1]=="'":
            del l[0]
            del l[0]
            for n, i in enumerate(l):
                if i=='F':
                    l[n]='R'
                elif i=='R':
                    l[n]='B'
                elif i=='L':
                    l[n]='F'
                elif i=='B':
                    l[n]='L'

        elif l[0]=="y" and l[1]=="2":
            del l[0]
            del l[0]
            for n, i in enumerate(l):
                if i=='F':
                    l[n]='B'
                elif i=='R':
                    l[n]='L'
                elif i=='L':
                    l[n]='R'
                elif i=='B':
                    l[n]='F'

        elif l[0]=="y":
            del l[0]
            for n, i in enumerate(l):
                if i=='F':
                    l[n]='L'
                elif i=='R':
                    l[n]='F'
                elif i=='L':
                    l[n]='B'
                elif i=='B':
                    l[n]='R'

        elif l[0]=="z" and l[1]=="'":
            del l[0]
            del l[0]
            for n, i in enumerate(l):
                if i=='R':
                    l[n]='U'
                elif i=='U':
                    l[n]='L'
                elif i=='L':
                    l[n]='D'
                elif i=='D':
                    l[n]='R'

        elif l[0]=="z" and l[1]=="2":
            del l[0]
            del l[0]
            for n, i in enumerate(l):
                if i=='R':
                    l[n]='L'
                elif i=='U':
                    l[n]='D'
                elif i=='L':
                    l[n]='R'
                elif i=='D':
                    l[n]='U'

        elif l[0]=="z":
            del l[0]
            for n, i in enumerate(l):
                if i=='R':
                    l[n]='D'
                elif i=='U':
                    l[n]='R'
                elif i=='L':
                    l[n]='U'
                elif i=='D':
                    l[n]='L'

        elif l[0]=="Terminat!":
            del l[0]
            #print(l)
            print("Cubul a fost rezolvat! Introdu alt cub si apasa 'Solve' pentru a-l rezolva!")
            print(" ")
            ElevatorDown()
            FlipperUp()
            FlipperDown()
            FlipperUp()
            sleep(0.2)
            s1.write(b'h')
            b4 = time.time()
            
            t1=b1-a1
            t2=b2-a2
            t3=b3-a3
            t4=b4-a4
            t=t1+t2+t3+t4
            if q==1:
                med=0
            else:
                med=t4/(q-1)
            
            print('Scanarea a durat ' + str(round(t1,2)) + ' secunde.')
            print('Analizarea imaginilor a durat ' + str(round(t2,2)) + ' secunde.')
            print('Cautarea solutiei a durat ' + str(round(t3,2)) + ' secunde.')
            print('Rezolvarea cubului a durat ' + str(round(t4,2)) + ' secunde.')
            print('Timp mediu pe mutare: ' + str(round(med,2)) + ' secunde.')
            print('Timp total: ' + str(round(t,2)) + ' secunde.')

        else:

            i=i+1
            print("Prea multe mutari:" + i)
            
    return(t)
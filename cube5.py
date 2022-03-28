from subprocess import check_output
from time import sleep
import logging
import imutils
import serial
import time
import cv2

global Down, elevator1, elevator2, Up, FlUp, FlDown, coord, l,start,i
start = True
i = 0

l = []
coord = []

log = logging.getLogger(__name__)

Down=True
elevator1=False
medium1=False
medium2=False
elevator2=False
Up=False

FlUp=True
FlDown=False

def prepare():
    global s1, camera
    print("Conectarea la Arduino Mega...")
    s1 = serial.Serial('/dev/tty.usbmodem21401', 9600)
    print("Conectat! - MegaA")
    print(" ")

    camera = cv2.VideoCapture(0)
    sleep(1.5)

    (retval, img) = camera.read()

    cv2.imshow("Capture", img)

    print("Gata! Introdu un cub 5x5x5 amestecat iar apoi apasa 'Solve' pentru a rezolva cubul!")


def photo(name, angle):
    global camera
    sleep(0.4)
    (retval, img) = camera.read()
    name = '/Users/horia/MultiCuber/CubeScan/' + str(name)
    name = str(name)
    print(name)

    angle = int(angle)
    img = imutils.rotate(img, angle)
    cv2.imshow("Capture", img)
    cv2.waitKey(1)
    cv2.imwrite(name, img)


def status():
    s1.write(b'M')
    while(1):                
        r = s1.read()
        r = r.decode()
        if r=='A':
            break


def slow():
    s1.write(b'5')
    s1.write(b'7')


def normal():
    s1.write(b'5')
    s1.write(b'8')


def fast():
    s1.write(b'5')
    s1.write(b'9')


def ElevatorDown():
    global Down, elevator1, medium1, medium2, elevator2,Up
    
    if Down:
        pass
    
    elif elevator1:
        s1.write(b'g')
    
    elif medium1:
        s1.write(b'n')
    
    elif medium2:
        s1.write(b'i')
        
    elif elevator2:
        s1.write(b'd')
        
    elif Up:
        s1.write(b'e')
        
    if Down==False:
        Down=True
        elevator1=False
        medium1 = False
        medium2=False
        elevator2=False
        Up=False
    
    status()

def Elevator1():
    global Down, elevator1, medium1, medium2, elevator2,Up
    
    if Down:
        s1.write(b'G')
    
    elif elevator1:
        pass
    
    elif medium1:
        s1.write(b'j')
        
    elif medium2:
        s1.write(b'p')
        
    elif elevator2:
        s1.write(b'o')
        
    elif Up:
        s1.write(b'v')
        
    if elevator1==False:
        Down=False
        elevator1=True
        medium1=False
        medium2=False
        elevator2=False
        Up=False
    
    status()
    
def ElevatorMedium1():
    global Down, elevator1, medium1, medium2, elevator2,Up
    
    if Down:
        s1.write(b'N')
    
    elif elevator1:
        s1.write(b'J')
    
    elif medium1:
        pass
    
    elif medium2:
        s1.write(b'j')
        
    elif elevator2:
        s1.write(b'p')
        Down=False
        
    elif Up:
        s1.write(b'o')
        
    if medium1==False:
        Down=False
        elevator1=False
        medium1=True
        medium2=False
        elevator2=False
        Up=False
    
    status()
    
def ElevatorMedium2():
    global Down, elevator1, medium1, medium2, elevator2,Up
    
    if Down:
        s1.write(b'I')
        
    elif elevator1:
        s1.write(b'P')
    
    elif medium1:
        s1.write(b'J')
    
    elif medium2:
        pass
        
    elif elevator2:
        s1.write(b'j')
        
    elif Up:
        s1.write(b'p')
        
    if medium2==False:
        Down=False
        elevator1=False
        medium1=False
        medium2=True
        elevator2=False
        Up=False
    
    status()
    
def Elevator2():
    global Down, elevator1, medium1, medium2, elevator2,Up
    
    if Down:
        s1.write(b'D')
    
    elif elevator1:
        s1.write(b'O')
    
    elif medium1:
        s1.write(b'P')
        
    elif medium2:
        s1.write(b'J')
        
    elif elevator2:
        pass
        
    elif Up:
        s1.write(b'j')
        
    if elevator2==False:
        Down=False
        elevator1=False
        medium1=False
        medium2=False
        elevator2=True
        Up=False
    
    status()
    
def ElevatorUp():
    global Down, elevator1, medium1, medium2, elevator2,Up
    
    if Down:
        s1.write(b'E')
    
    elif elevator1:
        s1.write(b'V')
    
    elif medium1:
        s1.write(b'O')
        
    elif medium2:
        s1.write(b'P')
        
    elif elevator2:
        s1.write(b'J')
        
    elif Up:
        pass
    
    if Up==False:
        Down=False
        elevator1=False
        medium1=False
        medium2=False
        elevator2=False
        Up=True

    status()
    
def ElevatorUpScan():
    s1.write(b'S')
    status()
        
def ElevatorDownScan():
    s1.write(b's')
    status()
    
def RotatorPositive():
    s1.write(b'R')
    
    if elevator2 or Up or medium2:
        
        for n, i in enumerate(l):
            if i=='F':
                l[n]='L'
                
            elif i=='L':
                l[n]='B'
                
            elif i=='B':
                l[n]='R'
                
            elif i=='R':
                l[n]='F'
    
    status()
    
def RotatorNegative():
    s1.write(b'r')
    
    if elevator2 or Up or medium2:
        
        for n, i in enumerate(l):
            if i=='F':
                l[n]='R'
                
            elif i=='L':
                l[n]='F'
                
            elif i=='B':
                l[n]='L'
                
            elif i=='R':
                l[n]='B'      
    
    status()


def RotatorDouble():
    s1.write(b'B')
    
    if elevator2 or Up or medium2:
        
        for n, i in enumerate(l):
            if i=='F':
                l[n]='B'
                
            elif i=='L':
                l[n]='R'
                
            elif i=='B':
                l[n]='F'
                
            elif i=='R':
                l[n]='L'
    
    status()


def FlipperUp():
    global FlUp, FlDown
    
    if FlDown:                     
        if Down:
            s1.write(b'F')
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
            s1.write(b'X')
                
    elif FlUp:
        pass
    
    FlUp = True
    FlDown = False
    status()


def FlipperDown():
    global FlUp, FlDown
    
    if FlUp:        
        if Down:
            s1.write(b'f')
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
            s1.write(b'x')
    
    elif FlDown:
        pass
    
    FlDown = True
    FlUp = False
    status()


def close():
    global camera
    s1.write(b'H')
    FlipperUp()
    sleep(0.2)
    s1.write(b'h')
    del (camera)
    camera = None
    s1.write(b'Q')


def pattern1():
    global l
    l = []
    l.extend(("U", "2", "D", "2", "F", "2", "B", "2", "R", "2", "L", "2"))
    solver()


def pattern2():
    global l
    l = []
    l.extend(("U", "D", "'", "R", "L", "'", "F", "B", "'", "U", "D", "'"))
    solver()


def pattern3():
    global l
    l = []
    l.extend(("U", "F", "B", "'", "L", "2", "U", "2", "L", "2", "F", "'", "B", "U", "2", "L", "2", "U"))
    solver()


def pattern4():
    global l
    l = []
    l.extend(("R", "2", "L", "'", "D", "F", "2", "R", "'", "D", "'", "R", "'", "L", "U", "'", "D", "R", "D", "B", "2", "R", "'", "U", "D", "2"))
    solver()


def scanner():
    
    global l, coord, b1, a1, b2, a2, b3, a3
    a1 = time.time()
    s1.write(b'H')
    FlipperDown()
    photo('rubiks-side-U.png', '270')

    ElevatorUpScan()
    FlipperUp()
    ElevatorDownScan()
    FlipperDown()

    photo('rubiks-side-R.png', '180')

    ElevatorUpScan()
    FlipperUp()
    ElevatorDownScan()
    FlipperDown()

    photo('rubiks-side-D.png', '90')

    ElevatorUpScan()
    FlipperUp()
    ElevatorDownScan()
    FlipperDown()

    photo('rubiks-side-L.png', '0')

    ElevatorUp()
    RotatorNegative()
    ElevatorDown()
    FlipperUp()
    FlipperDown()

    photo('rubiks-side-B.png', '0')

    ElevatorUp()
    RotatorDouble()
    ElevatorDown()
    FlipperUp()
    FlipperDown()

    photo('rubiks-side-F.png', '0')
    
    s1.write(b'h')
    
    b1 = time.time()


def analyzer():
    global l,coord,b1,a1,b2,a2,b3,a3,q
    a2 = time.time()
    
    cmd1 = ("cd ~/MultiCuber/rubiks-cube-tracker/usr/bin; python3 rubiks-cube-tracker.py --directory ~/MultiCuber/CubeScan")
    log.info(cmd1)
    output1 = check_output(cmd1, shell=True)
    
    output1 = str(output1)
    output1 = output1[2:]
    output1 = output1.rstrip(output1[-1])
    output1 = output1.rstrip(output1[-1])
    output1 = output1.rstrip(output1[-1])
        
    cmd2 = ("cd ~/MultiCuber/rubiks-color-resolver/usr/bin; python3 rubiks-color-resolver.py --json --rgb" + " " + "'" + output1 + "'")
    log.info(cmd2)
    output2 = check_output(cmd2, shell=True)
    
    output2 = str(output2)
    contents = output2[22:172]
    print(contents)
    
    cmd3 = ("cd ~/MultiCuber/rubiks-cube-NxNxN-solver/; ./rubiks-cube-solver.py --state " + contents)
    log.info(cmd3)
    output3 = check_output(cmd3, shell=True)
    
    output3 = str(output3)
    output3 = output3[12:]
    output3 = output3.rstrip(output3[-1])
    output3 = output3.rstrip(output3[-1])
    output3 = output3.rstrip(output3[-1])
    
    l = list(output3)
    l = [e for e in l if e.strip()]
    
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
    
    b2 = time.time()

def solver():
    global l,coord,b1,a1,b2,a2,b3,a3,start,i
    a3 = time.time()
    
    s1.write(b'H')
    
    for x in range(q):
        if x>1 and x <3:
            start = False
        if l[0]=="F" and l[1]=="w" and l[2]=="'":
            
            FlipperDown()
            ElevatorDown()
            FlipperUp()
            ElevatorMedium1()
            RotatorNegative()
            del l[0]
            del l[0]
            del l[0]

        elif l[0]=="F" and l[1]=="w" and l[2]=="2":
            
            FlipperDown()
            ElevatorDown()
            FlipperUp()
            ElevatorMedium1()
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
            ElevatorMedium1()
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
            ElevatorMedium1()
            RotatorDouble()
            del l[0]
            del l[0]
            del l[0]

        elif l[0]=="U" and l[1]=="w" and l[2]=="'":
            ElevatorMedium1()
            RotatorNegative()
            del l[0]
            del l[0]
            del l[0]

        elif l[0]=="U" and l[1]=="w" and l[2]=="2":
            ElevatorMedium1()
            RotatorDouble()
            del l[0]
            del l[0]
            del l[0]

        elif l[0]=="B" and l[1]=="w" and l[2]=="'":
            if start:
                FlipperDown()
                ElevatorDown()
                FlipperUp()
                ElevatorMedium2()
                RotatorNegative()
            else:
                FlipperUp()
                ElevatorDown()
                FlipperDown()
                ElevatorMedium1()
                RotatorNegative() 
            del l[0]
            del l[0]
            del l[0]

        elif l[0]=="B" and l[1]=="w" and l[2]=="2":
            
            if start:
                FlipperDown()
                ElevatorDown()
                FlipperUp()
                ElevatorMedium2()
                RotatorDouble()
            else:
                FlipperUp()
                ElevatorDown()
                FlipperDown()
                ElevatorMedium1()
                RotatorDouble() 
            del l[0]
            del l[0]
            del l[0]

        elif l[0]=="D" and l[1]=="w" and l[2]=="'":
            
            ElevatorMedium2()
            RotatorNegative()
            del l[0]
            del l[0]
            del l[0]

        elif l[0]=="D" and l[1]=="w" and l[2]=="2":
            
            ElevatorMedium2()
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
            ElevatorMedium1()
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
            ElevatorMedium1()
            RotatorDouble()
            del l[0]
            del l[0]
            del l[0]

        elif l[0]=="F" and l[1]=="w":
            
            FlipperDown()
            ElevatorDown()
            FlipperUp()
            ElevatorMedium1()
            RotatorPositive()
            del l[0]
            del l[0]

        elif l[0]=="R" and l[1]=="w":
            
            ElevatorUp()
            RotatorPositive()
            FlipperDown()
            ElevatorDown()
            FlipperUp()
            ElevatorMedium1()
            RotatorPositive()
            del l[0]
            del l[0]

        elif l[0]=="U" and l[1]=="w":
            ElevatorMedium1()
            RotatorPositive()
            del l[0]
            del l[0]

        elif l[0]=="B" and l[1]=="w":
            
            if start:
                FlipperDown()
                ElevatorDown()
                FlipperUp()
                ElevatorMedium2()
                RotatorPositive()
            else:
                FlipperUp()
                ElevatorDown()
                FlipperDown()
                ElevatorMedium1()
                RotatorPositive() 
            del l[0]
            del l[0]

        elif l[0]=="D" and l[1]=="w":
            
            ElevatorMedium2()
            RotatorPositive()
            del l[0]
            del l[0]

        elif l[0]=="L" and l[1]=="w":
            
            ElevatorUp()
            RotatorNegative()
            FlipperDown()
            ElevatorDown()
            FlipperUp()
            ElevatorMedium1()
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
            
            if start:
                FlipperDown()
                ElevatorDown()
                FlipperUp()
                Elevator2()
                RotatorNegative()
            else:
                FlipperUp()
                ElevatorDown()
                FlipperDown()
                Elevator1()
                RotatorNegative() 
            del l[0]
            del l[0]

        elif l[0]=="B" and l[1]=="2":
            if start:
                FlipperDown()
                ElevatorDown()
                FlipperUp()
                Elevator2()
                RotatorDouble()
            else:
                FlipperUp()
                ElevatorDown()
                FlipperDown()
                Elevator1()
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
            
            if start:
                FlipperDown()
                ElevatorDown()
                FlipperUp()
                Elevator2()
                RotatorPositive()
            else:
                FlipperUp()
                ElevatorDown()
                FlipperDown()
                Elevator1()
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
            print("Cubul a fost rezolvat! Introdu alt cub si apasa 'Solve' pentru a-l rezolva!")
            print(" ")
            ElevatorDown()
            FlipperDown()
            FlipperUp()
            status()                
            s1.write(b'h')
            b3 = time.time()
            
            t1=b1-a1
            t2=b2-a2
            t3=b3-a3
            t=t1+t2+t3
            if q==1:
                med=0
            else:
                med=t3/(q-1)
            
            print('Scanarea a durat ' + str(round(t1,2)) + ' secunde.')
            print('Analizarea imaginilor si cautarea solutiei a durat ' + str(round(t2,2)) + ' secunde.')
            print('Rezolvarea cubului a durat ' + str(round(t3,2)) + ' secunde.')
            print('Timp mediu pe mutare: ' + str(round(med,2)) + ' secunde.')
            print('Timp total: ' + str(round(t,2)) + ' secunde.')

        else:

            i=i+1
            print("Prea multe mutari:" + i)
    
    return(t)

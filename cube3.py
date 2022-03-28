from subprocess import check_output
from time import sleep
import logging
import imutils
import serial
import time
import cv2

global Down, Medium1, Medium2, Up, FlUp, FlDown, coord, l, camera, i, start
start = True
i = 0

l = []
coord = []

log = logging.getLogger(__name__)

Down = True
Medium1 = False
Medium2 = False
Up = False

FlUp = True
FlDown = False


def photo(name, angle):
    global camera
    sleep(0.3)
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
    while (1):
        r = s1.read()
        r = r.decode()
        if r == 'A':
            break


def slow():
    s1.write(b'3')
    s1.write(b'7')


def normal():
    s1.write(b'3')
    s1.write(b'8')


def fast():
    s1.write(b'3')
    s1.write(b'9')

def ElevatorDown():
    global Down, Medium1, Medium2, Up

    if Down:
        pass

    elif Medium1:
        s1.write(b'g')

    elif Medium2:
        s1.write(b'd')

    elif Up:
        s1.write(b'e')

    if Down == False:
        Down = True
        Medium1 = False
        Medium2 = False
        Up = False

    status()


def Elevator1():
    global Down, Medium1, Medium2, Up

    if Down:
        s1.write(b'G')

    elif Medium1:
        pass

    elif Medium2:
        s1.write(b'j')

    elif Up:
        s1.write(b'p')

    if Medium1 == False:
        Down = False
        Medium1 = True
        Medium2 = False
        Up = False

    status()


def Elevator2():
    global Down, Medium1, Medium2, Up

    if Down:
        s1.write(b'D')

    elif Medium1:
        s1.write(b'J')

    elif Medium2:
        pass

    elif Up:
        s1.write(b'j')

    if Medium2 == False:
        Down = False
        Medium1 = False
        Medium2 = True
        Up = False

    status()


def ElevatorUp():
    global Down, Medium1, Medium2, Up

    if Down:
        s1.write(b'E')

    elif Medium1:
        s1.write(b'P')

    elif Medium2:
        s1.write(b'J')

    elif Up:
        pass

    if Up == False:
        Down = False
        Medium1 = False
        Medium2 = False
        Up = True

    status()


def ElevatorUpScan():
    global Down
    Down = False
    s1.write(b'S')
    status()


def ElevatorDownScan():
    global Down
    Down = True
    s1.write(b's')
    status()


def RotatorPositive():
    s1.write(b'R')

    if Medium2 or Up:

        for n, i in enumerate(l):
            if i == 'F':
                l[n] = 'L'

            elif i == 'L':
                l[n] = 'B'

            elif i == 'B':
                l[n] = 'R'

            elif i == 'R':
                l[n] = 'F'

    status()


def RotatorNegative():
    s1.write(b'r')

    if Medium2 or Up:

        for n, i in enumerate(l):
            if i == 'F':
                l[n] = 'R'

            elif i == 'L':
                l[n] = 'F'

            elif i == 'B':
                l[n] = 'L'

            elif i == 'R':
                l[n] = 'B'

    status()


def RotatorDouble():
    s1.write(b'B')

    if Medium2 or Up:

        for n, i in enumerate(l):
            if i == 'F':
                l[n] = 'B'

            elif i == 'L':
                l[n] = 'R'

            elif i == 'B':
                l[n] = 'F'

            elif i == 'R':
                l[n] = 'L'

    status()


def FlipperUp():
    global FlUp, FlDown

    if FlDown:
        if Down:
            s1.write(b'F')
            for n, i in enumerate(l):

                if i == 'F':
                    l[n] = 'U'
                elif i == 'U':
                    l[n] = 'B'
                elif i == 'B':
                    l[n] = 'D'
                elif i == 'D':
                    l[n] = 'F'

        elif Down == False:
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

                if i == 'F':
                    l[n] = 'D'
                elif i == 'U':
                    l[n] = 'F'
                elif i == 'B':
                    l[n] = 'U'
                elif i == 'D':
                    l[n] = 'B'

        elif Down == False:
            s1.write(b'x')

    elif FlDown:
        pass

    FlDown = True
    FlUp = False
    status()


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

    print("Gata! Introdu un cub 3x3x3 amestecat iar apoi apasa 'Solve' pentru a rezolva cubul!")


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
    l.extend(("R", "2", "L", "'", "D", "F", "2", "R", "'", "D", "'", "R", "'", "L", "U", "'", "D", "R", "D", "B", "2",
              "R", "'", "U", "D", "2"))
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
    global l, coord, b1, a1, b2, a2, b3, a3, q
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
    contents = output2[22:76]
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
    global l, coord, b1, a1, b2, a2, b3, a3, i, start
    a3 = time.time()

    s1.write(b'H')

    for x in range(q):
        if x > 1 and x < 3:
            start = False
        if l[0] == "F" and l[1] == "'":

            FlipperDown()
            ElevatorDown()
            FlipperUp()
            Elevator1()
            RotatorNegative()
            del l[0]
            del l[0]

        elif l[0] == "F" and l[1] == "2":

            FlipperDown()
            ElevatorDown()
            FlipperUp()
            Elevator1()
            RotatorDouble()
            del l[0]
            del l[0]

        elif l[0] == "R" and l[1] == "'":

            ElevatorUp()
            RotatorPositive()
            FlipperDown()
            ElevatorDown()
            FlipperUp()
            Elevator1()
            RotatorNegative()
            del l[0]
            del l[0]

        elif l[0] == "R" and l[1] == "2":

            ElevatorUp()
            RotatorPositive()
            FlipperDown()
            ElevatorDown()
            FlipperUp()
            Elevator1()
            RotatorDouble()
            del l[0]
            del l[0]

        elif l[0] == "U" and l[1] == "'":
            Elevator1()
            RotatorNegative()
            del l[0]
            del l[0]

        elif l[0] == "U" and l[1] == "2":
            Elevator1()
            RotatorDouble()
            del l[0]
            del l[0]

        elif l[0] == "B" and l[1] == "'":
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

        elif l[0] == "B" and l[1] == "2":

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

        elif l[0] == "D" and l[1] == "'":

            Elevator2()
            RotatorNegative()
            del l[0]
            del l[0]

        elif l[0] == "D" and l[1] == "2":

            Elevator2()
            RotatorDouble()
            del l[0]
            del l[0]

        elif l[0] == "L" and l[1] == "'":

            ElevatorUp()
            RotatorNegative()
            FlipperDown()
            ElevatorDown()
            FlipperUp()
            Elevator1()
            RotatorNegative()
            del l[0]
            del l[0]

        elif l[0] == "L" and l[1] == "2":

            ElevatorUp()
            RotatorNegative()
            FlipperDown()
            ElevatorDown()
            FlipperUp()
            Elevator1()
            RotatorDouble()
            del l[0]
            del l[0]

        elif l[0] == "F":

            FlipperDown()
            ElevatorDown()
            FlipperUp()
            Elevator1()
            RotatorPositive()
            del l[0]

        elif l[0] == "R":

            ElevatorUp()
            RotatorPositive()
            FlipperDown()
            ElevatorDown()
            FlipperUp()
            Elevator1()
            RotatorPositive()
            del l[0]

        elif l[0] == "U":
            Elevator1()
            RotatorPositive()
            del l[0]

        elif l[0] == "B":

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

        elif l[0] == "D":

            Elevator2()
            RotatorPositive()
            del l[0]

        elif l[0] == "L":

            ElevatorUp()
            RotatorNegative()
            FlipperDown()
            ElevatorDown()
            FlipperUp()
            Elevator1()
            RotatorPositive()
            del l[0]

        elif l[0] == "x" and l[1] == "'":
            del l[0]
            del l[0]
            for n, i in enumerate(l):
                if i == 'F':
                    l[n] = 'D'
                elif i == 'U':
                    l[n] = 'F'
                elif i == 'D':
                    l[n] = 'B'
                elif i == 'B':
                    l[n] = 'U'

        elif l[0] == "x" and l[1] == "2":
            del l[0]
            del l[0]
            for n, i in enumerate(l):
                if i == 'F':
                    l[n] = 'B'
                elif i == 'U':
                    l[n] = 'D'
                elif i == 'D':
                    l[n] = 'U'
                elif i == 'B':
                    l[n] = 'F'

        elif l[0] == "x":
            del l[0]
            for n, i in enumerate(l):
                if i == 'F':
                    l[n] = 'U'
                elif i == 'U':
                    l[n] = 'B'
                elif i == 'D':
                    l[n] = 'F'
                elif i == 'B':
                    l[n] = 'D'

        elif l[0] == "y" and l[1] == "'":
            del l[0]
            del l[0]
            for n, i in enumerate(l):
                if i == 'F':
                    l[n] = 'R'
                elif i == 'R':
                    l[n] = 'B'
                elif i == 'L':
                    l[n] = 'F'
                elif i == 'B':
                    l[n] = 'L'

        elif l[0] == "y" and l[1] == "2":
            del l[0]
            del l[0]
            for n, i in enumerate(l):
                if i == 'F':
                    l[n] = 'B'
                elif i == 'R':
                    l[n] = 'L'
                elif i == 'L':
                    l[n] = 'R'
                elif i == 'B':
                    l[n] = 'F'

        elif l[0] == "y":
            del l[0]
            for n, i in enumerate(l):
                if i == 'F':
                    l[n] = 'L'
                elif i == 'R':
                    l[n] = 'F'
                elif i == 'L':
                    l[n] = 'B'
                elif i == 'B':
                    l[n] = 'R'

        elif l[0] == "z" and l[1] == "'":
            del l[0]
            del l[0]
            for n, i in enumerate(l):
                if i == 'R':
                    l[n] = 'U'
                elif i == 'U':
                    l[n] = 'L'
                elif i == 'L':
                    l[n] = 'D'
                elif i == 'D':
                    l[n] = 'R'

        elif l[0] == "z" and l[1] == "2":
            del l[0]
            del l[0]
            for n, i in enumerate(l):
                if i == 'R':
                    l[n] = 'L'
                elif i == 'U':
                    l[n] = 'D'
                elif i == 'L':
                    l[n] = 'R'
                elif i == 'D':
                    l[n] = 'U'

        elif l[0] == "z":
            del l[0]
            for n, i in enumerate(l):
                if i == 'R':
                    l[n] = 'D'
                elif i == 'U':
                    l[n] = 'R'
                elif i == 'L':
                    l[n] = 'U'
                elif i == 'D':
                    l[n] = 'L'

        elif l[0] == "Terminat!":
            del l[0]
            print("Cubul a fost rezolvat! Introdu alt cub si apasa 'Solve' pentru a-l rezolva!")
            print(" ")
            ElevatorDown()
            FlipperDown()
            FlipperUp()
            status()
            s1.write(b'h')
            b3 = time.time()

            t1 = b1 - a1
            t2 = b2 - a2
            t3 = b3 - a3
            t = t1 + t2 + t3
            if q == 1:
                med = 0
            else:
                med = t3 / (q - 1)

            print('Scanarea a durat ' + str(round(t1, 2)) + ' secunde.')
            print('Analizarea imaginilor si cautarea solutiei a durat ' + str(round(t2, 2)) + ' secunde.')
            print('Rezolvarea cubului a durat ' + str(round(t3, 2)) + ' secunde.')
            print('Timp mediu pe mutare: ' + str(round(med, 2)) + ' secunde.')
            print('Timp total: ' + str(round(t, 2)) + ' secunde.')

        else:

            i = i + 1
            print("Prea multe mutari:" + i)

    return (t)

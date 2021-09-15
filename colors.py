import cv2
import numpy as np

res = 4    #setting resolution: 1 means 200x200, 4 means 400x400, 16 means 800x800
size = 5
#im1 = cv2.imread('/home/pi/MultiCuber/CubeScan/rubiks-side-U.png')
    
def extractor(frame):
    
    coord = []     #a list for coordonates of centers of squares
    image = frame
    original = image.copy()
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask = np.zeros(hsv.shape, dtype=np.uint8)
    
    Umin = np.array([18,50,50],np.uint8)    #yellow lower and upper
    Umax = np.array([48,255,255],np.uint8)

    Fmin = np.array([50,60,50],np.uint8)    #green
    Fmax = np.array([90,255,255],np.uint8)

    R1min = np.array([160,50,140],np.uint8)    #orange
    R1max = np.array([180,255,255],np.uint8)
    R2min = np.array([0,50,140],np.uint8)    
    R2max = np.array([6,255,255],np.uint8)

    L1min = np.array([0,100,0],np.uint8)    #red - for now this program cannot distinguish very well orange from red...
    L1max = np.array([6,255,190],np.uint8)
    L2min = np.array([160,100,0],np.uint8)
    L2max = np.array([180,255,190],np.uint8)

    Bmin = np.array([90,60,50],np.uint8)    #blue
    Bmax = np.array([120,255,255],np.uint8)

    Dmin = np.array([0,0,100],np.uint8)    #white
    Dmax = np.array([180,60,255],np.uint8)

    galben = cv2.inRange(hsv, Umin, Umax)
    verde = cv2.inRange(hsv, Fmin, Fmax)
    portocaliu1 = cv2.inRange(hsv, R1min, R1max)
    portocaliu2 = cv2.inRange(hsv, R2min, R2max)
    rosu1 = cv2.inRange(hsv, L1min, L1max)
    rosu2 = cv2.inRange(hsv, L2min, L2max)
    albastru = cv2.inRange(hsv, Bmin, Bmax)
    alb = cv2.inRange(hsv, Dmin, Dmax)
    portocaliu = portocaliu1 + portocaliu2
    rosu = rosu1 + rosu2
    
    cnts, _ = cv2.findContours(galben, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for c in cnts:        
        x,y,w,h = cv2.boundingRect(c)
        area = cv2.contourArea(c)
        if area > 12*12*res and area < 25*25*res and abs(w-h)<5*res:
                
            M = cv2.moments(c)
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            msk=galben[cy,cx]
            if msk==255:
                letterg = "U"
                coord.append((cx,cy,letterg))
                cv2.rectangle(original, (cx-6, cy-6), (cx+6, cy + 6), (0,0,0), 4)
                cv2.rectangle(original, (x, y), (x + w, y + h),(0,255,255) , 2)
        
    cnts, _ = cv2.findContours(verde, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for c in cnts:        
        x,y,w,h = cv2.boundingRect(c)
        area = cv2.contourArea(c)
        if area > 12*12*res and area < 25*25*res and abs(w-h)<5*res:
            
            M = cv2.moments(c)
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            msk=verde[cy,cx]
            if msk==255:
                letterv = "F"
                coord.append((cx,cy,letterv))
                cv2.rectangle(original, (cx-6, cy-6), (cx+6, cy + 6), (0,0,0), 4)
                cv2.rectangle(original, (x, y), (x + w, y + h),(0,255,0) , 2)
    
    cnts, _ = cv2.findContours(portocaliu, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for c in cnts:        
        x,y,w,h = cv2.boundingRect(c)
        area = cv2.contourArea(c)
        if area > 12*12*res and area < 25*25*res and abs(w-h)<5*res:
                
            M = cv2.moments(c)
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            msk=portocaliu[cy,cx]
            if msk==255:
                letterp = "R"
                coord.append((cx,cy,letterp))
                cv2.rectangle(original, (cx-6, cy-6), (cx+6, cy + 6), (0,0,0), 4)
                cv2.rectangle(original, (x, y), (x + w, y + h),(0,191,255) , 2)
    
    cnts, _ = cv2.findContours(albastru, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for c in cnts:        
        x,y,w,h = cv2.boundingRect(c)
        area = cv2.contourArea(c)
        if area > 12*12*res and area < 25*25*res and abs(w-h)<5*res:
                
            M = cv2.moments(c)
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            msk=albastru[cy,cx]
            if msk==255:
                lettera = "B"
                coord.append((cx,cy,lettera))
                cv2.rectangle(original, (cx-6, cy-6), (cx+6, cy + 6), (0,0,0), 4)
                cv2.rectangle(original, (x, y), (x + w, y + h),(255,0,0) , 2)
    
    cnts, _ = cv2.findContours(rosu, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for c in cnts:        
        x,y,w,h = cv2.boundingRect(c)
        area = cv2.contourArea(c)
        if area > 12*12*res and area < 25*25*res and abs(w-h)<5*res:
                
            M = cv2.moments(c)
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            msk=rosu[cy,cx]
            if msk==255:
                letterr = "L"
                coord.append((cx,cy,letterr))
                cv2.rectangle(original, (cx-6, cy-6), (cx+6, cy + 6), (0,0,0), 4)
                cv2.rectangle(original, (x, y), (x + w, y + h),(0,0,255) , 2)
    
    cnts, _ = cv2.findContours(alb, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for c in cnts:        
        x,y,w,h = cv2.boundingRect(c)
        area = cv2.contourArea(c)
        if area > 12*12*res and area < 25*25*res and abs(w-h)<5*res:
            
            M = cv2.moments(c)
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            msk=alb[cy,cx]
            if msk==255:
                letteralb = "D"
                coord.append((cx,cy,letteralb))
                cv2.rectangle(original, (cx-6, cy-6), (cx+6, cy + 6), (0,0,0), 4)
                cv2.rectangle(original, (x, y), (x + w, y + h),(255,255,255) , 2)
            
    return(original,coord)

#original, coord = extractor(im1)
#cv2.imwrite('test.jpg',original)
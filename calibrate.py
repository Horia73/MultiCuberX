import cv2
global k

res = 4
k = 0

def extractor4(frame):
    global k
    l = []
    l1 = []
    l2 = []
    l3 = []
    frame1 = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    i = 14
    j = 0
    
    for x in range(4):
        
        for x in range (4):
            j=j+20
            for x in range(6):
                i = i+1
                for x in range(6):
                    j = j+1
                    (h,s,v) = frame1[i*res,j*res]
                    #print(h,s,v)
                    l1.append(h)
                    l2.append(s)
                    l3.append(v)
                    frame[i*res,j*res] = (255,255,255)
                j=j-6
            i=i-6
        j=0
        i=i+20    
        
    k = k+1
    if k==7:
        k=1
    cv2.imwrite('c%d.jpg' %k, frame)
    a = sum(l1)/len(l1)
    b = sum(l2)/len(l2)
    c = sum(l3)/len(l3)
    d = min(l1)
    e = min(l2)
    f = min(l3)
    g = max(l1)
    h = max(l2)
    i = max(l3)
    
    l.append(round(a))
    l.append(round(b))
    l.append(round(c))
    
    return(l,d,e,f,g,h,i)    
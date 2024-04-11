import cv2 as cv
import numpy as np
import math

img=cv.imread(r"C:\Users\Chetna\Downloads\shapes.jpg")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

canny = cv.Canny (gray, 125, 175)

contours, hierarchies = cv.findContours (canny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

def rat(x,y,x1,y1):
    #print(x,y)
    try:
        j=math.dist(x,y)/math.dist(x1,y1)
    except ZeroDivisionError:
        j = 0
    if j>0.8 and j<1.2:
        return True
    else:
        return False

    
sh=input("enter shape name : ")
sh.lower()
fs=0.5

for x in contours:
    
    app = cv.approxPolyDP(x, 0.01 * cv.arcLength(x, True), True)
    
    i, j = app[0][0]

    
    if len(app) == 3:
        if sh=="triangle":
            cv.putText(img, "Triangle", (i, j), cv.FONT_HERSHEY_COMPLEX, fs, 0, 1)
            break
       
    elif len(app) == 4:
        
        l=app[0][0] #1
        
        k=app[len(app)//2][0] #3
        
        m=app[len(app)//4][0] #2
        n=app[3*len(app)//4][0] #4
        print(l,m,n,k)

            
        if rat(l,m,m,k):
            if rat(l,k,m,n):
                if sh=="square":
                    cv.putText(img, "square", (i, j), cv.FONT_HERSHEY_COMPLEX, fs, 0, 1)
                    break
                
            else:
                if sh=="rhombus":
                    cv.putText(img, "rhombus", (i, j), cv.FONT_HERSHEY_COMPLEX,fs, 0, 1)
                    break
            
        elif rat(l,m,n,k):
            if rat(l,k,m,n):
                if sh=="rectangle":
                    cv.putText(img, "rectangle", (i, j), cv.FONT_HERSHEY_COMPLEX, fs, 0, 1)
                    break
                
            else :
                if sh=="parellelogram":
                    cv.putText(img, "parellelogram", (i, j), cv.FONT_HERSHEY_COMPLEX, fs, 0, 1)
                    break
                
        else:
            if sh=="quadrilateral":
                cv.putText(img, "quadrilateral", (i, j), cv.FONT_HERSHEY_COMPLEX, fs, 0, 1)
                break
            
            
    elif len(app) == 5:
        if sh=="pentagon":
            cv.putText(img, "Pentagon", (i, j), cv.FONT_HERSHEY_COMPLEX, fs, 0, 1)
            break
        
    elif len(app) == 6:
        if sh=="hexagon":
            cv.putText(img, "hexagon", (i, j), cv.FONT_HERSHEY_COMPLEX, fs, 0,1)
            break

    elif len(app) == 7:
        if sh=="heptagon":
            cv.putText(img, "heptagon", (i, j), cv.FONT_HERSHEY_COMPLEX, fs, 0, 1)
            break

    elif len(app) == 8:
        if sh=="octagon":
            cv.putText(img, "octagon", (i, j), cv.FONT_HERSHEY_COMPLEX, fs, 0, 1)
            break

    elif len(app) == 10:
        if sh=="star":
            cv.putText(img, "star", (i, j), cv.FONT_HERSHEY_COMPLEX, fs, 0, 1)
            break
         
    else:
        l=app[0][0] #1
        k=app[len(app)//2][0] #3
        m=app[len(app)//4][0] #2
        n=app[3*len(app)//4][0] #4

        if rat(l,k,m,n):
            if sh=="circle":
                cv.putText(img, "Circle", (i, j),cv.FONT_HERSHEY_COMPLEX, fs, 0, 1)
                break
            
        else:
            if sh=="ellipse":
                cv.putText(img, "ellipse", (i, j),cv.FONT_HERSHEY_COMPLEX, fs, 0, 1)
                break

else:
    print("no such object found")
    

hola=cv.drawContours(img, x, -1, 0, 1)

cv.imshow('shapes',img)
cv.waitKey(1)

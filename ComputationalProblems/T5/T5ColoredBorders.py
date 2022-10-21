from turtle import bgcolor
import cv2 as cv
import numpy as np
from sqlalchemy import false

capture = cv.VideoCapture("ComputationalProblems\\T5\\vids\\Red.mp4")

picMode = False

# Predefined Colors - BGR - YOU CAN CHANGE IT ACCORDING TO YOUR NEEDS
WATERCOLOR = np.array([255,0,0])
TEACOLOR = np.array([0,255,0])
COFFECOLOR = np.array([0,0,255])

def isBlack(pixel):
    if pixel[0] < 20 and pixel[1] < 20 and pixel[2] < 20:
        return True
    else:
        return False
def isDark(pixel,bgCol):
    if pixel[0] < 250 or pixel[1] < 250 or pixel[2] < 250:
        return True
    else:
        return False

def isBg(pixel,bgCol):
    
    res = np.linalg.norm(bgCol - pixel,2) <= 20
    return res

def isNorBlackNorWhite(pixel):
    if (pixel[0] != 0 or pixel[1] != 0 or pixel[2] != 0) and (pixel[0] != 255 or pixel[1] != 255 or pixel[2] != 255):
        return True
    else:
        return False
def isWhite(pixel):
    if pixel[0] == 255 and pixel[1] == 255 and pixel[2] == 255:
        return True
    else:
        return False

def calculateArea(frame):
    area = 0
    colSize = frame.shape[1]
    RClist = []
    BoundList = []
    bgCol = frame[5][5]
    # print(bgCol)
    for rowIndex,row in enumerate(frame):
        rowSum = 0
        start = False
        end = False
        lPoint = 0
        rPoint = 0
        for colIndex,col in enumerate(row):
            if not isBg(col,bgCol):
                # print(rowIndex,colIndex)
                nIndex = colIndex + 1
                if nIndex < colSize:
                    if not start and isBg(frame[rowIndex][nIndex],bgCol):
                        start = True
                        end = False
                        lPoint = colIndex
                        RClist.append([rowIndex,colIndex])
                        

            if start and not end and not isBg(col,bgCol):
                rPoint = colIndex
                if(lPoint < rPoint):
                    RClist.append([rowIndex,colIndex])
                    BoundList.append([rowIndex,(lPoint,rPoint)])
                    # print(lPoint,rPoint)
                    end = True
                    start = False
                    lPoint = rPoint
            
    for bound in BoundList:
        area += bound[1][1] - bound[1][0]

    print("Area : ",area)
    # WORKS HELLA FINE xD
    return (area,RClist,BoundList)

def guessLiquid(pixel):
    bgr = [False] * 3 # rgb boolean list
    # print(pixel,bgr)
    # if not isNorBlackNorWhite(pixel):
    #     return bgr


    # Mini variation of K means clustering - Using only Euclidean distances
    wp = np.linalg.norm(pixel - WATERCOLOR,ord=2)
    tp = np.linalg.norm(pixel - TEACOLOR,ord=2)
    cp = np.linalg.norm(pixel - COFFECOLOR,ord=2)
    minn = min(wp,tp,cp)
    if minn == wp:
        bgr[0] = True
    elif minn == tp:
        bgr[1] = True
    elif minn == cp:
        bgr[2] = True
    # print(pixel,bgr)
    return bgr

def calculateFill(frame,BoundList):
    wFill = 0
    tFill = 0
    cFill = 0
    colSize = frame.shape[1]      
    allsum = 0
    bgCol = frame[0][0]
    for bound in BoundList:
        wSum = 0
        tSum = 0
        cSum = 0
        avgInd = int(bound[1][0] + (bound[1][1] - bound[1][0]) / 2)
        
        rowSum = bound[1][1] - bound[1][0] 
        if isBg(frame[bound[0]][avgInd],bgCol):
            continue

        # if not isNorBlackNorWhite(frame[bound[0],avgInd]):
        #     continue
        allsum += rowSum
        # print(frame[bound[0]][avgInd])
        gbr = guessLiquid(frame[bound[0]][avgInd])
        
        if gbr[0]:
            wSum = rowSum
        if gbr[1]:
            tSum = rowSum
        if gbr[2]:
            cSum = rowSum

        wFill += wSum
        tFill += tSum
        cFill += cSum

    # WORKS HELLA FINE xD
    print("Fill in %:")
    print("-------------------------------------------")
    print("Water: ",wFill)
    print("Tea: ", tFill)
    print("Coffe:",cFill)
    print("AllSum: ",allsum)
    print("-------------------------------------------")
    return (wFill,tFill,cFill)


areaCalculated = False
area = 0
fill = 0
RClist = []
while True and not picMode:
    isTrue,frame = capture.read()
    # print(frame.shape)
    if not isTrue:
        break
 
    if not areaCalculated:
        area,RClist,BoundList = calculateArea(frame)
        areaCalculated = True
    # print(area)
    # print(BoundList)
    wFill,tFill,cFill = calculateFill(frame,BoundList)

    wp = int(round(wFill/area, 2)*100)
    tp = int(round(tFill/area, 2)*100)
    cp = int(round(cFill/area, 2)*100)

    print("-----------------")
    print(f"{wp}% ± 1% Water")
    print(f"{tp}% ± 1% Tea")
    print(f"{cp}% ± 1% Coffe")
    print("-----------------")
    resString = str(wp) + "% Water |" + "| " +  str(tp) + "% Tea |" + str(cp) + "% Coffe"
    font = cv.FONT_HERSHEY_SIMPLEX
    cv.putText(frame, resString, (20,650), font, .5, (255, 0, 0), 0, cv.LINE_AA)

    cv.imshow("Video", frame)
    cv.waitKey(100)
   
    if cv.waitKey(20) & 0xFF == ord('d'):
        capture.release()
        cv.destroyAllWindows()
        break

if picMode:
    isTrue, frame = capture.read()
    frame = cv.imread('ComputationalProblems\\T5\\imgs\\.png')
    
    area,RClist,BoundList = calculateArea(frame)

    cv.imshow('Video', frame)

    wFill,tFill,cFill = calculateFill(frame,BoundList)
    wp = int(round(wFill/area, 2)*100)
    tp = int(round(tFill/area, 2)*100)
    cp = int(round(cFill/area, 2)*100)

    print("-----------------")
    print(f"{wp}% ± 1% Water")
    print(f"{tp}% ± 1% Tea")
    print(f"{cp}% ± 1% Coffe")
    print("-----------------") 
    # print(waterFill)
    
    cv.waitKey(10000)
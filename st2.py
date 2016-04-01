import numpy as np
import cv2
import sys
from matplotlib import pyplot as plt

# imgL = cv2.imread('Yeuna9x.png',0)
# imgR = cv2.imread('SuXT483.png',0)
k = 0
D = 0.0
dd = 0
DD = 0.0

for i in range(10):
    capL = cv2.VideoCapture(int(sys.argv[1]))
    capR = cv2.VideoCapture(int(sys.argv[2]))
    ret1, frame1 = capL.read()
    imgL = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    ret2, frame2 = capR.read()
    imgR = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

    stereo = cv2.StereoBM_create(0, 19)
    disparity = stereo.compute(imgL, imgR)

    D = 0
    k = 0
    for y in range(100):
        for x in range(200):
            k += 1
            d = disparity[190 + y][220 + x]
            if d > 0:
                print(d)
                D += d
                dd = d
            else:
                D += dd
    DD += D / k
    print(D / k)
    del(capR)
    del(capL)

print(DD / 10)

import numpy as np
import cv2
from matplotlib import pyplot as plt
import sys

capL = cv2.VideoCapture(int(sys.argv[1]))
capR = cv2.VideoCapture(int(sys.argv[2]))

ret1, frame1 = capL.read()
imgL = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
ret2, frame2 = capR.read()
imgR = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

window_size = int(sys.argv[3])
minDisparity = int(sys.argv[4])
numDisparities = 112 - minDisparity
blockSize = int(sys.argv[5])
P1 = 8*3*window_size**2,
P2 = 32*3*window_size**2,
disp12MaxDiff = int(sys.argv[6]),
uniquenessRatio = int(sys.argv[7]),
speckleWindowSize = int(sys.argv[8]),
speckleRange = int(sys.argv[9])

print(
    "minDisparity = %s\n" % (minDisparity),
    "numDisparities = %s\n" % (numDisparities),
    "blockSize = %s\n" % (blockSize),
    "P1 = %s\n" % (P1),
    "P2 = %s\n" % (P2),
    "disp12MaxDiff = %s\n" % (disp12MaxDiff),
    "uniquenessRatio = %s\n" % (uniquenessRatio),
    "speckleWindowSize = %s\n" % (speckleWindowSize),
    "speckleRange = %s\n" % (speckleRange),
)
stereo = cv2.StereoSGBM_create(
    minDisparity = minDisparity,
    numDisparities = numDisparities,
    blockSize = blockSize,
    P1 = P1[0],
    P2 = P2[0],
    disp12MaxDiff = disp12MaxDiff[0],
    uniquenessRatio = uniquenessRatio[0],
    speckleWindowSize = speckleWindowSize[0],
    speckleRange = speckleRange,
)

disparity = stereo.compute(imgL,imgR).astype(np.float32) / 16.0



cv2.imshow('left', frame1)
cv2.imshow('right', frame2)
cv2.imshow('disp', (disparity - minDisparity) / numDisparities)
cv2.waitKey()
cv2.destroyAllWindows()

capL.release()
capR.release()

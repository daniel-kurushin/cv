import numpy as np
import cv2
import sys
from matplotlib import pyplot as plt
imgL = cv2.imread('/home/dan/Yandex.Disk/Src/cv/IMG_20160511_174552.jpg',0)
imgR = cv2.imread('/home/dan/Yandex.Disk/Src/cv/IMG_20160511_174556.jpg',0)


# imgR = cv2.imread('Yeuna9x.png',0)
# imgL = cv2.imread('SuXT483.png',0)

# capL = cv2.VideoCapture(0)
# capR = cv2.VideoCapture(1)
# ret1, frame1 = capL.read()
# imgL = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
# ret2, frame2 = capR.read()
# imgR = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

stereo = cv2.StereoBM_create(0, 25)
disparity = stereo.compute(imgL, imgR)

# f = open('/tmp/%s' % (sys.argv[1]),'w')
# for y in range(96):
# 	for x in range(128):
# 		z = disparity[y*5][x*5]
# 		if z > 0:
# 			z = -2.6162 + 2089.6758 / z
# 			f.write("%s %s %s\n" % (x,y,z))
# 		else:
# 			z = 0
# 		# if 300 < z < 600: 

# f.close()
# d=-2.6162+2089.6758/x
plt.imshow(disparity,'gray')
plt.show()
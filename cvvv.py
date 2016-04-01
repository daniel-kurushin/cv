import numpy as np
import cv2
from matplotlib import pyplot as plt

img1 = cv2.imread('../0.png')
img2 = cv2.imread('../1.png')
rows, cols = 480, 640

pts1 = 
pts2 = 

dst = cv2.warpAffine(img2,cv2.getAffineTransform(
    np.float32([[10,10],[600,10],[600,400]]),
    np.float32([[10,20],[600,30],[600,420]])
),(cols,rows))

plt.subplot(121),plt.imshow(img1),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()

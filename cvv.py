import numpy as np
import cv2
from matplotlib import pyplot as plt
import sys
from urllib import request

MIN_MATCH_COUNT = 5

if len(sys.argv) == 4:
    resp = request.urlopen('http://192.168.0.100/jpg/1/image.jpg')
    imgL = np.asarray(bytearray(resp.read()), dtype="uint8")
    imgL = cv2.imdecode(imgL, cv2.IMREAD_COLOR)    
    img1 = cv2.imread(sys.argv[3],0) # queryImage
else:
    exit(2)

# Initiate SIFT detector
sift = cv2.xfeatures2d.SIFT_create()

# find the keypoints and descriptors with SIFT
kp1, des1 = sift.detectAndCompute(img1,None)
kp2, des2 = sift.detectAndCompute(imgL,None)

FLANN_INDEX_KDTREE = 0
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
search_params = dict(checks = 50)

flann = cv2.FlannBasedMatcher(index_params, search_params)
matches = flann.knnMatch(des1,des2,k=2)

# store all the good matches as per Lowe's ratio test.
good = []
for m,n in matches:
    if m.distance < 0.7*n.distance:
        good.append(m)

if len(good)>MIN_MATCH_COUNT:
    src_pts = np.float32([ kp1[m.queryIdx].pt for m in good ]).reshape(-1,1,2)
    dst_pts = np.float32([ kp2[m.trainIdx].pt for m in good ]).reshape(-1,1,2)

    M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC,5.0)
    matchesMask = mask.ravel().tolist()

    h,w = img1.shape
    pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)
    dst = cv2.perspectiveTransform(pts,M)

    H = max(dst[1][0][1],dst[2][0][1]) - min(dst[0][0][1],dst[3][0][1])
    W = max(dst[2][0][0],dst[3][0][0]) - min(dst[1][0][0],dst[0][0][0])

    print(h/w,H/W)
# [[[190  96]]

#  [[190 402]]

#  [[331 359]]

#  [[419  95]]]

    imgL = cv2.polylines(imgL,[np.int32(dst)],True,255,3, cv2.LINE_AA)

else:
    print ("Not enough matches are found - %d/%d" % (len(good),MIN_MATCH_COUNT))
    matchesMask = None


draw_params = dict(matchColor = (0,255,0), # draw matches in green color
                   singlePointColor = None,
                   matchesMask = matchesMask, # draw only inliers
                   flags = 2)

img2 = cv2.drawMatches(img1,kp1,imgL,kp2,good,None,**draw_params)

plt.imshow(img2, 'gray'),plt.show()


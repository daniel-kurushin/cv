from math import *
from datetime import *
from urllib.request import urlopen
import numpy as np
import cv2	
import sys

try:
	mismp_speed = int(sys.argv[1])
	mismp_dist = int(sys.argv[2])
except Exception:
	print("Usage %s [0-5] [0-5]" % (sys.argv[0]), file = sys.stderr)
	print("1-st arg -- speed (m/s)", file = sys.stderr)
	print("2-nd arg -- distance (m)", file = sys.stderr)
	print("", file = sys.stderr)
	exit(1)

k_lft = 1
k_mdl = 1/30
k_rgt = 1

MOVE_URL="http://192.168.0.101:8000/manual/"
move = 0

cap = cv2.VideoCapture("http://192.168.0.115/axis-cgi/mjpg/video.cgi?resolution=320x240")
t0 = datetime.now()
t1 = t0
t_start = t0
Dt_1 = 0
spd_mdl = 0.0
# params for ShiTomasi corner detection
feature_params = dict( maxCorners = 100,
						qualityLevel = 0.3,
						minDistance = 7,
						blockSize = 7 )

# Parameters for lucas kanade optical flow
lk_params = dict( winSize  = (15,15),
						maxLevel = 2,
						criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

# Create some random colors
color = np.random.randint(0,255,(100,3))

# Take first frame and find corners in it
ret, old_frame = cap.read()
old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)
p0 = cv2.goodFeaturesToTrack(old_gray, mask = None, **feature_params)

# Create a mask image for drawing purposes
mask = np.zeros_like(old_frame)

open('/tmp/log','w').write("\n")

while(1):
	ret,frame = cap.read()

	t = datetime.now()
	Dt = (t - t0).microseconds / 1000000
	Dt_1 += (t - t1).microseconds
	t0 = t

	if (t - t_start).seconds == 1 and move == 0:
		cmd = "angle=0&speed=0"
		post = cmd.encode('UTF-8')
		response = urlopen(MOVE_URL, post)
		print(response.read())
		move = 1
		exit(1)
	elif (t - t_start).seconds == 5 and move == 1:
		cmd = "angle=0&speed=0"
		post = cmd.encode('UTF-8')
		response = urlopen(MOVE_URL, post)
		print(response.read())
		move = 0
	elif (t - t_start).seconds == 7 and move == 0:
		cmd = "angle=0&speed=-3"
		post = cmd.encode('UTF-8')
		response = urlopen(MOVE_URL, post)
		print(response.read())
		move = -1
	elif (t - t_start).seconds == 11 and move == -1:
		cmd = "angle=0&speed=0"
		post = cmd.encode('UTF-8')
		response = urlopen(MOVE_URL, post)
		print(response.read())
		move = 0
	elif (t - t_start).seconds == 13:
		exit(0)

	frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	# calculaangle=-0&speed=0te optical flow
	p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)

	# Select good points
	good_new = p1[st==1]
	good_old = p0[st==1]

	dx_lft, dx_mdl, dx_rgt, nn_lft, nn_mdl, nn_rgt = [0]*6

	for i,(new,old) in enumerate(zip(good_new,good_old)):
		a,b = new.ravel()
		c,d = old.ravel()
		if ((0 < a < 55) or (132 < a < 187) or (265 < a < 320)) and \
		   ((0 < c < 55) or (132 < c < 187) or (265 < c < 320)):
			if 0 < a < 55:
				dx_lft += sqrt((a-c)**2+(b-d)**2)
				nn_lft += 1
			if 132 < a < 187:
				dx_mdl += sqrt((a-c)**2+(b-d)**2)
				nn_mdl += 1
			if 265 < a < 320:
				dx_rgt += sqrt((a-c)**2+(b-d)**2)
				nn_rgt += 1
	# 	mask = cv2.line(mask, (a,b),(c,d), color[i].tolist(), 2)
	# 	frame = cv2.circle(frame,(a,b),5,color[i].tolist(),-1)
	# img = cv2.add(frame,mask)
	
	# cv2.imshow('frame',img)
	# k = cv2.waitKey(30) & 0xff
	# if k == 27:
	# 	break

	if Dt_1 > 2000000:
		Dt_1 = 0
	else:
		try:
			spd_mdl += k_mdl * ( dx_mdl / nn_mdl ) / Dt
		except ZeroDivisionError:
			spd_mdl += 0
	try:
		spd_lft = k_lft * ( dx_lft / nn_lft ) / Dt
	except ZeroDivisionError:
		spd_lft = 0
	try:
		spd_rgt = k_rgt * ( dx_rgt / nn_rgt ) / Dt
	except ZeroDivisionError:
		spd_rgt = 0

	print(t.second, spd_lft, spd_mdl, spd_rgt)

	# Now update the previous frame and previous points
	old_gray = frame_gray.copy()
	p0 = good_new.reshape(-1,1,2)

cv2.destroyAllWindows()
cap.release()


# POST
# MOVE_URL="http://192.168.0.101:8000/manual/"
# angle=-0&speed=0


# from urllib.request import urlopen
# CAMERA_URL = 'http://192.168.0.122:5555/'


# result = self.from_camera(CAMERA_URL + 'state')
# 	print(result)
# 	if data['key'][0] == 'a':
# 		cmd = {
# 			'a': result.get('a') / KX + int(data['value'][0]),
# 			'b': result.get('b') / KX,
# 			'speed': 3000
# 		}
# 	elif data['key'][0] == 'b':
# 		cmd = {
# 			'a': result.get('a') / KX,
# 			'b': result.get('b') / KX + int(data['value'][0]),
# 			'speed': 3000
# 		}
# 	print(cmd)
# 	post = json.dumps(cmd).encode('UTF-8')
# 	response = urlopen(CAMERA_URL + 'rotate', post)
# 	#print(response.read())
# 	self.load_str(response.read().decode('UTF-8'))
# elif self.path.startswith('/camera2/'):
# 	result = self.from_camera(CAMERA_URL + 'state')
# 	command = data.get('command')[0]
# 	print(data)
# 	if command == 'range':
# 		response = urlopen(
# 			CAMERA_URL + 'range',
# 			json.dumps({'a': result.get('a') / KX, 'b': result.get('b') / KX, 'speed': 3000}).encode('UTF-8')
# 		)
# 		self.load_str(response.read().decode('UTF-8'))
# 	elif command == 'recognize':
# 		response = urlopen(
# 			CAMERA_URL + 'recognize',
# 			json.dumps({
# 				'a': {'min': result.get('a') / KX - 50, 'max': result.get('a') / KX + 50},
# 				'b': {'min': result.get('b') / KX - 1, 'max': result.get('b') / KX + 1}
# 			}).encode('UTF-8')
# 		)
# 		self.load_str(response.read().decode('UTF-8'))
# 	else:
# 		self.load_str('ok')


# response = urlopen(url)
# 		return json.loads(response.read().decode("utf-8"))
import numpy as np
import cv2
import matplotlib.pyplot as plt
import matcher
from scipy.spatial import distance
from PIL import Image

#%matplotlib inline
plt.ion()

img1 = cv2.imread('sample_image/coke2.jpg',0) # query image
img2 = cv2.imread('sample_image/coke2.jpg',0)
#------------------------------------------------
hessian_th = 400
surf = cv2.xfeatures2d.SURF_create(hessian_th)
star = cv2.xfeatures2d.StarDetector_create()
brief = cv2.xfeatures2d.BriefDescriptorExtractor_create()
fast = cv2.FastFeatureDetector_create()
brief = cv2.xfeatures2d.BriefDescriptorExtractor_create()

transx=0
transy=0
translated=0
while translated <=500:
	filename = "./Tranlacao em x %d.jpg"%transx
	M2T = np.float32([[1,0,transx],[0,1,transy]])
	rows2t,cols2t = img2.shape
	desloc2 =cv2.warpAffine(img2,M2T,(cols2t,rows2t))
	matcher.draw_ransac(img1, desloc2, cv2.ORB_create(), cv2.ORB_create(), is_binary_descriptor=True, match_method='BRUTE_FORCE', description='ORB, BRUTE_FORCE, RANSAC')
	#plt.figure(figsize=(16, 12))
	#plt.title(filename)
	#plt.imshow(desloc2,cmap='gray')
	#plt.show()
	#plt.savefig(filename)
	transx+=50
	translated+=50

transx=0
transy=0
translated=0
while translated <=500:
	filename = "./Tranlacao em x %d.jpg"%transx
	M2T = np.float32([[1,0,transx],[0,1,transy]])
	rows2t,cols2t = img2.shape
	desloc2 =cv2.warpAffine(img2,M2T,(cols2t,rows2t))

	matcher.draw_ransac(img1, desloc2, cv2.xfeatures2d.SIFT_create(nfeatures=25), cv2.xfeatures2d.SIFT_create(nfeatures=25), is_binary_descriptor=False, match_method='BRUTE_FORCE', description='SIFT, BRUTE_FORCE, RANSAC')	
	#plt.figure(figsize=(16, 12))
	#plt.title(filename)
	#plt.imshow(desloc2,cmap='gray')
	#plt.show()
	#plt.savefig(filename)
	transx+=50
	translated+=50	
transx=0
transy=0
translated=0
while translated <=500:
	filename = "./Tranlacao em x %d.jpg"%transx
	M2T = np.float32([[1,0,transx],[0,1,transy]])
	rows2t,cols2t = img2.shape
	desloc2 =cv2.warpAffine(img2,M2T,(cols2t,rows2t))

	
	matcher.draw_ransac(img1, desloc2, surf, surf,is_binary_descriptor=False, match_method='BRUTE_FORCE', description='SURF, BRUTE_FORCE, RANSAC')
	#plt.figure(figsize=(16, 12))
	#plt.title(filename)
	#plt.imshow(desloc2,cmap='gray')
	#plt.show()
	#plt.savefig(filename)
	transx+=50
	translated+=50	

transx=0
transy=0
translated=0
while translated <=500:
	filename = "./Tranlacao em x %d.jpg"%transx
	M2T = np.float32([[1,0,transx],[0,1,transy]])
	rows2t,cols2t = img2.shape
	desloc2 =cv2.warpAffine(img2,M2T,(cols2t,rows2t))

	
	matcher.draw_ransac(img1, desloc2, star, brief, is_binary_descriptor=True, match_method='BRUTE_FORCE', description='STAR + BRIEF, BRUTE_FORCE, RANSAC')	
	#plt.figure(figsize=(16, 12))
	#plt.title(filename)
	#plt.imshow(desloc2,cmap='gray')
	#plt.show()
	#plt.savefig(filename)
	transx+=50
	translated+=50	
transx=0
transy=0
translated=0
while translated <=500:
	filename = "./Tranlacao em x %d.jpg"%transx
	M2T = np.float32([[1,0,transx],[0,1,transy]])
	rows2t,cols2t = img2.shape
	desloc2 =cv2.warpAffine(img2,M2T,(cols2t,rows2t))

	
	matcher.draw_ransac(img1, desloc2, fast, brief, is_binary_descriptor=True, match_method='BRUTE_FORCE', description='FAST + BRIEF, BRUTE_FORCE, RANSAC')
	#plt.figure(figsize=(16, 12))
	#plt.title(filename)
	#plt.imshow(desloc2,cmap='gray')
	#plt.show()
	#plt.savefig(filename)
	transx+=50
	translated+=50	

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

fx=0.25
fy=1.0
scale=0
#rescalando em x e y
while scale <=3:
	small2 = cv2.resize(img2, (0,0), fx=fx, fy=fy) 
	filename = "./escala em  x %f e y %f"%(fx,fy)
	#plt.figure(figsize=(16, 12))
	#plt.title(filename)
	#plt.imshow(small2,cmap='gray')
	#plt.show()
	#plt.savefig(filename)
	matcher.draw_ransac(img1, small2, cv2.ORB_create(nfeatures=25), cv2.ORB_create(nfeatures=25),  is_binary_descriptor=True, match_method='BRUTE_FORCE',  description='ORB, BRUTE_FORCE, RANSAC'+str(fx))
	fx+=0.25
	scale+=1

fx=0.25
fy=1.0
scale=0
while scale <=3:
	small2 = cv2.resize(img2, (0,0), fx=fx, fy=fy) 
	filename = "./escala em  x %f e y %f"%(fx,fy)
	#plt.figure(figsize=(16, 12))
	#plt.title(filename)
	#plt.imshow(small2,cmap='gray')
	#plt.show()
	#plt.savefig(filename)
	matcher.draw_ransac(img1, small2, cv2.xfeatures2d.SIFT_create(nfeatures=25), cv2.xfeatures2d.SIFT_create(nfeatures=25),	is_binary_descriptor=False,	match_method='BRUTE_FORCE', description='SIFT, BRUTE_FORCE, RANSAC'+str(fx))	
	fx+=0.25
	scale+=1


fx=0.25
fy=1.0
scale=0
while scale <=3:
	small2 = cv2.resize(img2, (0,0), fx=fx, fy=fy) 
	filename = "./escala em  x %f e y %f"%(fx,fy)
	#plt.figure(figsize=(16, 12))
	#plt.title(filename)
	#plt.imshow(small2,cmap='gray')
	#plt.show()
	#plt.savefig(filename)
	matcher.draw_ransac(img1, small2, surf,	surf, is_binary_descriptor=False, match_method='BRUTE_FORCE', description='SURF, BRUTE_FORCE, RANSAC'+str(fx))
	fx+=0.25
	scale+=1
	
fx=0.25
fy=1.0
scale=0
while scale <=3:
	small2 = cv2.resize(img2, (0,0), fx=fx, fy=fy) 
	filename = "./escala em  x %f e y %f"%(fx,fy)
	#plt.figure(figsize=(16, 12))
	#plt.title(filename)
	#plt.imshow(small2,cmap='gray')
	#plt.show()
	#plt.savefig(filename)
	matcher.draw_ransac(img1, small2, star,	brief, is_binary_descriptor=True, match_method='BRUTE_FORCE', description='STAR + BRIEF, BRUTE_FORCE, RANSAC'+str(fx))
	fx+=0.25
	scale+=1


fx=0.25
fy=1.0
scale=0
while scale <=3:
	small2 = cv2.resize(img2, (0,0), fx=fx, fy=fy) 
	filename = "./escala em  x %f e y %f"%(fx,fy)
	#plt.figure(figsize=(16, 12))
	#plt.title(filename)
	#plt.imshow(small2,cmap='gray')
	#plt.show()
	#plt.savefig(filename)

	matcher.draw_ransac(img1, small2, fast,	brief, is_binary_descriptor=True, match_method='BRUTE_FORCE', description='FAST + BRIEF, BRUTE_FORCE, RANSAC'+str(fx))
	fx+=0.25
	scale+=1

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


angulo=0
rotation=0
while rotation <=6:
	rows2r,cols2r = img2.shape
	filename = "./Rotation em %d.jpg"%angulo
	M2R = cv2.getRotationMatrix2D(((cols2r-1)/2.0,(rows2r-1)/2.0),angulo,1)
	rt2 = cv2.warpAffine(img2,M2R,(cols2r,rows2r))
	matcher.draw_ransac(img1, rt2, cv2.ORB_create(nfeatures=25), cv2.ORB_create(nfeatures=25), is_binary_descriptor=True, match_method='BRUTE_FORCE', description='ORB, BRUTE_FORCE, RANSAC'+str(angulo))
	#plt.figure(figsize=(16, 12))
	#plt.title(filename)
	#plt.imshow(rt2,cmap='gray')
	#plt.savefig(filename)
	angulo+=60
	rotation+=1

angulo=0
rotation=0
while rotation <=6:
	rows2r,cols2r = img2.shape
	filename = "./Rotation em %d.jpg"%angulo
	M2R = cv2.getRotationMatrix2D(((cols2r-1)/2.0,(rows2r-1)/2.0),angulo,1)
	rt2 = cv2.warpAffine(img2,M2R,(cols2r,rows2r))
	matcher.draw_ransac(img1, rt2, cv2.xfeatures2d.SIFT_create(nfeatures=25), cv2.xfeatures2d.SIFT_create(nfeatures=25), is_binary_descriptor=False, match_method='BRUTE_FORCE', description='SIFT, BRUTE_FORCE, RANSAC'+str(angulo))	
	#plt.figure(figsize=(16, 12))
	#plt.title(filename)
	#plt.imshow(rt2,cmap='gray')
	#plt.savefig(filename)
	angulo+=60
	rotation+=1


angulo=0
rotation=0
while rotation <=6:
	rows2r,cols2r = img2.shape
	filename = "./Rotation em %d.jpg"%angulo
	M2R = cv2.getRotationMatrix2D(((cols2r-1)/2.0,(rows2r-1)/2.0),angulo,1)
	rt2 = cv2.warpAffine(img2,M2R,(cols2r,rows2r))
	matcher.draw_ransac(img1, rt2, surf, surf, is_binary_descriptor=False, match_method='BRUTE_FORCE',  description='SURF, BRUTE_FORCE, RANSAC'+str(angulo))	
	#plt.figure(figsize=(16, 12))
	#plt.title(filename)
	#plt.imshow(rt2,cmap='gray')
	#plt.savefig(filename)
	angulo+=60
	rotation+=1


angulo=0
rotation=0
while rotation <=6:
	rows2r,cols2r = img2.shape
	filename = "./Rotation em %d.jpg"%angulo
	M2R = cv2.getRotationMatrix2D(((cols2r-1)/2.0,(rows2r-1)/2.0),angulo,1)
	rt2 = cv2.warpAffine(img2,M2R,(cols2r,rows2r))
	matcher.draw_ransac(img1, rt2, star, brief, is_binary_descriptor=True,match_method='BRUTE_FORCE', description='STAR + BRIEF, BRUTE_FORCE, RANSAC'+str(angulo))	
	#plt.figure(figsize=(16, 12))
	#plt.title(filename)
	#plt.imshow(rt2,cmap='gray')
	#plt.savefig(filename)
	angulo+=60
	rotation+=1



angulo=0
rotation=0
while rotation <=6:
	rows2r,cols2r = img2.shape
	filename = "./Rotation em %d.jpg"%angulo
	M2R = cv2.getRotationMatrix2D(((cols2r-1)/2.0,(rows2r-1)/2.0),angulo,1)
	rt2 = cv2.warpAffine(img2,M2R,(cols2r,rows2r))
	matcher.draw_ransac(img1, rt2, fast, brief, is_binary_descriptor=True, match_method='BRUTE_FORCE', description='FAST + BRIEF, BRUTE_FORCE, RANSAC'+str(angulo))	
	#plt.figure(figsize=(16, 12))
	#plt.title(filename)
	#plt.imshow(rt2,cmap='gray')
	#plt.savefig(filename)
	angulo+=60
	rotation+=1

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


darker=2
while darker <=8:
	filename = "./Darker divisor em %d.jpg"%darker
	imgDarker=img2/darker
	
	matcher.draw_ransac(img1, imgDarker, 
                    cv2.ORB_create(nfeatures=25), 
                    cv2.ORB_create(nfeatures=25), 
                    is_binary_descriptor=True, 
                    match_method='BRUTE_FORCE', description='ORB, BRUTE_FORCE, RANSAC')
	#cv2.imshow(filename,imgDarker)
	#cv2.imwrite(filename,imgDarker)
	darker+=2


darker=2
while darker <=8:
	filename = "./Darker divisor em %d.jpg"%darker
	imgDarker=img2/darker
	matcher.draw_ransac(img1, imgDarker, 
                    cv2.xfeatures2d.SIFT_create(nfeatures=25), 
                    cv2.xfeatures2d.SIFT_create(nfeatures=25), 
                    is_binary_descriptor=False, 
                    match_method='BRUTE_FORCE', 
                    description='SIFT, BRUTE_FORCE, RANSAC')
	#cv2.imshow(filename,imgDarker)
	#cv2.imwrite(filename,imgDarker)
	darker+=2
	
	
darker=2
while darker <=8:
	filename = "./Darker divisor em %d.jpg"%darker
	imgDarker=img2/darker
	

	matcher.draw_ransac(img1, imgDarker, 
                    surf, 
                    surf, 
                    is_binary_descriptor=False, 
                    match_method='BRUTE_FORCE', 
                    description='SURF, BRUTE_FORCE, RANSAC')
	#cv2.imshow(filename,imgDarker)
	#cv2.imwrite(filename,imgDarker)
	darker+=2


darker=2
while darker <=8:
	filename = "./Darker divisor em %d.jpg"%darker
	imgDarker=img2/darker
	matcher.draw_ransac(img1, imgDarker, 
                    star, 
                    brief,
                    is_binary_descriptor=True, 
                    match_method='BRUTE_FORCE', 
                    description='STAR + BRIEF, BRUTE_FORCE, RANSAC')
	#cv2.imshow(filename,imgDarker)
	#cv2.imwrite(filename,imgDarker)
	darker+=2
	
darker=2
while darker <=8:
	filename = "./Darker divisor em %d.jpg"%darker
	imgDarker=img2/darker
	matcher.draw_ransac(img1, imgDarker, 
                    fast, 
                    brief,
                    is_binary_descriptor=True, 
                    match_method='BRUTE_FORCE', 
                    description='FAST + BRIEF, BRUTE_FORCE, RANSAC')
	#cv2.imshow(filename,imgDarker)
	#cv2.imwrite(filename,imgDarker)
	darker+=2

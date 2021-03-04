from pylab import *
import sys, cv2

filename = 'C:\\Users\\Wellis_air\\program\\pythontest\\dot.jpg'
img = cv2.imread(filename);
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cimg = cv2.cvtColor(gray,cv2.COLOR_GRAY2BGR);
circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,2,15,param1=100,param2=30,minRadius=11,maxRadius=13);
circles = np.uint16(np.around(circles));
for i in circles[0,:]:
    cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),1);
    cv2.circle(img,(i[0],i[1]),2,(0,0,255),3);
cv2.imwrite('123.png',img)
print ("%d 개 박테리아 발견."%(len(circles[0])));
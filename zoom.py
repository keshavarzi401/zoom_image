import cv2 as cv
import numpy as np
image=cv.imread("digitalart.jpg")
print(image.shape)
number=int(input("please enter number:"))
new_width=int(image.shape[1]*number)
new_height=int(image.shape[0]*number)
resize_image=cv.resize(image,(new_width,new_height),interpolation=cv.INTER_LINEAR)
cv.imshow("image1",image)
cv.imshow("image2",resize_image)
cv.waitKey(0)




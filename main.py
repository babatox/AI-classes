import cv2
import matplotlib.pyplot as plt

image=cv2.imread('OIP.jpg')

#convert image from BRG to RGB
image_rgb=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
plt.title("RGB IMAGE")
plt.show()

gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
plt.imshow(gray_image)
plt.title("RGB IMAGE")
plt.show()
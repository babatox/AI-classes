import cv2
import numpy as np

img=cv2.imread('OIP (1).jpg')
image=cv2.resize(img, (600, 400))

def apply_red_filter(img):
    red=img.copy()
    red[:,:,0]=0 #remove green
    red[:,:,1]=0 #remove red

    return red


def apply_blue_filter(img):
    blue=img.copy()
    blue[:,:,1]=0 #remove blue
    blue[:,:,2]=0 #remove green

    return blue

def apply_green_filter(img):
    green=img.copy()
    green[:,:,0]=0 #remove blue
    green[:,:,2]=0 #remove red

    return green

def apply_margenta_filter(img):
    margenta=img.copy()
    margenta[:,:,0]=0 #remove green

    return margenta

def apply_neutral_filter(img):
    return img.copy()

print('press keys to apply fiters')
print("n for neutral")
print("r for red")
print("g for green")
print("b for blue")
print("m for margenta")
print("q to Quit")

cv2.imshow("Filtered Images",img)
while True:
    key = cv2.waitKey(0) & 0xFF
    if key==ord('n'):
        filtered = apply_neutral_filter(img)
    elif key==ord('r'):
        filtered = apply_red_filter(img)
    elif key==ord('g'):
        filtered = apply_green_filter(img)
    elif key==ord('b'):
        filtered = apply_blue_filter(img)
    elif key==ord('m'):
        filtered = apply_margenta_filter(img)
    elif key==ord('q'):
        break
    else:
        continue
    cv2.imshow('Filtered Image', filtered)

cv2.destroyAllWindows()
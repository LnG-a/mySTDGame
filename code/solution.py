# Import packages
import cv2
import numpy as np
import math
from level1 import *


def solution():
    RES = str(1)
    LEVEL = str(3)
    # Load the two images
    img1 = cv2.imread('images/resource'+RES+'.jpg')
    img2 = cv2.imread('images/copy'+RES+'_level'+LEVEL+'.jpg')

    # Resize images if necessary
    img1 = resize_image(img1)
    img2 = resize_image(img2)

    img_height = img1.shape[0]

    # Grayscale
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    # Calculate absolute difference
    diff = cv2.absdiff(gray1, gray2)
    cv2.imshow("Dif", diff)

    # Apply threshold
    thresh = cv2.threshold(diff, 15, 255, cv2.THRESH_BINARY)[1]
    cv2.imshow("Threshold", thresh)

    # Dilation
    kernel = np.ones((5, 5), np.uint8)
    dilate = cv2.dilate(thresh, kernel, iterations=2)
    cv2.imshow("Dilate", dilate)

    # Calculate contours
    contours, hierarchy = cv2.findContours(
        dilate.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) > 200:
            # Calculate bounding box around contour
            x, y, w, h = cv2.boundingRect(contour)
            center = (int(x+w/2), int(y+h/2))
            radius = int(math.sqrt(w*w+h*h)/2)
            color = (255, 255, 255)
            thickness = 3
            cv2.circle(img1, center, radius, color, thickness)
            cv2.circle(img2, center, radius, color, thickness)

    # Show images with circles on differences
    img1 = cv2.copyMakeBorder(img1, 0, 0, 0, 10, cv2.BORDER_CONSTANT)
    result = cv2.hconcat([img1, img2])
    cv2.imshow("Differences", result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def resize_image(image):
    if (image.shape[0] > 1080 or image.shape[1] > 1920/2):
        image = cv2.resize(
            image, (int(image.shape[0]/2), int(image.shape[1]/2)))
    return image


if __name__ == '__main__':
    solution()

import cv2
import matplotlib.pyplot as plt
import numpy
import random
from level1 import *


def level3(RES):
    # import file
    resource = cv2.imread('images/resource'+RES+'.jpg', 1)
    copy = resource.copy()
    gray = cv2.cvtColor(resource, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 1.5)
    # sosanh
    edged = cv2.Canny(copy, 100, 350)
    cv2.imshow("edged1", edged)
    contours, hierarchy = cv2.findContours(
        edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    black_and_white = numpy.zeros(
        (gray.shape[0], gray.shape[1], 3), dtype="uint8")
    for i in contours:
        cv2.fillPoly(black_and_white, pts=[i], color=[255, 255, 255])

    cv2.imshow("black_and_white1", black_and_white)
    # sosanh
    edged = cv2.Canny(blur, 100, 250)
    cv2.imshow("edged2", edged)

    contours, hierarchy = cv2.findContours(
        edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    black_and_white = numpy.zeros(
        (gray.shape[0], gray.shape[1], 3), dtype="uint8")
    for i in contours:
        cv2.fillPoly(black_and_white, pts=[i], color=[255, 255, 255])

    cv2.imshow("black_and_white2", black_and_white)

    # choose contours to modify
    choices = []
    for contour in contours:
        area = cv2.contourArea(contour)
        x, y, w, h = cv2.boundingRect(contour)
        if (250 < area < 1000 and w*h < 2500):

            choices.append(contour)

    choices = random.sample(choices, min(3, len(choices)))

    key = numpy.zeros(
        (gray.shape[0], gray.shape[1], 3), dtype="uint8")
    # modify chosen contours
    for choice in choices:
        mask = np.zeros(copy.shape[:2], dtype=np.uint8)
        cv2.fillPoly(mask, pts=[choice], color=[255, 255, 255])
        mean = cv2.mean(copy, mask)
        b = min(255, mean[0]+25)
        g = min(255, mean[1]+25)
        r = min(255, mean[2]+25)
        cv2.fillPoly(key, pts=[choice], color=[b, g, r])
        cv2.fillPoly(copy, pts=[choice], color=[b, g, r])

    cv2.imshow("key", key)

    # write copy image file
    cv2.imwrite('images/copy'+RES+'_level3.jpg', copy,
                [cv2.IMWRITE_JPEG_QUALITY, 90])

    # show result
    resource = resize_image(resource)
    copy = resize_image(copy)
    resource = cv2.copyMakeBorder(resource, 0, 0, 0, 10, cv2.BORDER_CONSTANT)
    result = cv2.hconcat([resource, copy])

    cv2.imshow("Result", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    # for i in range(1, 6):
    #     level3(str(i))
    level3(str(6))

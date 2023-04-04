import cv2
import matplotlib.pyplot as plt
import numpy as np
from level1 import *


def level2(RES):
    # import file
    resource = cv2.imread('images/resource'+RES+'.jpg', 1)
    copy = resource.copy()

    point_array = random_square(resource)

    for point in point_array:
        print(point[0], point[1])
        flip_horizontal(int(point[0]), int(point[1]), resource, copy)

    # write copy image file
    cv2.imwrite('images/copy'+RES+'_level2.jpg',
                copy, [cv2.IMWRITE_JPEG_QUALITY, 90])

    # show result
    resource = resize_image(resource)
    copy = resize_image(copy)
    resource = cv2.copyMakeBorder(resource, 0, 0, 0, 10, cv2.BORDER_CONSTANT)
    result = cv2.hconcat([resource, copy])

    cv2.imshow("Result", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def flip_horizontal(x, y, resource, copy):
    for i in range(x, x+SQUARE_SIZE):
        for j in range(y, y+SQUARE_SIZE):
            copy[i][j] = resource[i][y+SQUARE_SIZE-j+y]


if __name__ == '__main__':
    for i in range(1, 7):
        level2(str(i))

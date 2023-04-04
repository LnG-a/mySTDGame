import cv2
import matplotlib.pyplot as plt
import numpy as np
import random

SQUARE_SIZE = 40


def level1(RES):
    # import file
    resource = cv2.imread('images/resource'+RES+'.jpg', 1)
    copy = resource.copy()

    point_array = random_square(resource)

    for point in point_array:
        print(point[0], point[1])
        add_color(int(point[0]), int(point[1]), copy)

    # write copy image file
    cv2.imwrite('images/copy'+RES+'_level1.jpg', copy,
                [cv2.IMWRITE_JPEG_QUALITY, 90])

    # show result
    resource = resize_image(resource)
    copy = resize_image(copy)
    resource = cv2.copyMakeBorder(resource, 0, 0, 0, 10, cv2.BORDER_CONSTANT)
    result = cv2.hconcat([resource, copy])

    cv2.imshow("Result", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def add_color(x, y, copy):
    for i in range(x, x+SQUARE_SIZE):
        for j in range(y, y+SQUARE_SIZE):
            copy[i][j][0] = min(255, copy[i][j][0]+25)
            copy[i][j][1] = min(255, copy[i][j][1]+25)
            copy[i][j][2] = min(255, copy[i][j][2]+25)
            # copy[i][j] = copy[i][j]+25


def random_square(resource):
    point_array = np.empty((0, 2))
    count = 0
    while (count < 3):
        skip = False
        x = random.randint(0, resource.shape[0]-SQUARE_SIZE)
        y = random.randint(0, resource.shape[1]-SQUARE_SIZE)
        for i in range(len(point_array)):
            if ((x < point_array[i][0]+SQUARE_SIZE and x > point_array[i][0]-SQUARE_SIZE) and (y < point_array[i][1]+SQUARE_SIZE and y > point_array[i][1]-SQUARE_SIZE)):
                skip = True

        if not skip:
            new_array = np.array([[x, y]])
            point_array = np.concatenate((point_array, new_array), axis=0)
            count = count + 1

    return point_array


def resize_image(image):
    while (image.shape[0] > 1080 or image.shape[1] > 1920/2):
        image = cv2.resize(
            image, (int(image.shape[0]/2), int(image.shape[1]/2)))
    return image


# 1 is the first images
# 7 is the last images
if __name__ == '__main__':
    for i in range(1, 6):
        level1(str(i))

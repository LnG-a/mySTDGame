import pygame
import sys
from random import randrange
from pynput.mouse import Controller


class Point(object):
    def __init__(self, x, y):
        """
        Construct a point object given the x and y coordinates

        Parameters:
            x (float): x coordinate in the 2D cartesian plane
            y (float): y coordinate in the 2D cartesian plane
        """
        self.x = x
        self.y = y


def main():
    global screen

    pygame.init()
    mouse = Controller()

    background = pygame.image.load('images/bg.png')
    diff_img = pygame.image.load('images/resource7.jpg')
    diff_img_2 = pygame.image.load('images/copy7.jpg')

    WINDOW_WIDTH = pygame.display.Info().current_w
    WINDOW_HEIGHT = pygame.display.Info().current_h

    img_width = diff_img.get_width()
    img_height = diff_img.get_height()

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    offset_img_1 = Point((WINDOW_WIDTH/2-img_width)/2,
                         (WINDOW_HEIGHT-img_height)/2)
    offset_img_2 = Point(WINDOW_WIDTH/2+(WINDOW_WIDTH/2 -
                         img_width)/2, (WINDOW_HEIGHT-img_height)/2)

    screen.blit(background, (0, 0))
    screen.blit(diff_img, (offset_img_1.x, offset_img_1.y))
    screen.blit(diff_img_2, (offset_img_2.x, offset_img_2.y))

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = Point(pygame.mouse.get_pos()[
                            0], pygame.mouse.get_pos()[1])
                if (check_pos(pos, offset_img_1, img_width, img_height)):
                    draw_circle(pos.x, pos.y)
                    draw_circle(pos.x+WINDOW_WIDTH/2, pos.y)

        pygame.display.update()


def check_pos(pos: Point, offset: Point, width, height):
    return pos.x < offset.x + width and pos.x > offset.x and pos.y > offset.y and pos.y < offset.y + height


def draw_circle(x, y):
    pygame.draw.circle(screen, (150, 0, 0), (x, y), 40, 3)


if __name__ == '__main__':
    main()

# scream = pygame.mixer.Sound("images/scream.wav")

# sleep(randrange(5,15))

# scream.play()
# sleep(0.4)
# screen.blit(zombie, (0,0))

# sleep(3)
# scream.stop()
# pygame.quit()

# testing github

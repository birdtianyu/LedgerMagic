# -*- coding:utf-8 -*-
import sys
import numpy as np
import cv2
import pygame

from PIL import Image
import PIL.ImageOps

from Networks import *
from get_images import *
from recognition import *

drawing = False  # true if mouse is pressed
previous_x0, previous_y0 = 0, 0
previous_x, previous_y = 0, 0


# sample data
images = np.load("./SampleData.npy")
sample_targets = get_images(images)
strs = [u"\u2661", u"\u2662", '?', '?', u"\u266B", u"\u26E4", u"\u2715", 3, 4]

def Handling(Prediction_strs):
    Copy_strs = Prediction_strs.copy()
    is_number = False
    will_cut = False
    Characters = []
    NUMBERS = '0'
    images_index = []
    
    for i, item in enumerate(Copy_strs, 0):
        
        if is_number and item != '✕':
            if isinstance(item, np.int64) or isinstance(item, int):
                NUMBERS = NUMBERS + str(item)
            else:
                is_number = False
                will_cut = True
                images_index.append(i)
            continue

        if item == u"\u2715" or item == '✕':
            is_number = True
            continue
        elif item != '?' and not will_cut:
            Characters.append(item)
            continue
        elif item == '?' or will_cut:
            images_index.append(i)
            continue
            
    return Characters, int(NUMBERS), images_index

def display_Gallery(arrstr, targets):
    Width, Length = 600, 600
    clock = pygame.time.Clock()
    pygame.font.init()
    mainSurface = pygame.display.set_mode((Length,Width))
    pygame.display.set_caption("Gallery")
    f = pygame.font.SysFont("segoe-ui-symbol",40)

    Characters, Numbers, Images_index = Handling(arrstr)
    # print(Handling(arrstr))
    
    if Numbers == 0:
        Numbers = 1

    if len(Characters) == 0 and len(Images_index) > 0:
        Images_index.append(0)

    print(f"Command: {Characters} x {Numbers} times")
    
    SIZE = len(Characters)*Numbers + len(Images_index)

    x_position = np.random.randint(Width-25, size=(SIZE))
    y_position = np.random.randint(-Numbers*15, 0, size=(SIZE))
    R = np.random.randint(30, 255, size=(len(Characters)*Numbers))
    G = np.random.randint(30, 255, size=(len(Characters)*Numbers))
    B = np.random.randint(30, 255, size=(len(Characters)*Numbers))

    y_position[0] = -10

    while np.min(y_position) < 600:
        clock.tick(15)
        mainSurface.fill((0,0,0))

        for i, item in enumerate(Characters, 0):
            for j in range(Numbers):
                index = i * Numbers + j
                mainSurface.blit(f.render(item,True,(R[index],G[index],B[index])), (x_position[index], y_position[index]))

        if len(Images_index) > 0:
            for no, image_number in enumerate(Images_index, 0):
                mainSurface.blit(pygame.surfarray.make_surface(np.transpose(targets[image_number], (1,0))), (x_position[len(Characters)*Numbers+no],y_position[len(Characters)*Numbers+no]))
                
        y_position += 5

        pygame.display.update()

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                # sys.exit()

    pygame.quit()
 

class Tablet():
    
    # mouse callback function
    def __init__(self):
        self.img = 255*np.ones((150, 800, 3), np.uint8) # White background

    def draw_circle(self, event, x, y, flags, param):
        global previous_x0, previous_y0, previous_x, previous_y, drawing
        if event == cv2.EVENT_LBUTTONDOWN:
            drawing = True
            previous_x0, previous_y0 = x, y
            previous_x, previous_y = x, y
        elif event == cv2.EVENT_MOUSEMOVE:
            if drawing:
                pts = np.array([[previous_x0, previous_y0], [previous_x, previous_y], [x, y]], np.int32)
                pts = pts.reshape((-1,1,2))
                cv2.polylines(self.img, pts, True, (0, 0, 0), 3)
                cv2.circle(self.img, (x, y), 3, (0, 0, 0), -1)
                previous_x0, previous_y0 = previous_x, previous_y
                previous_x, previous_y = x, y
        elif event == cv2.EVENT_LBUTTONUP:
            drawing = False
            cv2.circle(self.img, (x, y), 3, (0, 0, 0), -1)

    def save(self):
        # cut images
        new_targets = get_images(self.img)

        # 展示裁切结果
        ShowAllImages(new_targets)

    def clear(self):
        self.img = 255*np.ones((150, 800, 3), np.uint8)

    def start(self):
        # np.save("SampleData.npy", self.img)
        
        # cut images
        new_targets = get_images(self.img)

        # prediction
        print("===================================================")
        predictions = recognition(new_targets, THRESHOLD = 0.9)
        print("prediction:", predictions)
        display_Gallery(predictions, new_targets)

    def create_image(self):
        cv2.namedWindow('Handwriting tablet')
        cv2.setMouseCallback('Handwriting tablet', self.draw_circle)
        
        while (1):
            cv2.imshow('Handwriting tablet', self.img)
            k = cv2.waitKey(1) & 0xFF
            # Esc
            if k == 27 or k == ord('q'):
                break
            # Enter
            elif k == 13:
                self.start()
            elif k == ord('c'):
                self.clear()
            elif k == ord('s'):
                self.save()
                
        cv2.destroyAllWindows()


if __name__ == '__main__':
    tablet = Tablet()
    tablet.create_image()

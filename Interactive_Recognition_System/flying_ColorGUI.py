import pygame
import sys
import numpy as np
from PIL import Image
import PIL.ImageOps
from get_images import *

Width, Length = 600, 600
clock = pygame.time.Clock()
pygame.font.init()
mainSurface = pygame.display.set_mode((Length,Width))
pygame.display.set_caption("Gallery")
f = pygame.font.SysFont("segoe-ui-symbol",40)

strs = [u"\u2661", u"\u2662", '?', '?', u"\u266B", u"\u26E4", u"\u2715", 3, 4]

def Handling(strs):
    is_number = False
    will_cut = False
    Characters = []
    NUMBERS = '0'
    images_index = []
    for i, item in enumerate(strs, 0):
        if is_number:
            if type(item) == type(1):
                NUMBERS = NUMBERS + str(item)
            else:
                is_number = False
                will_cut = True
            continue

        if item == u"\u2715":
            is_number = True
        elif item != '?' and not will_cut:
            Characters.append(item)
        elif item == '?':
            images_index.append(i)
            
    return Characters, int(NUMBERS), images_index

    
Characters, Numbers, Images_index = Handling(strs)
x_position = np.random.randint(Width-10, size=(len(Characters)*Numbers + len(Images_index)))
y_position = np.random.randint(-Numbers*15, 0, size=(len(Characters)*Numbers + len(Images_index)))
R = np.random.randint(255, size=(len(Characters)*Numbers))
G = np.random.randint(255, size=(len(Characters)*Numbers))
B = np.random.randint(255, size=(len(Characters)*Numbers))


CONTROL = True

y_position[0] = -10


images = np.load("./SampleData.npy")
targets = get_images(images)


while True:
    clock.tick(15)
    mainSurface.fill((0,0,0))

    if CONTROL:
        if np.min(y_position) < 600:
            for i, item in enumerate(Characters, 0):
                for j in range(Numbers):
                    index = i * Numbers + j
                    mainSurface.blit(f.render(item,True,(R[index],G[index],B[index])), (x_position[index], y_position[index]))

            if len(Images_index) > 0:
                for no, image_number in enumerate(Images_index, 0):
                    mainSurface.blit(pygame.surfarray.make_surface(targets[image_number]), (x_position[len(Characters)*Numbers+no],y_position[len(Characters)*Numbers+no]))
                
            y_position += 5
        else:
            y_position[0] = -10
            CONTROL = False

    pygame.display.update()

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    

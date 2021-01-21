# -*- coding: utf-8 -*-
"""Recognition_tutorial.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ERpAvQNhaDeGhOEcaTlGm4lyVTzdPzue
"""

import torch
from torch import optim
import torch.nn as nn

import torchvision
import torchvision.transforms as transforms

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import PIL.ImageOps
import random

from invert import Invert

from get_images import *
from Networks import *

"""## Load Models and Mean tensors"""

# Load Model
model1 = torch.load('./model/Model1.pkl') # Siamese Network
model2 = torch.load('./model/Model2.pkl') # CNNs
model3 = torch.load('./model/Model3.pkl') # MNIST Model

# Load tensors
Mean_Vectors = torch.load('./model/Mean_Tensor.pt')

# Class name
Class_name = [u'\u2661', u'\u2662', u'\u266B', u'\u26E4', u'\u2715']
print(Class_name)

"""## Load Targets"""

IMG_SIZE1 = 256
IMG_SIZE2 = 28

transform1 = transforms.Compose([transforms.Resize((IMG_SIZE1, IMG_SIZE1)),
                                transforms.Grayscale(num_output_channels=1), # 灰度化
                                # Invert(),
                                # transforms.RandomHorizontalFlip(), # 随机水平翻转
                                transforms.ToTensor(),
                                ])

transform2 = transforms.Compose([transforms.Resize((IMG_SIZE2, IMG_SIZE2)),
                                transforms.Grayscale(num_output_channels=1), # 灰度化
                                # Invert(),
                                # transforms.RandomHorizontalFlip(), # 随机水平翻转
                                transforms.ToTensor(),
                                ])

transform3 = transforms.Compose([transforms.Resize((IMG_SIZE1, IMG_SIZE1)),
                                transforms.Grayscale(num_output_channels=1), # 灰度化
                                Invert(),
                                # transforms.RandomHorizontalFlip(), # 随机水平翻转
                                transforms.ToTensor(),
                                ])

# 返回每一类的距离
def get_distance(vector, Mean_Vectors):
    result = []
    for key in Mean_Vectors.keys():
        dis = torch.nn.functional.pairwise_distance(vector,Mean_Vectors[key].unsqueeze(0)).item()
        result.append(dis)
    return result

# 展示所有裁切后的照片
def ShowAllImages(targets):
    for item in targets:
        img = Image.fromarray(item)
        img256 = transform3(img)
        img256 = torchvision.utils.make_grid(img256)
        plt.figure(figsize=(4,4))
        plt.imshow(np.transpose(img256, (1,2,0)))
        plt.axis('off')
        plt.show()
        
"""## Recognition"""

def recognition(targets, THRESHOLD = 0.8):
    Predictions = []
    Digital_Switch = False # Whether to identify the number

    for i, item in enumerate(targets, 0):
        img = Image.fromarray(item)

        # Step 1: Start with Siamese Network
        img256 = transform1(img)
        img256 = img256.unsqueeze(0) # 增加一个个数维度
        Prediction_vector1, _ = model1(img256, img256)
        distance_list = get_distance(Prediction_vector1, Mean_Vectors)
        Prediction_Class = np.argmin(distance_list)
        Prediction_Dissimilarity = np.min(distance_list)
        print(f"part{i}, Siamese Prediction:{Prediction_Class}, Dissimilarity:{Prediction_Dissimilarity}")

        # print(Prediction_vector.shape)
        # print(distance_list)
        # print(Prediction_Class, Prediction_Dissimilarity)

        # Step 2: Check by CNNs
        Prediction_vector2 = model2(img256)
        possible = torch.nn.functional.softmax(Prediction_vector2, dim=1)
        # print(possible)
        Check_Prediction_Class = np.argmax(possible.detach().numpy())
        Check_Probability = np.max(possible.detach().numpy())
        print(f"CNNs Prediction:{Check_Prediction_Class}, Probability:{Check_Probability}")
        
        ########################### Output Processing ###########################
    
        if Digital_Switch:
            # Step 2: identify the number 
            img28 = transform2(img)
            img28 = img28.unsqueeze(0) # 增加一个个数维度
            Prediction_number_vector = model3(img28)
            number = np.argmax(Prediction_number_vector.detach().numpy())
            Predictions.append(number)
            continue

        # Greater than the threshold
        if Prediction_Dissimilarity < THRESHOLD:
            if Prediction_Class == Check_Prediction_Class:
                Digital_Switch = False
                Predictions.append(Class_name[Prediction_Class])
                if Prediction_Class == 4:
                    Digital_Switch = True
                continue
            elif Prediction_Class == 0 or Prediction_Class == 1:
                if (Check_Prediction_Class == 0 or Check_Prediction_Class == 1) and Check_Probability < 0.3:
                    Digital_Switch = False
                    Predictions.append(Class_name[Prediction_Class])
                    continue
        elif (Prediction_Class == 0 or Prediction_Class == 1) and (Check_Prediction_Class == 0 or Check_Prediction_Class == 1):
            if Check_Probability > 0.7:
                Digital_Switch = False
                Predictions.append(Class_name[Check_Prediction_Class])
                continue
        
        Predictions.append("?")

    return Predictions



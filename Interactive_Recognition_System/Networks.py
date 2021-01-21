import torch
from torch import optim
import torch.nn as nn

# all models

class SiameseNetwork(nn.Module):
    def __init__(self):
        super(SiameseNetwork, self).__init__()
        self.cnn1 = nn.Sequential(
            # 1, 256, 256
            nn.Conv2d(1, 4, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.BatchNorm2d(4),
            nn.MaxPool2d(2, stride=2),
            
            # 4, 128, 128
            nn.Conv2d(4, 8, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.BatchNorm2d(8),
            nn.MaxPool2d(2, stride=2),
            
            # 8, 64, 64
            nn.Conv2d(8, 8, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.BatchNorm2d(8),
            nn.MaxPool2d(2, stride=2)
            
            # 8, 32, 32
        )

        self.fc1 = nn.Sequential(
            # 8, 32, 32
            nn.Linear(8*32*32, 1000),
            nn.ReLU(inplace=True),
            
            # 1000
            nn.Linear(1000, 100),
            nn.ReLU(inplace=True),
            
            # 100
            nn.Linear(100, 3)
            
            # 3
        )
        
        
    def onceforward(self, inputvec):
        outputvec = self.cnn1(inputvec)
        outputvec = outputvec.view(outputvec.size()[0], -1)
        outputvec = self.fc1(outputvec)

        return outputvec
    
        
    def forward(self, input1, input2):
        output1 = self.onceforward(input1)
        output2 = self.onceforward(input2)
        return output1, output2
        
        # output = torch.cat((output1, output2),1)
        # output = self.fc1(output)
        # return output



class ConvolutionalNetwork(nn.Module):
    def __init__(self):
        super(ConvolutionalNetwork, self).__init__()
        self.cnn1 = nn.Sequential(
            # 1, 256, 256
            nn.Conv2d(1, 4, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.BatchNorm2d(4),
            nn.MaxPool2d(2, stride=2),
            
            # 4, 128, 128
            nn.Conv2d(4, 8, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.BatchNorm2d(8),
            nn.MaxPool2d(2, stride=2),
            
            # 8, 64, 64
            nn.Conv2d(8, 8, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.BatchNorm2d(8),
            nn.MaxPool2d(2, stride=2)
            
            # 8, 32, 32
        )

        self.fc1 = nn.Sequential(
            # 8, 32, 32
            nn.Linear(8*32*32, 1000),
            nn.ReLU(inplace=True),
            
            # 1000
            nn.Linear(1000, 100),
            nn.ReLU(inplace=True),
            
            # 100
            nn.Linear(100, 5)
            
            # 5
        )
        
        
    def forward(self, inputvec):
        outputvec = self.cnn1(inputvec)
        outputvec = outputvec.view(outputvec.size()[0], -1)
        outputvec = self.fc1(outputvec)

        return outputvec



class ConvNetwork(nn.Module):
    def __init__(self):
        super(ConvNetwork, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=1, out_channels=6, kernel_size=5, stride=1, padding=0)
        self.conv2 = nn.Conv2d(in_channels=6, out_channels=12, kernel_size=3, stride=1, padding=1)

        self.fc1 = nn.Linear(in_features=12*6*6, out_features=120)
        # self.fc2 = nn.Linear(in_features=120, out_features=60)
        self.out = nn.Linear(in_features=120, out_features=10)
        
    def forward(self, d):
        # conv1 layer
        d = self.conv1(d)
        d = nn.functional.relu(d)
        d = nn.functional.max_pool2d(d, kernel_size=2, stride=2)
    
        # conv2 layer
        d = self.conv2(d)
        d = nn.functional.relu(d)
        d = nn.functional.max_pool2d(d, kernel_size=2, stride=2)

        # fully connected Layer1
        # d = d.reshape(-1, 12*4*4)
        d = d.flatten(start_dim=1)
        d = self.fc1(d)
        d = nn.functional.relu(d)

        # fully connected Layer2
        # d = self.fc2(d)
        # d = nn.functional.relu(d)

        # output layer
        d = self.out(d)
        # d = nn.functional.softmax(d)

        return d

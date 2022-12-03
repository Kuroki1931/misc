import torch
import torch.nn as nn
import torch.nn.functional as F


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 64, 3)
        self.batch1 = nn.BatchNorm2d(64)
        self.conv2 = nn.Conv2d(64, 128, 3)
        self.pool = nn.MaxPool2d(2, 2)
        self.batch2 = nn.BatchNorm2d(128)
        self.batch3 = nn.BatchNorm2d(64)
        self.conv3 = nn.Conv2d(128, 64, 5)
        self.fc1 = nn.Linear(64 * 3 * 3, 64)
        self.fc2 = nn.Linear(64, 32)
        self.fc3 = nn.Linear(32, 2)

    def forward(self, x):
        x = self.pool(self.batch1(F.relu(self.conv1(x))))
        x = self.pool(self.batch2(F.relu(self.conv2(x))))
        x = self.batch3(F.relu(self.conv3(x)))
        x = x.view(-1, 64 * 3 * 3)
        #x = torch.flatten(x, start_dim=1)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x



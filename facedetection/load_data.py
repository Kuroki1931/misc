import numpy as np
import torch
import torchvision
import torchvision.transforms as transforms
from torch.utils.data.sampler import SubsetRandomSampler
import random
import tqdm



def load(train_dir, test_dir, valid_size=0.2, batch_size=32):
    transform = transforms.Compose(
        [transforms.Grayscale(), 
        transforms.ToTensor(), 
        transforms.Normalize(mean=(0,),std=(1,))])

    train_data = torchvision.datasets.ImageFolder(train_dir, transform=transform)
    test_data = torchvision.datasets.ImageFolder(test_dir, transform=transform)
    
    # remove images to have as many negatives as positives
    nb_negatifs = len([1 for t in train_data.imgs if t[1] == 0])
    nb_positifs = len(train_data) - nb_negatifs
    nb_to_remove = nb_positifs - nb_negatifs

    if nb_to_remove > 0:
        items_to_remove = random.sample(train_data.imgs[nb_negatifs:], nb_to_remove)
        print('removing the excess of positive images...')
        [train_data.imgs.remove(item) for item in tqdm.tqdm(items_to_remove)]

    num_train = len(train_data)
    indices_train = list(range(num_train))
    np.random.shuffle(indices_train)
    split_tv = int(np.floor(valid_size * num_train))
    train_new_idx, valid_idx = indices_train[split_tv:],indices_train[:split_tv]

    train_sampler = SubsetRandomSampler(train_new_idx)
    valid_sampler = SubsetRandomSampler(valid_idx)

    train_loader = torch.utils.data.DataLoader(train_data, batch_size=batch_size, sampler=train_sampler, num_workers=1)
    valid_loader = torch.utils.data.DataLoader(train_data, batch_size=batch_size, sampler=valid_sampler, num_workers=1)
    test_loader = torch.utils.data.DataLoader(test_data, batch_size=batch_size, shuffle=True, num_workers=1)
    #classes = ('noface','face')
    return train_loader, valid_loader, test_loader


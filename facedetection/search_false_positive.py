from net import Net
from sliding_window import *
import torch
from pathlib import Path
from sliding_window import pyramid_sliding_window_detection
import cv2
import tqdm
import json
import random
import config as cfg

import os
if not os.path.exists(cfg.false_positives_images):
    os.mkdir(cfg.false_positives_images)

def main():
    net = Net()
    net.load_state_dict(torch.load('checkpoint.pt'))

    rootdir = Path(cfg.texture_images)
    file_list = [f for f in rootdir.glob('**/*') if f.is_file()]
    random.shuffle(file_list)

    if os.path.exists('files_searched.json'):
        with open('files_searched.json', 'r') as f:
            searched_files = json.load(f)
    else:
        searched_files = []

    nb_images = 0
    progress_bar = tqdm.tqdm(file_list)
    for file in progress_bar:
        progress_bar.set_description(str(nb_images))
        if str(file).split('/')[-1] in searched_files:
            continue
        else:
            searched_files.append(str(file).split('/')[-1])
            with open('files_searched.json', 'w') as f:
                json.dump(searched_files, f)
        img = cv2.imread(str(file), 0)
        faces = pyramid_sliding_window_detection(net, img, 1.2, 36, 36, 5)
        i = 1
        for face in faces:
            if face[1]:
                for box in face[1]:
                    patch = img[int(box[1]):int(box[3]), int(box[0]):int(box[2])]
                    if patch.shape[0] != 36 or patch.shape[1] != 36:
                        patch = cv2.resize(patch, (36, 36))
                    cv2.imwrite(cfg.false_positives_images + file.name.split('.')[0] + f'_{i}.jpg', patch)
                    nb_images += 1
                    i += 1


if __name__ == '__main__':
    main()
from net import Net
from sliding_window import *
import torch
from sliding_window import pyramid_sliding_window_detection
import cv2
import matplotlib.pyplot as plt
from skimage.draw import rectangle_perimeter
from skimage.color import rgb2gray
from torchvision.ops import nms
    

def main():
    net = Net()
    net.load_state_dict(torch.load('checkpoint.pt'))

    img = cv2.imread('yfb_petit.jpg')
    img = rgb2gray(img/255)
    
    faces = pyramid_sliding_window_detection(net, img, 1.1, 36, 36, 3)

    boxes = []
    scores = []

    for face in faces:
        if face[1]:
            for box in face[1]:
                boxes.append(list(box[:-1]))
                scores.append(box[-1])
    
    boxes_to_keep = nms(boxes = torch.Tensor(boxes), scores = torch.Tensor(scores), iou_threshold=0.2)

    for i in boxes_to_keep:
        box = boxes[i]
        rect = rectangle_perimeter((box[1], box[3]), (box[0], box[2]), shape=img.shape, clip=True)
        img[rect] = 1
    
    plt.imshow(img)
    plt.show()

if __name__ == '__main__':
    main()

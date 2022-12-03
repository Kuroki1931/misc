import cv2
import torch

def pyramid(image, scale=1.5, minSize=(30, 30)):
    # yield the original image
    print(f'search {image.shape}')
    yield image
    # keep looping over the pyramid
    while True:
        # compute the new dimensions of the image and resize it
        w = int(image.shape[0] / scale)
        h = int(image.shape[1] / scale)
        print(f'search new size : {w} x {h}')
        #image = imutils.resize(image, width=w)
        image = cv2.resize(image, (h,w))
        
        # if the resized image does not meet the supplied minimum
        # size, then stop constructing the pyramid
        if image.shape[0] < minSize[1] or image.shape[1] < minSize[0]:
            break
        # yield the next image in the pyramid
        yield image

def sliding_window(image, stepSize, windowSize):
    # slide a window across the image
    for y in range(0, image.shape[0], stepSize):
        for x in range(0, image.shape[1], stepSize):
            # yield the current window
            yield (x, y, image[y:y + windowSize[1], x:x + windowSize[0]])


def pyramid_sliding_window_detection(net, image, scale, winW=36, winH=36, stepSize=5):
    # Store the initial image before resize, it will be used for the final printing
    faces_img = image.copy()
   
    # loop over the image pyramid
    # all_detected_faces : contains for each pyramid level the scaling factor and the detected faces corresponding to
    # pyramid level
    all_detected_faces = []
    for resized in pyramid(image, scale=scale):
        detected_faces = []
        curr_scale_factor = image.shape[0] / resized.shape[0]
        # loop over the sliding window for each layer of the pyramid
        for (x, y, window) in sliding_window(resized, stepSize=stepSize, windowSize=(winW, winH)):
            # if the window does not meet our desired window size, ignore it
            if window.shape[0] != winH or window.shape[1] != winW:
                continue
            # We use the 36*36 window to match the net's img input size
            resized_tensor = torch.from_numpy(window).float()
            # Transform the 500*500 (2d) img to a 4d tensor (the additional 2 dimensions contain no information)
            resized_tensor = resized_tensor[None, None, :, :]  # tensor shape is now [1,1,500,500]
            # Feed the network the input tensor
            output = net(resized_tensor)

            # We only register faces with a prob higher than 0.99 to avoid false positives
            # (softmax dim parameter : dim=0->rows add up to 1, dim=1->rows add up to 1)
            softmax = torch.nn.functional.softmax(output, dim=1)
            if softmax[0][1] >= 0.9999:
                detected_faces.append((x, y, float(softmax[0][1])))

        #Add the detected faces and the corresponding factors to the all_faces variable
        all_detected_faces.append([curr_scale_factor,detected_faces])
  

    # We use the non_max_supp algorithm to delete overlaping bounding boxes
    # to avoid detecting the same face multiple times
    for j in range(len(all_detected_faces)):
        for i in range(len(all_detected_faces[j][1])): #all_detected_faces[j][1]->detected faces of the i-pyramid-level
            # in this line we both :
            # - change the tuple from a 2d (startX, startY) to a 4d (startX, startY, endX, endY)
            # - multiply each number of the tuple by the current scale factor
            all_detected_faces[j][1][i] = (
                                              all_detected_faces[j][1][i][0] * all_detected_faces[j][0], all_detected_faces[j][1][i][1] * all_detected_faces[j][0]
                                          ) + (
                                            (all_detected_faces[j][1][i][0] + winW)*all_detected_faces[j][0],
                                            (all_detected_faces[j][1][i][1] + winH)*all_detected_faces[j][0],
                                            (all_detected_faces[j][1][i][-1])
                                            )
    # Concatenate detected faces into the same array
    final_detected_faces = all_detected_faces
    return final_detected_faces

# Copyright 2019 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import numpy as np
#import picamera
import cv2
import argparse
from PIL import Image

import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

from visualization_utils import draw_bounding_boxes_on_image_array
from utils import load_image
from detector import ObjectDetectorLite

def parse_args():
    parser = argparse.ArgumentParser(description='Object Detection')
    parser.add_argument('--model_path', type=str, help='Specify the model path', required=True)
    parser.add_argument('--label_path', type=str, help='Specify the label map', required=True)
    parser.add_argument('--confidence', type=float, help='Minimum required confidence level of bounding boxes',
                        default=0.6)

    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = parse_args()
    detector = ObjectDetectorLite(model_path=args.model_path, label_path=args.label_path)
    input_size = detector.get_input_size()

    plt.ion()
    plt.tight_layout()
    
    fig = plt.gcf()
    fig.canvas.set_window_title('Object Detection')
    fig.suptitle('Detecting')
    ax = plt.gca()
    ax.set_axis_off()
    tmp = np.zeros(input_size + [3], np.uint8)
    preview = ax.imshow(tmp)
    
    #####################################################################################
    # test laptop with single image

    # img = Image.open("dog.jpg").convert('RGB')
    # # Preprocess image
    # img = img.resize((480, 640))
    # img = np.array(img, dtype=np.uint8)
    # image = load_image(img)
    # boxes, scores, classes = detector.detect(image, args.confidence)
    # for label, score in zip(classes, scores):
    #     print(label, score)

    # if len(boxes) > 0:
    #     draw_bounding_boxes_on_image_array(image, boxes, display_str_list=classes)
    
    # preview.set_data(image)
    # fig.canvas.get_tk_widget().update()
    # while True:
    #     pass

    #####################################################################################
    # code for rasberry pi

    # with picamera.PiCamera() as camera:
    #     camera.resolution = (640, 480)
    #     while True:
    #         stream = np.empty((480, 640, 3), dtype=np.uint8)
    #         camera.capture(stream, 'rgb')
          
    #         image = load_image(stream)
    #         boxes, scores, classes = detector.detect(image, args.confidence)
    #         for label, score in zip(classes, scores):
    #             print(label, score)
  
    #         if len(boxes) > 0:
    #             draw_bounding_boxes_on_image_array(image, boxes, display_str_list=classes)
            
    #         preview.set_data(image)
    #         fig.canvas.get_tk_widget().update()


    #####################################################################################
    # code for laptop with opencv
    cv2.namedWindow("preview")
    vc = cv2.VideoCapture(0)

    if vc.isOpened(): # try to get the first frame
        rval, frame = vc.read()
    else:
        rval = False

    while rval:
        #cv2.imshow("preview", frame)
        rval, frame = vc.read()
        frame = np.array(frame, dtype=np.uint8)
        image = load_image(frame)
        boxes, scores, classes = detector.detect(image, args.confidence)
        for label, score in zip(classes, scores):
            print(label, score)

        if len(boxes) > 0:
            draw_bounding_boxes_on_image_array(image, boxes, display_str_list=classes)
        
        preview.set_data(image)
        fig.canvas.get_tk_widget().update()

        
        key = cv2.waitKey(20)
        if key == 27: # exit on ESC
            break

    cv2.destroyWindow("preview")


    # with picamera.PiCamera() as camera:
    #     camera.resolution = (640, 480)
    #     while True:
    #         stream = np.empty((480, 640, 3), dtype=np.uint8)
    #         camera.capture(stream, 'rgb')
          
    #         image = load_image(stream)
    #         boxes, scores, classes = detector.detect(image, args.confidence)
    #         for label, score in zip(classes, scores):
    #             print(label, score)
  
    #         if len(boxes) > 0:
    #             draw_bounding_boxes_on_image_array(image, boxes, display_str_list=classes)
            
    #         preview.set_data(image)
    #         fig.canvas.get_tk_widget().update()          
    detector.close()

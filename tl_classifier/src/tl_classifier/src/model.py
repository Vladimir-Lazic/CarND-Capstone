#!/usr/bin/env python
import rospy
import cv2
import csv
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from keras.models import Sequential
from keras.layers import Flatten, Dense, Lambda, Conv2D, Cropping2D

IMG_COUNTER = 100
IMAGE_FOLDER_PATH = "/home/lazic/udacity/CarND-Capstone/tl_classifier/src/tl_classifier/training_data/images/"


class TrafficLightsClassifierTrainer(object):
    def __init__(self):
        rospy.init_node("tl_classifier_train")
        self.training_set = None
        self.test_set = None
        self.model = None
        self.image_buffer = []
        self.images_written = False

        sub = rospy.Subscriber("/image_raw", Image, self.image_cb)
        self.bridge = CvBridge()

        rospy.loginfo("Initialized node")

        rospy.spin()

    def image_cb(self, image_raw):
        if len(self.image_buffer) < IMG_COUNTER:
            rospy.loginfo("Writting image to buffer")
            self.image_buffer.append(self.bridge.imgmsg_to_cv2(image_raw, "bgr8"))
        else:
            if not self.images_written:
                self.create_training_set()
                self.images_written = True

    def create_training_set(self):
        i = 0
        rospy.loginfo("Writting images")
        for image in self.image_buffer:
            file_name = IMAGE_FOLDER_PATH + "image_" + str(i) + ".jpeg"
            cv2.imwrite(file_name, image)
            i += 1

    def create_test_set(self):
        pass

    def define_model(self):
        pass

    def train_model(self):
        pass

    def test_model(self):
        pass


if __name__ == "__main__":
    try:
        TrafficLightsClassifierTrainer()
    except rospy.ROSInterruptException:
        rospy.logerr("Could not start TrafficLightsClassifierTrainer node.")

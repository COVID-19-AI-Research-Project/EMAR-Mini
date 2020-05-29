############################################################################################
#
# Project:       Peter Moss COVID-19 AI Research Project
# Repository:    EMAR Mini, Emergency Assistance Robot
#
# Author:        Adam Milton-Barker (AdamMiltonBarker.com)
# Contributors:
# Title:         EMAR Mini Realsense D415 Reader Class
# Description:   Realsense D415 reader functions for EMAR Mini Emergency Assistance Robot.
# Credit:        MobileNet-SSD-RealSense
#                https://github.com/PINTO0309/MobileNet-SSD-RealSense
# License:       MIT License
# Last Modified: 2020-05-26
#
############################################################################################

import base64, cv2, sys, time

import pyrealsense2 as rs

import numpy as np

from datetime import datetime
from threading import Thread

from Classes.Helpers import Helpers
from Classes.Model import Model
from Classes.Realsense import Realsense
from Classes.Socket import Socket

class RealsenseRead(Thread):
    """ Realsense D415 Reader Class

    Realsense D415 reader functions for EMAR Mini Emergency Assistance Robot.
    """

    def __init__(self):
        """ Initializes the class. """

        super(RealsenseRead, self).__init__()

        self.Helpers = Helpers("Realsense D415 Reader")   
        
        self.colorizer = rs.colorizer()     
        
        # OpenCV fonts
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        self.black = (0, 0, 0)
        self.green = (0, 255, 0)
        
        # Starts the Realsense module
        self.Realsense = Realsense()
        # Connects to the Realsense camera
        self.profile = self.Realsense.connect()
        
        # Starts the socket module
        self.Socket = Socket("Realsense D415 Reader")
        
        # Sets up the object detection model
        self.Model = Model()
        
        self.Helpers.logger.info("Realsense D415 Reader Class initialization complete.")

    def run(self):
        """ Runs the module. """

        t1 = 0
        t2 = 0
        fc = 0
        dc = 0
        fps = ""
        dfps = ""
        
        # Starts the socket server
        soc = self.Socket.connect(self.Helpers.confs["EMAR"]["ip"], 
                                  self.Helpers.confs["Realsense"]["socket"]["port"])

        try:
            while True:
                t1 = time.perf_counter()

                # Wait for a coherent pair of frames: depth and color
                frames = self.Realsense.pipeline.wait_for_frames()
                
                depth_frame = frames.get_depth_frame()
                color_frame = frames.get_color_frame()
                
                #ir1_frame = frames.get_infrared_frame(1)
                #ir2_frame = frames.get_infrared_frame(2)
                
                if not depth_frame or not color_frame:
                #if not not ir1_frame or not ir2_frame:
                    self.Helpers.logger.info("Realsense D415 streams not ready, continuing.")
                    continue

                # Convert images to numpy arrays
                depth_image = np.asanyarray(depth_frame.get_data())
                color_image = np.asanyarray(color_frame.get_data())
                #ir1_image = np.asanyarray(self.colorizer.colorize(ir1_frame).get_data())
                #ir2_image = np.asanyarray(self.colorizer.colorize(ir2_frame).get_data())
                colorized_depth = np.asanyarray(self.colorizer.colorize(depth_frame).get_data())

                width, height = self.Model.getDims(color_image)
                
                self.Model.setBlob(color_image)
                detections = self.Model.forwardPass()
                
                # Writes header to frame
                cv2.putText(color_image, "EMAR Mini Color Stream", (30,50), self.font,
                            0.7, self.black, 2, cv2.LINE_AA)
    
                # Writes date to frame
                cv2.putText(color_image, str(datetime.now()), (30,80), self.font,
                            0.5, self.black, 2, cv2.LINE_AA)
                
                # Writes header to frame
                cv2.putText(colorized_depth, "EMAR Mini Depth Stream", (30,50), self.font,
                            0.7, self.black, 2, cv2.LINE_AA)
    
                # Writes date to frame
                cv2.putText(colorized_depth, str(datetime.now()), (30,80), self.font,
                            0.5, self.black, 2, cv2.LINE_AA)

                for i in range(100):
                    bi = i * 7
                    if i == 0:
                        dc += 1

                    # Object location 
                    x1 = max(0, int(detections[bi + 3] * height))
                    y1 = max(0, int(detections[bi + 4] * width))
                    x2 = min(height, int(detections[bi + 5] * height))
                    y2 = min(width, int(detections[bi + 6] * width))

                    overlay = detections[bi:bi + 7]

                    bi = 0
                    class_id = overlay[bi + 1]
                    percentage = int(overlay[bi + 2] * 100)
                    if (percentage <= self.Helpers.confs["MobileNetSSD"]["threshold"]):
                        continue

                    # Calculates box coordinates
                    box_left = int(overlay[bi + 3] * width)
                    box_top = int(overlay[bi + 4] * height)
                    box_right = int(overlay[bi + 5] * width)
                    box_bottom = int(overlay[bi + 6] * height)
                    
                    # Gets the meters from the depth frame
                    meters = depth_frame.as_depth_frame().get_distance(box_left+int((box_right-box_left)/2), 
                                                                       box_top+int((box_bottom-box_top)/2))
                    
                    if meters != 0.00:
                        label_text = self.Helpers.confs["MobileNetSSD"]["classes"][int(class_id)] + " (" + str(percentage) + "%)"+ " {:.2f}".format(meters) + "m"
                    else:
                        label_text = self.Helpers.confs["MobileNetSSD"]["classes"][int(class_id)] + " (" + str(percentage) + "%)"

                    cv2.rectangle(color_image, (box_left, box_top), (box_right, box_bottom), 
                                  self.green, 1)

                    # Positions and writes the label
                    label_size = cv2.getTextSize(label_text, self.font, 0.5, 1)[0]
                    label_left = box_left
                    label_top = box_top - label_size[1]
                    if (label_top < 1):
                        label_top = 1
                    label_right = label_left + label_size[0]
                    label_bottom = label_top + label_size[1]
                    cv2.putText(color_image, label_text, (label_left, label_bottom), self.font, 0.5, 
                                self.green, 1)

                # Writes FPS and Detection Frames Per Second
                cv2.putText(color_image, fps, (width-170,20), self.font, 0.5, 
                            self.black, 1, cv2.LINE_AA)
                cv2.putText(color_image, dfps, (width-170,35), self.font, 0.5,
                            self.black, 1, cv2.LINE_AA)
                    
                # Combine the color_image and colorized_depth frames together:
                frame = np.hstack((color_image, colorized_depth))
                # Combine the ir1_image and ir2_image frames together:
                #frame = np.hstack((ir1_image, ir2_image))
 
                # Streams the modified frame to the socket server
                encoded, buffer = cv2.imencode('.jpg', frame)
                soc.send(base64.b64encode(buffer))

                # FPS calculation
                fc += 1
                if fc >= 15:
                    fps = "Stream: {:.1f} FPS".format(t1/15)
                    dfps = "Detection: {:.1f} FPS".format(dc/t2)
                    fc = 0
                    dc = 0
                    t1 = 0
                    t2 = 0
                t2 = time.perf_counter()
                elapsedTime = t2-t1
                t1 += 1/elapsedTime
                t2 += elapsedTime

        finally:
            # Stop streaming
            self.Realsense.pipeline.stop()  
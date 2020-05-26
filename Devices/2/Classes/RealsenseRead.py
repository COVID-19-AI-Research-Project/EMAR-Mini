############################################################################################
#
# Project:       Peter Moss COVID-19 AI Research Project
# Repository:    EMAR Mini, Emergency Assistance Robot
#
# Author:        Adam Milton-Barker (AdamMiltonBarker.com)
# Contributors:
# Title:         EMAR Mini Realsense D415 Reader Class
# Description:   Realsense D415 reader functions for EMAR Mini Emergency Assistance Robot.
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
        
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        self.color = (0,0,0)
        
        # Starts the TASS module
        self.Realsense = Realsense()
        # Connects to the camera
        self.profile = self.Realsense.connect()
        # Starts the socket module
        self.Socket = Socket("Realsense D415 Reader")
        
        self.Helpers.logger.info("Realsense D415 Reader Class initialization complete.")

    def run(self):
        """ Runs the module. """
        # Starts the socket server
        soc = self.Socket.connect(self.Helpers.confs["EMAR"]["ip"], 
                                  self.Helpers.confs["Realsense"]["socket"]["port"])

        try:
            while True:
                start_time = time.time()

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
                
                # Writes header to frame
                cv2.putText(color_image, "EMAR Mini Color Stream", (30,50), self.font,
                            0.7, self.color, 2, cv2.LINE_AA)
    
                # Writes date to frame
                cv2.putText(color_image, str(datetime.now()), (30,80), self.font,
                            0.5, self.color, 2, cv2.LINE_AA)
                
                # Writes header to frame
                cv2.putText(colorized_depth, "EMAR Mini Depth Stream", (30,50), self.font,
                            0.7, self.color, 2, cv2.LINE_AA)
    
                # Writes date to frame
                cv2.putText(colorized_depth, str(datetime.now()), (30,80), self.font,
                            0.5, self.color, 2, cv2.LINE_AA)
                    
                # Combine the color_image and colorized_depth frames together:
                frame = np.hstack((color_image, colorized_depth))
                # Combine the ir1_image and ir2_image frames together:
                #frame = np.hstack((ir1_image, ir2_image))
 
                # Streams the modified frame to the socket server
                encoded, buffer = cv2.imencode('.jpg', frame)
                soc.send(base64.b64encode(buffer))
                
                fps = 1.0 / (time.time() - start_time)
                #self.Helpers.logger.info("Realsense D415 Frames Per Second: " + str(fps))

        finally:
            # Stop streaming
            self.Realsense.pipeline.stop() 
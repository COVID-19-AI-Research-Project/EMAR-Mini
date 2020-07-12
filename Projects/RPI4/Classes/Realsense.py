############################################################################################
#
# Project:       Peter Moss COVID-19 AI Research Project
# Repository:    EMAR Mini, Emergency Assistance Robot
#
# Author:        Adam Milton-Barker (AdamMiltonBarker.com)
# Contributors:
# Title:         EMAR Mini Realsense D415 Class
# Description:   Realsense D415 functions for EMAR Mini Emergency Assistance Robot.
# License:       MIT License
# Last Modified: 2020-05-26
#
############################################################################################

import pyrealsense2 as rs

from Classes.Helpers import Helpers

class Realsense():
    
    def __init__(self):
        """ Realsense D415 Class
    
        Realsense D415 functions for the EMAR Mini Emergency Assistance Robot.
        """
        
        self.Helpers = Helpers("Realsense D415", False)
        self.Helpers.logger.info("Realsense D415 Helper Class initialization complete.")
        
    def connect(self):
        """ Connects to the Realsense D415 camera. """
        
        self.pipeline = rs.pipeline()
        
        config = rs.config()
        #config.enable_stream(rs.stream.infrared, 1, 640, 480, rs.format.y8, 30)
        #config.enable_stream(rs.stream.infrared, 2, 640, 480, rs.format.y8, 30)
        config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
        config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
        
        prof = self.pipeline.start(config)
        
        self.Helpers.logger.info("Connected To Realsense D415")
        
        return prof
############################################################################################
#
# Project:       Peter Moss COVID-19 AI Research Project
# Repository:    EMAR Mini, Emergency Assistance Robot
#
# Author:        Adam Milton-Barker (AdamMiltonBarker.com)
# Contributors:
# Title:         EMAR Mini Model Class
# Description:   Model functions for EMAR Mini Emergency Assistance Robot.
# License:       MIT License
# Last Modified: 2020-07-12
#
############################################################################################

import cv2

from Classes.Helpers import Helpers

class Model():
    """ Model Class
    
    Model helper class for the Paper 1 Evaluation.
    """

    def __init__(self):
        """ Initializes the Model class. """

        self.Helpers = Helpers("Model", False)

        self.net = cv2.dnn.readNet(self.Helpers.confs["MobileNetSSD"]["xml"], self.Helpers.confs["MobileNetSSD"]["bin"])
        self.net.setPreferableTarget(cv2.dnn.DNN_TARGET_MYRIAD)
        
        self.imsize = self.Helpers.confs["MobileNetSSD"]["size"]
            
        self.Helpers.logger.info("Model class initialization complete.")
        
    def getDims(self, frame):
        """ Gets the width and height of frame """

        height = frame.shape[0]
        width = frame.shape[1]
        
        return width, height

    def setBlob(self, frame):
        """ Gets a blob from the color frame """

        blob = cv2.dnn.blobFromImage(frame, self.Helpers.confs["MobileNetSSD"]["inScaleFactor"], 
                                    size=(self.imsize, self.imsize), 
                                    mean=(self.Helpers.confs["MobileNetSSD"]["meanVal"], 
                                        self.Helpers.confs["MobileNetSSD"]["meanVal"], 
                                        self.Helpers.confs["MobileNetSSD"]["meanVal"]), 
                                    swapRB=False, crop=False)
        
        self.net.setInput(blob)
        
    def getCrop(self, width, height):
        """ Gets the crop size """
        
        ratio = self.imsize / float(self.imsize)
        
        if width / float(height) > ratio:
            crop = (int(height * ratio), height)
        else:
            crop = (width, int(width / ratio))
        
        return crop

    def forwardPass(self):
        """ Gets a blob from the color frame """

        out = self.net.forward()
        
        return out
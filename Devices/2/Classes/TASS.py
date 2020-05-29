############################################################################################
#
# Project:       Peter Moss COVID-19 AI Research Project
# Repository:    EMAR Mini, Emergency Assistance Robot
#
# Author:        Adam Milton-Barker (AdamMiltonBarker.com)
# Contributors:
# Title:         EMAR Mini TASS Class
# Description:   TASS functions for the EMAR Mini, Emergency Assistance Robot Emergency 
#                Assistance Robot.
# License:       MIT License
# Last Modified: 2020-05-26
#
############################################################################################

import cv2, os

from Classes.Helpers import Helpers

class TASS():
    
    def __init__(self):
        """ TASS Class
    
        TASS functions for the EMAR Mini, Emergency Assistance Robot Emergency
        Assistance Robot.
        """
        
        self.Helpers = Helpers("TASS", False)
        self.Helpers.logger.info("TASS Helper Class initialization complete.")
        
    def connect(self):
        """ Connects to the local TASS. """
        
        self.lcv = cv2.VideoCapture(self.Helpers.confs["TASS"]["vid"])
        
        self.Helpers.logger.info("Connected To TASS")
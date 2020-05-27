############################################################################################
#
# Project:       Peter Moss COVID-19 AI Research Project
# Repository:    EMAR Mini, Emergency Assistance Robot
#
# Author:        Adam Milton-Barker (AdamMiltonBarker.com)
# Contributors:
# Title:         EMAR Mini Wheels Class
# Description:   Wheel functions for EMAR Mini Emergency Assistance Robot.
# License:       MIT License
# Last Modified: 2020-05-26
#
############################################################################################

import sys

from Classes.Helpers import Helpers

class Wheels():
    """ Wheels Class
    
    Wheel functions for EMAR Mini Emergency Assistance Robot.
    """
    
    def __init__(self):
        """ Initializes the class. """
        
        self.Helpers = Helpers("Wheels", False)        
        self.Helpers.logger.info("Wheels Helper Class initialization complete.")
    
    def move(self, direction, message):
        """ Moves the wheels
        
        Interpret commands from the iotJumpWay into actions, moving the wheels.
        """
        
        if direction == "FORWARD":
            self.Helpers.logger.info("Move FORWARD not yet supported!")
        elif direction == "BACKWARD":
            self.Helpers.logger.info("Move BACKWARD not yet supported!")
        elif direction == "LEFT":
            self.Helpers.logger.info("Move LEFT not yet supported!")
        elif direction == "RIGHT":
            self.Helpers.logger.info("Move RIGHT not yet supported!")
############################################################################################
#
# Project:       Peter Moss COVID-19 AI Research Project
# Repository:    EMAR Mini, Emergency Assistance Robot
#
# Author:        Adam Milton-Barker (AdamMiltonBarker.com)
# Contributors:
# Title:         EMAR Mini Arm Class
# Description:   Arm functions for EMAR Mini Emergency Assistance Robot.
# License:       MIT License
# Last Modified: 2020-05-26
#
############################################################################################

import mraa, sys, time

from Classes.Helpers import Helpers
from Classes.Servos import Servos

class Arm():
    """ Arm Class
    
    Arm functions for EMAR Mini Emergency Assistance Robot.
    """
    
    def __init__(self):
        """ Initializes the class. """
        
        self.Helpers = Helpers("Servos", False)
        self.Servos = Servos()

        self.Servos.setup()
        
        self.Helpers.logger.info("Servos Helper Class initialization complete.")
    
    def move(self, direction, message):
        """ Moves the arm
        
        Interpret commands from the iotJumpWay into actions, moving the arm.
        """
        
        if direction == "LEFT":
            self.Servos.left(self.Servos.servo1)
            self.Helpers.logger.info("Moved LEFT!")
        elif direction == "RIGHT":
            self.Servos.right(self.Servos.servo1)
            self.Helpers.logger.info("Moved RIGHT!")
        elif direction == "UP":
            self.Servos.up(self.Servos.servo2)
            self.Helpers.logger.info("Move UP")
        elif direction == "DOWN":
            self.Servos.down(self.Servos.servo2)
            self.Helpers.logger.info("Move DOWN")
        elif direction == "CLOSE":
            self.Servos.close(self.Servos.servo3)
            self.Helpers.logger.info("Gripper CLOSED!")
        elif direction == "OPEN":
            self.Servos.right(self.Servos.servo3)
            self.Helpers.logger.info("Gripper OPEN!")
            
        self.Servos.reset(self.Servos.servo1) 
        self.Servos.reset(self.Servos.servo2) 
        self.Servos.reset(self.Servos.servo3) 
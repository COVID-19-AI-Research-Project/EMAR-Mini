############################################################################################
#
# Project:       Peter Moss COVID-19 AI Research Project
# Repository:    EMAR Mini, Emergency Assistance Robot
#
# Author:        Adam Milton-Barker (AdamMiltonBarker.com)
# Contributors:
# Title:         EMAR Mini Servo Class
# Description:   Servo functions for EMAR Mini Emergency Assistance Robot.
# License:       MIT License
# Last Modified: 2020-05-26
#
############################################################################################

import mraa, sys, time

from Classes.Helpers import Helpers

class Servos():
    """ Servos Class
    
    Servos function for the EMAR Mini, Emergency Assistance Robot.
    """
    
    def __init__(self):
        """ Initializes the class. """
        
        self.Helpers = Helpers("Servos", False)
        self.Helpers.logger.info("Servos Helper Class initialization complete.")

    def setup(self):
        
        # Sets up the servo pins
        self.servo1 = mraa.Pwm(32) 
        self.servo1.enable(True) 
        self.servo1.period_us(20000) 
        
        self.Helpers.logger.info("Servo 1 ready.")

        self.servo2 = mraa.Pwm(16) 
        self.servo2.enable(True) 
        self.servo2.period_us(20000) 
        
        self.Helpers.logger.info("Servo 2 ready.")

        self.servo3 = mraa.Pwm(33) 
        self.servo3.enable(True) 
        self.servo3.period_us(30000) 
        
        self.Helpers.logger.info("Servo 3 ready.")

    def open(self, servo):
        self.move(servo, 0.01)
        time.sleep(1)

    def close(self, servo):
        self.move(servo, 0.75)
        time.sleep(1)

    def up(self, servo):
        self.move(servo, 0.1)
        time.sleep(1)

    def down(self, servo):
        self.move(servo, 0.06)
        time.sleep(1)

    def left(self, servo):
        self.move(servo, 0.01)
        time.sleep(1)

    def right(self, servo):
        self.move(servo, 0.09)
        time.sleep(1)

    def move(self, servo, move):
        servo.write(move)

    def reset(self, servo):
        servo.write(0)
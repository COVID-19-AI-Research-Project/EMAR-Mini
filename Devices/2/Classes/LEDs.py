############################################################################################
#
# Project:       Peter Moss COVID-19 AI Research Project
# Repository:    EMAR Mini, Emergency Assistance Robot
#
# Author:        Adam Milton-Barker (AdamMiltonBarker.com)
# Contributors:
# Title:         EMAR Mini LEDs Class
# Description:   LED functions for EMAR Mini Emergency Assistance Robot.
# License:       MIT License
# Last Modified: 2020-05-26
#
############################################################################################

import mraa, sys, time

from Classes.Helpers import Helpers

class LEDs():
    """ LEDs Class
    
    LEDs function for the EMAR Mini Emergency Assistance Robot.
    """
    
    def __init__(self):
        """ Initializes the class. """
        
        self.Helpers = Helpers("LEDs", False)        
        self.Helpers.logger.info("LEDs Helper Class initialization complete.")
        
        self.Helpers.logger.info("Using MRAA version " + str(mraa.getVersion()))
        
    def setup(self):
        
        # Sets the power LED
        self.PowerLED = mraa.Gpio(15)
        time.sleep(0.1)
        self.PowerLED.dir(mraa.DIR_OUT)
        
        # Sets the communication LED
        self.CommunicationLED = mraa.Gpio(13)
        time.sleep(0.1)
        self.CommunicationLED.dir(mraa.DIR_OUT)
        
        self.Helpers.logger.info("LEDs ready!")

    def powerup(self):
        """ Flashes the EMAR power LED """
        
        # Alternates the power LED
        self.PowerLED.write(1)
        time.sleep(1)
        self.PowerLED.write(0)
        time.sleep(1)
        self.PowerLED.write(1)
        time.sleep(1)
        self.PowerLED.write(0)
        
        self.Helpers.logger.info("Power LED ready!")

    def cpowerup(self):
        """ Flashes the EMAR communication LED """
        
        # Alternates the communication LED
        self.CommunicationLED.write(1)
        time.sleep(1)
        self.CommunicationLED.write(0)
        time.sleep(1)
        self.CommunicationLED.write(1)
        
        self.Helpers.logger.info("Communication LED ready!")

    def dataReceived(self):
        """ Flashes the EMAR communication LED """
        
        # Alternates the communication LED
        self.CommunicationLED.write(1)
        time.sleep(1)
        self.CommunicationLED.write(0)
        time.sleep(1)
        self.CommunicationLED.write(1)
        
        self.Helpers.logger.info("Communication LED ready!")

    def shutdown(self, led):
        """ Resets the passed LED """
        
        led.write(0)
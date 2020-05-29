############################################################################################
#
# Project:       Peter Moss COVID-19 AI Research Project
# Repository:    EMAR Mini, Emergency Assistance Robot
#
# Author:        Adam Milton-Barker (AdamMiltonBarker.com)
# Contributors:
# Title:         EMAR Mini Emergency Assistance Robot Class
# Description:   The EMAR Mini Emergency Assistance Robot Class is the the core
#                for the EMAR Mini software.
# License:       MIT License
# Last Modified: 2020-05-29
#
############################################################################################

import geocoder, json, psutil, sys, threading

from threading import Thread

from Classes.Helpers import Helpers
from Classes.iotJumpWay import Device as iotJumpWay
from Classes.LEDs import LEDs
from Classes.RealsenseRead import RealsenseRead
from Classes.RealsenseStream import RealsenseStream

class EMAR():
    """ EMAR Mini Emergency Assistance Robot Class
    
    The EMAR Mini Emergency Assistance Robot Class is the the core wrapper class
    for the EMAR Mini software.
    """
    
    def __init__(self):
        """ Initializes the class. """

        self.Helpers = Helpers("EMAR")
        
        # Starts the iotJumpWay
        self.iotJumpWay = iotJumpWay()
        self.iotJumpWay.connect()
        
        # Subscribes to the EMAR Mini commands topic 
        self.iotJumpWay.channelSub("Commands")
        # Sets the EMAR Mini commands callback function 
        self.iotJumpWay.commandsCallback = self.commands

        self.Helpers.logger.info("EMAR Mini awaiting commands.")
        self.Helpers.logger.info("EMAR Mini Emergency Assistance Robot Class initialization complete.")

    def hardware(self):
        """ Loads the EMAR Mini hardware modules. """
        
        # Sets up EMAR Mini LEDs 
        self.LEDs = LEDs()
        self.LEDs.setup()

        self.Helpers.logger.info("EMAR Mini hardware modules loaded.")
            
    def commands(self, topic, payload):
        """ 
        iotJumpWay Commands Callback
        
        The callback function that is triggerend in the event of a
        command communication from the iotJumpWay.
        """
        
        self.Helpers.logger.info("Recieved iotJumpWay Command Data : " + str(payload))
        
    def life(self):
        """ Sends vital statistics to HIAS """
        
        cpu = psutil.cpu_percent()
        mem = psutil.virtual_memory()[2]
        hdd = psutil.disk_usage('/').percent
        tmp = psutil.sensors_temperatures()['coretemp'][0].current
        g = geocoder.ip('me')
        
        self.Helpers.logger.info("EMAR Mini Life (TEMPERATURE): " + str(tmp) + "\u00b0")
        self.Helpers.logger.info("EMAR Mini Life (CPU): " + str(cpu) + "%")
        self.Helpers.logger.info("EMAR Mini Life (Memory): " + str(mem) + "%")
        self.Helpers.logger.info("EMAR Mini Life (HDD): " + str(hdd) + "%")
        self.Helpers.logger.info("EMAR Mini Life (LAT): " + str(g.latlng[0]))
        self.Helpers.logger.info("EMAR Mini Life (LNG): " + str(g.latlng[1]))
        
        # Send iotJumpWay notification
        self.iotJumpWay.channelPub("Life", {
            "CPU": cpu,
            "Memory": mem,
            "Diskspace": hdd,
            "Temperature": tmp,
            "Latitude": g.latlng[0],
            "Longitude": g.latlng[1]
        })
        
        # Life thread
        threading.Timer(60.0, self.life).start()
        
    def threading(self):
        """ Starts the EMAR Mini software threads. """
        
        # Life thread
        threading.Timer(60.0, self.life).start()
        
        # LED startup threads
        Thread(target = self.LEDs.powerup, args = ()).start()
        Thread(target = self.LEDs.cpowerup, args = ()).start()
        
        # Realsense threads
        Thread(target=RealsenseRead().run).start()
        Thread(target=RealsenseStream().run).start()
        
    def shutdown(self):
        """ Shuts down the EMAR Mini software. """
        
        self.LEDs.shutdown(self.LEDs.PowerLED)
        self.LEDs.shutdown(self.LEDs.CommunicationLED)
        
        self.iotJumpWay.disconnect()
        self.Helpers.logger.info("EMAR Mini Exiting")
        sys.exit()
        
EMAR = EMAR()

def main():
    # Starts threading
    try:
        EMAR.hardware()
        EMAR.threading()
        #Continous loop to keep the program running
        while True:
            continue
        # Exits the program
        EMAR.shutdown()
        
    except KeyboardInterrupt:
        # Cathces CTRL + C and exits the program
        EMAR.shutdown()

if __name__ == "__main__":
    main()
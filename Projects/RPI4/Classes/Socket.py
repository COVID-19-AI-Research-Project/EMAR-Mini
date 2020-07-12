############################################################################################
#
# Project:       Peter Moss COVID-19 AI Research Project
# Repository:    EMAR Mini, Emergency Assistance Robot
#
# Author:        Adam Milton-Barker (AdamMiltonBarker.com)
# Contributors:
# Title:         EMAR Mini Socket Server Class
# Description:   Socket server functions for EMAR Mini Emergency Assistance Robot.
# License:       MIT License
# Last Modified: 2020-05-26
#
############################################################################################

import zmq, base64

import numpy as np

from Classes.Helpers import Helpers

class Socket():
    
    def __init__(self, typeo):
        """ Socket Server Class
    
        Socket server functions for EMAR Mini Emergency Assistance Robot.
        """
        
        self.Helpers = Helpers("Socket", False)
        self.type = typeo
        
        self.Helpers.logger.info(self.type + " Socket Helper Class initialization complete.")
        
    def connect(self, ip, port):
        """ Connects to the local Socket. """
        
        try:
            soc = zmq.Context().socket(zmq.PUB)
            soc.connect("tcp://"+ip+":"+str(port))
            self.Helpers.logger.info(self.type + " started & connected to socket server: tcp://"+ip+":"+str(port))
            return soc
        except:
            self.Helpers.logger.info(self.type + " failed to connect to socket server: tcp://"+ip+":"+str(port))
        
    def subscribe(self, ip, port):
        """ Subscirbes to the server. """
        
        try:
            context = zmq.Context()
            rsoc = context.socket(zmq.SUB)
            rsoc.bind("tcp://*:"+str(port))
            rsoc.setsockopt_string(zmq.SUBSCRIBE, np.unicode(''))
            self.Helpers.logger.info(self.type + " Subscribed to socket: tcp://"+ip+":"+str(port))
            return rsoc
        except:
            self.Helpers.logger.info(self.type + " failed to connect to tcp://"+ip+":"+str(port))
        
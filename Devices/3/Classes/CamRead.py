############################################################################################
#
# Project:       Peter Moss COVID-19 AI Research Project
# Repository:    EMAR Mini, Emergency Assistance Robot
#
# Author:        Adam Milton-Barker (AdamMiltonBarker.com)
# Contributors:
# Title:         EMAR Mini CamRead Class
# Description:   CamRead functions for the EMAR Mini Emergency Assistance Robot.
# License:       MIT License
# Last Modified: 2020-05-26
#
############################################################################################

import base64, cv2, sys, time

from datetime import datetime
from threading import Thread

from Classes.Helpers import Helpers
from Classes.TASS import TASS
from Classes.Socket import Socket

class CamRead(Thread):
    """ CamRead Class

    CamRead function for the EMAR Emergency Assistance Robot.
    """

    def __init__(self):
        """ Initializes the class. """

        super(CamRead, self).__init__()

        self.Helpers = Helpers("CamRead")        
        self.Helpers.logger.info("CamRead Class initialization complete.")

    def run(self):
        """ Runs the module. """
        
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        self.color = (0,0,0)
        
        # Starts the TASS module
        self.TASS = TASS()
        # Connects to the camera
        self.TASS.connect()
        # Starts the socket module
        self.Socket = Socket("CamRead")
        # Starts the socket server
        soc = self.Socket.connect(self.Helpers.confs["EMAR"]["ip"], 
                                  self.Helpers.confs["TASS"]["socket"]["port"])

        while True:
            try:
                start_time = time.time()
                # Reads the current frame
                _, frame = self.TASS.lcv.read()
                
                # Writes header to frame
                cv2.putText(frame, "EMAR Camera 1", (10,50), self.font,
                            1.5, self.color, 2, cv2.LINE_AA)
    
                # Writes date to frame
                cv2.putText(frame, str(datetime.now()), (10,80), self.font,
                            1, self.color, 2, cv2.LINE_AA)

                # Streams the frame to the socket server
                encoded, buffer = cv2.imencode('.jpg', frame)
                soc.send(base64.b64encode(buffer))
                
            except KeyboardInterrupt:
                self.TASS.lcv.release()
                break
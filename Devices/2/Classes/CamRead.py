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

        fps = ""
        framecount = 0
        time1 = 0
        time2 = 0
        
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
                t1 = time.perf_counter()
                # Reads the current frame
                _, frame = self.TASS.lcv.read()

                width = frame.shape[1]
                
                # Writes header to frame
                cv2.putText(frame, "EMAR Mini Live Stream", (30, 50), self.font,
                            0.7, self.color, 2, cv2.LINE_AA)
    
                # Writes date to frame
                cv2.putText(frame, str(datetime.now()), (30, 80), self.font,
                            0.5, self.color, 2, cv2.LINE_AA)
                
                cv2.putText(frame, fps, (width-170, 30), cv2.FONT_HERSHEY_SIMPLEX, 
                            0.5, self.color, 1, cv2.LINE_AA)

                # Streams the frame to the socket server
                encoded, buffer = cv2.imencode('.jpg', frame)
                soc.send(base64.b64encode(buffer))

                # FPS calculation
                framecount += 1
                if framecount >= 15:
                    fps       = "Stream: {:.1f} FPS".format(time1/15)
                    framecount = 0
                    time1 = 0
                    time2 = 0
                t2 = time.perf_counter()
                elapsedTime = t2-t1
                time1 += 1/elapsedTime
                time2 += elapsedTime
                
            except KeyboardInterrupt:
                self.TASS.lcv.release()
                break
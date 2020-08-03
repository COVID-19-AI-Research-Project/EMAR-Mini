/*
  Project:       Peter Moss COVID-19 AI Research Project
  Repository:    EMAR Mini, Emergency Assistance Robot

  Author:        Adam Milton-Barker (AdamMiltonBarker.com)
  Contributors:
  Title:         EMAR Mini Remote Control Receiver
  Description:   The EMAR Mini Remote Control Receiver receives 
                 IR commands and sends them to the iotJumpWay via
                 the EMAR Mini Remote Control iotJumpWay Publisher.
  License:       MIT License
  Last Modified: 2020-07-13
  Credit: Based on example code from www.elegoo.com
*/

#include <ArduinoJson.h>
#include "IRremote.h"
#include "IR.h"

IRrecv irrecv(RECEIVER);
decode_results results;

String deviceID = "";

void setup() {
  Serial.begin(9600);
  Serial.println("EMAR Mini Remote Control Receiver");
  irrecv.enableIRIn();
}

void send_communication(String cTypeR, String cValR, String cMessageR)
{
  String jsonString = "{\"From\":\""+deviceID+"\",\"Type\":\""+cTypeR+"\",\"Value\": \""+cValR+"\",\"Message\": \""+cMessageR+"\"}";
  char charBuff[89];
  jsonString.toCharArray(charBuff, 89);
  Serial.println(jsonString);
}

void loop()
{
  int tmpValue;
  if (irrecv.decode(&results))
  {
    for (int i = 0; i < 23; i++)
    {
      if ((keyValue[i] == results.value) && (i<KEY_NUM))
      {
        String aVal = keyBuf[i];
        String cType = "";
        String cVal = "";
        String cMessage = "";

        if(aVal=="VOL+")
        {
          cType = "Head";
          cVal = "UP";
          cMessage = "Move Head UP";
          send_communication(cType, cVal, cMessage);
        }
        else if(aVal=="VOL-")
        {
          cType = "Head";
          cVal = "DOWN";
          cMessage = "Move Head DOWN";
          send_communication(cType, cVal, cMessage);
        }
        else if(aVal=="FAST FORWADOWN")
        {
          cType = "Head";
          cVal = "RIGHT";
          cMessage = "Move Head RIGHT";
          send_communication(cType, cVal, cMessage);
        }
        else if(aVal=="FAST BACK")
        {
          cType = "Head";
          cVal = "LEFT";
          cMessage = "Move Head LEFT";
          send_communication(cType, cVal, cMessage);
        }
        else if(aVal=="PAUSE")
        {
          cType = "Head";
          cVal = "CENTER";
          cMessage = "Move Head CENTER";
          send_communication(cType, cVal, cMessage);
        }
        else if(aVal=="UP")
        {
          cType = "Arm";
          cVal = "UP";
          cMessage = "Move Arm 1 UP";
          send_communication(cType, cVal, cMessage);
        }
        else if(aVal=="DOWN")
        {
          cType = "Arm";
          cVal = "DOWN";
          cMessage = "Move Arm 1 DOWN";
          send_communication(cType, cVal, cMessage);
        }
        else if(aVal=="2")
        {
          cType = "Arm";
          cVal = "2UP";
          cMessage = "Move Arm 2 UP";
          send_communication(cType, cVal, cMessage);
        }
        else if(aVal=="5")
        {
          cType = "Arm";
          cVal = "2DOWN";
          cMessage = "Move Arm 2 DOWN";
          send_communication(cType, cVal, cMessage);
        }
        
        tmpValue = results.value;
        
      }
      else if(REPEAT==i)
      {
        results.value = tmpValue;
      }
    }
    irrecv.resume(); // receive the next value
  }
}

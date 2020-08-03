/*
  Project:       Peter Moss COVID-19 AI Research Project
  Repository:    EMAR Mini, Emergency Assistance Robot

  Author:        Adam Milton-Barker (AdamMiltonBarker.com)
  Contributors:
  Title:         EMAR Mini Remote Control iotJumpWay Publisher
  Description:   The EMAR Mini Remote Control iotJumpWay Publisher 
                 receives IR commands from the Remote Control Receiver 
                 via serial and sends them to the iotJumpWay.
  License:       MIT License
  Last Modified: 2020-07-04
  Credit: Based on example code from www.elegoo.com
*/

#include <ArduinoJson.h>
#include <ESP8266WiFi.h>
#include <PubSubClient.h>
#include <WiFiClientSecure.h> 

static const char hias_cert[] PROGMEM = R"EOF(
-----BEGIN CERTIFICATE-----
-----END CERTIFICATE-----
)EOF";

const char fingerprint[] PROGMEM = "";

const char* ssid = "";
const char* password = "";

const char* mqtt_server = "";
int mqttPort = 8883;

String locationID = "";
String applicationID = "";
char applicationName[] = ""; 
char mqttUsername[] = ""; 
char mqttPassword[] = ""; 
char willTopic[50];

String zoneID = "";
String deviceID = "";

BearSSL::WiFiClientSecure espClient;
PubSubClient client(espClient);
BearSSL::X509List cert(hias_cert);

char charBuf[50];

void setupWiFi() {
  
  delay(10);
  
  Serial.println();
  Serial.print("Connecting to WiFi network: ");
  Serial.println(ssid);
  
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  
  Serial.println("");
  Serial.println("WiFi connected succesfully!");
  Serial.print("Device IP address: ");
  Serial.println(WiFi.localIP());
  
}

void callback(char* topic, byte* payload, unsigned int length) {
  
  Serial.println("Unused");
  
}

void publishToApplicationStatus(const char* data){
  String statusTopic = locationID+"/Applications/"+applicationID+"/Status";
  statusTopic.toCharArray(charBuf, 50);
  client.publish(charBuf, data);
}

void publishToDeviceCommands(const char* data){
  String commandTopic = locationID+"/Devices/"+zoneID+"/"+deviceID+"/Commands";
  commandTopic.toCharArray(charBuf, 50);
  client.publish(charBuf, data);
}

void reconnect() {
  while (!client.connected()) {
    
    Serial.println("Attempting connection to HIAS iotJumpWay Broker...");
    
    String willTopicString = locationID+"/Applications/"+applicationID+"/Status";
    willTopicString.toCharArray(willTopic, 50);
    
    if (client.connect(applicationName, mqttUsername, mqttPassword, willTopic, 0, 0, "OFFLINE")) {
      Serial.println("Connected to HIAS iotJumpWay Broker!");
      publishToApplicationStatus("ONLINE");
    } else {
      Serial.print("Failed to connect to HIAS iotJumpWay Broker, rc=");
      Serial.println(client.state());
      Serial.println("... trying again in 5 seconds");
      delay(5000);
    }
    
  }
}

void setup() {
  
  Serial.begin(9600);
  
  setupWiFi();
  //espClient.setTrustAnchors(&cert);
  espClient.setFingerprint(fingerprint);
  client.setServer(mqtt_server, mqttPort);
  client.setCallback(callback);
}

void loop() {
  
  if (!client.connected()) {
    reconnect();
  }
  client.loop();
  
  while (Serial.available() > 0)
  {
    String jsReceived = Serial.readStringUntil('\n');

    StaticJsonDocument<200> jsonBuffer;
    auto error = deserializeJson(jsonBuffer, jsReceived);
    if(error)
    {
      Serial.println("Command Not Sent");
    }
    else
    {
      char jsData[89];
      jsReceived.toCharArray(jsData, 89);
      publishToDeviceCommands(jsData);
      Serial.println("Command Sent");
    }
  }
  
  delay(1000);
}

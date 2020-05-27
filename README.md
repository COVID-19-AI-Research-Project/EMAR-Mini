# Peter Moss COVID-19 AI Research Project
## EMAR Mini Emergency Assistance Robot
[![Emergency Assistance Robot](Media/Images/EMAR-Mini.png)](https://github.com/COVID-19-AI-Research-Project/EMAR-Mini)

[![VERSION](https://img.shields.io/badge/VERSION-0.0.0-blue.svg)](https://github.com/COVID-19-AI-Research-Project/EMAR-Mini/tree/0.0.0) [![DEV BRANCH](https://img.shields.io/badge/DEV%20BRANCH-0.1.0-blue.svg)](https://github.com/COVID-19-AI-Research-Project/EMAR-Mini/tree/0.1.0) [![Issues Welcome!](https://img.shields.io/badge/Contributions-Welcome-lightgrey.svg)](CONTRIBUTING.md) [![Issues](https://img.shields.io/badge/Issues-Welcome-lightgrey.svg)](issues) [![LICENSE](https://img.shields.io/badge/LICENSE-MIT-blue.svg)](LICENSE)

&nbsp; 

# Table Of Contents

- [Introduction](#introduction)
- [Key Features](#key-features)
- [Assistance Features](#assistance-features)
- [Open Technology](#open-technology)
- [Required Hardware](#required-hardware)
- [Installation](#installation)
- [Contributing](#contributing)
    - [Contributors](#contributors)
- [Versioning](#versioning)
- [License](#license)
- [Bugs/Issues](#bugs-issues)

&nbsp;

# Introduction

**EMAR Mini** is a minature version of EMAR, an open-source Emergency Robot Assistant to assist doctors, nurses and hospital staff during the COVID-19 pandemic, and similar situations we may face in the future.

The idea for this open-source tele-operated robot came as I was sat in room in a hospital surrounded by people with COVID-19 as a potential COVID-19 Pneumonia patient. The doctors, nurses and other teams were in among us for the whole 12 hours or more I was in the hospital.

Some of the common things I saw was nurses & doctors calling patients, giving paracetamol, taking temperatures, adjusting masks and blankets. Every time one of the medical staff had to do one of these tasks they were putting themselves in danger of catching COVID-19.

Each of these tasks can be carried out by tele-operated robots, so this is where the idea came from.   

EMAR Mini will be our official demonstration robot as it is smaller and more portable, though has obvious restrictions compared to EMAR. 

__This project is a work in progress, however our plan is to work with a local medical/health center or hospital to do a pilot project with EMAR (Large).__

&nbsp;

# Key Features

- **HIAS Network Device**
    - EMAR is a device on the HIAS network, allowing machine to machine/machine to application communication.
- **HIAS UI Plugin**
    - Integration with the HIAS UI.
- **3D printed**
    - EMAR's shell is 3D printed.
- **Tele-Operated** 
    - Remotely operated using the HIAS UI & voice control.
- **Realtime Camera Stream** 
    - Streams local camera frames to a local server, used by HIAS to allow users to see where they are navigating EMAR Mini.
- **Two way audio streaming** 
    - Two way audio streaming allows medical staff and patients to communicate.
- **Realtime Depth Sensing** 
    - Uses Intel Realsense D415 camera and streams depth frames to a local server, used by HIAS to allow users to see realtime stream of depth sensors.
- **Realtime Temperature Sensing** 
    - Uses thermal camera to take temperature readings of patients.

&nbsp;

# Assistance Features
- **Temperature Reading** 
    - Able to take temperatures of patients.
- **Adjusting Blankets** 
    - Able to adjust blankets on patients.
- **Adjusting Breathing Apparatus** 
    - Able to adjust beathing apparatus on patients.

&nbsp;

# Open Technology
- **Open Software** 
    - EMAR Mini's software is entirely open-source.
- **Open STLS** 
    - The STL files required to print EMAR are open-source.

&nbsp;

# Required Hardware
- **3 x UP2 Devices** 
    - Used to home the software reqired for all of EMAR Mini's features.
- **AAEON EP-DCOV2735-F36 - USB 1080P HD Camera** 
    - Used to stream real-time camera stream for navigation and communication.
- **Intel Realsense D415** 
    - Used to stream real-time depth sensor stream.
- **Thermal Camera** 
    - Used to take the temperature of patients.
- **6 DOF Robot Manipulator Metal Alloy Mechanical Arm Clamp Claw Kit MG996R** 
    - Controlled using HIAS UI.

&nbsp;

## Installation
Installation scripts and tutorials for setting up your Emergency Assistance Robot & UI are provided. To get started, please follow the installation guides provided below in the order they are given.

**PLEASE NOTE: This project requires a functioning installation of the [HIAS server](https://github.com/LeukemiaAiResearch/HIAS "HIAS server"). Follow the [HIAS server installation guide](https://github.com/LeukemiaAiResearch/HIAS/blob/master/Documentation/Installation/Installation.md "HIAS server installation guide") before beginning these tutorials.

| ORDER | GUIDE | INFORMATION | AUTHOR | Status |
| ----- | ----- | ----------- | ------ | ------ |
| 1 | [Device 1](Devices/1/Documentation/Installation/Installation.md "Device 1") | Device 1 installation guide covering wheels installation. |  [Adam Milton-Barker](https://www.leukemiaresearchassociation.ai.com/team/adam-milton-barker "Adam Milton-Barker") | DEVELOPMENT | 
| 2 | [Device 2](Devices/2/Documentation/Installation/Installation.md "Device 2") | Device 2 installation guide covering arm, Realsense and NCS2 installation |  [Adam Milton-Barker](https://www.leukemiaresearchassociation.ai.com/team/adam-milton-barker "Adam Milton-Barker") | DEVELOPMENT | 
| 3 | [Device 3](Devices/3/Documentation/Installation/Installation.md "Device 3") | Device 3 installation guide covering camera pan/tilt  and NCS2 installation |  [Adam Milton-Barker](https://www.leukemiaresearchassociation.ai.com/team/adam-milton-barker "Adam Milton-Barker") | DEVELOPMENT | 

&nbsp;

# Contributing

The Peter Moss Acute COVID-19 AI Research project encourages and welcomes code contributions, bug fixes and enhancements from the Github.

Please read the [CONTRIBUTING](CONTRIBUTING.md "CONTRIBUTING") document for a full guide to forking your repositories and submitting your pull requests. You will also find information about your code of conduct on this page.

## Contributors

- [Adam Milton-Barker](https://www.leukemiaresearchassociation.ai.com/team/adam-milton-barker "Adam Milton-Barker") - [Peter Moss Leukemia AI Research](https://www.leukemiaresearchassociation.ai "Peter Moss Leukemia AI Research") Founder & Intel Software Innovator, Sabadell, Spain
- [Jose Mario Garza](https://www.leukemiaresearchassociation.ai/team/jose-mario-garza "Jose Mario Garza") - [Peter Moss Leukemia AI Research](https://www.leukemiaresearchassociation.ai "Peter Moss Leukemia AI Research") 3D Designer/Printer, Mexico
- [Utkrisht Sharma](https://www.leukemiaresearchassociation.ai/team/utkrisht-sharma "Utkrisht Sharma") - [Peter Moss Leukemia AI Research](https://www.leukemiaresearchassociation.ai "Peter Moss Leukemia AI Research") Robotics Engineering & R&D, India
- [Rahul Gupta](https://www.leukemiaresearchassociation.ai/team/rahul-gupta "Rahul Gupta") - [Peter Moss Leukemia AI Research](https://www.leukemiaresearchassociation.ai "Peter Moss Leukemia AI Research") Robotics Engineering & R&D, India

&nbsp;

# Versioning

We use SemVer for versioning. For the versions available, see [Releases](releases "Releases").

&nbsp;

# License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE "LICENSE") file for details.

&nbsp;

# Bugs/Issues

We use the [repo issues](issues "repo issues") to track bugs and general requests related to using this project. See [CONTRIBUTING](CONTRIBUTING.md "CONTRIBUTING") for more info on how to submit bugs, feature requests and proposals.
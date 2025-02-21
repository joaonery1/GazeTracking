# Gaze Tracking with heat map

![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

This is a Python (2 and 3) library that provides a **webcam-based eye tracking system**. It gives you the exact position of the pupils and the gaze direction, in real time.
In addition, you can map pupil position onto screen coordinates, for example, to determine which window the user is looking at.
User is fixating at the red dots on the screen. The small white dots mark the EPOG estimate.


## Installation

Clone this project:

```
https://github.com/joaonery1/GazeTracking.git
```

Install dependencies (NumPy, OpenCV, Dlib), as well as other dependencies:

```
pip install -r requirements.txt
```

> The Dlib library has four primary prerequisites: Boost, Boost.Python, CMake and X11/XQuartx. If you do not have them, you can [read this article](https://www.pyimagesearch.com/2017/03/27/how-to-install-dlib/) to know how to easily install them.

In addition, if you want screen-size handling:
```
pip install pypiwin32  # for Windows
```
```
pip install pyobjc  # for MacOS
```
Screen-size handling in MacOS also requires AppKit, which is included in XCode.
```
pip install python3-xlib  # for Linux
```

Run the demo:

```
./screen_example.py
```

> [!WARNING]  
> Sometimes the program may have inaccuracies due to the environment, webcam, camera position and even posture.

>[!TIP]
>A bright environment is recommended and preferably a background without objects, to better capture your eye.


## Licensing

This project is released by Antoine Lamé under the terms of the MIT Open Source License. View LICENSE for more information.


## Hardware utilized
- Intel(R) Core(TM) i5-3470 CPU @ 3.20GHz   3.20 GHz
- 16,0 GB RAM
- Logitech C270 HD





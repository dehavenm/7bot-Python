# 7bot-Python

A Python library for controlling the 7Bot robot arm from a host PC.

The 7Bot is a desktop six-axis robot arm released on Kickstarter in 2015. It is driven by specialized digital servos connected to an Arduino Due in the base of the robot. It includes a small vacuum pump in its base for picking up objects, and offered an optional gripper with a seventh servo. The robot can be controlled from a PC by sending and receiving data through the USB link in the Arduino board.


## Presequisites

Arduino software (Can be downloadwed at https://www.arduino.cc/en/Main/Software)

Pyserial

For running GUI example code: PyQT5


## Installing

Follow the instructions in the file "Getting Started with 7Bot v1.0.pdf" to set up the Arduino Due drivers and 7Bot Arduino code.

For running the GUI example code, clone the repo into any convenient location. To use the library with your own code, copy the file sevenbot.py into the directory where your robot code will be located. 


Connect the USB port in the 7Bot base to the host PC. Open the Arduino software, go to Tools->Port, and look at the list of avilable COM ports. The COM port where the 7Bot is connected will be listed as "Arduino Due (Programming Port)". 


##Running the GUI code

Once installed, open the GUI code (either ikgui.py or sevenbotgui.py) and find the line:

'''
self.arm = SevenBot('COM10', 115200)
'''

Edit the argument "COM10" to change the number to the COM port to which your system has assigned the 7Bot's Arduino board (see previous step).


##Using the library

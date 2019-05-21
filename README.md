# 7bot-Python

A Python library for controlling the 7Bot robot arm from a host PC. It is a slightly refined version of the code found here:

https://github.com/woshialex/py7bot

The 7Bot is a desktop six-axis robot arm released on Kickstarter in 2015. It is driven by specialized digital servos connected to an Arduino Due in the base of the robot. It includes a small vacuum pump in its base for picking up objects, and offered an optional gripper with a seventh servo. The robot can be controlled from a PC by sending and receiving data through the USB link in the Arduino board.

## Prerequisites

Arduino software (Can be downloadwed at https://www.arduino.cc/en/Main/Software)

Numpy

Pyserial

For running GUI example code: PyQT5


## Installing

Follow the instructions in the file "Getting Started with 7Bot v1.0.pdf" to set up the Arduino Due drivers and 7Bot Arduino code.

For running the GUI example code, clone the repo into any convenient location. To use the library with your own code, copy the file sevenbot.py into the directory where your robot code will be located. 


Connect the USB port in the 7Bot base to the host PC. Open the Arduino software, go to Tools->Port, and look at the list of avilable COM ports. The COM port where the 7Bot is connected will be listed as "Arduino Due (Programming Port)". 


## Running the GUI code

Once installed, open the GUI code (either ikgui.py or sevenbotgui.py) in a Python IDE and find the line:

`self.arm = SevenBot('COM10', 115200)`

Edit the argument "COM10" to change the number to the COM port to which your system has assigned the 7Bot's Arduino board (see previous step). After that, you can run the Python file.


## Using the library

### Initialization:

`arm = SevenBot(port, baud_rate)`

Creates an object representing a SevenBot connected on a specified COM port, and attempts to open serial communication. See installation instructions for selecting correct COM port. Baud rate should always be set to 115200 (standard for serial communication with most Arduino boards).


### Force Status


`arm.setForceStatus(status)`

Sets the operational status of the robot's servo motors. Possible values for status are as follows:

0 - Forceless: The motors are powered off, but positions can still be read through their encoders

1 - Normal operation

2 - Protected: Allows for normal operation, but force status cannot be changed directly between "Protected" and "Forceless" (must change to "Normal" first)


### Speed

`arm.setSpeed(speed)`

Sets the motor speed for each individual servo of the robot, given as a Numpy array of 7 values from 0-250. Array indices 0-5 refer to the robot's joints, and index 6 controls the speed of the gripper servo (if using the optional gripper).

### Position

`arm.setAngle(angles)`

Sets the position of each servo (from 0-180 degrees) of the robot, given as a Numpy array of 7 values from 0-180. Array indices 0-5 refer to the robot's joints, and index 6 controls the speed of the gripper servo (if using the optional gripper). If using the vacuum pump, set the value of index 6 to 0 to turn the vacuum on, and 180 to turn it off. The servos have an effective angular resolution of roughly 0.18 degrees.


### Inverse Kinematics 

The included Arduino code includes a number of inverse kinematic functions for directly commanding the robot's position.

#### Function IK5

`arm.setIK5(position, vec56, theta5, theta6)`

Function arguments are as follows:

position: array of 3 integers defining the robot's wrist position in millimeters [x, y, z]

vec56: array defining unit vector (expressed as integers spaled from -1023 to 1023) describing the direction in which the robot's wrist is pointed [x, y, z]

theta5: rotation of robot's wrist (0-180 degrees)

theta6: position of gripper servo (8-180 degrees)

#### Function IK6

`arm.setIK6(self, j6, vec56, vec67, theta6)`

Function arguments are as follows:

position: array of 3 integers defining the robot's wrist position in millimeters [x, y, z]

vec56: array defining unit vector (expressed as integers spaled from -1023 to 1023) describing the direction in which the robot's wrist is pointed [x, y, z]

vec56: array defining unit vector (expressed as integers spaled from -1023 to 1023) describing the rotation of the robot's wrist [x, y, z]

theta6: position of gripper servo (8-180 degrees)

See the file "Communication Instruction (v1.0.1).pdf" for mode detailed information about the robot's communication protocol, coordinate system, and joints.


### Additional Links

[Pinecone AI](https://www.pinecone.ai/) - the startup which first created the 7Bot. They do not currently have it avilable for sale, but they claim they will release a new version of it in the near future.


[7Bot-Arduino-lib](https://github.com/7Bot/7Bot-Arduino-lib) - 7Bot Arduino files can be downloaded here.

robot_car_s
## Robot Car (Raspberry Pi 3 - simple)

The objective of setup the Raspberry Pi Robot Car is to demonstrate
the use of Python language through Raspberry Pi to control robots, 
visual and audio responses and display information. 
Different types of common hardware are used to enable movement 
(motors and servo), computer vision (USB webcam), audio response 
(sound and speaker), display information (LED matrix and LCD display) 
and sensor to detect environment changes (distance sensor and accelerometer)

![Robot Car - Raspberry Pi 3](images/Robot_Car.jpg)
![Robot Car - others](images/Robot_Car_others.JPG)

## Getting Started
**Physical setup (components):**
* Robot Car chassis, wheels, motors, power supply
 and circuit control board (L298N) for movement
* Single-board computer (Raspberry Pi 3) to 
run the Python program and control the Raspberry Pi Robot Car
* Separated Power supply for the robot car motors
* Separated Power supply for the Raspberry Pi 3
* Ultrasonic sensor (HC-SR04) to sense the distance
* Accelerometer (ADXL345) to sense the dips, humps, acceleration 
and deceleration
* Servo (sg90) micro-servo to move the HC-SR04 to scan the distance
 between the robot car and obstacles 
 * Mounting kit for the Servo
* RGB led display different colour (RGB led) to signal the status of the robot car
* 8x8 LED matrix (Maxim 7219) to display single character of scrolling message in LEDs
* 16x2 LCD display (lcd 1602 with i2c connection) to display message in 2 rows
* Logitech C310 webcam or equivalent that could be detected by Raspberry Pi 
for OpenCV (Computer Vision) in the future
* Mini-Speaker with amplifier for audio output in the future
* Bread board to connect related hardware together
* T-Cobbler connector and cable
* Wire Jumpers
* Mini On-Off Toggle switch
* 220 ohms resistors
* Mini-size wireless USB keyboard to enter commands in Raspberry Pi and 
control the Robot Car
* HDMI LCD display to show the Raspberry Pi desktop for easy calibration. 
We could use VNC to remote display the Raspberry Pi desktop also

![Robot Car - component 1](images/Robot_Car_component1.JPG)
![Robot Car - component 1](images/Robot_Car_component2.JPG)
![Robot Car - component 1](images/Robot_Car_component3.JPG)

**Wiring the Robot Car**
![Robot Car - wiring 1](images/Robot_Car_wiring1.JPG)
![Robot Car - wiring 2](images/Robot_Car_wiring2.JPG)




#### Prerequisites

What things you need to install the software and how to install them

```
Give examples
```

#### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc


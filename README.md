# IORO2021 FutureEngineers
<h3>Team SHP-1</h3>

<p>Innopolis Open Robotics Olympiad 2021 Future engineers WRO’s Self-driving vehicle challenge.</p>
<p>We created this robot to participate in World Robot Olympiad 2021 Future Engineers WRO’s Self-driving vehicle challenge.
Our robot is a four-wheeled vehicle with differential rotation of the rear wheelset, it also has сamera.</p>

<p>Rulles of World Robot Olympiad 2021 Future Engineers WRO’s Self-driving vehicle challenge can be found here https://wro-association.org/fileadmin/files/challenges/2021-power-bots-energy/WRO-2021-Future-Engineers-01-Game-Rules.pdf</p>

<h3>Video with our robot</h3>
<p>https://www.youtube.com/watch?v=qzl_4r_2yAc&feature=youtu.be</p>

<h3>Photos of the robot from different sides</h3>
<ul><li>Front view</li>
	
![Image of robot1](https://github.com/Glaurung2000/images/blob/master/photo_2021-09-23_17-11-24.jpg)

<li>Left view</li>
	
![Image of robot2](https://github.com/Glaurung2000/images/blob/master/photo_2021-09-23_17-12-11.jpg)
	
<li>Back view</li>

![Image of robot3](https://github.com/Glaurung2000/images/blob/master/photo_2021-09-23_17-12-03.jpg)

<li>Right view</li>
	
![Image of robot4](https://github.com/Glaurung2000/images/blob/master/photo_2021-09-23_17-11-50.jpg)

<li>Bottom view</li>

![Image of robot5](https://github.com/Glaurung2000/images/blob/master/photo_2021-09-23_17-12-25.jpg)

<li>View from above</li>
	
![Image of robot6](https://github.com/Glaurung2000/images/blob/master/photo_2021-09-23_17-12-19.jpg)

</ul>

<h3>Major Components and Parts</h3>
<p>To create this robot, special electronic components were needed, namely: Micro Metal Gearmotors, Two-channel motor driver DRV8833, servo motor and camera OpenMV Cam H7 Plus. All components are mounted on a plastic frame that has been 3D printed. All photos of the robot, a schematic diagram of electromechanical components and all other materials you can see in our repository.</p>

<h3>OpenMV Cam H7 Plus</h3>

![Image of OpenMV Cam](https://github.com/Glaurung2000/images/blob/master/pinout-openmv-cam-h7-plus-ov5640.png)

<p>The OpenMV Cam is a small, low power, microcontroller board which allows you to easily implement applications using machine vision in the real-world. You program the OpenMV Cam in high level Python scripts (courtesy of the MicroPython Operating System). This makes it easier to deal with the complex outputs of machine vision algorithms and working with high level data structures.</br>
OpenMV Cam allows us to detect field walls and traffic signs using the find_blobs(<...>) function. It finds all blobs (connected pixel regions that pass a threshold test) in the image that is satisfying the given parameters and returns a list of objects which describe each blob. After receiving information about the blobs we get the black area on the right and left sides of the screen, their difference is the deviation from the trajectory of the robot. Then we convert this to the value for the servo motor for turning the angle needed to return to the right trajectory, for this we use function map(<...>), the function proportionally transfers the value(x) from the current range of values (in_min, in_max) to the new range (out_min, out_max) specified by the parameters. Also if function find_blobs(<...>) gives us information about green or red blobs then instead of difference between left and right black area we use size and coordinates of the to get value for the servo motor that will help robot get around the red and green traffic signs. In addition, the find_blobs(<...>) function helps us detect and count the yellow and blue lines, which allows the robot to move around a fixed number of circles.</p>

<p>About OpenMV Cam https://docs.openmv.io/openmvcam/quickref.html</br>
More about the function find_blobs(<...>) here https://docs.openmv.io/library/omv.image.html?highlight=find_blobs#image.image.Image.image.find_blobs</br>
Read more about how to control a servo using OpenMV here https://docs.openmv.io/library/pyb.Servo.html?highlight=pwm</p>

<h3>Two-channel motor driver DRV8833</h3>

![Image of Motor drive](https://github.com/Glaurung2000/images/blob/master/DRV8833.jpg)

<p>The DRV8833 driver allows you to drive a brushed motor or a single stepper motor.</br>
We use it to control the speed and direction of rotation of the motor, for this we send two signals from the camera to the motor driver, one of the values is 0 or 1 (the direction of rotation of the motor depends on this), and the second value is from 0 to 100 (where 0 is the maximum speed, and 100 is the stop), we use pulse width modulation to pass the second value, for this we use the Timer from the pyb module.</p> 

<p>Aabout pyb https://docs.openmv.io/library/pyb.Timer.html?highlight=pwm</br>
About DRV8833 https://iarduino.ru/shop/Expansion-payments/drayver-motorov-dvuhkanalnyy-drv8833.html</br>
DRV8833 Dual H-Bridge Motor Driver datasheet https://www.ti.com/lit/ds/symlink/drv8833.pdf</p>


<h3>Micro Metal Gearmotors</h3>

![Image of Motor drive](https://github.com/Glaurung2000/images/blob/master/motor.jpg)

<p>You can read more about it here https://www.pololu.com/category/60/micro-metal-gearmotors </br>
 Micro Metal Gearmotor datasheet https://www.pololu.com/file/0J1487/pololu-micro-metal-gearmotors_rev-5-0.pdf</p>


<h3>Assembly of the robot</h3>
<p> Print out the parts on a 3D printer or otherwise make them from a file https://drive.google.com/file/d/18QiRaBWn18fe4b0wueTM7BMKxZXjLAZl/view?usp=drivesdk </br>
Assemble the parts according to the model in the file on the screws. Attach and connect the electronics (camera, motor driver, motor, servo and battery).</p>

<h3>Scheme of robot</h3>

![Image of robot](https://github.com/Glaurung2000/images/blob/master/Main-1.png)


<h3>Scheme of electronic components</h3>

![Image of scheme](https://github.com/Glaurung2000/IORO2021_FutureEngineers/blob/main/photo/scheme.png)

<h3>Install Software</h3>
<ul><li><h4>Install Software on PC</h4></li>
<p>Download OpenMV IDE https://openmv.io/pages/download</p>
<li><h4>Install Software on OpenMV Cam</h4></li>
<p>Download main.py, start OpenMV IDE, connect your OpenMV Cam to PC by USB cabel, press Ctrl+E to set connection. Then open the script, click Tools -> 
Save open script to OpenMV Cam, wait until script is uploaded. Now you can disconnect the robot, turn it on and press the start button to start the script.</p></ul>

<h3>Video from robot</h3>

![gif](https://github.com/Glaurung2000/IORO2021_FutureEngineers/blob/main/video_from_robot.gif)

<h3>People who worked on this project</h3>
	<ul><li>Orlik Konstantin</li>
	<li>Korobkina Arina</li></ul>

![Image 1](https://github.com/Glaurung2000/images/blob/master/photo_2021-09-24_12-39-30.jpg)

![Image 2](https://github.com/Glaurung2000/images/blob/master/photo_2021-09-24_12-39-10.jpg)


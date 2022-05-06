------LAUNCH PACKAGE IN GAZEBO-----
-----Follow the commands after the -> ----------
Terminal 1:
-> mkdir catkin_ws/src
 This will create the workspace. Now copy the package catkin_ws/src folder.
->cd ~/catkin_ws
->catkin_make
 This will build all your directories.
->source devel/setup.bash
->roslaunch my_car gazebo.launch
 This will spawn my robot in gazebo in the competition arena world.

Terminal 2:

->cd ~/catkin_ws
->source devel/setup.bash
->rosrun rviz rviz
This will open Rviz. Then open the configuration file rviz.rviz, this will demonstrate the LIDAR data.

Terminal 3:
->cd ~/catkin_ws
->source devel/setup.bash
->rosrun my_car teleop.py
This will run the teleop script, follow the commands on the terminal to navigate the robot.

-----Now kill all terminals-----

Terminal 1: 
->source devel/setup.bash
->roslaunch my_car gazebo.launch

Terminal 2:
->rosrun my_car pub.py
This will start the publisher script.

Terminal 3:
->rosrun my_car sub.py
This will start the subscriber script.
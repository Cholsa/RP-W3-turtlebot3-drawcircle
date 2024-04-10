# Assignment 3 

The first step in running turtlebot3: you need to get everthing installed and configured by go to the [Quick_Start_Guide](https://emanual.robotis.com/docs/en/platform/turtlebot3/quick-start/) section to get ready. follow this [link](https://emanual.robotis.com/docs/en/platform/turtlebot3/simulation/#gazebo-simulation) to run the simulation. 


This repo contain a package called "botcontroller" that have scripts to control the bot. 

Run this repo by: 


```
export TURTLEBOT3_MODEL=burger
roslaunch turtlebot3_gazebo turtlebot3_empty_world.launch 

```

```
export TURTLEBOT3_MODEL=burger
rosrun botcontroller drawcircle.py
```
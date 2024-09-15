# ROS2 Mediapipe Tracker
A node that publishes the location of a detected face in the frame of your webcam.

The node publishes a `geometry_msgs.msg.Point` message in the format:

`point.x`: A number between 0.0 and 1.0. Midpoint of the tracked face on the X axis, as a percentage of the frame size.

`point.y`: A number between 0.0 and 1.0. Midpoint of the tracked face on the Y axis, as a percentage of the frame size.

`point.z`: A number between 0.0 and 1.0. The width of the tracked face as a percentage of the frame size.

## Requirements
- `pip3 install mediapipe`

## Usage
Make sure you have a webcam attached to the computer.

Start the publisher node:
```
ros2 run mediapipe_face_tracker mediapipe_face_tracker
```

Start the example subscriber node:
```
ros2 run mediapipe_face_tracker example_subscriber
```

The example subscriber node will print the detected face location to the console.

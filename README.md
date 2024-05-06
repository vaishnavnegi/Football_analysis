# Football Video Analysis

## Introduction

The objective of this project is to utilize YOLO, a top-tier AI object detection model, to identify and monitor players, referees, and footballs in a video. Enhancing the model's performance through training is also part of the agenda. Additionally, we aim to utilize Kmeans for pixel segmentation and clustering to categorize players into teams based on their t-shirt colors. This categorization allows us to compute a team's ball possession percentage during a match. Optical flow will be employed to gauge the movement of the camera between frames, facilitating precise measurement of player motion. Moreover, perspective transformation will be implemented to convey depth and perspective within the scene, enabling measurements of player movement in meters rather than pixels. Ultimately, calculations will be made to determine player speed and the distance traveled. This comprehensive project encompasses a range of concepts and tackles real-world challenges, rendering it suitable for both novice and seasoned machine learning practitioners.

![Screenshot](output_videos/Screenshot.png)

## Components
- YOLO: AI object detection model
- Kmeans: Pixel segmentation and clustering to detect t-shirt color
- Optical Flow: Measure camera movement
- Perspective Transformation: Represent scene depth and perspective
- Speed and distance calculation per player

## Requirements
- Python 3.x
- ultralytics
- supervision
- OpenCV
- NumPy
- Matplotlib
- Pandas
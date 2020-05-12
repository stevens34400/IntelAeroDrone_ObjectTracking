# Flight Control System for Autonomous Drone
This project utilizes Intel's Ready To Fly (RTF) Drone kit to track a moving object autonomously. The drone marks red objects in its camera view using an image processing algorithm and maneuvers with the navigation control algorithm. Further information regarding design of algorithms and hardware can be found below. 

## Top Level Software Flowchart
<p align="center">
  <img width="600" height="500" src="https://github.com/stevens34400/IntelAeroDrone_ObjectTracking/blob/master/images/toplevel_flowchart.png">
</p>

## Image Processing flowchart
<p align="center">
  <img width="800" height="500" src="https://github.com/stevens34400/IntelAeroDrone_ObjectTracking/blob/master/images/imageprocessing_flowchart.png">
</p>

## Sample Frame of Outputs using Image Processing algorithm:

### Original Frame
<p align="center">
  <img width="800" height="500" src="https://github.com/stevens34400/IntelAeroDrone_ObjectTracking/blob/master/images/regular%20frame.png">
</p>
Sample frame with no adjustments.

### Median Blur
<p align="center">
  <img width="800" height="500" src="https://github.com/stevens34400/IntelAeroDrone_ObjectTracking/blob/master/images/Median%20Blur.png">
</p>
Median blur applied on sample frame.

### Masking, Eroding and Dilating
<p align="center">
  <img width="800" height="500" src="https://github.com/stevens34400/IntelAeroDrone_ObjectTracking/blob/master/images/Mask_Erosion_Dilation.png">
</p>
Masking of frame portraying white object as target object program should contour around.

### Contour and Centroid placement
<p align="center">
  <img width="800" height="500" src="https://github.com/stevens34400/IntelAeroDrone_ObjectTracking/blob/master/images/Contour_Centroid.png">
</p>
Contour of masked frame and centroid placement based of contour lines generated. Will obtain and utilize x-y position of centroid for navigation control. 

## Navigation Control flowchart
<p align="center">
  <img width="800" height="500" src="https://github.com/stevens34400/IntelAeroDrone_ObjectTracking/blob/master/images/navigation_flowchart.png">
</p>

## Hardware

### Intel RTF Drone
<p align="center">
  <img width="800" height="500" src="https://github.com/stevens34400/IntelAeroDrone_ObjectTracking/blob/master/images/IntelRTFDrone.jpg">
</p>

The **Intel Ready to Fly Drone** notably includes:

- Intel Aero Compute Board 
- Intel RealSense Camera R200
- Intel Aero Flight Controller
- Assembled Quadcopter

Further specifications and hardware can be found in the link below.

### Intel Aero Compute Board
<p align="center">
  <img width="800" height="500" src="https://github.com/stevens34400/IntelAeroDrone_ObjectTracking/blob/master/images/ComputeBoard.jpg">
</p>

**Intel Aero Compute Board** notably includes:

 - Intel Atom x7-Z8750 processor
 - 4 GB LPDDR3-1600
 - VGA camera, global shutter, monochrome (down-facing)
 - 8 MP RGB camera (front-facing)
 - Open-source, embedded Linux*, Yocto Project*
 
 Further specifications and hardware can be found in the link below.
 
 [Overview of Intel RTF Drone kit](https://www.intel.com/content/www/us/en/support/articles/000023271/drones/development-drones.html)

# No-Trespassing
An OpenCV Computer Vision Python project which detects tresspassing faces from a live camera feed and alerts security via email.

## Demo Video
https://user-images.githubusercontent.com/121593919/214203956-233a263b-dd76-4c42-a371-16d06a05a172.mov

## Requirements
This program was created using OpenCV 4.7.0, and programmed in Python 3.10. In order to use this program with full functionality, one must have access to a gmail account with App Passwords enabled through google account settings. It is also nessasary to have a working video input to draw faces from. Make sure you have all imported libraries installed and up to date.

## Instructions for Use
Simply fill the email_sender, email password, and email_reciever variables accordingly as per the comments within the "No Trespassing.py" file. Now simply position the camera in a region where you don't want people tresspassing, and when someone is detected to be trespassing, you will get an email alert as well as a picture of the tresspasser attatched. Please note this is not a prototype version, and needs to be reset after each detection. It also does not offer multiple face detection capabilities, so will only capture the first trespasser if there are multiple entering a frame.

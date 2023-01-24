# No-Trespassing
An OpenCV Computer Vision Python project which detects tresspassing faces from a live camera feed and alerts security via email.

## Demo Video
The video below shows the program in action, as it captures me "trespassing" into my friends room and sends an alert, which includes my photo and a clear view of my face. I then show my screen, demonstrating that an alert was sent to the "securities" gmail account!

https://user-images.githubusercontent.com/121593919/214207121-7d9a12fa-0226-4b9f-a7f0-406c19dc2006.mp4


## Requirements
This program was created using OpenCV 4.7.0, and programmed in Python 3.10. In order to use this program with full functionality, one must have access to a gmail account with App Passwords enabled through google account settings. It is also nessasary to have a working video input to draw faces from. Make sure you have all imported libraries installed and up to date.

## Instructions for Use
Simply fill the email_sender, email password, and email_reciever variables accordingly as per the comments within the "No Trespassing.py" file. Now simply position the camera in a region where you don't want people tresspassing, and when someone is detected to be trespassing, you will get an email alert as well as a picture of the tresspasser attatched. Please note this is not a prototype version, and needs to be reset after each detection. It also does not offer multiple face detection capabilities, so will only capture the first trespasser if there are multiple entering a frame.

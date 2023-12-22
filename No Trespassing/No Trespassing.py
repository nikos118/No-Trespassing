import cv2
import pathlib
from email.message import EmailMessage 
import ssl
import smtplib


email_sender = "Your Apps Username" #Your Gmail Apps username
email_password = "your Apps Password" #Your Gmail Apps password
email_reciever = "Alert recievers gmail" #Change to who you want to send the alert email to

subject ="Tresspasser photo captured - do you know them?"

body = """
Please review the photo attached. This tresspasser has been spotted on camera 1.

"""
email = EmailMessage()
email['From'] = email_sender
email['To'] = email_reciever
email['Subject'] = subject
email.set_content(body)

cascade_path = pathlib.Path(cv2.__file__).parent.absolute() / "data/haarcascade_frontalface_default.xml"

clf = cv2.CascadeClassifier(str(cascade_path))

videoFeed = cv2.VideoCapture(0)



while True:
    arbitrary, frame = videoFeed.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = clf.detectMultiScale(gray, scaleFactor = 1.2, minNeighbors = 5, minSize=(15,15),flags=cv2.CASCADE_SCALE_IMAGE)

    for(x,y,width,height) in faces:
        cv2.rectangle(frame,(x,y),(x+width,y+height),(255,0,0),2)
        cv2.imwrite("Faces\intruder.jpg",frame)
        videoFeed.release()
        cv2.destroyAllWindows

        with open("Faces\intruder.jpg","rb") as at:
            data = at.read()
            data_name = at.name
            email.add_attachment(data,maintype = "application", subtype="jpg",filename =data_name)


        with smtplib.SMTP_SSL('smtp.gmail.com',465,context = ssl.create_default_context()) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender,email_reciever, email.as_string())

            exit()

    cv2.imshow("Live Feed",frame)

    if cv2.waitKey(1) == ord(" "):   #Press space to exit the program
        break

videoFeed.release()
cv2.destroyAllWindows


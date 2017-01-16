#Write a program that ecourages a person to take a break every two hours
#by playing their favorite song on youtube. 

import time
import webbrowser

print("This program started on" + time.ctime())
for i in range(3):
    #tell program to pause for two hours
    time.sleep(2*60*60)
    webbrowser.open("https://youtu.be/0TxwYipMFxk")
    print("Take a break")

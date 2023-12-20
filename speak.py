#!/usr/bin/python3

from time import sleep
from os import system

#function to use as a module:
def speak(text_to_speak, gender): #change linux to windows if you want
    cmd = "echo '{}' | ./linux/piper --model linux/hu_HU-{}-medium.onnx --output_file test.wav".format(text_to_speak, gender)
    system(cmd)
    system("cvlc test.wav --play-and-exit --qt-start-minimized")



#when ran as a script
if (__name__ == "__main__"):
    #this is the first time I am using name==main, finally an actual use-case
    gender = input("Férfi vagy nő beszéljen? ")
    férfi = ["férfi", "ffi", "FÉRFI", "fiú", "srác", "Férfi", "csávó", "Csávó", "Fiú", "Srác"]
    #nő = ["Lány", "lány", "nő", "Nő", "Menyecske", "menyecske", "csaj", "Csaj", "CSAJ"]
    if (gender in férfi):
        gender = "imre"
    else:
        gender = "berta"


    while True:
        text_to_speak = input("say: ")
        if (text_to_speak == "exit"):
            break
        speak(text_to_speak, gender)
       


#start.sh is simpel shell script to run the program

#Reviewed 2/3/20 AA

#Authors:
#(Group 1)
#Alex Archer
#Naser Alkhateri
#Ryan Gurnick
#Cory Ingram
#Sean Wilson

#!/bin/bash
sips -z 200 200 ./images/*.png
python3 main.py

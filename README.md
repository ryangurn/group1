<!-- Group 1 Authors: Alex Archer, Naser Alkhateri, Ryan Gurnick, Cory Ingram, Sean Wilson. 2/2/20. This is the readme for github -->
# Official README
Cold call assist is a python program designed to show a selection of students to be "on deck" for cold calling in a classroom setting. 

Authors:
(Group 1)
Alex Archer
Naser Alkhateri
Ryan Gurnick
Cory Ingram
Sean Wilson

2/2/20 - Reviewed AA

Created for CS422, Project 1 at the University of Oregon. Winter '20

What needs to be done to compile the source code and run the program:

1. Double click on 'start.sh' 
  1.1- If there are xcode or permission issues on your operating system click instead on 'main.py'
2. When running the program we recommend you use a testfile in /testfiles/ like csvtest.csv to import as to simulate an effective Roster file.

Software Dependencies:
Python 3.7
Mac OSX 14.1
Unsupported but runs in Windows10 as well.

Directory Heiarchy:

/ColdCallAssist/ - The main directory of the Cold Call Assist. program. Contains the below subdirectories and files.

/images/ - This directory contains the images including default placeholder images and prepared student images for demonstrative purposes. 
Student IDs are the identifier used in this file. One would add the .png of a student with in the form "studentid.png" here to be displayed within the program.

/testfiles/ - This directory contains a roster in several different formats for testing purposes. We suggest you use csvtest.csv as an example Roster to
import when running the program.

readme.txt - This file. 

main.py - A python file that contains the Display Manager component of the program. Runs the tkinterface elements necessary to display on deck students.

Roster.py - A python file that contains the Student object and Roster object data structures.

StudentQueue.py - A python file that contains the Queue data structure that holds Student objects. Ensures students are appropriately randomized
when being put on deck and returned to the Queue.

config.py - A configuration parser that reads app.ini and applies user settings.

app.ini - A settings file that contains many user changeable settings. Works in conjunction with config.py

start.sh - A start up script for the program. Double click to use. 

Files generated during Use:

Data.* - A necessary copy of the roster to ensure data is being saved appropriately each time a student is removed from que with respect
to power off and unexpected exits.

dailylog.* - a summary of activity within the program


# Cold Call Assist 

This is a python program designed to assist in the fair and randomized selection of students for cold calling in a classroom. 
A graphical manager will display four students and associated data on screen. Key stroke interactions will cycle between or remove students from being on deck. Students can be flagged for review later. A daily and term roster can be generated. Many user settings are configurable. 


# [WIKI](https://github.com/ryangurn/group1/wiki)
Please observe our wiki for more information
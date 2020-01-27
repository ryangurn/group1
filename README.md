Group 1 - Cold Calling Assistant 
(basic structure for now...)
# Roster.py
Data structure for Student and Roster Class objects. A roster is a group of students. 
* Interacts with
  * csvtest.txt
  * tsvtest.txt ((may be formatted incorrectly))
# StudentQueue.py
A module that uses the objects created by the Roster and generate a queue for the Cold Calling Assistant.
Takes in the students and randomize their order before adding them into the queue.
Retrieves the students ondeck and replaces ondeck students when needed with the next in queue.
# main.py 
 Placeholder name for a program to putting student objects into a queue and retrieving. 
* Interacts with
  * queue.csv 
  * students.csv 
# guiprototype.py
Framework GUI that displays 4 names (with space for pictures, other text features) and rotates highlighting based on key commands.

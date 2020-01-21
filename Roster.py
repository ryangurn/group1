# Basic roster and student data structures
# Author Cory Ingram. Reviewed by Alex Archer ##**comments**

##Imports
import csv

## **Can this automatically detect which format is being uploaded during the read?** 
# Change between ',' and '\t' for csv or tsv
delim = '\t'

## **PEP8 standards, capital Class, rest lowercase**
class Student:
    """Class docstring. 
	Purpose and Behavior: Class used to represent a student. 
	Class Attriubes: 
		first : str    first name
                last : str     last name
                id : str       student ID
                email : str    student email
                phonetic : str phonetic of name
                reveal : bool  ?? 

	Public Methods:
        getters and setters needed? 
      """

	def __init__(self, first, last, ID, email, phonetic, reveal):
	    """ Parameters: See Student class for descriptions """

		self.first = first
		self.last = last
		self.ID = ID
		self.email = email
		self.phonetic = phonetic
		self.reveal = reveal
        
	## **Need __str__ or __repr__**
		
		
#list of Student objects
list = []  ##** should this be it's own class, "Roster" ?** 


#get roster file  ##**this should be a function of Roster class. "read_roster()" or something**
filename = raw_input("Enter roster file:")

#fill list with students from roster file  ##** This should be a function of Roster class, "populate()" or something.
with open(filename) as csv_file:
	csv_reader = csv.reader(csv_file, delimiter= delim)
	for row in csv_reader:  ##each row is a student's information
		list.append(Student(row[0], row[1], row[2], row[3], row[4], row[5]))

#display contents of list  ##**Should be the str or repr of the Roster class**
for obj in list:
	print(obj.first, obj.last, obj.ID, obj.email, obj.phonetic, obj.reveal)

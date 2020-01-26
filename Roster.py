# Basic roster and student data structures
# Author Cory Ingram. Reviewed by Alex Archer ##**comments**

##Imports
import csv
import os.path

## **Can this automatically detect which format is being uploaded during the read?** 
# Change between ',' and '\t' for csv or tsv
delim = '\t'

## **PEP8 standards, capital Class, rest lowercase**
class Student:
	"""
	Student Class
	functions:
	__init__ -- initialize the student class
	__repr__ -- representation of the student class
	"""

	def __init__(self, first, last, ID, email, phonetic, reveal):
		"""
		Initialize the student class and data structure
		Args:
		first -- first name of the student (first:string)
		last -- last name of the student (last:string)
		ID -- UO ID for the student (ID:int<9>)
		email -- email for the student (email:string)
		phonetic -- phonetic spelling for the students name (phonetic:string)
		reveal -- reveal the students phonetic spelling (reveal:bool)
		"""
		self.first = first
		self.last = last
		self.ID = ID
		self.email = email
		self.phonetic = phonetic
		self.reveal = reveal
		
	def __repr__(self):
		"""
		Defines the representation for the student when converted to string
		"""
		return 'student named {self.first} {self.last} ID {self.ID}'.format(self=self)
		
#list of Student objects
class Roster:
	def __init__(self):
		self.students = []
		
	def import_roster(self, filename):
		self.students.clear()
		if os.path.exists(filename):
			with open(filename) as csv_file:
				csv_reader = csv.reader(csv_file, delimiter= delim)
				for row in csv_reader: ##each row is a student's information
					self.students.append(Student(row[0], row[1], row[2], row[3], row[4], row[5]))
				csv_file.close()
		else:
			print('File does not exist!')
			
	def export_roster(self):
		expfile = open('export_roster.csv', 'w')
		for student in self.students:
			expfile.write('{student.first}{c}{student.last}{c}{student.ID}{c}{student.email}{c}{student.phonetic}{c}{student.reveal}\n'.format(student=student, c=delim))
		expfile.close()	

	def __str__(self):
		return '{self.students}'.format(self=self)


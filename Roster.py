# Basic roster and student data structures
# Author Cory Ingram. Reviewed by Alex Archer 
# Docstrings added by Ryan Gurnick

# Imports from std lib
import csv
import os.path

## TODO: **Can this automatically detect which format is being uploaded during the read?** 
# Change between ',' and '\t' for csv or tsv
delim = ','

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
		

class Roster:
	"""
	Student Class
	functions:
	__init__ -- initialize the student class
	__str__ -- representation of the student class
	import_roster -- allows importing of CSV/TSV based on delim
	export_roster -- allowed exporting of roster to CSV/TSV based on delim
	"""

	def __init__(self):
		"""
		Initialize the Roster class and data structure
		Args:
		None
		"""
		self.students = [] # list of student objects
		
	def import_roster(self, filename):
		"""
		Allows the roster to be imported from CSV/TSV
		args:
		filename -- the location at which the file to be imported is stored
		globals used:
		delim -- this will determine what deliminator is used and thus if its using TSV or CSV
		None
		"""
        
        #csv files ends with .csv tsv files ends with .tsv
        #temp delim switch
		if filename[-3] == 'c':
			delim = ','
        
		self.students.clear() # empties the student list on import
		if os.path.exists(filename): # checks if the specified file exists
            
			with open(filename) as csv_file: # opens the file
				csv_reader = csv.reader(csv_file, delimiter=delim) # reads the csv data
				next(csv_reader) #skips first line
				for row in csv_reader: # loops through each row
					self.students.append(Student(row[0], row[1], row[2], row[3], row[4], row[5])) # appends the data into the list
				csv_file.close() # closes the file
		else: # if the file does not exist
			print('File does not exist!') # print warning
			
	def export_roster(self, filename):
		"""
		Allows the roster to be exported to TSV/CSV
		args:
		None
		globals used:
		delim -- this will determine what deliminator is used and thus if its using TSV or CSV
		"""
		expfile = open(filename, 'w') # open the file stream
		for student in self.students: # loop through the students stored in the roster
			# output the file information with the correct delim and student
			expfile.write('{student.first}{c}{student.last}{c}{student.ID}{c}{student.email}{c}{student.phonetic}{c}{student.reveal}\n'.format(student=student, c=delim))
		expfile.close()	# close the file stream

	def __str__(self):
		"""
		Defines the representation for the student when converted to string
		args:
		None
		"""
		return '{self.students}'.format(self=self)


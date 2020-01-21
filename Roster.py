# Basic roster data structure
# Author Cory Ingram

# Change between ',' and '\t' for csv or tsv
delim = '\t'

class student:
	def __init__(self, first, last, ID, email, phonetic, reveal):
		self.first = first
		self.last = last
		self.ID = ID
		self.email = email
		self.phonetic = phonetic
		self.reveal = reveal

#list of student objects
list = []

import csv

#get roster file
filename = raw_input("Enter roster file:")

#fill list with students from roster file
with open(filename) as csv_file:
	csv_reader = csv.reader(csv_file, delimiter= delim)
	for row in csv_reader:
		list.append(student(row[0], row[1], row[2], row[3], row[4], row[5]))

#display contents of list
for obj in list:
	print(obj.first, obj.last, obj.ID, obj.email, obj.phonetic, obj.reveal)
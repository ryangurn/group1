# queue data structure for the Logic
# Naser Alkhateri

#StudentQueue.py

import queue
import Roster
import random
import os
import csv
import copy


#check wich file to start
#returns a queue for the deck

def students_list(filename, startbool):
    """
        Chooses the appropriate file to import
        Returns a list of objects from the imported file
        Args:
        startbool: whether the file exists True/False
        filename: a string of the filename
    """
    student_roster = Roster.Roster()

    #checks if there is an updated queue
    if startbool:
        student_roster.import_roster(filename)
    
    else:
        student_roster.import_roster(filename)
            #send list to randomize
        student_roster.students = randomizer(student_roster.students)
    return student_roster.students

#create_queue
def create_queue(list):
    """
        Takes in a list of object and places it in a queue
        then returns queue
        Args:
        list -- a list of student objects
    """
    #takes in a list and returns a queue
    studentQ = queue.Queue()
    
    for i in range(len(list)):
        studentQ.put(list[i])
    return studentQ

#randomizer for new queue
#takes a list of objects randomizes first half
def randomizer(studentList):
    """
        Takes the list of objects and shuffles the first half
        Args:
        studentList -- list of Student objects
        tempList -- a list that takes half of studentList
        first_half -- integer of the half of the list's size
    """
    first_half = len(studentList) // 2
    tempList = []
    for i in range(first_half):
        tempList.append(studentList[i])
    
    random.shuffle(tempList)
    for i in range(first_half):
        studentList[i] = tempList[i]

    return studentList


#save during
#export queue after each interaction
#useful if user interupts the deck

def export_queue_during(studentQ,deck):
    """
        updates the queue's csv/tsv file while on deck is updated
        Args:
        studentQ -- a queue of students
        deck -- list of 4 student objects
        tempQ -- a copy of studentQ
        size -- Queue's size
        
    """
    
    #places on deck at the start of the queue.csv
    #to keep same students on deck for next use
    tempQ = queue.Queue()
    tempQ.queue = copy.deepcopy(studentQ.queue)
    size = tempQ.qsize()
    with open('queue.csv', 'w') as csvfile:
        filewriter = csv.writer(csvfile, lineterminator='\n')
        filewriter.writerow(['First', 'Last','UO ID','Email','Phonetic','Reveal'])
        for d in range(4):
            filewriter.writerow([deck[d].first, deck[d].last,deck[d].ID,deck[d].email,deck[d].phonetic,deck[d].reveal])
        for i in range(size-4):
            out = tempQ.get()
            filewriter.writerow([out.first, out.last,out.ID,out.email,out.phonetic,out.reveal])

    csvfile.close()
#save after
def export_queue_after(studentQ,deck):
    """
        updates the queue's csv/tsv file before a successful exit
        Args:
        studentQ -- a queue of students
        deck -- list of 4 student objects
        tempQ -- a copy of studentQ
        size -- Queue's size
        
    """
    #returns on deck students to queue
    deck_to_queue(studentQ,deck)
    size = studentQ.qsize()
    with open('queue.csv', 'w') as csvfile:
        filewriter = csv.writer(csvfile, lineterminator='\n')
        filewriter.writerow(['First', 'Last','UO ID','Email','Phonetic','Reveal'])
        for i in range(size):
            out = studentQ.get()
            filewriter.writerow([out.first, out.last,out.ID,out.email,out.phonetic,out.reveal])
    csvfile.close()

def remove_student(s_num,deck,studentQ):
    
    """
        Removes a Student object from deck and replaces it
        with the next object in queue
        Args:
        s_num -- a number of the object's location
        deck -- list of 4 student objects
        studentQ -- a queue of students
        
    """
    
    
    #takes the number selected from the deck
    #takes the next student in queue and replace it with the selected
    #the student that was removed is placed at the end of the queue
    
    #TO DO ----- add flags
    
    #decrement for list's index
    s_num -= 1
    #place the student at the end of the queue
    studentQ.put(deck[s_num])
    deck[s_num] = studentQ.get()
    #studentQ.put(deck[s_num])
    
    return deck

def deck_to_queue(studentQ,deck):
    """
        takes the the deck and return it to the queue
        Args:
        deck -- list of 4 student objects
        studentQ -- a queue of students
        
    """
    #used to return the on deck students to queue
    for i in deck:
        studentQ.put(i)

def on_deck(studentQ):
    """
        returns a list of the first 4 objects in queue
        Args:
        studentQ -- a queue of students
        deck -- list of 4 objects
    """
    deck = []

    #students are removed from queue
    #and placed on deck
    for i in range(4):
        deck.append(studentQ.get())


    return deck

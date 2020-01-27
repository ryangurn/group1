#queue.py

import queue
import Roster
import random
import os
import csv
import copy
#os.path.isfile('./queue.csv')

#check wich file to start
#returns a queue for the deck

def students_list():
    student_roster = Roster.Roster()
    isQueue = os.path.isfile('./queue.csv')

    #checks if there is an updated queue
    if isQueue:
        student_roster.import_roster('queue.csv')
    
    else:
        student_roster.import_roster('csvtest.csv')
            #send list to randomize
        student_roster.students = randomizer(student_roster.students)
    return student_roster.students

#create_queue
def create_queue(list):
    #takes in a list and returns a queue
    studentQ = queue.Queue()
    
    for i in range(len(list)):
        studentQ.put(list[i])
    return studentQ

#randomizer for new queue
#takes a list of objects randomizes first half
def randomizer(studentList):
    
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
    #places on deck at the start of the queue.csv
    #to keep same students on deck for next use
    tempQ = queue.Queue()
    tempQ.queue = copy.deepcopy(studentQ.queue)
    size = tempQ.qsize()
    with open('queue.csv', 'w') as csvfile:
        filewriter = csv.writer(csvfile)
        #filewriter.writerow(['First', 'Last','UO ID','Email','Phonetic','Reveal'])
        for d in range(4):
            filewriter.writerow([deck[d].first, deck[d].last,deck[d].ID,deck[d].email,deck[d].phonetic,deck[d].reveal])
        for i in range(size-4):
            out = tempQ.get()
            filewriter.writerow([out.first, out.last,out.ID,out.email,out.phonetic,out.reveal])

#save after
def export_queue_after(studentQ):
    size = studentQ.qsize()
    with open('queue.csv', 'w') as csvfile:
        filewriter = csv.writer(csvfile)
        #filewriter.writerow(['First', 'Last','UO ID','Email','Phonetic','Reveal'])
        for i in range(size):
            out = studentQ.get()
            filewriter.writerow([out.first, out.last,out.ID,out.email,out.phonetic,out.reveal])

def remove_student(s_num,deck,studentQ):
    #takes the number selected from the deck
    #takes the next student in queue and replace it with the selected
    #the student that was removed is placed at the end of the queue
    
    #decrement for list's index
    s_num -= 1
    deck[s_num] = studentQ.get()
    studentQ.put(deck[s_num])
    
    return deck

def on_deck(studentQ):
    
    student1 = studentQ.get()
    student2 = studentQ.get()
    student3 = studentQ.get()
    student4 = studentQ.get()
    #places those students end of the queue
    studentQ.put(student1)
    studentQ.put(student2)
    studentQ.put(student3)
    studentQ.put(student4)
    return student1, student2 , student3, student4



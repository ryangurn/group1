# queue data structure for the Logic
# Naser Alkhateri

# StudentQueue.py

import queue
import Roster
import random
import os
import csv
import copy
import config

# global
CONFIG = config.configuration()
QUEUE_PATH = "-.csv"


def students_list(filename, startbool):
    """
        Chooses the appropriate file to import
        Returns a list of objects from the imported file
        Args:
        student_roster: object for Roster
        startbool: to diffrentate wether user is changing file
        isQueue: to see if a queue file associated with the roster given exists
        interruptedQ: to see if a queue that is from a previous run that did not exit properly
        filename: a string of the filename
        GLOBAL:
        QUEUE_PATH
    """
    student_roster = Roster.Roster()
    # queue are saved in _queue.csv while running
    global QUEUE_PATH
    queue_file = filename.split('.')
    student_roster = Roster.Roster()

    QUEUE_PATH = str(queue_file[0] + "_queue.csv")
    isQueue = os.path.exists(QUEUE_PATH)

    # this file will only exist if the program was not closed properly
    # it gets deleted at exit
    interruptedQ = os.path.exists('_queue.csv')
    # checks if there is an updated queue
    if startbool and interruptedQ:
        student_roster.import_roster('_queue.csv')
    elif isQueue:
        student_roster.import_roster(QUEUE_PATH)
        student_roster.students = randomizer(student_roster.students)
    else:
        student_roster.import_roster(filename)
        # send list to randomize
        student_roster.students = randomizer(student_roster.students)

    return student_roster.students

def create_queue(list):
    """
        Takes in a list of object and places it in a queue
        then returns queue
        Args:
        list -- a list of student objects
    """
    # takes in a list and returns a queue
    studentQ = queue.Queue()

    for i in range(len(list)):
        studentQ.put(list[i])
    return studentQ


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


def export_queue_during(studentQ, deck):
    """
        updates the queue's csv/tsv file while on deck is updated
        Args:
        studentQ -- a queue of students
        deck -- list of 4 student objects
        tempQ -- a copy of studentQ
        size -- Queue's size

    """

    # places on deck at the start of the queue.csv
    # to keep same students on deck for next use
    tempQ = queue.Queue()
    tempQ.queue = copy.deepcopy(studentQ.queue)
    size = tempQ.qsize()
    with open('_queue.csv', 'w') as csvfile:
        filewriter = csv.writer(csvfile, lineterminator='\n')
        filewriter.writerow(
            [CONFIG.STUDENT_FIRST, CONFIG.STUDENT_LAST, CONFIG.STUDENT_ID, CONFIG.STUDENT_EMAIL, CONFIG.STUDENT_PHONETIC, CONFIG.STUDENT_REVEAL, CONFIG.STUDENT_FLAGS, CONFIG.STUDENT_CALLS])
        for d in range(4):
            filewriter.writerow(
                [deck[d].first, deck[d].last, deck[d].ID, deck[d].email, deck[d].phonetic, deck[d].reveal,
                 deck[d].noFlag, deck[d].noCalled])
        for i in range(size):
            out = tempQ.get()
            filewriter.writerow(
                [out.first, out.last, out.ID, out.email, out.phonetic, out.reveal, out.noFlag, out.noCalled])

    csvfile.close()


def export_queue_after(studentQ, deck):
    """
        updates the queue's csv/tsv file before a successful exit
        Args:
        studentQ -- a queue of students
        deck -- list of 4 student objects
        tempQ -- a copy of studentQ
        size -- Queue's size

    """
    # returns on deck students to queue
    deck_to_queue(studentQ, deck)
    size = studentQ.qsize()
    with open(QUEUE_PATH, 'w') as csvfile:
        filewriter = csv.writer(csvfile, lineterminator='\n')
        filewriter.writerow([CONFIG.STUDENT_FIRST, CONFIG.STUDENT_LAST, CONFIG.STUDENT_ID, CONFIG.STUDENT_EMAIL, CONFIG.STUDENT_PHONETIC, CONFIG.STUDENT_REVEAL, CONFIG.STUDENT_FLAGS, CONFIG.STUDENT_CALLS])
        for i in range(size):
            out = studentQ.get()
            filewriter.writerow(
                [out.first, out.last, out.ID, out.email, out.phonetic, out.reveal, out.noFlag, out.noCalled])
    csvfile.close()


def remove_student(s_num, deck, studentQ, flag=False):
    """
        Removes a Student object from deck and replaces it
        with the next object in queue
        Args:
        s_num -- a number of the object's location
        deck -- list of 4 student objects
        studentQ -- a queue of students

    """

    # decrement for list's index
    s_num -= 1

    f = "X" if flag else ""
    dailyLog = "{}\t{} {} <{}>\n".format(f, deck[s_num].first, deck[s_num].last, deck[s_num].email)
    if flag:
        deck[s_num].noFlag += 1
    deck[s_num].noCalled += 1

    # write to a file for use later.
    f = open(CONFIG.DAILY_LOG_PATH, "a+")
    f.write(dailyLog)
    f.close()

    # place the student at the end of the queue
    studentQ.put(deck[s_num])
    deck[s_num] = studentQ.get()
    # studentQ.put(deck[s_num])

    return deck


def deck_to_queue(studentQ, deck):
    """
        takes the the deck and return it to the queue
        Args:
        deck -- list of 4 student objects
        studentQ -- a queue of students

    """
    # used to return the on deck students to queue
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

    # students are removed from queue
    # and placed on deck
    for i in range(4):
        deck.append(studentQ.get())

    return deck

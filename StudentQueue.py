# queue data structure for main.py
# Naser Alkhateri

# StudentQueue.py

import queue
from datetime import date

import Roster
import random
import os
import csv
import copy
import config
import shutil

# global
CONFIG = config.configuration()
QUEUE_PATH = "-.csv"


def students_list(filename, startbool):
    """
        This function is called in main.py and uses Roster.py
        to import a list of student objects from a given file.
        
        The purpose of this function is to check to see if the program
        has interacted with the same roster before and to check if there are any
        files made for that roster and imports it. If the program did not close
        properly, a file that contains the last interaction will be loaded to continue 
        where its left off.
        
        Chooses the appropriate file to import
        Returns a list of objects from the imported file
        Args:
        student_roster: object for Roster
        startbool: to diffrentate wether user is changing file
        isQueue: to see if a queue file associated with the roster given exists
        interruptedQ: to see if a queue that is from a previous run that did not exit properly
        filename: a string of the filename
        GLOBAL:
        QUEUE_PATH -- a string containing the path of a file's queue.
    """
    if CONFIG.DEBUG:
        print("Running students_list")

    student_roster = Roster.Roster()
    # queue are saved in _queue.csv while running
    global QUEUE_PATH
    queue_file = filename.split('.')
    student_roster = Roster.Roster()

    QUEUE_PATH = str(queue_file[0] + "_queue.csv")
    if filename != CONFIG.DATA_PATH:
        isQueue = os.path.exists(QUEUE_PATH)
    else:
        isQueue = False
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
        This function is called in main.py to return a queue of objects.
        
        The Cold Call Assistant is using the queue data structure
        which is ideal for the purpose of this application. Having the first
        object in to leave last makes this program efficient in making
        objects leave the queue and returning to the end of the queue.
        
        Takes in a list of objects and places it in a queue
        then returns queue.
        Args:
        studentQ -- a queue of students
        list -- a list of student objects
    """
    if CONFIG.DEBUG:
        print("Creating Queue")

    # takes in a list and returns a queue
    studentQ = queue.Queue()

    for i in range(len(list)):
        studentQ.put(list[i])
    return studentQ


def randomizer(studentList):
    """
        This function is called in the students_list function.
        
        To make the system less predictable and to insure that all
        students have an equal chance to ba called in deck. This function shuffles
        the first half of a list and returns it.
    
    
        Takes the list of objects and shuffles the first half and returns
        the list.
        Args:
        studentList -- list of Student objects
        tempList -- a list that takes half of studentList
        first_half -- integer of the half of the list's size
    """
    if CONFIG.DEBUG:
        print("Randomizing StudentList")

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
        This function is called in main.py to export a file of
        the current stage of the queue after each change.
        
        The purpose of this function is to prevent data loss
        when the application is not closed properly.
        
        
        Updates the queue's csv/tsv file while on deck is updated
        Args:
        studentQ -- a queue of students
        deck -- list of 4 student objects
        tempQ -- a copy of studentQ
        size -- Queue's size

    """

    if CONFIG.DEBUG:
        print("Exporting Queue During")

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
        This function is called in main.py to export a file of
        the current stage of the queue before program recieve an exit code.
    
        The purpose of this function is to save the queue order and flag's information.
        The order of the queue is important to be saved to avoid repetition in calls
        and to provide an equal chance for others to be called.
    
        updates the queue's csv/tsv file before a successful exit
        Args:
        studentQ -- a queue of students
        deck -- list of 4 student objects
        tempQ -- a copy of studentQ
        size -- Queue's size

    """

    if CONFIG.DEBUG:
        print("Exporting Queue After")
    if CONFIG.DECK_LAST:
        if CONFIG.DEBUG:
                print("second half")
        # returns on deck students to queue
        deck_to_queue(studentQ, deck)
    
    size = studentQ.qsize()
    with open(QUEUE_PATH, 'w') as csvfile:
        filewriter = csv.writer(csvfile, lineterminator='\n')
        filewriter.writerow([CONFIG.STUDENT_FIRST, CONFIG.STUDENT_LAST, CONFIG.STUDENT_ID, CONFIG.STUDENT_EMAIL, CONFIG.STUDENT_PHONETIC, CONFIG.STUDENT_REVEAL, CONFIG.STUDENT_FLAGS, CONFIG.STUDENT_CALLS])
 
        if not CONFIG.DECK_LAST:
            if CONFIG.DEBUG:
                print("First half")
            for student_deck in deck:
                filewriter.writerow(
                [student_deck.first, student_deck.last, student_deck.ID, student_deck.email, student_deck.phonetic, student_deck.reveal, student_deck.noFlag, student_deck.noCalled])

        for i in range(size):
            out = studentQ.get()
            filewriter.writerow(
                [out.first, out.last, out.ID, out.email, out.phonetic, out.reveal, out.noFlag, out.noCalled])
    csvfile.close()
    shutil.copyfile(QUEUE_PATH, CONFIG.DATA_PATH)


def remove_student(s_num, deck, studentQ, flag=False):
    """ 
        This function is called in main.py after the user made a 
        selection from deck.
        
        The student that is to be removed from deck is added to the 
        log with an 'X' before their name if flagged, then replaced with the next
        student in queue, and the previous student is placed at the end of the queue.
        
    
        Removes a Student object from deck and replaces it.
        with the next object in queue
        Args:
        s_num -- a number of the object's location
        deck -- list of 4 student objects
        studentQ -- a queue of students
        dailylog -- a string formatted with the object's information.
        f -- a string to distinguish between flagged and non-flagged
    """



    # decrement for list's index
    s_num -= 1

    f = "X" if flag else ""
    today = date.today().isoformat()

    if CONFIG.DEBUG:
        print("Removing a Student({} {}) Flag({})".format(deck[s_num].first, deck[s_num].last, f))

    dailyLog = "{}\t{}\t{} {} <{}>\n".format(today, f, deck[s_num].first, deck[s_num].last, deck[s_num].email)
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
   

    return deck


def deck_to_queue(studentQ, deck):
    """
        This function is called by export_queue_after.
        
        The purpose of this function is to return the on deck objects
        to the queue. 'on deck' students are not part of the queue unless they
        are removed from the deck or the program is exiting and they are to be 
        returned to the queue.
    
    
        Takes the the deck and return it to the queue
        Args:
        deck -- list of 4 student objects
        studentQ -- a queue of students

    """
    if CONFIG.DEBUG:
        print("Deck to Queue")

    # used to return the on deck students to queue
    for i in deck:
        studentQ.put(i)


def on_deck(studentQ):
    """
        This function is called in main.py to populate the deck
        with the first 4 students in the queue.
        
        The program is made to view 4 students at a time on deck.
        This list is generated by this function at the start. The list is then used 
        to easily navigate through and removing a student from a specific index.
    
        returns a list of the first 4 objects in queue
        Args:
        studentQ -- a queue of students
        deck -- list of 4 objects
    """
    if CONFIG.DEBUG:
        print("on Deck")

    deck = []

    # students are removed from queue
    # and placed on deck
    for i in range(4):
        deck.append(studentQ.get())

    return deck

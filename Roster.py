# Basic roster and student data structures
# Author Cory Ingram. Reviewed by Alex Archer 
# Docstrings added by Ryan Gurnick

# Imports from std lib
import csv
import os.path
import config

CONFIG = config.configuration()


class Student:
    """
    Student Class
    functions:
    __init__ -- initialize the student class
    __repr__ -- representation of the student class
    """

    def __init__(self, first, last, ID, email, phonetic, reveal, noFlag=None, noCalled=None):
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

        if noFlag is None:
            nf = 0
        else:
            nf = noFlag

        if noCalled is None:
            nc = 0
        else:
            nc = noCalled

        self.first = first
        self.last = last
        self.ID = ID
        self.email = email
        self.phonetic = phonetic
        self.reveal = reveal
        self.noFlag = nf
        self.noCalled = nc

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
        self.students = []  # list of student objects

    def import_roster(self, filename):
        """
        Allows the roster to be imported from CSV/TSV
        args:
        filename -- the location at which the file to be imported is stored
        globals used:
        delim -- this will determine what deliminator is used and thus if its using TSV or CSV
        None
        """

        # csv files ends with .csv tsv files ends with .tsv
        # temp delim switch

        self.students.clear()  # empties the student list on import
        if os.path.exists(filename):  # checks if the specified file exists
            file_explode = filename.split(".")
            if file_explode[1] == 'csv':
                delim = ','
            elif file_explode[1] == 'tsv':
                delim = "\t"
            elif file_explode[1] == 'txt':
                delim = ','
            with open(filename) as csv_file:  # opens the file
                csv_reader = csv.reader(csv_file, delimiter=delim)  # reads the csv data
                next(csv_reader)  # skips first line
                count = 0
                for row in csv_reader:  # loops through each row
                    try:
                        if len(row) is 8:
                            self.students.append(
                                Student(row[0], row[1], row[2], row[3], row[4], row[5], int(row[6]), int(row[7])))
                        elif len(row) is 6:
                            self.students.append(Student(row[0], row[1], row[2], row[3], row[4],
                                                         row[5]))  # appends the data into the list
                    except IndexError:
                        self.students.append(
                            Student('place', 'holder', 000000000, 'place@holder', 'place holder', 0, 0, 0))
                    count = count + 1
                if count < 4:
                    self.students.append(Student('place', 'holder', 000000000, 'place@holder', 'place holder', 0, 0, 0))
                    self.students.append(Student('place', 'holder', 000000000, 'place@holder', 'place holder', 0, 0, 0))
                    self.students.append(Student('place', 'holder', 000000000, 'place@holder', 'place holder', 0, 0, 0))
                    self.students.append(Student('place', 'holder', 000000000, 'place@holder', 'place holder', 0, 0, 0))
                csv_file.close()  # closes the file
        else:  # if the file does not exist
            print('File does not exist!')  # print warning

    def export_roster(self, filename, dlm):
        """
        Allows the roster to be exported to TSV/CSV
        args:
        None
        globals used:
        delim -- this will determine what deliminator is used and thus if its using TSV or CSV
        """
        expfile = open(filename, 'w')  # open the file stream
        expfile.write(
            '{CONFIG.STUDENT_FIRST}{c}{CONFIG.STUDENT_LAST}{c}ID{c}{CONFIG.STUDENT_EMAIL}{c}{CONFIG.STUDENT_PHONETIC}{c}{CONFIG.STUDENT_REVEAL}{c}{CONFIG.STUDENT_FLAGS}{c}{CONFIG.STUDENT_CALLS}\n'.format(CONFIG=CONFIG, c=dlm))
        for student in self.students:  # loop through the students stored in the roster
            # output the file information with the correct delim and student
            expfile.write(
                '{student.first}{c}{student.last}{c}{student.ID}{c}{student.email}{c}{student.phonetic}{c}{student.reveal}{c}{student.noFlag}{c}{student.noCalled}\n'.format(
                    student=student, c=dlm))
        expfile.close()  # close the file stream

    def export_term_report(self, filename, dlm):
        """
        Allows the roster to be exported to TSV/CSV
        args:
        None
        globals used:
        delim -- this will determine what deliminator is used and thus if its using TSV or CSV
        """
        self.import_roster('_queue.csv')
        expfile = open(filename, 'w')  # open the file stream
        expfile.write(
            '{CONFIG.STUDENT_CALLS}{c}{CONFIG.STUDENT_FLAGS}{c}{CONFIG.STUDENT_FIRST}{c}{CONFIG.STUDENT_LAST}{c}{CONFIG.STUDENT_ID}{c}{CONFIG.STUDENT_EMAIL}{c}{CONFIG.STUDENT_PHONETIC}{c}{CONFIG.STUDENT_REVEAL}\n'.format(
                c=dlm))
        for student in self.students:  # loop through the students stored in the roster
            # output the file information with the correct delim and student
            expfile.write(
                '{student.noCalled}{c}{student.noFlag}{c}{student.first}{c}{student.last}{c}{student.ID}{c}{student.email}{c}{student.phonetic}{c}{student.reveal}\n'.format(
                    student=student, c=dlm))
        expfile.close()  # close the file stream

    def __str__(self):
        """
        Defines the representation for the student when converted to string
        args:
        None
        """
        return '{self.students}'.format(self=self)

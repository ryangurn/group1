"""
Sean Wilson - 1/20/20
GUI Prototype v2.0
Group1 cis422 @ U of O W'20
"""

from tkinter import *
from tkinter import filedialog
import StudentQueue
import os
import os.path
import Roster
import config

CONFIG = config.configuration()
# CONFIG.DATA_PATH = 'data.csv'
# CONFIG.DAILY_LOG_PATH = 'dailylog.log'
# CONFIG.BACKGROUND_COLOR = 'white'
# CONFIG.SELECTOR_COLOR = 'yellow'
# CONFIG.FLAG_COLOR = 'red'
# CONFIG.REMOVE_COLOR = 'green'
# CONFIG.STUDENT_FIRST = 'First Name'
# CONFIG.STUDENT_LAST = 'Last Name'
# CONFIG.STUDENT_ID = 'UO ID'
# CONFIG.STUDENT_EMAIL = 'Email'
# CONFIG.STUDENT_PHONETIC = 'Phonetic'
# CONFIG.STUDENT_REVEAL = 'Revealible?'
# CONFIG.STUDENT_FLAGS = 'Number of Flags'
# CONFIG.STUDENT_CALLS = 'Number of Calls'
# CONFIG.KEYBIND_FLAG = '<Up>'
# CONFIG.KEYBIND_REMOVE = '<Down>'
# CONFIG.KEYBIND_LEFT = '<Left>'
# CONFIG.KEYBIND_RIGHT = '<Right>'
#
# CONFIG.IMPORT_KEYBIND = True
# CONFIG.KEYBIND_IMPORT = '<I>'
#
# CONFIG.EXPORT_CSV_KEYBIND = False
# CONFIG.KEYBIND_EXPORT_CSV = '<Alt-c>'
# CONFIG.EXPORT_TSV_KEYBIND = False
# CONFIG.KEYBIND_TSV_EXPORT = '<Alt-t>'


CWD = os.getcwd()  # current working directory


class coldCallGui:

    def __init__(self):

        if os.path.exists(CONFIG.DATA_PATH):
            self.studentList = StudentQueue.students_list(CONFIG.DATA_PATH, True)
            self.studentQ = StudentQueue.create_queue(self.studentList)

            self.deck = StudentQueue.on_deck(self.studentQ)

            # incase it interrupts before removing anyone from deck
            StudentQueue.export_queue_during(self.studentQ, self.deck)

            self.r = Roster.Roster()
            self.r.import_roster(CONFIG.DATA_PATH)
        else:
            data = open(CONFIG.DATA_PATH, 'w')
            data.write('first,last,ID,email,phonetic,reveal\n')
            data.write('place,holder,000000001,placeholder@placeholder,place holder,0\n')
            data.write('place,holder,000000002,placeholder@placeholder,place holder,0\n')
            data.write('place,holder,000000003,placeholder@placeholder,place holder,0\n')
            data.write('place,holder,000000004,placeholder@placeholder,place holder,0\n')
            data.write('place,holder,000000005,placeholder@placeholder,place holder,0\n')
            data.close()
            self.studentList = StudentQueue.students_list(CONFIG.DATA_PATH, True)
            self.studentQ = StudentQueue.create_queue(self.studentList)

            self.deck = StudentQueue.on_deck(self.studentQ)

            # incase it interrupts before removing anyone from deck
            StudentQueue.export_queue_during(self.studentQ, self.deck)
            self.r = Roster.Roster()
            self.r.import_roster(CONFIG.DATA_PATH)

        # main window
        self.main = Tk()

        # setting the icon
        self.main.call('wm', 'iconphoto', self.main._w, PhotoImage(file='images/icon.png'))

        # initializing a menu bar
        menubar = Menu(self.main)

        # pul ldown menu for file?(name could be changed) operations (import roster, exit program)
        filemenu = Menu(menubar, tearoff=0)
        # create option menu
        optionmenu = Menu(menubar, tearoff=0)
        # create submenu for choosing picture functionality
        picturemenu = Menu(optionmenu, tearoff=0)
        # create submenu for exporting roster
        exportmenu = Menu(filemenu, tearoff=0)

        # file menu commands
        filemenu.add_command(label="Import Roster", command=self.importRoster)
        filemenu.add_separator()
        filemenu.add_cascade(label="Export Roster As", menu=exportmenu)
        filemenu.add_command(label="Export Term Report", command=self.exporttermreport)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.main.destroy)

        # option menu submenu commands
        picturemenu.add_command(label="Use Pictures", command=self.usePics)
        picturemenu.add_command(label="Do Not Use Pictures", command=self.noPics)

        # export menu commands
        exportmenu.add_command(label="csv", command=self.exportcsv)
        exportmenu.add_command(label="tsv", command=self.exporttsv)
        exportmenu.add_command(label="txt", command=self.exporttxt)

        # add cascading menus to menubar labels
        menubar.add_cascade(label="File", menu=filemenu)
        optionmenu.add_cascade(label="Include Pictures?", menu=picturemenu)
        menubar.add_cascade(label="Options", menu=optionmenu)

        # display the menu
        self.main.config(menu=menubar)

        # used to determine which student select is on
        self.select = 1

        # used to determine which deleiminator is selected (csv default)
        self.delim = "csv"

        # size of main window (short and wide for top of screen)
        # getting size of user-specific screen width
        self.width = self.main.winfo_screenwidth()
        self.main.geometry("{}x230".format(self.width))
        self.main.title("Welcome to Cold-Call Assist")

        # 4 frames for the 4 students on deck
        self.frame1 = Frame(self.main, borderwidth=2, relief="solid")
        self.frame2 = Frame(self.main, borderwidth=2, relief="solid")
        self.frame3 = Frame(self.main, borderwidth=2, relief="solid")
        self.frame4 = Frame(self.main, borderwidth=2, relief="solid")

        # string variables to store student names
        self.n1 = StringVar()
        self.n2 = StringVar()
        self.n3 = StringVar()
        self.n4 = StringVar()

        # names are set with the .set() command, queueTest() finds next name in queue
        self.n1.set('{self.deck[0].first} {self.deck[0].last}'.format(self=self))
        self.n2.set('{self.deck[1].first} {self.deck[1].last}'.format(self=self))
        self.n3.set('{self.deck[2].first} {self.deck[2].last}'.format(self=self))
        self.n4.set('{self.deck[3].first} {self.deck[3].last}'.format(self=self))

        # select automatically starts at the first student, so highlight student1
        self.frame1['bg'] = 'yellow'

        # labels to be filled with student names
        self.label1 = Label(self.frame1, textvariable=self.n1)
        self.label2 = Label(self.frame2, textvariable=self.n2)
        self.label3 = Label(self.frame3, textvariable=self.n3)
        self.label4 = Label(self.frame4, textvariable=self.n4)
        self.label1.pack()
        self.label2.pack()
        self.label3.pack()
        self.label4.pack()

        # adding responsive scaling to the columns
        self.frame1.pack(side="left", expand=True, fill="both")
        self.frame2.pack(side="left", expand=True, fill="both")
        self.frame3.pack(side="left", expand=True, fill="both")
        self.frame4.pack(side="left", expand=True, fill="both")

        # adding the buttons to display the pictures
        self.image1 = PhotoImage(file=self.path2image(self.deck[0]))
        self.image2 = PhotoImage(file=self.path2image(self.deck[1]))
        self.image3 = PhotoImage(file=self.path2image(self.deck[2]))
        self.image4 = PhotoImage(file=self.path2image(self.deck[3]))

        self.piclabel1 = Label(self.frame1, image=self.image1)
        self.piclabel2 = Label(self.frame2, image=self.image2)
        self.piclabel3 = Label(self.frame3, image=self.image3)
        self.piclabel4 = Label(self.frame4, image=self.image4)
        self.piclabel1.pack()
        self.piclabel2.pack()
        self.piclabel3.pack()
        self.piclabel4.pack()

        # keybindings for the directional keys
        self.main.bind(CONFIG.KEYBIND_LEFT, self.leftKey)
        self.main.bind(CONFIG.KEYBIND_RIGHT, self.rightKey)
        self.main.bind(CONFIG.KEYBIND_FLAG, self.upKey)
        self.main.bind(CONFIG.KEYBIND_REMOVE, self.downKey)

        if CONFIG.IMPORT_KEYBIND:
            self.main.bind(CONFIG.KEYBIND_IMPORT, self.importRoster)
        if CONFIG.EXPORT_CSV_KEYBIND:
            self.main.bind(CONFIG.KEYBIND_EXPORT_CSV, self.exportcsv)
        if CONFIG.EXPORT_TSV_KEYBIND:
            self.main.bind(CONFIG.KEYBIND_TSV_EXPORT, self.exporttsv)

        if CONFIG.USE_PICTURES_KEYBIND:
            self.main.bind(CONFIG.KEYBIND_PICTURES, self.usePics)
        if CONFIG.NO_PICTURES_KEYBIND:
            self.main.bind(CONFIG.KEYBIND_NO_PICTURES, self.noPics)

        if not CONFIG.PICTURES_BY_DEFAULT:
            self.noPics()

        # main window loop initiation
        self.main.attributes("-topmost", True)
        self.main.mainloop()

        StudentQueue.export_queue_after(self.studentQ, self.deck)
        # gets rid of _queue.csv since its exiting correctly
        if os.path.exists('_queue.csv'):
            os.remove('_queue.csv')

    # -------------------------------------------------------------------------------
    # ---Menu Functions--------------------------------------------------------------
    # -------------------------------------------------------------------------------

    def importRoster(self, f=None):
        print("Import Roster Selected")
        self.main.filename = filedialog.askopenfilename(initialdir=CWD, title="Select file", filetypes=(
            ("csv/tsv files", "*.csv *.tsv *.txt"), ("all files", "*.*")))
        if self.main.filename:
            self.r.import_roster(self.main.filename)
            self.studentList = StudentQueue.students_list(self.main.filename, False)
            self.studentQ = StudentQueue.create_queue(self.studentList)

            self.deck = StudentQueue.on_deck(self.studentQ)
            self.n1.set('{self.deck[0].first} {self.deck[0].last}'.format(self=self))
            self.n2.set('{self.deck[1].first} {self.deck[1].last}'.format(self=self))
            self.n3.set('{self.deck[2].first} {self.deck[2].last}'.format(self=self))
            self.n4.set('{self.deck[3].first} {self.deck[3].last}'.format(self=self))
            new_image1 = PhotoImage(file=self.path2image(self.deck[0]))
            self.piclabel1.configure(image=new_image1)
            self.piclabel1.image = new_image1
            new_image2 = PhotoImage(file=self.path2image(self.deck[1]))
            self.piclabel2.configure(image=new_image2)
            self.piclabel2.image = new_image2
            new_image3 = PhotoImage(file=self.path2image(self.deck[2]))
            self.piclabel3.configure(image=new_image3)
            self.piclabel3.image = new_image3
            new_image4 = PhotoImage(file=self.path2image(self.deck[3]))
            self.piclabel4.configure(image=new_image4)
            self.piclabel4.image = new_image4
            StudentQueue.export_queue_during(self.studentQ, self.deck)

    # -------------------------------------------------------------------------------

    def exportcsv(self, f=None):
        self.main.filename = filedialog.asksaveasfilename(initialdir=CWD, title="Select file",
                                                          filetypes=(("csv files", ".csv"), ("all files", "*.*")),
                                                          defaultextension='.csv')
        if self.main.filename:
            self.r.export_roster(self.main.filename, ',')

    # -------------------------------------------------------------------------------

    def exporttsv(self, f=None):
        self.main.filename = filedialog.asksaveasfilename(initialdir=CWD, title="Select file",
                                                          filetypes=(("tsv files", ".tsv"), ("all files", "*.*")),
                                                          defaultextension='.tsv')
        if self.main.filename:
            self.r.export_roster(self.main.filename, '\t')

    # -------------------------------------------------------------------------------

    def exporttxt(self):
        self.main.filename = filedialog.asksaveasfilename(initialdir=CWD, title="Select file",
                                                          filetypes=(("text files", ".txt"), ("all files", "*.*")),
                                                          defaultextension='.txt')
        if self.main.filename:
            self.r.export_roster(self.main.filename, ',')

    def exporttermreport(self):
        self.main.filename = filedialog.asksaveasfilename(initialdir=CWD, title="Select file",
                                                          filetypes=(("text files", ".txt"), ("all files", "*.*")),
                                                          defaultextension='.txt')
        if self.main.filename:
            self.r.export_term_report(self.main.filename, ',')

    # -------------------------------------------------------------------------------

    def usePics(self, f=None):
        print("Use Pictures")

        self.main.geometry("{}x230".format(self.width))

        # add images to frames
        self.piclabel1.pack()
        self.piclabel2.pack()
        self.piclabel3.pack()
        self.piclabel4.pack()

    # -------------------------------------------------------------------------------

    def noPics(self, f=None):
        print("Do Not Use Pictures")

        self.main.geometry("{}x40".format(self.width))
        # add images to frames
        self.piclabel1.pack_forget()
        self.piclabel2.pack_forget()
        self.piclabel3.pack_forget()
        self.piclabel4.pack_forget()

    # -------------------------------------------------------------------------------
    # ---name-to-image-path Function-------------------------------------------------
    # -------------------------------------------------------------------------------

    def path2image(self, student):
        if student.reveal == 0:
            return "./images/default.png"
        else:
            if os.path.exists("./images/" + str(student.ID) + ".png"):
                return "./images/" + str(student.ID) + ".png"
            else:
                return "./images/default.png"

    # -------------------------------------------------------------------------------
    # ---Key-Binding Functions-------------------------------------------------------
    # -------------------------------------------------------------------------------

    def leftKey(self, event):
        print("Left key pressed")

        # reset all colums color to white
        self.frame1['bg'] = CONFIG.BACKGROUND_COLOR
        self.frame2['bg'] = CONFIG.BACKGROUND_COLOR
        self.frame3['bg'] = CONFIG.BACKGROUND_COLOR
        self.frame4['bg'] = CONFIG.BACKGROUND_COLOR

        # if select not on leftmost student, move select left
        if self.select != 1:
            self.select -= 1
        else:
            self.select = 4

        # recolor the frame the select is now on
        if self.select == 1:
            self.frame1['bg'] = CONFIG.SELECTOR_COLOR
        if self.select == 2:
            self.frame2['bg'] = CONFIG.SELECTOR_COLOR
        if self.select == 3:
            self.frame3['bg'] = CONFIG.SELECTOR_COLOR
        if self.select == 4:
            self.frame4['bg'] = CONFIG.SELECTOR_COLOR

    # -------------------------------------------------------------------------------

    def rightKey(self, event):
        print("Right key pressed")

        # reset all colums color to white
        self.frame1['bg'] = CONFIG.BACKGROUND_COLOR
        self.frame2['bg'] = CONFIG.BACKGROUND_COLOR
        self.frame3['bg'] = CONFIG.BACKGROUND_COLOR
        self.frame4['bg'] = CONFIG.BACKGROUND_COLOR

        # if select not on rightmost student, move select right
        if self.select != 4:
            self.select += 1
        else:
            self.select = 1

        # recolor the frame the select is now on
        if self.select == 1:
            self.frame1['bg'] = CONFIG.SELECTOR_COLOR
        if self.select == 2:
            self.frame2['bg'] = CONFIG.SELECTOR_COLOR
        if self.select == 3:
            self.frame3['bg'] = CONFIG.SELECTOR_COLOR
        if self.select == 4:
            self.frame4['bg'] = CONFIG.SELECTOR_COLOR

    # -------------------------------------------------------------------------------

    def upKey(self, event):
        print("Up key pressed")

        # indicate the selected student was selected by coloring frame green
        if self.select == 1:
            self.deck = StudentQueue.remove_student(self.select, self.deck, self.studentQ)
            self.n1.set('{self.deck[0].first} {self.deck[0].last}'.format(self=self))

            new_image = PhotoImage(file=self.path2image(self.deck[0]))
            self.piclabel1.configure(image=new_image)
            self.piclabel1.image = new_image

            self.frame1['bg'] = CONFIG.REMOVE_COLOR

        if self.select == 2:
            self.deck = StudentQueue.remove_student(self.select, self.deck, self.studentQ)
            self.n2.set('{self.deck[1].first} {self.deck[1].last}'.format(self=self))

            new_image = PhotoImage(file=self.path2image(self.deck[1]))
            self.piclabel2.configure(image=new_image)
            self.piclabel2.image = new_image

            self.frame2['bg'] = CONFIG.REMOVE_COLOR

        if self.select == 3:
            self.deck = StudentQueue.remove_student(self.select, self.deck, self.studentQ)
            self.n3.set('{self.deck[2].first} {self.deck[2].last}'.format(self=self))

            new_image = PhotoImage(file=self.path2image(self.deck[2]))
            self.piclabel3.configure(image=new_image)
            self.piclabel3.image = new_image

            self.frame3['bg'] = CONFIG.REMOVE_COLOR

        if self.select == 4:
            self.deck = StudentQueue.remove_student(self.select, self.deck, self.studentQ)
            self.n4.set('{self.deck[3].first} {self.deck[3].last}'.format(self=self))

            new_image = PhotoImage(file=self.path2image(self.deck[3]))
            self.piclabel4.configure(image=new_image)
            self.piclabel4.image = new_image

            self.frame4['bg'] = CONFIG.REMOVE_COLOR

        StudentQueue.export_queue_during(self.studentQ, self.deck)

    # -------------------------------------------------------------------------------

    def downKey(self, event):
        print("Down key pressed")

        # indicate the selected student has been flagged by coloring frame red
        if self.select == 1:
            self.deck = StudentQueue.remove_student(self.select, self.deck, self.studentQ, True)
            self.n1.set('{self.deck[0].first} {self.deck[0].last}'.format(self=self))

            new_image = PhotoImage(file=self.path2image(self.deck[0]))
            self.piclabel1.configure(image=new_image)
            self.piclabel1.image = new_image

            self.frame1['bg'] = CONFIG.FLAG_COLOR

        if self.select == 2:
            self.deck = StudentQueue.remove_student(self.select, self.deck, self.studentQ, True)
            self.n2.set('{self.deck[1].first} {self.deck[1].last}'.format(self=self))

            new_image = PhotoImage(file=self.path2image(self.deck[1]))
            self.piclabel2.configure(image=new_image)
            self.piclabel2.image = new_image

            self.frame2['bg'] = CONFIG.FLAG_COLOR

        if self.select == 3:
            self.deck = StudentQueue.remove_student(self.select, self.deck, self.studentQ, True)
            self.n3.set('{self.deck[2].first} {self.deck[2].last}'.format(self=self))

            new_image = PhotoImage(file=self.path2image(self.deck[2]))
            self.piclabel3.configure(image=new_image)
            self.piclabel3.image = new_image

            self.frame3['bg'] = CONFIG.FLAG_COLOR

        if self.select == 4:
            self.deck = StudentQueue.remove_student(self.select, self.deck, self.studentQ, True)
            self.n4.set('{self.deck[3].first} {self.deck[3].last}'.format(self=self))

            new_image = PhotoImage(file=self.path2image(self.deck[3]))
            self.piclabel4.configure(image=new_image)
            self.piclabel4.image = new_image

            self.frame4['bg'] = CONFIG.FLAG_COLOR

        StudentQueue.export_queue_during(self.studentQ, self.deck)


# -------------------------------------------------------------------------------

if __name__ == '__main__':
    Gui = coldCallGui()

# -------------------------------------------------------------------------------

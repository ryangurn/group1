#
# Sean Wilson - 1/20/20
# -GUI prototype v2.0
# -Group1 cis422 @ U of O W'20
#

#-------------------------------------------------------------------------------

# import all the the tkinter library has to offer
from tkinter import *
from tkinter import filedialog
import StudentQueue
import os
import os.path
import Roster

#-------------------------------------------------------------------------------
#---Global----------------------------------------------------------------------
#-------------------------------------------------------------------------------

CWD = os.getcwd()

#-------------------------------------------------------------------------------
#---GUI Class-------------------------------------------------------------------
#-------------------------------------------------------------------------------

class coldCallGui:

#-------------------------------------------------------------------------------
#---Initializer-----------------------------------------------------------------
#-------------------------------------------------------------------------------

    def __init__(self):

        if os.path.exists('data.csv'):
            self.studentList = StudentQueue.students_list('data.csv')
            self.studentQ = StudentQueue.create_queue(self.studentList)

            self.deck = StudentQueue.on_deck(self.studentQ)
            
            #incase it interrupts before removing anyone from deck
            StudentQueue.export_queue_during(self.studentQ,self.deck)
            
            self.r = Roster.Roster()
            self.r.import_roster('data.csv')
        else:
            data = open('data.csv', 'w')
            data.write('first,last,ID,email,phonetic,reveal\n')
            data.write('place,holder,000000001,placeholder@placeholder,place holder,0\n')
            data.write('place,holder,000000002,placeholder@placeholder,place holder,0\n')
            data.write('place,holder,000000003,placeholder@placeholder,place holder,0\n')
            data.write('place,holder,000000004,placeholder@placeholder,place holder,0\n')
            data.write('place,holder,000000005,placeholder@placeholder,place holder,0\n')
            data.close()
            self.studentList = StudentQueue.students_list('data.csv')
            self.studentQ = StudentQueue.create_queue(self.studentList)

            self.deck = StudentQueue.on_deck(self.studentQ)
            
            #incase it interrupts before removing anyone from deck
            StudentQueue.export_queue_during(self.studentQ,self.deck)
            self.r = Roster.Roster()
            self.r.import_roster('data.csv')

        #self.head = -1
        # self.queue = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]
        # self.max = 11
        #self.queue = ["Alex Archer", "Naser Alkhateri", "Cory Ingram", "Ryan Gurnick", "Sean Wilson"]
        #self.max = 5
        # !!! TODO: FOR TESTING PURPOSES ONLY !!!

        # main window
        self.main = Tk()

        # initializing a menu bar
        menubar = Menu(self.main)

        # pulldown menu for file?(name could be changed) operations (import roster, exit program)
        filemenu = Menu(menubar, tearoff=0)
        # create option menu
        optionmenu = Menu(menubar, tearoff=0)
        # create submenu for choosing picture functionality
        picturemenu = Menu(optionmenu, tearoff=0)
        # create submenu for exporting roster
        exportmenu = Menu(filemenu, tearoff=0)

        # file menu commands
        filemenu.add_command(label="Import Roster", command=self.importRoster)
        filemenu.add_cascade(label="Export Roster As", menu=exportmenu)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.main.quit)

        # option menu commands
        #optionmenu.add_command(label="Use tsv format", command=self.changeDelimTSV)
        #optionmenu.add_command(label="Use csv format", command=self.changeDelimCSV)

        # option menu submenu commands
        picturemenu.add_command(label="Use Pictures", command=self.usePics)
        picturemenu.add_command(label="Do Not Use Pictures", command=self.noPics)

        # export menu commands
        exportmenu.add_command(label="csv", command=self.exportcsv)
        exportmenu.add_command(label="tsv", command=self.exporttsv)
        exportmenu.add_command(label="txt", command=self.exporttxt)

        #add cascading menus to menubar labels
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
        self.main.geometry(f"{self.width}x200")
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
        # TODO: initialize the stringVars w/ the first four names
        self.n1.set('{self.deck[0].first} {self.deck[0].last}'.format(self=self))
        self.n2.set('{self.deck[1].first} {self.deck[1].last}'.format(self=self))
        self.n3.set('{self.deck[2].first} {self.deck[2].last}'.format(self=self))
        self.n4.set('{self.deck[3].first} {self.deck[3].last}'.format(self=self))

        # select autmatically starts at the first student, so highlight student1
        self.frame1['bg'] = 'yellow'

        # labels to be filled with student names
        self.label1 = Label(self.frame1, textvariable = self.n1)
        self.label2 = Label(self.frame2, textvariable = self.n2)
        self.label3 = Label(self.frame3, textvariable = self.n3)
        self.label4 = Label(self.frame4, textvariable = self.n4)
        self.label1.pack()
        self.label2.pack()
        self.label3.pack()
        self.label4.pack()

        # adding responive scaling to the columns
        self.frame1.pack(side="left", expand=True, fill="both")
        self.frame2.pack(side="left", expand=True, fill="both")
        self.frame3.pack(side="left", expand=True, fill="both")
        self.frame4.pack(side="left", expand=True, fill="both")

        # adding the buttons to display the pictures
        # TODO: need a function to take name and return path to picture file


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

        # keybinding the arrows to their functions
        self.main.bind('<Left>', self.leftKey)
        self.main.bind('<Right>', self.rightKey)
        self.main.bind('<Up>', self.upKey)
        self.main.bind('<Down>', self.downKey)

        #main window loop initiaition
        self.main.mainloop()
        
        print("exiting")
        StudentQueue.export_queue_after(self.studentQ,self.deck)
        #gets rid of _queue.csv since its exiting correctly
        if os.path.exists('_queue.csv'):
            os.remove('_queue.csv')
        
#-------------------------------------------------------------------------------
#---Queue Function for Testing--------------------------------------------------
#-------------------------------------------------------------------------------

    def queueTest(self):
        # iterates through the queue and loops back around at the end
        if ((self.head + 1) >= self.max):
            self.head = 0
        else:
            self.head += 1
        return self.queue[self.head]

#-------------------------------------------------------------------------------
#---Menu Functions--------------------------------------------------------------
#-------------------------------------------------------------------------------

    def importRoster(self):
        print ("Import Roster Selected")
        self.main.filename = filedialog.askopenfilename(initialdir = CWD,title = "Select file",filetypes = (("csv/tsv files","*.csv *.tsv *.txt"),("all files","*.*")))
        if self.main.filename:
            self.r.import_roster(self.main.filename)
            self.studentList = StudentQueue.students_list(self.main.filename)
            self.studentQ = StudentQueue.create_queue(self.studentList)
            
            self.deck = StudentQueue.on_deck(self.studentQ)
            self.n1.set('{self.deck[0].first} {self.deck[0].last}'.format(self=self))
            self.n2.set('{self.deck[1].first} {self.deck[1].last}'.format(self=self))
            self.n3.set('{self.deck[2].first} {self.deck[2].last}'.format(self=self))
            self.n4.set('{self.deck[3].first} {self.deck[3].last}'.format(self=self))
            StudentQueue.export_queue_during(self.studentQ,self.deck)

#-------------------------------------------------------------------------------

    def exportcsv(self):
        self.main.filename = filedialog.asksaveasfilename(initialdir = CWD,title = "Select file",filetypes = (("csv files",".csv"),("all files","*.*")), defaultextension='.csv')
        if self.main.filename:
            self.r.export_roster(self.main.filename, ',')


#-------------------------------------------------------------------------------

    def exporttsv(self):
        self.main.filename = filedialog.asksaveasfilename(initialdir = CWD,title = "Select file",filetypes = (("tsv files",".tsv"),("all files","*.*")), defaultextension='.tsv')
        if self.main.filename:
            self.r.export_roster(self.main.filename, '\t')

#-------------------------------------------------------------------------------

    def exporttxt(self):
        self.main.filename = filedialog.asksaveasfilename(initialdir = CWD,title = "Select file",filetypes = (("text files",".txt"),("all files","*.*")), defaultextension='.txt')
        if self.main.filename:
            self.r.export_roster(self.main.filename, ',')

#-------------------------------------------------------------------------------

    def usePics(self):
        print ("Use Pictures")

        self.main.geometry(f"{self.width}x200")

        # add images to frames
        self.piclabel1.pack()
        self.piclabel2.pack()
        self.piclabel3.pack()
        self.piclabel4.pack()

#-------------------------------------------------------------------------------

    def noPics(self):
        print ("Do Not Use Pictures")

        self.main.geometry(f"{self.width}x50")

        # add images to frames
        self.piclabel1.pack_forget()
        self.piclabel2.pack_forget()
        self.piclabel3.pack_forget()
        self.piclabel4.pack_forget()

#-------------------------------------------------------------------------------
#---name-to-image-path Function-------------------------------------------------
#-------------------------------------------------------------------------------

    def path2image(self, student):
        # outputs path to students respective picture
        print (student.reveal, "reveal")
        print (student.ID, "id")

        if student.reveal == 0:
            return "./images/default.png"
        else:
            if os.path.exists("./images/" + str(student.ID) + ".png"):
                return "./images/" + str(student.ID) + ".png"
            else:
                return "./images/default.png"

#-------------------------------------------------------------------------------
#---Key-Binding Functions-------------------------------------------------------
#-------------------------------------------------------------------------------

    def leftKey(self, event):
        print ("Left key pressed")

        #reset all colums color to white
        self.frame1['bg'] = 'white'
        self.frame2['bg'] = 'white'
        self.frame3['bg'] = 'white'
        self.frame4['bg'] = 'white'

        #if select not on leftmost student, move select left
        if(self.select != 1):
            self.select -= 1
        else:
            self.select = 4

        #recolor the frame the select is now on
        if (self.select == 1):
            self.frame1['bg'] = 'yellow'
        if (self.select == 2):
            self.frame2['bg'] = 'yellow'
        if (self.select == 3):
            self.frame3['bg'] = 'yellow'
        if (self.select == 4):
            self.frame4['bg'] = 'yellow'

#-------------------------------------------------------------------------------

    def rightKey(self, event):
        print ("Right key pressed")

        #reset all colums color to white
        self.frame1['bg'] = 'white'
        self.frame2['bg'] = 'white'
        self.frame3['bg'] = 'white'
        self.frame4['bg'] = 'white'

        #if select not on rightmost student, move select right
        if(self.select != 4):
            self.select += 1
        else:
            self.select = 1

        #recolor the frame the select is now on
        if (self.select == 1):
            self.frame1['bg'] = 'yellow'
        if (self.select == 2):
            self.frame2['bg'] = 'yellow'
        if (self.select == 3):
            self.frame3['bg'] = 'yellow'
        if (self.select == 4):
            self.frame4['bg'] = 'yellow'

#-------------------------------------------------------------------------------

    def upKey(self, event):
        print ("Up key pressed")

        #indicate the selected student was selected by coloring frame green
        # TODO: here is where the name will be swapped w/ next student in queue
        if (self.select == 1):
            self.deck = StudentQueue.remove_student(self.select, self.deck, self.studentQ)
            self.n1.set('{self.deck[0].first} {self.deck[0].last}'.format(self=self))
            #StudentQueue.export_queue_during(self.studentQ,self.deck)

            # TODO: need a function to take name and return path to picture file

            new_image = PhotoImage(file=self.path2image(self.deck[0]))
            self.piclabel1.configure(image=new_image)
            self.piclabel1.image = new_image

            self.frame1['bg'] = 'green'

        if (self.select == 2):
            self.deck = StudentQueue.remove_student(self.select, self.deck, self.studentQ)
            self.n2.set('{self.deck[1].first} {self.deck[1].last}'.format(self=self))
            #StudentQueue.export_queue_during(self.studentQ,self.deck)

            # TODO: need a function to take name and return path to picture file

            new_image = PhotoImage(file=self.path2image(self.deck[1]))
            self.piclabel2.configure(image=new_image)
            self.piclabel2.image = new_image

            self.frame2['bg'] = 'green'

        if (self.select == 3):
            self.deck = StudentQueue.remove_student(self.select, self.deck, self.studentQ)
            self.n3.set('{self.deck[2].first} {self.deck[2].last}'.format(self=self))
            #StudentQueue.export_queue_during(self.studentQ,self.deck)

            # TODO: need a function to take name and return path to picture file

            new_image = PhotoImage(file=self.path2image(self.deck[2]))
            self.piclabel3.configure(image=new_image)
            self.piclabel3.image = new_image

            self.frame3['bg'] = 'green'

        if (self.select == 4):
            self.deck = StudentQueue.remove_student(self.select, self.deck, self.studentQ)
            self.n4.set('{self.deck[3].first} {self.deck[3].last}'.format(self=self))
            #StudentQueue.export_queue_during(self.studentQ,self.deck)

            # TODO: need a function to take name and return path to picture file

            new_image = PhotoImage(file=self.path2image(self.deck[3]))
            self.piclabel4.configure(image=new_image)
            self.piclabel4.image = new_image

            self.frame4['bg'] = 'green'

        StudentQueue.export_queue_during(self.studentQ,self.deck)
#-------------------------------------------------------------------------------

    def downKey(self, event):
        print ("Down key pressed")

        #indicate the selected student has been flagged by coloring frame red
        # TODO: here is where the name will marked as flagged
        if (self.select == 1):
            # TODO: flag student1
            self.deck = StudentQueue.remove_student(self.select, self.deck, self.studentQ)
            self.n1.set('{self.deck[0].first} {self.deck[0].last}'.format(self=self))
            #StudentQueue.export_queue_during(self.studentQ,self.deck)

            # TODO: need a function to take name and return path to picture file

            new_image = PhotoImage(file=self.path2image(self.deck[0]))
            self.piclabel1.configure(image=new_image)
            self.piclabel1.image = new_image

            self.frame1['bg'] = 'red'

        if (self.select == 2):
            # TODO: flag student2
            self.deck = StudentQueue.remove_student(self.select, self.deck, self.studentQ)
            self.n2.set('{self.deck[1].first} {self.deck[1].last}'.format(self=self))
            #StudentQueue.export_queue_during(self.studentQ,self.deck)

            # TODO: need a function to take name and return path to picture file

            new_image = PhotoImage(file=self.path2image(self.deck[1]))
            self.piclabel2.configure(image=new_image)
            self.piclabel2.image = new_image

            self.frame2['bg'] = 'red'

        if (self.select == 3):
            # TODO: flag student3
            self.deck = StudentQueue.remove_student(self.select, self.deck, self.studentQ)
            self.n3.set('{self.deck[2].first} {self.deck[2].last}'.format(self=self))
            #StudentQueue.export_queue_during(self.studentQ,self.deck)

            # TODO: need a function to take name and return path to picture file

            new_image = PhotoImage(file=self.path2image(self.deck[2]))
            self.piclabel3.configure(image=new_image)
            self.piclabel3.image = new_image

            self.frame3['bg'] = 'red'

        if (self.select == 4):
            # TODO: flag student4
            self.deck = StudentQueue.remove_student(self.select, self.deck, self.studentQ)
            self.n4.set('{self.deck[3].first} {self.deck[3].last}'.format(self=self))
            #StudentQueue.export_queue_during(self.studentQ,self.deck)

            # TODO: need a function to take name and return path to picture file

            new_image = PhotoImage(file=self.path2image(self.deck[3]))
            self.piclabel4.configure(image=new_image)
            self.piclabel4.image = new_image

            self.frame4['bg'] = 'red'

        StudentQueue.export_queue_during(self.studentQ,self.deck)
#-------------------------------------------------------------------------------

if __name__ == '__main__':

    Gui = coldCallGui()

#-------------------------------------------------------------------------------

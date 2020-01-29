#
# Sean Wilson - 1/20/19
# -GUI prototype v1.0
# -Group1 cis422 @ U of O W'20
#

#-------------------------------------------------------------------------------

# import all the the tkinter library has to offer
from tkinter import *

#-------------------------------------------------------------------------------
#---GUI Class-------------------------------------------------------------------
#-------------------------------------------------------------------------------

class coldCallGui:

#-------------------------------------------------------------------------------
#---Initializer-----------------------------------------------------------------
#-------------------------------------------------------------------------------

    def __init__(self):

        # !!! TODO: FOR TESTING PURPOSES ONLY !!!
        self.head = -1
        # self.queue = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]
        # self.max = 11
        self.queue = ["Alex Archer", "Naser Alkhateri", "Cory Ingram", "Ryan Gurnick", "Sean Wilson"]
        self.max = 5
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

        # file menu commands
        filemenu.add_command(label="Import Roster", command=self.importRoster)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.main.quit)

        # option menu commands
        optionmenu.add_command(label="Use tsv format", command=self.changeDelimTSV)
        optionmenu.add_command(label="Use csv format", command=self.changeDelimCSV)

        # option menu submenu commands
        picturemenu.add_command(label="Use Pictures", command=self.usePics)
        picturemenu.add_command(label="Do Not Use Pictures", command=self.noPics)

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
        self.main.geometry("1500x200")
        self.main.title("Welcome to Cold-Call Assist")

        # 4 frames for the 4 students on deck
        self.left = Frame(self.main, borderwidth=2, relief="solid")
        self.right = Frame(self.main, borderwidth=2, relief="solid")
        self.left2 = Frame(self.main, borderwidth=2, relief="solid")
        self.right2 = Frame(self.main, borderwidth=2, relief="solid")

        # string variables to store student names
        self.n1 = StringVar()
        self.n2 = StringVar()
        self.n3 = StringVar()
        self.n4 = StringVar()

        # names are set with the .set() command, queueTest() finds next name in queue
        self.n1.set(self.queueTest())
        self.n2.set(self.queueTest())
        self.n3.set(self.queueTest())
        self.n4.set(self.queueTest())

        # select autmatically starts at the first student, so highlight student1
        self.left['bg'] = 'yellow'

        # labels to be filled with student names
        self.label1 = Label(self.left, textvariable = self.n1)
        self.label2 = Label(self.right, textvariable = self.n2)
        self.label3 = Label(self.left2, textvariable = self.n3)
        self.label4 = Label(self.right2, textvariable = self.n4)
        self.label1.pack()
        self.label2.pack()
        self.label3.pack()
        self.label4.pack()

        # adding responive scaling to the columns
        self.left.pack(side="left", expand=True, fill="both")
        self.right.pack(side="left", expand=True, fill="both")
        self.left2.pack(side="left", expand=True, fill="both")
        self.right2.pack(side="left", expand=True, fill="both")

        # adding the buttons to display the pictures
        # TODO: need a function to take name and return path to picture file
        self.image1 = PhotoImage(file='./head2.png')
        self.image2 = PhotoImage(file='./head2.png')
        self.image3 = PhotoImage(file='./head2.png')
        self.image4 = PhotoImage(file='./head2.png')
        self.piclabel1 = Label(self.left, image=self.image1)
        self.piclabel2 = Label(self.right, image=self.image2)
        self.piclabel3 = Label(self.left2, image=self.image3)
        self.piclabel4 = Label(self.right2, image=self.image4)
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

#-------------------------------------------------------------------------------

    def changeDelimTSV(self):
        print ("TSV was selected")

        self.delim = "tsv"

#-------------------------------------------------------------------------------

    def changeDelimCSV(self):
        print ("CSV was selected")

        self.delim = "csv"

#-------------------------------------------------------------------------------

    def usePics(self):
        print ("Use Pictures")

        self.main.geometry("1500x200")

        # add images to frames
        self.piclabel1.pack()
        self.piclabel2.pack()
        self.piclabel3.pack()
        self.piclabel4.pack()

#-------------------------------------------------------------------------------

    def noPics(self):
        print ("Do Not Use Pictures")

        self.main.geometry("1500x50")

        # add images to frames
        self.piclabel1.pack_forget()
        self.piclabel2.pack_forget()
        self.piclabel3.pack_forget()
        self.piclabel4.pack_forget()

#-------------------------------------------------------------------------------
#---name-to-image-path Function-------------------------------------------------
#-------------------------------------------------------------------------------

    def path2image(self, name):
        # takes a stringVar() as an arg (can be converted to string with get())
        # outputs path to that names respective picture
        print (name.get() + " path")

        return "./head4.png"

#-------------------------------------------------------------------------------
#---Key-Binding Functions-------------------------------------------------------
#-------------------------------------------------------------------------------

    def leftKey(self, event):
        print ("Left key pressed")

        #reset all colums color to white
        self.left['bg'] = 'white'
        self.right['bg'] = 'white'
        self.left2['bg'] = 'white'
        self.right2['bg'] = 'white'

        #if select not on leftmost student, move select left
        if(self.select != 1):
            self.select -= 1
        else:
            self.select = 4

        #recolor the frame the select is now on
        if (self.select == 1):
            self.left['bg'] = 'yellow'
        if (self.select == 2):
            self.right['bg'] = 'yellow'
        if (self.select == 3):
            self.left2['bg'] = 'yellow'
        if (self.select == 4):
            self.right2['bg'] = 'yellow'

#-------------------------------------------------------------------------------

    def rightKey(self, event):
        print ("Right key pressed")

        #reset all colums color to white
        self.left['bg'] = 'white'
        self.right['bg'] = 'white'
        self.left2['bg'] = 'white'
        self.right2['bg'] = 'white'

        #if select not on rightmost student, move select right
        if(self.select != 4):
            self.select += 1
        else:
            self.select = 1

        #recolor the frame the select is now on
        if (self.select == 1):
            self.left['bg'] = 'yellow'
        if (self.select == 2):
            self.right['bg'] = 'yellow'
        if (self.select == 3):
            self.left2['bg'] = 'yellow'
        if (self.select == 4):
            self.right2['bg'] = 'yellow'

#-------------------------------------------------------------------------------

    def upKey(self, event):
        print ("Up key pressed")

        #indicate the selected student was selected by coloring frame green
        # TODO: here is where the name will be swapped w/ next student in queue
        if (self.select == 1):
            self.n1.set(self.queueTest())

            # TODO: need a function to take name and return path to picture file
            new_image = PhotoImage(file=self.path2image(self.n1))
            self.piclabel1.configure(image=new_image)
            self.piclabel1.image = new_image

            self.left['bg'] = 'green'

        if (self.select == 2):
            self.n2.set(self.queueTest())

            # TODO: need a function to take name and return path to picture file
            new_image = PhotoImage(file=self.path2image(self.n2))
            self.piclabel2.configure(image=new_image)
            self.piclabel2.image = new_image

            self.right['bg'] = 'green'

        if (self.select == 3):
            self.n3.set(self.queueTest())

            # TODO: need a function to take name and return path to picture file
            new_image = PhotoImage(file=self.path2image(self.n3))
            self.piclabel3.configure(image=new_image)
            self.piclabel3.image = new_image

            self.left2['bg'] = 'green'

        if (self.select == 4):
            self.n4.set(self.queueTest())

            # TODO: need a function to take name and return path to picture file
            new_image = PhotoImage(file=self.path2image(self.n4))
            self.piclabel4.configure(image=new_image)
            self.piclabel4.image = new_image

            self.right2['bg'] = 'green'

#-------------------------------------------------------------------------------

    def downKey(self, event):
        print ("Down key pressed")

        #indicate the selected student has been flagged by coloring frame red
        # TODO: here is where the name will marked as flagged
        if (self.select == 1):
            # TODO: flag student1
            self.n1.set(self.queueTest())

            # TODO: need a function to take name and return path to picture file
            new_image = PhotoImage(file=self.path2image(self.n1))
            self.piclabel1.configure(image=new_image)
            self.piclabel1.image = new_image

            self.left['bg'] = 'red'

        if (self.select == 2):
            # TODO: flag student2
            self.n2.set(self.queueTest())

            # TODO: need a function to take name and return path to picture file
            new_image = PhotoImage(file=self.path2image(self.n2))
            self.piclabel2.configure(image=new_image)
            self.piclabel2.image = new_image

            self.right['bg'] = 'red'

        if (self.select == 3):
            # TODO: flag student3
            self.n3.set(self.queueTest())

            # TODO: need a function to take name and return path to picture file
            new_image = PhotoImage(file=self.path2image(self.n3))
            self.piclabel3.configure(image=new_image)
            self.piclabel3.image = new_image

            self.left2['bg'] = 'red'

        if (self.select == 4):
            # TODO: flag student4
            self.n4.set(self.queueTest())

            # TODO: need a function to take name and return path to picture file
            new_image = PhotoImage(file=self.path2image(self.n4))
            self.piclabel4.configure(image=new_image)
            self.piclabel4.image = new_image

            self.right2['bg'] = 'red'

#-------------------------------------------------------------------------------

if __name__ == '__main__':

    Gui = coldCallGui()

#-------------------------------------------------------------------------------

import queue
import csv
import os

clear = lambda: os.system('clear')
os.path.isfile('./queue.csv')

def students_list():
    with open('students.csv') as csvfile:
        studentList = []
        csv_reader = csv.reader(csvfile)
    
        next(csv_reader)
    
        for line in csv_reader:
            studentList.append(Students(line[0], line[1], line[2]))
        
    return studentList
    
def students_list2():
    with open('queue.csv') as csvfile:
        studentList = []
        csv_reader = csv.reader(csvfile)
    
        next(csv_reader)
    
        for line in csv_reader:
            studentList.append(Students(line[0], line[1], line[2]))
        
    return studentList

class Students(object):
    def __init__(self,first,last,uo_id):
        self.__first = first
        self.__last = last
        self.__uo_id = uo_id
        self.__flag = False
        
    def getFirst(self):
        return self.__first
        
    def getLast(self):
        return self.__last
        
    def getUO_ID(self):
        return self.__uo_id
        
    def isFlag(self):
        return self.__flag
        
    def setFirst(self,first_name):
        self.__first = first_name
        
    def setLast(self,last_name):
        self.__last = last_name
    
    def setFlag(self):
        self.__flag = True
        

def randomizer(studentList):
    
    first_half = len(studentList) // 2
    tempList = []
    for i in first_half:
        tempList.append(studentList[i])
        
    random.shuffle(tempList)

def on_deck(q):
    
    student1 = q.get()
    student2 = q.get()
    student3 = q.get()
    student4 = q.get()
    q.put(student1)
    q.put(student2)
    q.put(student3)
    q.put(student4)
    return student1, student2 , student3, student4 
    
    

def display_deck(deck_list):
    
    print()
    print('\t1.'+
    str(deck_list[0].getFirst()),str(deck_list[0].getLast()),'\t','2.'+
    str(deck_list[1].getFirst()),str(deck_list[1].getLast()),'\t','3.'+
    str(deck_list[2].getFirst()),str(deck_list[2].getLast()),'\t','4.'+
    str(deck_list[3].getFirst()),str(deck_list[3].getLast()))
    print()
    
def remove_student(s_num,deck,q):
    deck[s_num] = q.get()
    q.put(deck[s_num])
    
    return deck
    
def output_queue_csv(q,deck):
    size = q.qsize()
    with open('queue.csv', 'w') as csvfile:
        filewriter = csv.writer(csvfile)
        filewriter.writerow(['Name', 'Lastname','UO ID'])
        for d in range(4):
            filewriter.writerow([deck[d].getFirst(), deck[d].getLast(),deck[d].getUO_ID()])
        for i in range(size-4):
            out = q.get()
            filewriter.writerow([out.getFirst(), out.getLast(),out.getUO_ID()])
    
    
    
def test_menu():
    print("1.remove1\n2.remove2\n3.remove3\n4.remove4\n0.exit")

def main():
    clear()
    isQueue = os.path.isfile('./queue.csv')
    
    if isQueue:
        studentList = students_list2()
    else:
        studentList = students_list()
        
    
    q = queue.Queue()
    
    for i in range(len(studentList)):
        first = studentList[i].getFirst()
        q.put(studentList[i])
        #print(first)
    #print(q.qsize())
    
    #print(q.qsize())
    s1, s2, s3, s4 = on_deck(q)
    deck = [s1, s2, s3, s4]
    display_deck(deck)
    choice = -1
    while (choice != 0):
        test_menu()
        while True:
            try:
                choice = int(input('\nchoice: '))
                break
            except:
                print("please choose a valid input")
        if choice == 0:
            break
        
        deck = remove_student(choice - 1, deck, q)
        clear()
        display_deck(deck)
            #print(q.qsize())
    output_queue_csv(q,deck)
    
    
if __name__=="__main__":
    main()

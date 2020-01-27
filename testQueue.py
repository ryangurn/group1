
import StudentQueue
import os

clear = lambda: os.system('clear')

def display_deck(deck_list):
    
    print()
    print('\t1.'+
          str(deck_list[0].first),str(deck_list[0].last),'\t','2.'+
          str(deck_list[1].first),str(deck_list[1].last),'\t','3.'+
          str(deck_list[2].first),str(deck_list[2].last),'\t','4.'+
          str(deck_list[3].first),str(deck_list[3].last))
    print()

def test_menu():
    print("1.remove1\n2.remove2\n3.remove3\n4.remove4\n0.exit")

          

#for queue testing
def main():
    clear()
    studentList = StudentQueue.students_list()
    studentQ = StudentQueue.create_queue(studentList)
    s1, s2, s3, s4 = StudentQueue.on_deck(studentQ)
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
        
        deck = StudentQueue.remove_student(choice, deck, studentQ)
        clear()
        display_deck(deck)
        
        StudentQueue.export_queue_during(studentQ,deck)
    #print(q.qsize())
    
    StudentQueue.export_queue_after(studentQ)

if __name__=="__main__":
    main()


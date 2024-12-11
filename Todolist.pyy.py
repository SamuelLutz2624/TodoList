#Varibles

'''
Samuel Lutz
12/10/24
To Do list
This is a To do List that you can add on item, remove item, reset the list and show the list. The list is all different sports

'''

#My List us a global varible that holds the to do items
# It is a list and the items
myList = ("red","orange","Yellow","Green")
def show_menu():
    '''This is docstring and it can be
    multiline
    The show menu funtion has no parameters and returns
    noting it i used as the entry point to the
    to do program and displays a menu'''
    while True:
        print("Pick 1 to have fun")
        print("Pick 2 to do work")
        print("Pick 3 to quit")
        #Choice holds the input choice from the menu
        choice = input("Enter your choice: ")
        if choice == "1":
            have_fun()
        elif choice == "2":
            #Do something
            pass
        elif choice == "3":
            print("Thank you for playing")
            break
    else:
            print("invalid choice")



#variables


todoList = []
def add_item(item): # 1 usage
    # add an item to the to do list
    todoList.append(item)
def remove_item():
    # remove an item from the to do list
    todoList.pop()
def reset_list():
    to_Do_List.clear()
def print_list():
    # print the to do list
    print(todoList)
def show_menu():
    pass
def have_fun():
    print("have fun")
def save_file():
    myList = ["red","orange","yellow","green"]
    with open(fname,"a") as file:
        File.writelives(item + "\n" for item in myList)
def load_file():
    with open(frame,"r")as file:
        myList = (Line.strip() for line in file)
        print("myList")
def remove_something():
    for c in range(0, len(myList)):
        print(str(c)+". " + myList(c))
choice = input("which one do you want to remove: ")
if choice_isnumeric():
    choice = int(choice)
    if choice -1 >= 0 and choice< len(myList):
        myList.pop(choice - 1)
    else:
        print("Invalid choice")
else:
    print("Invlid choice")
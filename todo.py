#peyton mcadams
#to do list

list = []
done = []
def todo():
    while True:
        menu = input("Would you like to... ADD an item to the grocery list, Mark an item as BOUGHT, REMOVE an item or CLEAR the list, or EXIT the program ")
        if menu == "add" or menu == "ADD":
            addition = input("What item would you like to add to the list? ")
            if addition == " ":
                print("Error! Not a valid item. Try again")
            list.append(addition)
            print(list)
        elif menu == "BOUGHT" or menu == "bought":
            mark = input("What item would you like to mark as bought? ")
            try:
                list.remove(mark)
            except:
                print("That item does not exist. Try again.")
            done.append(mark)
            print(done)
        elif menu == "REMOVE" or menu == "remove":
            eliminate = input("What item would you like to remove from the list? ")
            try:
                list.remove(eliminate)
            except:
                print("Error occurred. Please try again.")
            print(list)
        elif menu == "CLEAR" or menu == "clear":
            list.clear()
        else:
            break

todo()

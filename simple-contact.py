contacts = {}

def show_menu():
    print("/n 1-view 2-add 3-search, 4-exit")
    
def view():
    if not contacts:
        print("The contact is not avaliable")
    else:
        print(contacts)

def add():
    n1 = input("Give the persons name ").lower()
    n2= int(input("Give the persons phone number : "))
    contacts[n1] = n2
    print(contacts)

2
def search():
    choice = input("Search by name (n) or phone number (p)? ")

    if choice.lower() == 'n':
        name = input("Enter name: ")
        if name in contacts:
            print(f"{name} → {contacts[name]}")
        else:
            print("Contact not found.")

    elif choice.lower() == 'p':
        phone = int(input("Enter phone number: "))
        found = False
        for name, number in contacts.items():
            if number == phone:
                print(f"Found: {name} → {number}")
                found = True
                break
        if not found:
            print("Phone number not found.")

    else:
        print("Invalid choice.")
        
def delete():
    n = input("Enter the name or number you want to delete: ").lower()
    for name, num in contacts.items():
        if n == name:
            del contacts['name']
            print("The new updated contacts are : " + contacts)
        else :
            key = [key for key,value in contacts.items() if value == n]
            del contacts[key]
            print("The new updated contacts are:  "+ contacts)
            

while True:
    show_menu()
    choice = int(input("Enter the choice you want to do"))
    if choice == 1:
        view()
    elif choice == 2:
        add()
    elif choice == 3:
        search()
    elif choice == 4:
        delete()
    elif choice == 5:
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

    
        
   
    
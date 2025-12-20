print("Welcome to area calculator")

print("Choose the area you want to find \n 1) Triangle \n 2) Rectangle \n 3) Square \n 4) Circle \n 5) Quit")

choice = int(input("Which shape"))
while choice!=5 :
    if choice == 1:
        base = int(input("Base: "))
        height = int(input("Height: "))
        area = 0.5*base*height
        print(area)
    elif choice == 2:
        lenght = int(input("Lenght: "))
        breadth = int(input("Breadth: "))
        area = lenght * breadth
        print(area)
    elif choice == 3:
        side = int(input("Side: "))
        area = side* side
        print(area)
    elif choice == 4:
        radius = int(input("Radius: "))
        area = 3.14*radius*radius
    elif choice == 5:
        print("You are done with the game")
    else:
        print("Wrong input")
def get_item(a):
  if a == 1:
    print("Cheeseburger")
  elif a == 2:
    print("Fries")
  elif a == 3:
    print("Ice cream")
  elif a == 5:
    print("Cookie")
  else:
    print("Exit")


def welcome():
  print("Welcome to my drive thru and have a good day")

welcome()
  
option = int(input("What would you like to order?"))
print(get_item(option))
def km_miles():
    n1 = float(input("Give the number to converted into miles: "))
    miles = n1 * 0.621371
    return miles

def kg_lb():
    n1 = float(input("Give the kg to be converted into pounds:  "))
    pounds = n1 * 2.20462
    return pounds

def c_f():
    n1 = float(input("Give the temperature to be converted: "))
    f = (n1*9/5) + 32
    return f
    
choice = int(input("\nEnter the conversion you want to achieve : 1 km-miles 2 kg-lb 3 c-f : "))
if(choice == 1):
    print("Result: ", km_miles())
elif(choice == 2):
    print("Result: ", kg_lb())
elif(choice == 3):
    print("Result:", c_f())
else:
    print("Invalid conversions")

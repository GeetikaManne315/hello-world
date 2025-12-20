def add(n1,n2):
    a= n1+n2
    return a
    
def sub(n1,n2):
    b = abs(n1-n2)
    return b

def mul(n1,n2):
    c = n1*n2
    return c

def div(n1,n2):
    try:
        d = n1/n2
        return d
    except ZeroDivisionError:
        return 'Error'

def rem(n1,n2):
    r = n1%n2
    return r

n1 = float(input("Enter the first number :"))

n2 = float(input("Enter the second number :"))

choice = int(input("Enter any number from 1 to 4 : "))

if(choice == 1):
    print("Sum : ", add(n1,n2))
elif(choice == 2):
    print("Sub: ", sub(n1,n2))
elif(choice == 3):
    print("Mul :", mul(n1,n2))
elif(choice == 4):
    print("div :",div(n1,n2))
elif(choice == 5):
    print("rem :",rem(n1,n2))
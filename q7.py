def add():
    print("Enter two Arguments to add")
    x=int(input("Enter first no."))
    y=int(input("Enter second no."))
    print(x+y)
def subs():
    print("Enter two Arguments to substraction")
    x=int(input("Enter first no."))
    y=int(input("Enter second no."))
    print(x-y)
def mult():
    print("Enter two Arguments to multiply")
    x=int(input("Enter first no."))
    y=int(input("Enter second no."))
    print(x*y)
def div():
    print("Enter two Arguments to divi")
    x=int(input("Enter first no."))
    y=int(input("Enter second no."))
    print(x/y)
while True:
    print("\nEnter your choice accordingly:")
    print("1: Addition")
    print("2: Substraction")
    print("3: Multiplication")
    print("4: Division")
    print("5: Exit the Progrma")
    x=int(input("Enter the Choice :"))
    if x==1:
        add()
    elif x==2:
        subs()
    elif x==3:
        mult()
    elif x==4:
        div()
    elif x==5:
        print("Exiting the program:)")
        break
    else:
        print("Enter the right choice")
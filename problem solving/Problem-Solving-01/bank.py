def read ():
    global principal`
    global interest
    global years
    global time
    principal=int(input ('Enter Your Principal : '))
    interest=float(input('Enter Your Interest : '))
    years=int(input('Enter The Number of Years :  '))
    time=int(input("Enter The Compounding time :   "))
def calc ():
    global amount
    amount=principal*(1+(interest/time))**(years*time)
def Print():
    print(int(amount))
def main ():
    read()
    calc()
    Print()
main()



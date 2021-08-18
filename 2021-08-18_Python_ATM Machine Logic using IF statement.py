#ATM Machine Logic in Python using "IF" statement.

"Computer Programming Tutor, Aug17th,2021"

print("Welcome to ATM Machine")

pin = int(input("Enter Your 4 Digit Pin Number:"))
amt = 110000

if(pin == 1111):
    print("1- Widthdraw")
    print("2- Balance Enquiry")
    print("3- Fast Cash")
    choice = int(input("Please Choose Transactions: "))
    if (choice == 1):
        w = int(input("Enter Widthdrawn Amount[£]:"))
        if (w <amt and w%100 == 0):
            print("Please Take Your Amount [£]:",w)
        else:
            print("Invalid Cash")
    elif(choice == 2):
        print("Your Balance,[£]:",amt)

    elif(choice == 3):
        print("1-> 1000")
        print("2-> 2000")
        print("3-> 5000")
        print("4-> 10000")

        op = int(input("Enter Fast Cash Option:"))
        if (op == 1 and 1000 < amt):
            print("Please Take Cash 1000")
        elif (op == 2 and 2000 < amt):
            print("Please Take Cash 2000")
        elif (op == 3 and 5000 < amt):
            print("Please Take Cash 5000")
        elif (op == 4 and 10000 < amt):
            print("Please Take Cash 10000")
        else:
            print("Invalid Fast Cash Option")

    else:
        print("Wrong Choice")

else:
    print("Wrong Pin Number")
            
     




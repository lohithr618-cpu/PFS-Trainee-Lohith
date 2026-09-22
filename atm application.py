#ATM APPLICATION
Account=int(100000)
Card="c"
pwd=int(1234)
while True:
    a=str(input("insert the card"))
    if a==Card:
        print("Welcome lohith")
        b=int(input("enter the password"))
        if b==pwd:
            print("options \n1.balnce enquiry \n2.withdrawal")
            option=int(input("enter the number"))
            if option==1:
                print(Account)
            elif option==2:
                print("enter the amount")
                withdraw=int(input())
                balance=Account-withdraw
                print("remaining balane",balance)
            else:
                print("invalid option")
        else:
            print("incorrect password")
    else:
        print("invalid card")
        

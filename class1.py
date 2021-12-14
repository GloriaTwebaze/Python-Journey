#Develop a system with one function that prompts a user to enter name, pin and once a pin is valid. 
#When pin is  correct ask  user to enter an amount to withdraw and system should be able to determine if the user has sufficient 
# bal then the system should be able to reduce the balance on the account.
# Account bal should be displayed after withdraw



def transaction():
    name = "Ishimwe"
    pin = "1888"
    accountbalance = 600000
    username =input("Enter your name \n" )
    pincode =input("Enter your pin \n" )
    amount = int(input("Enter the amount you want to withdraw \n"))
    if username == name and pincode == pin:
        if amount<accountbalance:
            print("you have withdrawn ", amount)
            print("your account balance is", accountbalance-amount)
        else:
                print(name + "you have insufficient balance")
    else: 
        print("Please enter the right info")

transaction()




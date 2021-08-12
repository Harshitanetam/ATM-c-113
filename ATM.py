class Atm:
    def __init__(self,cardnumber, pin):
        self.cardnumber = cardnumber
        self.pin = pin

        def check balance(self)
        print("Youre balance is 50000")

        def withdraw1(self,amount):
            new_amount = 50000 - amount
            print("You have withdrawn amount "+str(amount) +". Your remaining balance is "+ str (new_amount)


def main():
    Card_number = input("insert your card number:-")
    pin_number = input("enter your pin number:-")

    new_user = Atm(Card_number, pin_number)

    print("Choose your activity")
    print(("1 Balance Enquiry   2.windraw1"))
    activity = int(input("enter the amount:-"))

    if(activity == 1):
        new_user.check_balance()
        elif (activity == 2)
        amount = int(input("enter the amount:-"))
        new_user.withdraw1(amount)
        else:
            print("enter a vaild number")


            if __name__ =="__main__":
                main()
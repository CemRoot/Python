from os import system as comm
import time
class Customer():
    def __init__(self,ID,PASSWORD,NAME):
        self.name = NAME
        self.id = ID
        self.password = PASSWORD
        self.Balance = 0

class Bank():
    def __init__(self):
        self.customers = list()

    def OurCustomer(self,ID:str,PASSWORD:str,NAME:str):
        self.customers.append(Customer(ID,PASSWORD,NAME))
        print("Welcome the MAzE BANK !")

def main():
    banka = Bank()
    while True:
        time.sleep(2)
        comm("cls")
        print("""
        [1] I'm also your Customer
        [2] I want to be Customer
        """)

        choose = input("Choose: ")

        if choose == "1":
            ids = [i.id for i in banka.customers]
            ID = input("ID:")
            if ID in ids:
                for Customer in banka.customers:
                    if ID == Customer.id:
                        print("Welcome {}".format(Customer.name))
                        password = input("Password:")
                        if password == Customer.password:
                            print("Succes Login!")
                            while True:
                                time.sleep(2)
                                comm("cls")
                                print("""
                                    [1]-Balance
                                    [2]-Send Money (own account)
                                    [3]-Send Money
                                    [4]-Draw Money
                                    [0]-EXIT
                                """)
                                choose2 = input("Your transaction-->")

                                if choose2 == "1":
                                    print("Balance:{}".format(Customer.Balance))
                                    input("Press ENTER to back to MENU")

                                elif choose2 == "2":
                                    Amount = int(input("Amount:"))
                                    Check = input("Do you approve the {} TL deposit to your own account?:Y/N\n".format(Amount))
                                    if Check == "Y" or Check == "y":
                                        Customer.Balance += Amount
                                        print("Your money has been deposited.")
                                        input("Press ENTER to back to MENU")
                                    elif Check == "N" or Check == "n":
                                        print("The transaction has been canceled.")
                                        input("Press ENTER to back to MENU")
                                    else:
                                        print("ERROR??")
                                        input("Press ENTER to back to MENU")

                                elif choose2 == "3":
                                    SearchID = input("Customer ID=")
                                    if SearchID in ids:
                                        for othercos in banka.customers:
                                            if SearchID == othercos.id:
                                                print("to {}".format(othercos.name))
                                                Amount = int(input("Amount:"))
                                                if Amount <= Customer.Balance:
                                                    Check = input("Do you approve the {} TL deposit to our custome named {}?: Y/N\n".format(Amount,othercos.name))
                                                    if Check == "Y" or Check == "y":
                                                        othercos.Balance += Amount
                                                        Customer.Balance -= Amount
                                                        print("The money was successfully transferred.")
                                                        input("Press ENTER to back to MENU")

                                                    elif Check == "N" or Check == "n":
                                                        print("The transaction has been canceled.")
                                                        input("Press ENTER to back to MENU")

                                                    else:
                                                        print("ERROR??")
                                                        input("Press ENTER to back to MENU")
                                                else:
                                                    print("Your balance is insufficient!")
                                                    input("Press ENTER to back to MENU")
                                    else:   
                                        print("Customer cannot founded!")
                                        input("Press ENTER to back to MENU")

                                elif choose2 == "4":
                                        Amount = int(input("Amount"))
                                        if Amount <= Customer.Balance:
                                            Customer.Balance -= Amount
                                            print("Your balance is insufficient!")
                                            input("Press ENTER to back to MENU")
                                        else: 
                                            print("Your balance is insufficient!") #burada bir hata var amount küçük olsada burayı bastırıyor! 
                                            input("Press ENTER to back to MENU")
                
                                elif choose2 == "0":
                                    break
                                    
            
            else:
                print("Customer cannot founded!")

        elif choose == "2":
            ID = input("Your ID:")
            NAME = input("Your Name:")
            PASSWORD = input("Enter passw:")
            banka.OurCustomer(ID,PASSWORD,NAME)
            
if __name__ == "__main__":
    main()

class account():
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance=balance
    def deposit(self,dep_amt):
        self.balance = self.balance + dep_amt
        print(f"added {dep_amt} to the balance")

    def withdrawal(self,wd_amt):
            if self.balance >=wd_amt:
                self.balance =self.balance - wd_amt
                print(f"withdraw {wd_amt} to the balance")
            else:
                print("insufficient balance")
    def currentstatus(self):
        print("owner name: ",self.owner)
        print("current balance: ",self.balance)

a = account((input("enter ownername: ")),int(input("enter balance: ")))
a.deposit(int(input("enter deposit ammount: ")))
a.withdrawal(int(input("enter withdraw ammount: ")))
a.currentstatus()   

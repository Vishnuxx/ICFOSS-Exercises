class BankAccount:

    def __init__(_self , owner  , balance):
        _self.name = owner
        _self.balance = balance

    def deposit(_self , amount):
        _self.balance += amount
        print('amount of {} deposited successfully'.format(amount))
    
    def withdraw(_self , amount):
        if(not amount > _self.balance):
            _self.balance -= amount
            print("Withdrawal of Rs.{} was successful".format(amount))
        else:
            print("Withdrawal of Rs.{} failed. amount exceeded the currrent balance".format(amount))



user = BankAccount("Vishnu" , 1000)
user.deposit(500)
user.withdraw(300)
user.deposit(1000)
user.withdraw(2300)
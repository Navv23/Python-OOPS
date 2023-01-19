#Banking EcoSystem Using Oops
#PARENT CLASS - USER#
#HOLDS DETAILS ABOUT THE USER
#HAS A FUNCTION TO SHOW USER DETAILS
#CHILD CLASS: BANK#
#STORES DETAILS ABOUT THE ACCOUNT BALANCE 
#ALLOWS FOR DEPOSITS, WITHDRAWS, VIEW_BALANCE

#parent class
class User():
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        
    def show_user_details(self):
        print("Personal Details")
        print('name: ', self.name)
        print('age: ',self.age)
        print('gender: ',self.gender)
        
henry = User('henry',21,'male')
        
henry.show_user_details()

#child class 
class Bank(User):
    def __init__(self,name,age,gender):
        super().__init__(name, age, gender)
        self.balance=0
    
    def deposit(self, amount):
        self.amount=amount
        self.balance=self.balance + self.amount
        print("Your Account Balance Has Been Updated: ",self.balance)
    
    def withdrawl(self, amount):
        self.amount=amount
        if(self.amount>self.balance):
            print("insufficient funds, balance available : Rs",self.balance)
        else:
            self.balance = self.balance-self.amount
            print("your balance has been updated: Rs.",self.balance)
            
    def view_balance(self):
        self.show_user_details()
        print('your current balance is: ',self.balance)
        


tommy = Bank('tommy',40,'Male')
tommy.deposit(300)   
tommy.withdrawl(100)       
tommy.view_balance()
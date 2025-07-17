from django.db import models

#  Create your models here.
# class users(models.Model):
#     full_name=models.CharField(max_length=100)
#     email=models.EmailField(unique=True)
#     password=models.CharField(max_length=100)
#     phone=models.CharField(max_length=15,blank=True,null=True)
#     address=models.TextField(blank=True,null=True)
#     birth_date=models.DateField(null=True)

#  this is a home page = this-is-a-home-page
# class products(models.Model):
#     name=models.CharField(max_length=100)
#     description=models.TextField()
#     price=models.DecimalField(max_digits=10, decimal_places=2)
#     inventory=models.IntegerField(default=0)
#     created_at=models.DateTimeField(auto_now=True)

class Animal():
    def speak(self):
        print("Animal Function invoked")

class Dog(Animal):
    
    def speak(self):
        print("Dog class function invoked")
    def parentSpeak(self):
        super().speak()
        
animal = Animal()
animal.speak()


dog = Dog()
dog.parentSpeak()
dog.speak()


# Hands on create a bank account class with transactions and test cases 
#init withdraw get_balance show_transactions deposit
class Bankaccount():
    def __init__(self, owner,balance=0):
        self .owner=owner
        self .balance=balance
        self .transaction=[]
        self .transaction.append(f"Account created with balance { self .balance}")

    def deposit(self,amount):
        if amount <= 0:
            return "Deposite Must be Positive"
        self.balance += amount
        self.transaction.append(f"deposite:{amount}")
        return f"deposite {amount} sucessfully!"
    
    def withdraw(self,amount):
        if amount <=0:
            return f"withdraw Must be positive"
        
        if amount>self.balance:
            return f"Insufficient Balance"

        



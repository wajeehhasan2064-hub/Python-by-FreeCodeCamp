'''Encapsulation is the bundling of the attributes and methods of an object into a single unit, the class.
With encapsulation, you can hide the internal state of the object behind a simple set of public methods and 
attributes that act like doors. Behind those doors are private attributes and methods that control how the data 
changes and who can see it.

prefixing attribute and methods with a single underscore mean they are meant for internal use. No one should 
directly access them from outside class since it defies the principle of encapsulation, which can lead to bugs.

While a single underscore prefix is just a convention, prefixing attributes and methods with a double underscore 
effectively prevents them to be accessed from the outside of their class, making those attributes and methods 
private.'''

class Wallet:
   def __init__(self):
       self.__balance = 0

   def __validate(self, amount):
       if amount < 0:
           raise ValueError('Amount must be positive')

   def deposit(self, amount):
       self.__validate(amount)
       self.__balance += amount

   def withdraw(self, amount):
       self.__validate(amount)
       if amount > self.__balance:
           raise ValueError('Insufficient funds')
       self.__balance -= amount

   def get_balance(self):
       return self.__balance

acct_one = Wallet()
acct_one.deposit(3)
print(acct_one.get_balance()) # 3

acct_one.deposit(50)
print(acct_one.get_balance()) # 53

acct_one.deposit(-4)  # ValueError: Amount must be positive
acct_one.withdraw(-8) # ValueError: Amount must be positive
acct_one.withdraw(58) # ValueError: Insufficient funds

'''Getters and setters are methods that let you control how the attributes of a class are accessed and modified. 
With getters you retrieve a value, and with setters you set a value.

A deleter runs custom logic when you use the del statement on a property. To create one, you use the 
@<property_name>.deleter decorator'''
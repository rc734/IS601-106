# Task 1 (50 points)

print("Question 1")
arr1 = [89, 52, 36, 24, 17, 99, 82, 73, 61, 48] # 1
arr2 = [89, 52, 36, 24, 17, 99, 82, 73, 61, 48] # 2
arr3 = [15, 13, 16, 12, 17, 11, 18, 10, 19, 9] # 3

# only output the odd values from the above lists (print the output for all lists)
def odd_values(num,arr): # pass the num as list number and arr as list name
    print(f'output for arr {num}: \n')
    arr1 = [89, 52, 36, 24, 17, 99, 82, 73, 61, 48]  # 1
    arr2 = [89, 52, 36, 24, 17, 99, 82, 73, 61, 48]  # 2
    arr3 = [15, 13, 16, 12, 17, 11, 18, 10, 19, 9]    # 3

def odd_values(num, arr):
    print(f'Output for arr {num}: \n')
    for val in arr:
        if val % 2 != 0:
            print(val)

    print('\n End of odd values')
odd_values(1, arr1)
odd_values(2, arr2)
odd_values(3, arr3)


print('\n End of odd values')
print("------------------------------------------------------")


print("Question 2")
arr1 = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20] # 1
arr2 = [17, 19, 15, 16, 14, 18, 13, 12, 11, 20] #2
arr3 = [55, 66, 77, 88, 99, 11, 22, 33, 44] #3

# Only output the sum/total of the lists values (print the output for all lists)
def sum_values(num, arr): # pass the num as list number and arr as list name
    print(f'output for arr {num} : \n')
    #your code here
    arr1 = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]  
    arr2 = [17, 19, 15, 16, 14, 18, 13, 12, 11, 20]  
    arr3 = [55, 66, 77, 88, 99, 11, 22, 33, 44]       

def sum_values(num, arr):
    print(f'Output for arr {num} : \n')
    total_sum = sum(arr)
    print(f'Total sum: {total_sum}')

    print('\n End of sum values')
sum_values(1, arr1)
sum_values(2, arr2)
sum_values(3, arr3)

print('\n End of sum values')
print("-------------------------------------------------")



print("Question 3")
arr1 = [-10, 20, -30, 40, -50, 60, -70, 80, -90, 100] #1
arr2 = [5, -8, 13, -21, 34, -55, 89, -144, 233] #2 
arr3 = [-7, 12, -15, 18, -21, 24, -27, 30, -33] #3
arr4 = [11, -22, 33, -44, 55, -66, 77, -88, 99] #4
arr5 = [-3, 6, -9, 12, -15, 18, -21, 24, -27, 30] #5

# Convert the negative values in the following lists to positive and ouput the sum of all values (print the output for all lists).
def converted_sum_values(num, arr): # pass the num as list number and arr as list name
    print(f'output for arr {num} : \n')
    #your code here
arr1 = [-10, 20, -30, 40, -50, 60, -70, 80, -90, 100]  # 1
arr2 = [5, -8, 13, -21, 34, -55, 89, -144, 233]  # 2 
arr3 = [-7, 12, -15, 18, -21, 24, -27, 30, -33]  # 3
arr4 = [11, -22, 33, -44, 55, -66, 77, -88, 99]  # 4
arr5 = [-3, 6, -9, 12, -15, 18, -21, 24, -27, 30]  # 5

def converted_sum_values(num, arr):
    print(f'Output for arr {num} : \n')
    positive_value_arr = [abs(value) for value in arr]
    sum_total = sum(positive_value_arr)
    
    print(f'Sum of all values (after converting negatives to positive): {sum_total}')

    print('\n End of converted sum values')
converted_sum_values(1, arr1)
converted_sum_values(2, arr2)
converted_sum_values(3, arr3)
converted_sum_values(4, arr4)
converted_sum_values(5, arr5)


print('\n End of converted sum values')
print("----------------------------------------------")


print("Question 4")
arr1 = ['apple', '', 'banana', '', 'cherry'] #1
arr2 = ['', 'dog', '', 'cat', ''] #2
arr3 = ['hello', '', 'world', '', ''] #3
arr4 = ['', '', '', '', ''] #4
arr5 = ['one', '', 'two', '', 'three'] #5
# Remove empty strings from the above lists and output the lists (print the output for all lists)
def empty_str(num, arr): # pass the num as list number and arr as list name
    print(f'output for arr {num} : \n')
    #your code here
arr1 = ['apple', '', 'banana', '', 'cherry']  
arr2 = ['', 'dog', '', 'cat', '']  
arr3 = ['hello', '', 'world', '', '']  
arr4 = ['', '', '', '', '']  
arr5 = ['one', '', 'two', '', 'three']  

def empty_str(num, arr):
    print(f'Output for arr {num} : \n')
    non_null_arr = list(filter(None, arr))
    
    print(f'List after removing empty strings: {non_null_arr}')

    print('\n End of empty str values')
empty_str(1, arr1)
empty_str(2, arr2)
empty_str(3, arr3)
empty_str(4, arr4)
empty_str(5, arr5)

    
print('\n End of empty str values')
print("---------------------------------------------------------")

print("Question 5")
# Write a function that takes in a list and prints the smallest value from that list.
def smallest_value_from_list(arr):
    if not arr:
        print("The list is empty.")
    else:
        smallest_value = min(arr)
        print(f"The smallest value in the list is: {smallest_value}")

# Example usage:
my_list = [10, 5, 8, 3, 12, 6]
smallest_value_from_list(my_list)
print("-------------------------------------------------------")



print("Task 2 (50 Points)")
# This task is divided into sub parts.

# Part 1: Bank Account Class
# 1. Create BankAccount class with following attributes and methods:
    # Attributes:
        # account_number: An integer.
        # balance: A float. 
        # account_holder: A string.
    # Methods:
        # deposit(self, amount): Adds the amount to current balance.
        # withdraw(self, amount): Subtracts the amount from current balance.
        # get_balance(self): Returns the current balance.
# call the BankAccount class by creating an instance of it and pass in the values.
# pass the balance as 1000, give a account number and account holder name  
# call deposit() method, withdraw() method by passing deposit amount as 200, withdraw amount as 700
# then print the total balance of the account (call the get_balance() method)
class BankAccount:
    def __init__(self, account_number, balance, account_holder):
        self.account_number = account_number
        self.balance = balance
        self.account_holder = account_holder

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. latest balance: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds. Withdrawal failed.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. latest balance: ${self.balance}")

    def get_balance(self):
        return self.balance
my_account = BankAccount(account_number=2013449604, balance=1000, account_holder="Nick")
my_account.deposit(200)
my_account.withdraw(700)
total_balance = my_account.get_balance()
print(f"Total balance: ${total_balance}")
print("--------------------------------------------------------")



print("Part 2: Checking Account Class")
# 1. Create CheckingAccount class that inherits from BankAccount
# 2. Add the following attributes and methods to the CheckingAccount class:
    # Attributes:
        # transaction_fees: A float, transaction fees charged for each transaction.
    # Methods:
        # apply_transaction_fees(self): Subtracts the transaction fees from current balance.
# call CheckingAccount class by creating an instance of it
# pass the transaction fees as 34.50 and call the apply_transaction_fees() method
# then print the total balance of the account (call the get_balance() method)
class CheckingAccount(BankAccount):
    def __init__(self, account_number, balance, account_holder, transaction_fees):
        super().__init__(account_number, balance, account_holder)
        self.transaction_fees = transaction_fees

    def apply_transaction_fees(self):
        self.balance -= self.transaction_fees
        print(f"Transaction fees applied. latest balance: ${self.balance}")
my_checking_account = CheckingAccount(account_number=2013449604, balance=1500, account_holder="Nick", transaction_fees=34.50)
my_checking_account.apply_transaction_fees()
total_balance_after_fees = my_checking_account.get_balance()
print(f"Total balance after transaction fees: ${total_balance_after_fees}")
print("------------------------------------------------------------------")




print("Part 3: Savings Account Class")
# 1. Create SavingsAccount class that inherits from BankAccount.
# 2. Add the following attributes and methods to the SavingsAccount class:
    # Attributes:
        # interest_rate: A float
    # Methods:
        # calculate_interest(self): Calculates and adds the interest to the current balance.
# call SavingsAccount class by creating an instance of it
# pass the interest rate as 0.12 and call the calculate_interest() method
# then print the total balance of the account (call the get_balance() method)
class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, account_holder, interest_rate):
        super().__init__(account_number, balance, account_holder)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest_got = self.balance * self.interest_rate
        self.balance += interest_got
        print(f"Interest earned: ${interest_got}. New balance: ${self.balance}")
my_savings_account = SavingsAccount(account_number=2013449604, balance=2000, account_holder="Nick", interest_rate=0.12)
my_savings_account.calculate_interest()
total_balance_including_interest = my_savings_account.get_balance()
print(f"Total balance with interest: ${total_balance_including_interest}")


class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited ₹{amount}. New balance:  ₹{self.__account_balance}")
        else:
            print("Invalid deposit amount. Amount must be greater than zero.")

    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            print(f"Withdrew  ₹{amount}. New balance: ₹{self.__account_balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def display_balance(self):
        print(f"Account Balance for {self.__account_holder_name} (Account #{self.__account_number}): ${self.__account_balance}")


# Testing the BankAccount class
if __name__ == "__main__":
    # Create an instance of BankAccount
    account = BankAccount("1234567890", "Dharani", 1000.0)

    # Display initial balance
    account.display_balance()

    # Deposit some money
    account.deposit(500.0)

    # Withdraw some money
    account.withdraw(200.0)

    # Display updated balance
    account.display_balance()
          
                
  
         
          


          
            
                  
            
            
            
          
          
          
          
        
        
        
      
      


print("Welcome to Standard Chartered Bank")

while True:
   print("\n1. Create Account")
   print("2. Biometric Verification")
   print("3. Initial Deposit")
   print("4. Withdrawal Amount")
   print("5. ATM")
   print("6. Deactivate Account")
   print("7. Exit")

   choice = input("\nEnter your choice: ")

   if choice == '1':
      print("Creating Account")

      # Input account information
      account_number = input("Enter account number: ")
      name = input("Enter your name: ")
      age = int(input("Enter your age: "))
      address = input("Enter your address: ")
      initial_deposit = float(input("Enter initial deposit amount: $"))

      # Print account information
      print("\nYour account is created.")
      print("Account Number:", account_number)
      print("Name:", name)
      print("Age:", age)
      print("Address:", address)
      print("Initial Deposit Amount: $", initial_deposit)

   elif choice == '2':
      print("\nBiometric Verification")
      class BiometricVerification:
         def __init__(self):
           self.registered_users = {}

         def register_user(self, username, pin):
           self.registered_users[username] = pin
           print(f"\nUser {username} registered successfully with PIN {pin}")
           
         def verify_user(self, username, entered_pin):
           if username in self.registered_users:
               if self.registered_users[username] == entered_pin:
                  print(f"Biometric verification of {username} successful.")
                       
                  return True
               else:
                  print(f"Biometric verification of {username} failed. Incorrect PIN.")
                  return False

           else:
               print(f"User {username} not found.")
               return False

      raining = BiometricVerification()
      raining.register_user("abdullah", "0404")
      raining.register_user("ahmed",    "0405")
      raining.register_user("ibraheem", "0406")
      username = input("\nEnter your username: ")
      pin = input("Enter your PIN: ")
      raining.verify_user(username, pin)
         
     
   elif choice == '3':
      print("\nInitial Deposit")
      class BankAccount:
        def __init__(self):
          self.balance = 0

        def deposite(self, amount):
          if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount} . \nNew balance: ${self.balance}")

          else:
            print("Deposit minimum 100 Euros.")
          
      account = BankAccount()
     
      while account.balance < 100:
        depo_euro = float(input("\ndeposit euros: "))
        account.deposite(depo_euro)
      
  
   elif choice == '4':
      print("Withdrawal Amount")

      class BankAccount1:
          def __init__(self):
              self.balance = 0

          def withdraw(self, amount):
              if self.balance >= amount > 0:
                  self.balance -= amount
                  print(f"Withdrawn ${amount}. \nNew balance: ${self.balance}")
              else:
                  print("Withdraw minimum 100 Euros.")

      account1 = BankAccount1()

      while account1.balance < 100:
          depo1_euro = float(input("\nDeposit euros: "))  # Convert input to float
          account1.balance += depo1_euro
          print(f"New balance: ${account1.balance}")

      while True:  
          wid_euro = float(input("\nWithdraw euros: "))
          if wid_euro > account1.balance:
              print("Insufficient funds.")
              break
          account1.withdraw(wid_euro)


  
   elif choice == '5':
      print("ATM")
      class ATM:
        daily_cash_limit = 100
        daily_withdrawal_limit = 500

        def __init__(self, card_num, balance, pin):
            self.card_num = card_num
            self.balance = balance
            self.pin = pin

        def balance_inquiry(self):
            print(f"card Number. {self.card_num}")
            print(f"Balance. {self.balance}")

        def withdraw(self, amount):
            if amount > self.balance:
              print("Insufficient funds.")
              return False

            if amount > self.daily_cash_limit:
           
              print("Exceeded daily cash limit.")
              return False

            if amount > self.daily_withdrawal_limit:
              print("Exceeded daily withdrawal limit.")
              return False

            self.balance -= amount
            print(f"Cash withdrawal:   ${amount}")
            print(f"Remaining Balance: ${self.balance}")
            print(f"Daily Cash Limit : ${self.daily_cash_limit - amount}")
            return True

      




        
   elif choice == '6':
      print("Deactivate Account")
      class User:
        def __init__(self):
            
            self.is_active = True

        def deactivate_temporarily(self):
            self.is_active = False
            print("Account deactivated temporarily.")

        def deactivate_permanently(self):
            self.is_active = False
            print("Account  deactivated permanently.")


      if __name__ == "__main__":
          # Create a User object
          user1 = User()


          # Ask the user for deactivation choice
          print("\nChoose deactivation option:")
          print("1. Deactivate account temporarily")
          print("2. Deactivate account permanently")
          choice = input("\nEnter your choice: ")
  
          # Deactivate account based on user's choice
          if choice == '1':
              user1.deactivate_temporarily()
          elif choice == '2':
              user1.deactivate_permanently()
          else:
              print("Invalid choice ")


   elif choice == '7':
      print("Exit")
      print("Thanks for using Standard Chartered Bank")
      print("Have a nice day")
      

      break
   else:
      print("Invalid choice. Please try again.")
   break

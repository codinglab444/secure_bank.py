# secure_bank.py
class Bank:
  def __init__(self, name, account_no, account_password, balance=0):
    self.name = name
    self.account_no = account_no
    self.__account_password = str(account_password)
    self.balance = balance
    if self.balance < 0 or not(isinstance(balance, (int, float))):
      self.balance = 0
      print(f"Invalid Balance! Resetting Balance : {self.balance}\n")
  def show_passbook(self):
    print("---Pass Book---")
    print(f"Costmer ID : {self}")
    print(f"Name : {self.name}")
    print(f"Account No : {self.account_no}\n")
  def credit(self, account_no, amount):
    if self.account_no == account_no:
      if amount > 0 and isinstance(amount, (int, float)):
        self.balance += amount
        print(f"Credit Amount : {amount}\nCurrent Balance : {self.balance}")
        if self.balance >= 10000000:
          print("VIP Card Activated.")
      else:
        print("Invalid Amount! No Credit.")
    else:
      print("Account Not Found.")
  def debit(self, account_no, account_password, amount):
    if self.account_no == account_no:
      for el in range(5):
        if self.__account_password == str(account_password):
          if amount > 0 and self.balance >= amount and isinstance(amount, (int, float)):
            self.balance -= amount
            print(f"Debit Amount : {amount}\nCurrent Balance : {self.balance}")
          else:
            print("Invalid Amount! No Debit.")
          break
        else:
          if el < 4:
            print("Incorrect Password")
            account_password = input(f"Attempt left : ({4 - el}) Try Agian : ")
          else:
            print("5 Attempts Incorrect Password")
            print("Incorrect Password! No Debit. Account Locked.")
    else:
      print("Account Not Found.")


#use class
costmer1 = Bank("usename", 1234, 1111, 5000)
costmer1.show_passbook()
costmer1.credit(1234, 2000)
costmer1.debit(1234, 1111, 4000)
costmer1.credit(1234, 10000000)

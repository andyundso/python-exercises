import datetime


# taken from http://www.discoversdk.com/blog/working-with-class-and-method-decorators-in-python
# I have 0 clue how this works
def account_must_be_open(method):
    def method_wrapper(self, *args, **kwargs):
        if self._active:
            method(self, *args, **kwargs)
        else:
            print("The bank account is closed, so you can't modify it!")

    return method_wrapper


class BankAccount(object):
    # properties
    _active: bool = True
    _balance: float = 0
    _currency: str = "Dollar"
    _interest: float = 0.0
    _first_name: str = ""
    _last_name: str = ""

    @property
    def active(self):
        return self._active

    @property
    def currency(self):
        return self._currency

    @currency.setter
    @account_must_be_open
    def currency(self, currency):
        if isinstance(currency, str):
            self._currency = currency
        else:
            print("The currency needs to be a string!")

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    @account_must_be_open
    def first_name(self, first_name):
        if isinstance(first_name, str):
            self._first_name = first_name
        else:
            print("The name needs to be a string!")

    @property
    def interest(self):
        return self._interest

    @interest.setter
    @account_must_be_open
    def interest(self, interest: float):
        self._interest = interest
        print("Interest of this bank account successfully set to " + str(self._interest))

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    @account_must_be_open
    def last_name(self, last_name):
        if isinstance(last_name, str):
            self._last_name = last_name
        else:
            print("The name needs to be a string!")

    # public methods
    def close_account(self):
        self._active = False
        print("The bank account is now closed!")

    @account_must_be_open
    def deposit_money(self, money: float):
        if 100000 < self._balance + money:
            print("You cannot store more than 100'000 in your account.")
        else:
            self._balance = self._balance + money
            print("You successfully deposited " + str(money) + "!")
        self.show_balance()

    def open_account(self):
        self._active = True
        print("The bank account is now active!")

    def show_balance(self):
        print("Your balance is currently " + str(self._balance) + " " + self._currency)

    @account_must_be_open
    def withdraw_money(self, money: float):
        if 0 > self._balance - money:
            print("You dont have enough money in your account.")
        else:
            self._balance = self._balance - money
            print("You successfully withdrawed " + str(money) + "!")
        self.show_balance()


class SavingAccount(BankAccount):
    def __init__(self):
        super().__init__()
        self.interest = 0.01

    @account_must_be_open
    def withdraw_money(self, money: float):
        if 0 > self._balance - money:
            print("Attention, you don't have enough money on your bank account, so this withdraw will cost more!")
            self._balance = self._balance - (money * 1.02)
        else:
            self._balance = self._balance - money
        self.show_balance()


class YouthAccount(BankAccount):
    def __init__(self, year: int, month: int, day: int):
        #  verify that nobody above the age of 25 can open an account
        todays_date = datetime.datetime.now().date()
        birth_date = datetime.date(year, month, day)

        if int((todays_date - birth_date).days / 365.25) > 25:
            print("Sorry, you're too old to open a youth account")
        else:
            super().__init__()
            self.interest = 0.05

    @account_must_be_open
    def withdraw_money(self, money: float):
        if money > 2000:
            print("Sorry, you can only withdraw an amount below 2000")
        else:
            super().withdraw_money(money)


# test normal account
account = BankAccount()
account.first_name = "Andy"
print(account.first_name)
account.last_name = "Pfister"
print(account.last_name)
account.close_account()
print(account.active)
account.open_account()
print(account.active)
account.deposit_money(3500)
account.show_balance()
account.withdraw_money(3000)

# test saving account
saving_account = SavingAccount()
saving_account.withdraw_money(3500)
saving_account.interest = 0.03

# test youth account
youth_account = YouthAccount(2000, 10, 8)

# test somebody who's too old for a youth account
invalid_youth_account = YouthAccount(1989, 12, 24)

# check withdraw restriction
#  this should give a message about "you don't have this much money"
youth_account.withdraw_money(1500)
youth_account.deposit_money(5000)

#  this should give a message about "thats too much money you want to withdraw"
youth_account.withdraw_money(2500)

#  this one should work tho
youth_account.withdraw_money(1500)

# lets test both the saving and the youth account a bit more
better_youth_account = YouthAccount(2000, 10, 8)
better_youth_account.first_name = "Andy"
print(better_youth_account.first_name)
better_youth_account.last_name = "Pfister"
print(better_youth_account.last_name)
better_youth_account.currency = "Swiss francs"
print(better_youth_account.currency)
better_youth_account.deposit_money(3500)
better_youth_account.show_balance()
better_youth_account.withdraw_money(3000)

# try to do something when the account is closed
#  should give an error message each time
better_youth_account.close_account()
better_youth_account.show_balance()
better_youth_account.deposit_money(3500)
better_youth_account.withdraw_money(3500)
better_youth_account.open_account()
better_youth_account.deposit_money(3500)

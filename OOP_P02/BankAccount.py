class BankAccount(object):
    # decorator
    def account_must_be_open(method):
        def method_wrapper(self, *args, **kwargs):
            if self._active:
                method(self, *args, **kwargs)
            else:
                print("The bank account is closed, so you can't modify it!")

        return method_wrapper

    # properties
    _active: bool = True
    _balance: float = 0
    _currency: str = "Dollar"
    _first_name: str = ""
    _last_name: str = ""

    @property
    def active(self):
        return self._active

    @property
    def currency(self):
        return self._currency

    @currency.setter
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


account = BankAccount()
account.first_name = "Andy"
print(account.first_name)
account.last_name = "Pfister"
print(account.last_name)
print(account.active)
print(account.active)
account.open_account()
print(account.active)
account.deposit_money(3500)
account.show_balance()
account.withdraw_money(3000)

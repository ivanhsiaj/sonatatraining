class Account:
    def __init__(self,accountnum,name,type,balance):
        self.accno=accountnum
        self.name=name
        self.type=type
        self.balance=balance
    def display(self):
        return self.accountnum + self.name + self.type + self.balance
from typing import List


class Account:
    def __init__(self, owner: str, amount: int = 0):
        self.owner = owner
        self.amount = amount
        self._transactions: List[float] = []

    @property
    def balance(self):
        return sum(self._transactions) + self.amount

    def handle_transaction(self, transaction_amount):
        if self.balance + transaction_amount < 0:
            raise ValueError("sorry cannot go in debt!")

        self._transactions.append(transaction_amount)
        return f"New balance: {self.balance}"

    def add_transaction(self, amount: int):
        if not isinstance(amount, int):
            raise ValueError("please use int for amount")
        return self.handle_transaction(amount)

    # magic methods
    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.amount}"

    def __repr__(self):
        return f"Account({self.owner}, {self.amount})"

    # връщаме дължината на списъка
    def __len__(self):
        return len(self._transactions)

    # трябва да итерираме през списъка, като получаваме всяка трансакция като резултат
    # за целта в инпут данните се пише for transaction in acc: \n print(transaction)
    # тоест трябва да му се подават неща по индекс
    def __getitem__(self, idx):
        return self._transactions[idx]

    # ревърсваме списъка
    # за целта в инпут данните се пише print(list(reversed(acc)))
    def __reversed__(self):
        return self._transactions[::-1] # може и с return reversed(self._transactions)

    def __gt__(self, other): # щом сме написали условието за >, автоматично имаме и за <. Те връщат True или False
        return self.amount > other.amount

    def __ge__(self, other):
        return self.balance >= other.balance

    def __eq__(self, other):
        return self.balance == other.balance

    def __add__(self, other): #подава ни се: acc3 = acc + acc2; print(acc3); print(acc3._transactions)
        new_account = Account(f"{self.owner}&{other.owner}", self.amount + other.amount)
        new_account._transactions = self._transactions + other._transactions
        return new_account


acc = Account('bob', 10)
acc2 = Account('john')
print(acc)
print(repr(acc))
acc.add_transaction(20)
acc.add_transaction(-20)
acc.add_transaction(30)
print(acc.balance)
print(len(acc))
for transaction in acc:
    print(transaction)
print(acc[1])
print(list(reversed(acc)))
acc2.add_transaction(10)
acc2.add_transaction(60)
print(acc > acc2)
print(acc >= acc2)
print(acc < acc2)
print(acc <= acc2)
print(acc == acc2)
print(acc != acc2)
acc3 = acc + acc2
print(acc3)
print(acc3._transactions)





from UserDetails.user import userDetails


class Transactions:
    def __init__(self, username: str):
        self.username: str = username
        self.balance: float = userDetails["AccountNumber"][username]["Balance"]

    def withdrawal(self, value) -> float:
        """
        This handles the withdrawal from a account and updates the new account balance.
        :param value:
        :return: The new account balance
        """
        amount: float = self.balance - value
        userDetails["AccountNumber"][self.username]["Balance"] = amount
        return amount

    def deposit(self, value) -> float:
        """
        This handles the deposting of money into the account and updates the new account balance.
        :param value:
        :return:
        """
        amount: float = self.balance + value
        userDetails["AccountNumber"][self.username]["Balance"] = amount
        return amount

    def getBalance(self) -> float:
        return self.balance

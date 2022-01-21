from typing import *
expense: Dict[str, Dict] = {
    "AccountNumber":
        {
            "000243":
                {
                    "Phone": 5000.00
                    "House": 15000.00
                    "Car": 30000:00
                    "Balance": 3000.00
                },
            "0000324":
                {
                    "Phone": 25000:00
                    "House": 13000:00
                    "Car": 40000:00
                    "Balance": 250.00
                }
        }
}


class Expense:
    def __init__(self, acctNo):
        self.acctNo = acctNo

    def getPhone(self):
        return userDetails["AccountNumber"][self.acctNo]["Phone"]
    def getHouse(self):
        return userDetails["AccountNumber"][self.acctNo]["House"]
    def getCar(self):
        return userDetails["AccountNumber"][self.acctNo]["Car"]
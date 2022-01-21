from typing import *

userDetails: Dict[str, Dict] = {
    "AccountNumber":
        {
            "0000":
                {
                    "Firstname": "Tom",
                    "Lastname": "Phil",
                    "Password": "0000",
                    "Balance": 3000.00
                },
            "0000324":
                {
                    "Firstname": "John",
                    "Lastname": "Ogunyale",
                    "Password": "!@#@%^#",
                    "Balance": 250.00
                }
        }
}


class User:
    def __init__(self, acctNo):
        self.acctNo = acctNo

    def getFirstname(self):
        """
        This returns the First name of the account holder
        :return:
        """
        return userDetails["AccountNumber"][self.acctNo]["Firstname"]

    def getLastName(self):
        """
        This returns the last name of the account holder
        :return:
        """
        return userDetails["AccountNumber"][self.acctNo]["Lastname"]

    def getBalance(self):
        """
        This returns the balance of the account holder
        :return:
        """
        return userDetails["AccountNumber"][self.acctNo]["Balance"]

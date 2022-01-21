from UserDetails.user import userDetails


class Authentication:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    def login(self) -> str:
        """
        This method checks if the username and password is an accepted combination.
        :return:
        """
        if self.username in userDetails["AccountNumber"]:
            if self.password == userDetails["AccountNumber"][self.username]["Password"]:
                return "OK"
            else:
                return "FAIL"
        else:
            return "FAIL"

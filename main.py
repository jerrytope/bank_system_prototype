import streamlit as st
from Authentication.auth import Authentication
from UserDetails.user import User
#import expenses.Expense
from Transactions.transactions import Transactions
import time
from PIL import Image



def login(accountNumber: str, pin: str):
    """
    The method handles the login process. It gets the account number and pin and makes a call to the authentication
    class to handle if the account number and pin has been saved.
    :param accountNumber:
    :param pin:
    :return:
    """
    auth: Authentication = Authentication(accountNumber, pin)

    if auth.login() == "OK":
        st.sidebar.success("Successfully logged In")
        user: User = User(accountNumber)
        st.write(f"## Welcome {user.getFirstname()} {user.getLastName()}")
        accountDetails(accountNumber)

    else:
        st.sidebar.error("Username or Password Incorrect")


def initiateLogin():
    """
    Handles the input of the account number and the name
    :return:
    """
    accountNumber: str = st.sidebar.text_input(label="Account Number")
    pin: str = st.sidebar.text_input(label="Pin", type="password")
    login(accountNumber, pin)


def accountDetails(accountNumber):
    """
    This uses the account details to get the current account balance and in turn uses this information to handle
    :param accountNumber: float
    :return:
    """
    accountBalance: Transactions = Transactions(accountNumber)
    currentBalance: float = accountBalance.getBalance()
    st.write(f"### Your Account Balance is ${currentBalance}")
    choices = st.selectbox("Which Action do you want to perform? ", ("Withdrawal", "Deposit", "expense"))

    if choices == "Deposit":
        amount: float = st.number_input("How much do you want to deposit?", min_value=0.00,
                                        max_value=10000000000000.000000)
        currentBalance: float = accountBalance.deposit(amount)
        st.write(f" ${amount} was deposited to you account and your new account balance is {currentBalance}")

    elif choices == "Withdrawal":
        amount: float = st.number_input("How much do you want to withdraw?", min_value=0.00, max_value=currentBalance)
        currentBalance: float = accountBalance.withdrawal(amount)
        st.write(f"${amount} was withdrawn from you account and your new account balance is ${currentBalance}")
""""
    elif choices == "expense":
        expense = st.selectbox("check your expenses ", ("amount_withdraw", "amount_deposited"))
        if expense == "amount_withdraw":
            user: User = User(accountNumber)
            expense: Expense = Expense(accountNumber)
            st.write(f"## Welcome to your database{user.getFirstname()} {user.getLastName()}")
            st.write(f"## you withdrawal the sum of {expense.getPhone()} to pruchase a phone")
            #st.write(f"## you withdrawal the sum of {expense.getHouse()} to pruchase a phone")
            

    return currentBalance

"""
def homeScreenPage():
    st.write("# *ABM Banking System*")
    image = Image.open("bank.jpeg")
    st.image(image, caption='Welcome to ABM')


homeScreenPage()
initiateLogin()

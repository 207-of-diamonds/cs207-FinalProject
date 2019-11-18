'''
This file contains a number of unit tests
to confirm proper errors and behavior during our Bitter Dispute.

Unit tests include:
- test_
'''

# Import necessary module
from forward_mode import AD

def test_massive_values():
    '''
    Test for handling overly large input values or derived values during operations
    Formula: sin(x*y*z)**tanh(z)
    Values:
        z = 4.6
        y = 9.2
        x = 5.0
    Error: RuntimeWarning: invalid value encountered in log
    Returns nan - TODO Should we handle this or change error message?
    Reference: https://stackoverflow.com/questions/27784528/numpy-division-with-runtimewarning-invalid-value-encountered-in-double-scalars
    '''
    # test = AD();
    pass







    user.addAccount(AccountType.SAVINGS);
    user.deposit(AccountType.SAVINGS, 100000);
    try:
        print("Scenario: Attempting to withdraw more money than is in my account")
        user.withdraw(AccountType.SAVINGS, 500000);
    except Exception as e:
        print(e)

def test_negative_withdrawal():
    '''
    Test for proper error in case of attempt at negative withdrawal
    '''
    user = BankUser("Will");
    user.addAccount(AccountType.SAVINGS);
    user.deposit(AccountType.SAVINGS, 100000);
    try:
        print("Scenario: Attempting to withdraw a negative amount of money")
        user.withdraw(AccountType.SAVINGS, -500000);
    except Exception as e:
        print(e)

def test_negative_deposit():
    '''
    Test for proper error in case of attempt at negative deposit
    '''
    user = BankUser("Will");
    user.addAccount(AccountType.SAVINGS);
    try:
        print("Scenario: Attempting to deposit a negative amount of money")
        user.deposit(AccountType.SAVINGS, -500000);
    except Exception as e:
        print(e)

def test_multiple_accounts_savings():
    '''
    Test for proper error in case of creation of more than one Savings account
    '''
    user = BankUser("Will")
    user.addAccount(AccountType.SAVINGS);
    try:
        print("Scenario: Attempting to create a second Savings account")
        user.addAccount(AccountType.SAVINGS);
    except Exception as e:
        print(e)

def test_multiple_accounts_checking():
    '''
    Test for proper error in case of creation of more than one Checking account
    '''
    user = BankUser("Will")
    user.addAccount(AccountType.CHECKING);
    try:
        print("Scenario: Attempting to create a second Savings account")
        user.addAccount(AccountType.CHECKING);
    except Exception as e:
        print(e)

def test_missing_account_get_balance():
    '''
    Test for proper error in case of missing account for selected account: getBalance
    '''
    user = BankUser("Will")
    user.addAccount(AccountType.CHECKING);
    try:
        print("Scenario: Attempting to get balance from a non-existent Savings account")
        user.getBalance(AccountType.SAVINGS)
    except Exception as e:
        print(e)

def test_missing_account_deposit():
    '''
    Test for proper error in case of missing account for selected account: deposit
    '''
    user = BankUser("Will")
    user.addAccount(AccountType.SAVINGS);
    try:
        print("Scenario: Attempting to deposit into a non-existent Savings account")
        user.deposit(AccountType.CHECKING, 5.0)
    except Exception as e:
        print(e)

def test_missing_account_withdraw():
    '''
    Test for proper error in case of missing account for selected account: withdraw
    '''
    user = BankUser("Will")
    user.addAccount(AccountType.CHECKING);
    try:
        print("Scenario: Attempting to withdraw from a non-existent Savings account")
        user.withdraw(AccountType.SAVINGS, 5.0)
    except Exception as e:
        print(e)

# Run all unit tests
test_over_withdrawal();
test_negative_deposit();
test_negative_withdrawal();
test_multiple_accounts_savings();
test_multiple_accounts_checking();
test_missing_account_get_balance();
test_missing_account_deposit();
test_missing_account_withdraw();

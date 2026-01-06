#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  1 20:34:15 2025

@author: rupertjwebb
"""

class BankAccount:
    '''represents a bank account'''

    def __init__(self, accountNum, bal):
        '''BankAccount(accountNum, bal) -> BankAccount
        creates a new bank account with the given account
          number and balance'''
        self.actNum = accountNum
        self.balance = bal

    def __str__(self):
        '''str(BankAccount) -> str'''
        return 'Account #{} with balance ${:.2f}'.format(self.actNum, self.balance)

    def check_funds(self, amt):
        '''BankAccount.check_funds(amt) -> boolean
        returns True if the balance is at least amt, False otherwise
        prints warning message if not enough funds'''
        if amt > self.balance:
            print('Not enough funds!')
            return False
        return True

    def deposit(self, amt):
        '''BankAcount.deposit(amt)
        adds amt to balance of account'''
        self.balance += amt

    def withdraw(self, amt):
        '''BankAccount.withdraw(amt)
        remove amt from balance of account
        does nothing and prints warning if insufficient funds'''
        if self.check_funds(amt):
            self.balance -= amt

    def transfer(self, other, amt):
        '''BankAccount.transfer(other, amt)
        transfers amt from account to other account
        does nothing and prints warning if insufficient funds'''
        if self.check_funds(amt):
            self.withdraw(amt)
            other.deposit(amt)

class CheckingAccount(BankAccount):
    '''represents a checking account'''

    def __init__(self, accountNum, bal):
        '''CheckingAccount(accountNum, bal) -> CheckingAccount
        creates a new checking account with the given account
          number and balance'''
        BankAccount.__init__(self, accountNum, bal)
        self.checks = {}

    def __str__(self):
        '''str(CheckingAccount) -> str'''
        return 'Checking ' + BankAccount.__str__(self)

    def write_check(self, checkNum, payee, amt):
        '''CheckingAccount.write_check(checkNum, payee, amt)
        writes a check numbered checkNum to payee for amt
        prints an error message if the checkNum is already used
          or if insufficient funds'''
        if checkNum in self.checks:
            print('Check #' + str(checkNum) + ' is already used!')
        elif self.check_funds(amt):
            self.checks[checkNum] = (payee, amt)
            self.withdraw(amt)

    def print_checks(self):
        '''CheckingAccount.print_checks()
        print the list of checks'''
        checksString = ''
        checkNumList = list(self.checks.keys())
        checkNumList.sort()
        for check in checkNumList:
            checksString += 'Check #{} to {}: ${:.2f}\n'.format(check, \
                            self.checks[check][0], self.checks[check][1])
        return checksString

class SavingsAccount(BankAccount):
    '''represents a savings account'''

    def __init__(self, accountNum, bal, intrate):
        '''SavingsAccount(accountNum, bal, intrate) -> SavingsAccount
        creates a new savings account with the given account
          number, balance, and interest rate.'''
        BankAccount.__init__(self, accountNum, bal)
        self.interestRate = intrate

    def __str__(self):
        '''str(SavingsAccount) -> str'''
        return 'Savings ' + BankAccount.__str__(self)

    def earn_interest(self):
        '''SavingsAccount.earn_interest(self)
        adds interest to account'''
        self.balance += (self.balance * self.interestRate)

# tests
c = CheckingAccount(1234, 1000)
s = SavingsAccount(5678, 2000, 0.02)
c.write_check(100, 'Dave', 75)
c.write_check(102, 'Tina', 110)
c.transfer(s, 200)
print(c)
print(c.print_checks())
print(s)
s.earn_interest()
print(s)
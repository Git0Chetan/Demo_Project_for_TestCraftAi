import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Service import *


def test_create_customer():
    bank = BankService()
    customer = bank.create_customer("John Doe", "john.doe@example.com")
    assert customer.id == "CUST-1"
    assert customer.name == "John Doe"
    assert customer.email == "john.doe@example.com"
    assert customer.id in bank._customers

def test_create_customer_duplicate_email():
    bank = BankService()
    bank.create_customer("John Doe", "john.doe@example.com")
    with pytest.raises(Exception) as e:
        bank.create_customer("Jane Doe", "john.doe@example.com")


def test_create_account_checking():
    bank = BankService()
    customer = bank.create_customer("John Doe", "john.doe@example.com")
    account = bank.create_account(customer)
    assert account.id == "ACC-1"
    assert account.customer == customer
    assert isinstance(account, CheckingAccount)
    assert account.balance == 0.0
    assert account.id in bank._accounts

def test_create_account_savings():
    bank = BankService()
    customer = bank.create_customer("John Doe", "john.doe@example.com")
    account = bank.create_account(customer, account_type="savings", initial_balance=100.0)
    assert account.id == "ACC-1"
    assert account.customer == customer
    assert isinstance(account, SavingsAccount)
    assert account.balance == 100.0
    assert account.interest_rate == 0.02
    assert account.id in bank._accounts

def test_get_account():
    bank = BankService()
    customer = bank.create_customer("John Doe", "john.doe@example.com")
    account = bank.create_account(customer)
    retrieved_account = bank.get_account(account.id)
    assert retrieved_account == account
    assert bank.get_account("nonexistent_id") is None

def test_deposit():
    bank = BankService()
    customer = bank.create_customer("John Doe", "john.doe@example.com")
    account = bank.create_account(customer, initial_balance=100.0)
    new_balance = bank.deposit(account.id, 50.0)
    assert new_balance == 150.0
    assert account.balance == 150.0

def test_deposit_nonexistent_account():
    bank = BankService()
    with pytest.raises(ValueError) as e:
        bank.deposit("nonexistent_id", 50.0)
    assert "Account nonexistent_id not found." in str(e.value)

def test_withdraw():
    bank = BankService()
    customer = bank.create_customer("John Doe", "john.doe@example.com")
    account = bank.create_account(customer, initial_balance=100.0)
    new_balance = bank.withdraw(account.id, 25.0)
    assert new_balance == 75.0
    assert account.balance == 75.0

def test_withdraw_overdraft():
    bank = BankService()
    customer = bank.create_customer("John Doe", "john.doe@example.com")
    account = bank.create_account(customer, initial_balance=100.0)
    with pytest.raises(ValueError) as e:
        account.withdraw(150.0)
    assert "Insufficient funds" in str(e.value)


def test_withdraw_nonexistent_account():
    bank = BankService()
    with pytest.raises(ValueError) as e:
        bank.withdraw("nonexistent_id", 50.0)
    assert "Account nonexistent_id not found." in str(e.value)

def test_transfer():
    bank = BankService()
    customer1 = bank.create_customer("John Doe", "john.doe@example.com")
    customer2 = bank.create_customer("Jane Doe", "jane.doe@example.com")
    account1 = bank.create_account(customer1, initial_balance=100.0)
    account2 = bank.create_account(customer2, initial_balance=50.0)
    bank.transfer(account1.id, account2.id, 25.0)
    assert account1.balance == 75.0
    assert account2.balance == 75.0

def test_transfer_insufficient_funds():
    bank = BankService()
    customer1 = bank.create_customer("John Doe", "john.doe@example.com")
    customer2 = bank.create_customer("Jane Doe", "jane.doe@example.com")
    account1 = bank.create_account(customer1, initial_balance=100.0)
    account2 = bank.create_account(customer2, initial_balance=50.0)
    with pytest.raises(ValueError) as e:
        bank.transfer(account1.id, account2.id, 150.0)
    assert "Insufficient funds" in str(e.value)

def test_transfer_nonexistent_account():
    bank = BankService()
    with pytest.raises(ValueError) as e:
        bank.transfer("nonexistent_id1", "nonexistent_id2", 50.0)
    assert "One or both accounts not found." in str(e.value)

def test_transfer_negative_amount():
    bank = BankService()
    with pytest.raises(ValueError) as e:
        bank.transfer("acc1", "acc2", -50.0)
    assert "Transfer amount must be positive." in str(e.value)


def test_list_accounts_for_customer():
    bank = BankService()
    customer = bank.create_customer("John Doe", "john.doe@example.com")
    account1 = bank.create_account(customer)
    account2 = bank.create_account(customer, account_type="savings")
    accounts = bank.list_accounts_for_customer(customer.id)
    assert len(accounts) == 2
    assert account1.id in accounts
    assert account2.id in accounts

def test_list_accounts_for_nonexistent_customer():
    bank = BankService()
    accounts = bank.list_accounts_for_customer("nonexistent_id")
    assert len(accounts) == 0

def test_get_customer():
    bank = BankService()
    customer = bank.create_customer("John Doe", "john.doe@example.com")
    retrieved_customer = bank.get_customer(customer.id)
    assert retrieved_customer == customer
    assert bank.get_customer("nonexistent_id") is None

# tests/test_bank_service.py

import pytest

from service import BankService
from account import Customer, CheckingAccount, SavingsAccount, Account


def test_create_customer_and_get_customer():
    bs = BankService()
    customer = bs.create_customer("Alice", "alice@example.com")

    assert isinstance(customer, Customer)
    assert customer.name == "Alice"
    assert customer.email == "alice@example.com"

    # get_customer should return the same object
    retrieved = bs.get_customer(customer.id)
    assert retrieved is customer


def test_create_accounts():
    bs = BankService()
    customer = bs.create_customer("Bob", "bob@example.com")

    acc_check = bs.create_account(customer, account_type="checking", initial_balance=100.0)
    assert isinstance(acc_check, CheckingAccount)
    assert acc_check.balance == 100.0
    assert acc_check.customer is customer

    acc_sav = bs.create_account(customer, account_type="savings", initial_balance=50.0)
    assert isinstance(acc_sav, SavingsAccount)
    assert acc_sav.balance == 50.0
    assert acc_sav.customer is customer

    # IDs should be in expected format
    assert acc_check.id.startswith("ACC-")
    assert acc_sav.id.startswith("ACC-")

    # list_accounts_for_customer should include both accounts
    accounts = bs.list_accounts_for_customer(customer.id)
    assert acc_check.id in accounts
    assert acc_sav.id in accounts


def test_deposit_withdraw_and_get_account():
    bs = BankService()
    customer = bs.create_customer("Charlie", "charlie@example.com")
    acc = bs.create_account(customer, "checking", 0.0)

    # Deposit
    new_bal = bs.deposit(acc.id, 200.0)
    assert new_bal == 200.0
    assert acc.balance == 200.0

    # Withdraw
    new_bal = bs.withdraw(acc.id, 50.0)
    assert new_bal == 150.0
    assert acc.balance == 150.0

    # get_account should return the same object
    got = bs.get_account(acc.id)
    assert got is acc


def test_transfer():
    bs = BankService()
    c1 = bs.create_customer("Dave", "dave@example.com")
    c2 = bs.create_customer("Eve", "eve@example.com")

    a1 = bs.create_account(c1, "checking", 100.0)
    a2 = bs.create_account(c2, "checking", 50.0)

    transferred = bs.transfer(a1.id, a2.id, 30.0)
    assert transferred == 30.0

    assert a1.balance == 70.0
    assert a2.balance == 80.0


def test_transfer_validation_and_errors():
    bs = BankService()
    c = bs.create_customer("Frank", "frank@example.com")
    a = bs.create_account(c, "checking", 10.0)

    # Negative transfer amount
    with pytest.raises(ValueError):
        bs.transfer(a.id, a.id, -5.0)

    # Zero transfer amount
    with pytest.raises(ValueError):
        bs.transfer(a.id, a.id, 0.0)

    # Missing accounts
    with pytest.raises(ValueError):
        bs.transfer("NONEXIST", a.id, 5.0)

    with pytest.raises(ValueError):
        bs.transfer(a.id, "NONEXIST", 5.0)


def test_deposit_and_withdraw_errors():
    bs = BankService()

    # Deposit to non-existent account
    with pytest.raises(ValueError):
        bs.deposit("NONEXIST", 10.0)

    # Withdraw from non-existent account
    with pytest.raises(ValueError):
        bs.withdraw("NONEXIST", 5.0)

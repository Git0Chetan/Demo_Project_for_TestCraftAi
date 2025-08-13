# services.py
# Bank service to manage customers and accounts (in-memory)

import os
from typing import Dict, Optional
from account import Customer, CheckingAccount, SavingsAccount, Account

class BankService:
    def __init__(self):
        self._customers: Dict[str, Customer] = {}
        self._accounts: Dict[str, Account] = {}
        # Demonstration: load a sensitive token from environment (not used in this in-memory example)
        self._api_token = os.environ.get("BANK_API_TOKEN")
        # If token is not provided, we simply proceed (no credentials used here)

    def _generate_customer_id(self) -> str:
        return f"CUST-{len(self._customers) + 1}"

    def _generate_account_id(self) -> str:
        return f"ACC-{len(self._accounts) + 1}"

    def create_customer(self, name: str, email: str) -> Customer:
        customer_id = self._generate_customer_id()
        customer = Customer(id=customer_id, name=name, email=email)
        self._customers[customer_id] = customer
        return customer

    def create_account(self, customer: Customer, account_type: str = "checking", initial_balance: float = 0.0) -> Account:
        account_id = self._generate_account_id()
        if account_type.lower() == "savings":
            account = SavingsAccount(account_id, customer, balance=initial_balance, interest_rate=0.02)
        else:
            account = CheckingAccount(account_id, customer, balance=initial_balance)
        self._accounts[account_id] = account
        return account

    def get_account(self, account_id: str) -> Optional[Account]:
        return self._accounts.get(account_id)

    def deposit(self, account_id: str, amount: float) -> float:
        account = self.get_account(account_id)
        if account is None:
            raise ValueError(f"Account {account_id} not found.")
        return account.deposit(amount)

    def withdraw(self, account_id: str, amount: float) -> float:
        account = self.get_account(account_id)
        if account is None:
            raise ValueError(f"Account {account_id} not found.")
        return account.withdraw(amount)

    def transfer(self, from_account_id: str, to_account_id: str, amount: float) -> float:
        if amount <= 0:
            raise ValueError("Transfer amount must be positive.")
        from_acc = self.get_account(from_account_id)
        to_acc = self.get_account(to_account_id)
        if from_acc is None or to_acc is None:
            raise ValueError("One or both accounts not found.")
        from_acc.withdraw(amount)
        to_acc.deposit(amount)
        return amount

    def list_accounts_for_customer(self, customer_id: str) -> Dict[str, Account]:
        return {acc_id: acc for acc_id, acc in self._accounts.items() if acc.customer.id == customer_id}

    def get_customer(self, customer_id: str) -> Optional[Customer]:
        return self._customers.get(customer_id)
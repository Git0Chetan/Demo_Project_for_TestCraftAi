import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from payment2 import *


import pytest
import datetime
from wallet_system import Wallet

class TestWalletClass:
    def test_add_funds_valid_amount(self):
        wallet = Wallet("Test", "123")
        wallet.add_funds(100)
        assert wallet.balance == 100
        assert len(wallet.transaction_history) == 1
        assert wallet.transaction_history[0]['type'] == 'Credit'

    def test_add_funds_invalid_amount(self):
        wallet = Wallet("Test", "123")
        wallet.add_funds(-100)
        assert wallet.balance == 0
        assert len(wallet.transaction_history) == 0

    def test_add_funds_zero_amount(self):
        wallet = Wallet("Test", "123")
        wallet.add_funds(0)
        assert wallet.balance == 0
        assert len(wallet.transaction_history) == 0

    def test_deduct_funds_valid_amount(self):
        wallet = Wallet("Test", "123")
        wallet.add_funds(100)
        wallet.deduct_funds(50)
        assert wallet.balance == 50
        assert len(wallet.transaction_history) == 2
        assert wallet.transaction_history[1]['type'] == 'Debit'

    def test_deduct_funds_insufficient_funds(self):
        wallet = Wallet("Test", "123")
        wallet.add_funds(100)
        wallet.deduct_funds(150)
        assert wallet.balance == 100
        assert len(wallet.transaction_history) == 1

    def test_deduct_funds_invalid_amount(self):
        wallet = Wallet("Test", "123")
        wallet.add_funds(100)
        wallet.deduct_funds(-50)
        assert wallet.balance == 100
        assert len(wallet.transaction_history) == 1

    def test_deduct_funds_zero_amount(self):
        wallet = Wallet("Test", "123")
        wallet.add_funds(100)
        wallet.deduct_funds(0)
        assert wallet.balance == 100
        assert len(wallet.transaction_history) == 1


    def test_transfer_funds_valid(self):
        wallet1 = Wallet("Alice", "1")
        wallet2 = Wallet("Bob", "2")
        wallet1.add_funds(100)
        wallet1.transfer_funds(wallet2, 50)
        assert wallet1.balance == 50
        assert wallet2.balance == 50
        assert len(wallet1.transaction_history) == 2
        assert len(wallet2.transaction_history) == 2


    def test_transfer_funds_insufficient_funds(self):
        wallet1 = Wallet("Alice", "1")
        wallet2 = Wallet("Bob", "2")
        wallet1.add_funds(100)
        wallet1.transfer_funds(wallet2, 150)
        assert wallet1.balance == 100
        assert wallet2.balance == 0
        assert len(wallet1.transaction_history) == 1
        assert len(wallet2.transaction_history) == 0

    def test_transfer_funds_invalid_amount(self):
        wallet1 = Wallet("Alice", "1")
        wallet2 = Wallet("Bob", "2")
        wallet1.add_funds(100)
        wallet1.transfer_funds(wallet2, -50)
        assert wallet1.balance == 100
        assert wallet2.balance == 0
        assert len(wallet1.transaction_history) == 1
        assert len(wallet2.transaction_history) == 0

    def test_transfer_funds_zero_amount(self):
        wallet1 = Wallet("Alice", "1")
        wallet2 = Wallet("Bob", "2")
        wallet1.add_funds(100)
        wallet1.transfer_funds(wallet2, 0)
        assert wallet1.balance == 100
        assert wallet2.balance == 0
        assert len(wallet1.transaction_history) == 1
        assert len(wallet2.transaction_history) == 0

    def test_record_transaction(self):
        wallet = Wallet("Test", "123")
        wallet.record_transaction("Credit", 100)
        assert len(wallet.transaction_history) == 1
        assert wallet.transaction_history[0]['type'] == "Credit"
        assert wallet.transaction_history[0]['amount'] == 100

    def test_record_transaction_with_other_party(self):
        wallet = Wallet("Test", "123")
        wallet.record_transaction("Transfer", 100, "456")
        assert len(wallet.transaction_history) == 1
        assert wallet.transaction_history[0]['other_party_id'] == "456"

    def test_print_statement(self, capsys): # capsys fixture for capturing print output
        wallet = Wallet("Test", "123")
        wallet.add_funds(100)
        wallet.deduct_funds(50)
        wallet.print_statement()
        captured = capsys.readouterr()
        assert "Current Balance: $50.00" in captured.out
        assert "Credit" in captured.out
        assert "Debit" in captured.out

    def test_wallet_initialization(self):
        wallet = Wallet("Test User", "12345")
        assert wallet.customer_name == "Test User"
        assert wallet.customer_id == "12345"
        assert wallet.balance == 0.0
        assert wallet.transaction_history == []


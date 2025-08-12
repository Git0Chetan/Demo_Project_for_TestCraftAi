import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from payment1 import *


import pytest
import datetime
from payment_gateway import Card, PaymentProcessor

# Fixtures for creating cards and payment processor
@pytest.fixture
def valid_card():
    return Card('4532015112830366', '12/2025', 123, 'Alice Smith')

@pytest.fixture
def expired_card():
    return Card('4532015112830366', '12/2022', 123, 'Bob Johnson')

@pytest.fixture
def invalid_card_number():
    return Card('4532015112830367', '12/2025', 123, 'Charlie Brown') #invalid luhn

@pytest.fixture
def invalid_cvv():
    return Card('4532015112830366', '12/2025', 12, 'David Lee')

@pytest.fixture
def payment_processor():
    return PaymentProcessor()


# Test cases for Card class
def test_validate_card_number_valid(valid_card):
    assert valid_card.validate_card_number() == True

def test_validate_card_number_invalid(invalid_card_number):
    assert invalid_card_number.validate_card_number() == False

def test_validate_expiry_valid(valid_card):
    assert valid_card.validate_expiry() == True

def test_validate_expiry_invalid(expired_card):
    assert expired_card.validate_expiry() == False

def test_validate_expiry_invalid_format():
    card = Card('4532015112830366', '13/2025', 123, 'Eve Adams') #invalid month
    assert card.validate_expiry() == False
    card = Card('4532015112830366', '12/20255', 123, 'Eve Adams') #invalid year format
    assert card.validate_expiry() == False

def test_validate_cvv_valid(valid_card):
    assert valid_card.validate_cvv() == True

def test_validate_cvv_invalid(invalid_cvv):
    assert invalid_cvv.validate_cvv() == False

def test_validate_cvv_valid_four_digit():
    card = Card('4532015112830366', '12/2025', 1234, 'Frank Miller')
    assert card.validate_cvv() == True



# Test cases for PaymentProcessor class
def test_process_payment_success(payment_processor, valid_card):
    #Increase chances of success for testing
    random.seed(10)  
    result = payment_processor.process_payment(valid_card, 100)
    assert result == True
    assert len(payment_processor.transactions) == 1
    assert payment_processor.transactions[0]['status'] == 'Success'

def test_process_payment_failure_card_number(payment_processor, invalid_card_number):
    result = payment_processor.process_payment(invalid_card_number, 100)
    assert result == False
    assert len(payment_processor.transactions) == 0

def test_process_payment_failure_expiry(payment_processor, expired_card):
    result = payment_processor.process_payment(expired_card, 100)
    assert result == False
    assert len(payment_processor.transactions) == 0

def test_process_payment_failure_cvv(payment_processor, invalid_cvv):
    result = payment_processor.process_payment(invalid_cvv, 100)
    assert result == False
    assert len(payment_processor.transactions) == 0

def test_process_payment_failure_simulated(payment_processor, valid_card):
    # Reduce chances of success for testing failure case
    random.seed(5)
    result = payment_processor.process_payment(valid_card, 100)
    assert result == False
    assert len(payment_processor.transactions) == 1
    assert payment_processor.transactions[0]['status'] == 'Failed'

def test_print_transaction_log(payment_processor, valid_card):
    payment_processor.process_payment(valid_card, 100)
    captured_output = pytest.capfd.readouterr()
    payment_processor.print_transaction_log()
    captured_output = pytest.capfd.readouterr()
    assert "Transaction Log:" in captured_output.out
    assert "ID: 1" in captured_output.out
    assert "$100" in captured_output.out



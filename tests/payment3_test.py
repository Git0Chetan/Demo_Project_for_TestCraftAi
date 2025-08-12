import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from payment3 import *


import pytest
import datetime
from subscription_system import SubscriptionPlan, Customer, BillingSystem

# Fixtures for test setup
@pytest.fixture
def basic_plan():
    return SubscriptionPlan("Basic", 9.99, ["Feature A", "Feature B"])

@pytest.fixture
def pro_plan():
    return SubscriptionPlan("Pro", 29.99, ["Feature A", "Feature B", "Feature C"])

@pytest.fixture
def customer1(basic_plan):
    return Customer("CUST001", "Alice Smith", "alice@example.com", basic_plan)

@pytest.fixture
def customer2(pro_plan):
    return Customer("CUST002", "Bob Johnson", "bob@example.com", pro_plan)

@pytest.fixture
def billing_system():
    return BillingSystem()


# Test cases for SubscriptionPlan
def test_subscription_plan_creation(basic_plan):
    assert basic_plan.name == "Basic"
    assert basic_plan.price_per_month == 9.99
    assert basic_plan.features == ["Feature A", "Feature B"]

# Test cases for Customer
def test_customer_creation(customer1):
    assert customer1.customer_id == "CUST001"
    assert customer1.name == "Alice Smith"
    assert customer1.email == "alice@example.com"
    assert customer1.plan.name == "Basic"
    assert customer1.active == True
    assert isinstance(customer1.subscription_start, datetime.datetime)
    assert customer1.last_billed_date is None

def test_customer_generate_invoice(customer1):
    invoice = customer1.generate_invoice(datetime.datetime(2024,3,1))
    assert invoice['invoice_id'] == f"INV-CUST001-20240301"
    assert invoice['customer_name'] == "Alice Smith"
    assert invoice['amount'] == 9.99
    assert invoice['billing_date'] == "2024-03-01"
    assert customer1.last_billed_date == datetime.datetime(2024,3,1)

def test_customer_generate_invoice_invalid_date(customer1):
    with pytest.raises(TypeError):
        customer1.generate_invoice("invalid date")

# Test cases for BillingSystem

def test_billing_system_add_customer(billing_system, customer1):
    billing_system.add_customer(customer1)
    assert len(billing_system.customers) == 1
    assert billing_system.customers[0] == customer1

def test_billing_system_run_billing_cycle(billing_system, customer1, customer2):
    billing_system.add_customer(customer1)
    billing_system.add_customer(customer2)
    billing_system.run_billing_cycle(datetime.datetime(2024, 1, 15))
    assert len(billing_system.invoices) == 2

def test_billing_system_run_billing_cycle_inactive_customer(billing_system, customer1):
    customer1.active = False
    billing_system.add_customer(customer1)
    billing_system.run_billing_cycle(datetime.datetime(2024,1,1))
    assert len(billing_system.invoices) == 0


def test_billing_system_run_billing_cycle_already_billed(billing_system, customer1):
    billing_system.add_customer(customer1)
    billing_system.run_billing_cycle(datetime.datetime(2024,1,1))
    billing_system.run_billing_cycle(datetime.datetime(2024,1,15)) # same month, should not bill again.
    assert len(billing_system.invoices) == 1


def test_billing_system_generate_report(billing_system, customer1):
    billing_system.add_customer(customer1)
    billing_system.run_billing_cycle(datetime.datetime(2024, 1, 1))
    billing_system.generate_report() # This test checks for output -  more robust testing would capture and check the output.  This is a simplification for brevity.

def test_billing_system_empty_report(billing_system):
    billing_system.generate_report() #Expect no error on an empty report



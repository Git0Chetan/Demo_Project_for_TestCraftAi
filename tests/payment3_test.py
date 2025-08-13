import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from payment3 import *

from subscription_system import SubscriptionPlan, Customer, BillingSystem

# Test cases for SubscriptionPlan class
def test_subscriptionplan_creation():
    plan = SubscriptionPlan("Basic", 9.99, ["Feature A", "Feature B"])
    assert plan.name == "Basic"
    assert plan.price_per_month == 9.99
    assert plan.features == ["Feature A", "Feature B"]

def test_subscriptionplan_invalid_price():
    with pytest.raises(TypeError):
        SubscriptionPlan("Basic", "9.99", ["Feature A"])

def test_subscriptionplan_invalid_features():
    with pytest.raises(TypeError):
        SubscriptionPlan("Basic", 9.99, "Feature A")


# Test cases for Customer class
def test_customer_creation():
    plan = SubscriptionPlan("Basic", 9.99, ["Feature A"])
    customer = Customer("CUST001", "Alice", "alice@example.com", plan)
    assert customer.customer_id == "CUST001"
    assert customer.name == "Alice"
    assert customer.email == "alice@example.com"
    assert customer.plan == plan
    assert customer.active is True
    assert isinstance(customer.subscription_start, datetime.datetime)
    assert customer.last_billed_date is None

def test_customer_generate_invoice():
    plan = SubscriptionPlan("Basic", 9.99, ["Feature A"])
    customer = Customer("CUST001", "Alice", "alice@example.com", plan)
    billing_date = datetime.datetime(2024, 1, 1)
    invoice = customer.generate_invoice(billing_date)
    assert invoice['invoice_id'] == f"INV-CUST001-20240101"
    assert invoice['customer_name'] == "Alice"
    assert invoice['amount'] == 9.99
    assert invoice['billing_date'] == "2024-01-01"
    assert customer.last_billed_date == billing_date

def test_customer_generate_invoice_no_plan():
    with pytest.raises(AttributeError):
        customer = Customer("CUST001", "Alice", "alice@example.com", None)
        customer.generate_invoice(datetime.datetime(2024,1,1))


# Test cases for BillingSystem class
def test_billingsystem_creation():
    billing_system = BillingSystem()
    assert billing_system.customers == []
    assert billing_system.invoices == []

def test_billingsystem_add_customer():
    billing_system = BillingSystem()
    plan = SubscriptionPlan("Basic", 9.99, ["Feature A"])
    customer = Customer("CUST001", "Alice", "alice@example.com", plan)
    billing_system.add_customer(customer)
    assert len(billing_system.customers) == 1
    assert billing_system.customers[0] == customer

def test_billingsystem_run_billing_cycle():
    billing_system = BillingSystem()
    plan = SubscriptionPlan("Basic", 9.99, ["Feature A"])
    customer = Customer("CUST001", "Alice", "alice@example.com", plan)
    billing_system.add_customer(customer)
    date = datetime.datetime(2024, 1, 1)
    billing_system.run_billing_cycle(date)
    assert len(billing_system.invoices) == 1

def test_billingsystem_run_billing_cycle_inactive_customer():
    billing_system = BillingSystem()
    plan = SubscriptionPlan("Basic", 9.99, ["Feature A"])
    customer = Customer("CUST001", "Alice", "alice@example.com", plan)
    customer.active = False
    billing_system.add_customer(customer)
    date = datetime.datetime(2024,1,1)
    billing_system.run_billing_cycle(date)
    assert len(billing_system.invoices) == 0

def test_billingsystem_generate_report():
    billing_system = BillingSystem()
    plan = SubscriptionPlan("Basic", 9.99, ["Feature A"])
    customer = Customer("CUST001", "Alice", "alice@example.com", plan)
    billing_system.add_customer(customer)
    date = datetime.datetime(2024, 1, 1)
    billing_system.run_billing_cycle(date)
    report = billing_system.generate_report()
    assert len(billing_system.invoices) == 1

def test_billingsystem_run_billing_cycle_multiple_months():
    billing_system = BillingSystem()
    plan = SubscriptionPlan("Basic", 9.99, ["Feature A"])
    customer = Customer("CUST001", "Alice", "alice@example.com", plan)
    billing_system.add_customer(customer)
    date1 = datetime.datetime(2024,1,1)
    date2 = datetime.datetime(2024,2,1)
    billing_system.run_billing_cycle(date1)
    billing_system.run_billing_cycle(date2)
    assert len(billing_system.invoices) == 2

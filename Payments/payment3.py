# subscription_system.py
import datetime
import random

class SubscriptionPlan:
    def __init__(self, name, price_per_month, features):
        self.name = name
        self.price_per_month = price_per_month
        self.features = features

class Customer:
    def __init__(self, customer_id, name, email, plan):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.plan = plan
        self.active = True
        self.subscription_start = datetime.datetime.now()
        self.last_billed_date = None

    def generate_invoice(self, billing_date):
        invoice_id = f"INV-{self.customer_id}-{billing_date.strftime('%Y%m%d')}"
        total_amount = self.plan.price_per_month
        invoice = {
            'invoice_id': invoice_id,
            'customer_name': self.name,
            'email': self.email,
            'plan_name': self.plan.name,
            'features': self.plan.features,
            'amount': total_amount,
            'billing_date': billing_date.strftime("%Y-%m-%d")
        }
        print(f"\nGenerated Invoice: {invoice_id}")
        print(f"Customer: {self.name}")
        print(f"Plan: {self.plan.name}")
        print(f"Features: {', '.join(self.plan.features)}")
        print(f"Amount Due: ${total_amount:.2f}")
        print(f"Billing Date: {invoice['billing_date']}")
        # Update last billed date
        self.last_billed_date = billing_date
        return invoice

class BillingSystem:
    def __init__(self):
        self.customers = []
        self.invoices = []

    def add_customer(self, customer):
        self.customers.append(customer)
        print(f"Added customer {customer.name} with ID {customer.customer_id}")

    def run_billing_cycle(self, date):
        print(f"\nRunning billing cycle for {date.strftime('%Y-%m-%d')}")
        for customer in self.customers:
            if customer.active:
                # Assuming billing once per month
                if not customer.last_billed_date or \
                   (date.month != customer.last_billed_date.month):
                    invoice = customer.generate_invoice(date)
                    self.invoices.append(invoice)

    def generate_report(self):
        print("\nAll Invoices:")
        for invoice in self.invoices:
            print(f"{invoice['invoice_id']} | Customer: {invoice['customer_name']} | Amount: ${invoice['amount']:.2f} | Date: {invoice['billing_date']}")

# Usage demo
def main():
    # Create plans
    basic_plan = SubscriptionPlan("Basic", 9.99, ["Feature A", "Feature B"])
    pro_plan = SubscriptionPlan("Pro", 29.99, ["Feature A", "Feature B", "Feature C"])

    # Create customers
    customer1 = Customer("CUST001", "Alice Smith", "alice@example.com", basic_plan)
    customer2 = Customer("CUST002", "Bob Johnson", "bob@example.com", pro_plan)
    customer3 = Customer("CUST003", "Charlie Brown", "charlie@example.com", pro_plan)
    customer4 = Customer("CUST004", "Diana Prince", "diana@example.com", basic_plan)
    customer5 = Customer("CUST005", "Ethan Hunt", "ethan@example.com", pro_plan)
    customer6 = Customer("CUST006", "Grace Hopper", "grace@example.com", basic_plan)
    



    # Initialize billing system
    billing_system = BillingSystem()
    billing_system.add_customer(customer1)
    billing_system.add_customer(customer2)
    billing_system.add_customer(customer3)
    billing_system.add_customer(customer4)
    billing_system.add_customer(customer5)
    billing_system.add_customer(customer6)

    # Simulate billing for two months
    billing_dates = [
        datetime.datetime(2024, 1, 1),
        datetime.datetime(2024, 2, 1)
    ]
    for date in billing_dates:
        billing_system.run_billing_cycle(date)

    # Generate report
    billing_system.generate_report()

if __name__ == "__main__":
    main()
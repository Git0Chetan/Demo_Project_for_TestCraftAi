# wallet_system.py
import datetime

class Wallet:
    def __init__(self, customer_name, customer_id):
        self.customer_name = customer_name
        self.customer_id = customer_id
        self.balance = 0.0
        self.transaction_history = []

    def add_funds(self, amount):
        if amount > 0:
            self.balance += amount
            self.record_transaction('Credit', amount)
            print(f"Added ${amount:.2f} to {self.customer_name}'s wallet.")
        else:
            print("Invalid amount.")

    def deduct_funds(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.record_transaction('Debit', amount)
            print(f"Deducted ${amount:.2f} from {self.customer_name}'s wallet.")
        else:
            print("Insufficient funds or invalid amount.")

    def transfer_funds(self, recipient_wallet, amount):
        if amount > 0 and self.balance >= amount:
            self.deduct_funds(amount)
            recipient_wallet.add_funds(amount)
            print(f"Transferred ${amount:.2f} to {recipient_wallet.customer_name}.")
            self.record_transaction('Transfer Out', amount, recipient_wallet.customer_id)
            recipient_wallet.record_transaction('Transfer In', amount, self.customer_id)
        else:
            print("Transfer failed due to insufficient funds or invalid amount.")

    def record_transaction(self, trans_type, amount, other_party_id=None):
        trans_record = {
            'type': trans_type,
            'amount': amount,
            'date': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'balance': self.balance
        }
        if other_party_id:
            trans_record['other_party_id'] = other_party_id
        self.transaction_history.append(trans_record)

    def print_statement(self):
        print(f"\nStatement for {self.customer_name} (ID: {self.customer_id}):")
        print(f"Current Balance: ${self.balance:.2f}")
        print("Transaction History:")
        for t in self.transaction_history:
            detail = f"{t['date']} | {t['type']} | ${t['amount']:.2f} | Balance: ${t['balance']:.2f}"
            if 'other_party_id' in t:
                detail += f" | With ID: {t['other_party_id']}"
            print(detail)

# Usage Demonstration
def main():
    wallet1 = Wallet('Alice', 'CUST1001')
    wallet2 = Wallet('Bob', 'CUST1002')

    wallet1.add_funds(500)
    wallet2.add_funds(300)

    wallet1.deduct_funds(50)
    wallet2.deduct_funds(100)

    wallet1.transfer_funds(wallet2, 100)

    wallet1.print_statement()
    wallet2.print_statement()

if __name__ == "__main__":
    main()
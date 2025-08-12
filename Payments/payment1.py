# payment_gateway.py
import random
import datetime

class Card:
    def __init__(self, card_number, expiry_date, cvv, cardholder_name):
        self.card_number = card_number
        self.expiry_date = expiry_date
        self.cvv = cvv
        self.cardholder_name = cardholder_name

    def validate_card_number(self):
        def luhn_check(card_num):
            total = 0
            reverse_digits = card_num[::-1]
            for i, digit in enumerate(reverse_digits):
                n = int(digit)
                if i % 2 == 1:
                    n *= 2
                    if n > 9:
                        n -= 9
                total += n
            return total % 10 == 0

        return luhn_check(self.card_number)

    def validate_expiry(self):
        try:
            expiry = datetime.datetime.strptime(self.expiry_date, "%m/%Y")
            return expiry > datetime.datetime.now()
        except:
            return False

    def validate_cvv(self):
        return len(str(self.cvv)) == 3 or len(str(self.cvv)) == 4

class PaymentProcessor:
    def __init__(self):
        self.transactions = []

    def process_payment(self, card, amount, payment_method='credit_card'):
        print(f"\nProcessing payment of ${amount} via {payment_method} for {card.cardholder_name}...")
        # Validate card details
        if not card.validate_card_number():
            print("Invalid card number.")
            return False

        if not card.validate_expiry():
            print("Card has expired.")
            return False

        if not card.validate_cvv():
            print("Invalid CVV.")
            return False

        # Simulate random transaction success/failure
        success = random.choice([True, True, True, False])  # 75% success rate

        transaction = {
            'transaction_id': len(self.transactions) + 1,
            'amount': amount,
            'date_time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'status': 'Success' if success else 'Failed',
            'payment_method': payment_method,
            'cardholder_name': card.cardholder_name
        }
        self.transactions.append(transaction)

        if success:
            print(f"Payment successful. Transaction ID: {transaction['transaction_id']}")
            return True
        else:
            print("Payment failed due to network error. Please try again.")
            return False

    def print_transaction_log(self):
        print("\nTransaction Log:")
        for t in self.transactions:
            print(f"ID: {t['transaction_id']} | Amount: ${t['amount']} | Status: {t['status']} | Date: {t['date_time']} | Method: {t['payment_method']} | Cardholder: {t['cardholder_name']}")

# Sample usage
def main():
    processor = PaymentProcessor()
    # Sample cards
    card1 = Card('4532015112830366', '12/2025', 123, 'Alice Smith')
    card2 = Card('6011514433546201', '11/2023', 456, 'Bob Johnson')
    card3 = Card('378282246310005', '01/2024', 789, 'Charlie Brown')  # American Express, 15 digits

    # Process some payments
    processor.process_payment(card1, 150.75)
    processor.process_payment(card2, 89.60, payment_method='debit_card')
    processor.process_payment(card3, 200, payment_method='american_express')

    # Print log
    processor.print_transaction_log()

if __name__ == "__main__":
    main()
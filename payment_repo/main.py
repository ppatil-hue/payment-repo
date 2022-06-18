from pay.order import Order, LineItem
from pay.payment import pay_order
from pay.credit_card import CreditCard
from pay.processor import PaymentProcessor


def main():
    card = input("Enter card no:")
    month = int(input("Enter card expiry month"))
    year = int(input("Enter card expiry year"))

    o = Order()
    p = PaymentProcessor()
    c = CreditCard(card, year, month)

    o.line_items.append(LineItem(name="Shoes", price=24, quantity=2))
    o.line_items.append(LineItem(name="Dress", price=12, quantity=4))

    print(pay_order(o, c, p))


if __name__ == "__main__":
    main()

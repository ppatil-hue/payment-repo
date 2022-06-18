
from typing import Protocol
from pay.credit_card import CreditCard
from pay.order import Order


class PaymentProcessor(Protocol):

    def charge(self, card: CreditCard, amount: int) -> None:
        ...


def pay_order(order: Order, card: CreditCard, processor: PaymentProcessor) -> None:

    if order.total == 0:
        raise ValueError(" Couldn't pay with null amount")

    processor.charge(card, amount=order.total)
    order.pay()

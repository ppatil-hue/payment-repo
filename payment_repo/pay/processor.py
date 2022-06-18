from datetime import datetime

from pay.credit_card import CreditCard
import re


def validate_key(key: str) -> str:
    uuid_pattern = r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}"
    if not re.match(uuid_pattern, key):
        raise ValueError("Invalid key")

    return key


class PaymentProcessor:

    def __init__(self, key: str = "6cfb67f3-6281-4031-b893-ea85db0dce20") -> None:
        self.api_key = validate_key(key)

    def charge(self, card: CreditCard, amount: int) -> None:
        if not self.validate_card(card):
            raise ValueError("Invalid Card")
        print(f"Charging card for the amount {amount} EUR")

    def validate_card(self, card: CreditCard) -> bool:
        print(type(card.expiry_year), card.expiry_month)
        return (
                checksum_(card.card_number)
                and datetime(card.expiry_year, card.expiry_month, 1)
        )


def checksum_(card_number: str) -> bool:
    def digits_of(card_nr: str):
        return [int(d) for d in card_nr]

    digits = digits_of(card_number)
    odd_ = digits[-1::-2]
    even_ = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_)
    for digit in even_:
        checksum += sum(digits_of(str(digit * 2)))
    return checksum % 10 == 0

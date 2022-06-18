from dataclasses import dataclass, field
from typing import List


@dataclass
class CreditCard:
    card_number: str
    expiry_year: int
    expiry_month: int

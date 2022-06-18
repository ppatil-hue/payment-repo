from dataclasses import dataclass, field
from typing import List
from enum import Enum


class OrderStatus(Enum):
    OPEN = "not paid"
    PAID = "paid"


@dataclass
class LineItem:
    name: str
    price: int
    quantity: int = 1

    @property
    def total(self) -> int:
        return self.price * self.quantity


@dataclass
class Order:
    line_items: List[LineItem] = field(default_factory=list)
    status: OrderStatus = OrderStatus.OPEN

    def pay(self) -> None:
        self.status = OrderStatus.PAID

    @property
    def total(self) -> int:
        return sum(item.total for item in self.line_items)

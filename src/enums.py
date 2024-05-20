from enum import Enum


class Side(str, Enum):
    BUY = "buy"
    SELL = "sell"


class Currency(str, Enum):
    EUR = "eur"
    USD = "usd"
    CHF = "chf"

class Status(str, Enum):
    PENDING = "pending"
    CANCELED = "canceled"
    CLEARED = "cleared"
    DECLINED = "declined"
    EXPIRED = "expired"


class Clearing(str, Enum):
    PENDING = "pending"
    PARTIALLY_CLEARED = "partially_cleared"
    CLEARED = "cleared"
    REJECT = "reject"



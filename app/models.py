from dataclasses import dataclass, asdict

@dataclass
class Expense:
    title: str
    amount: float
    category: str
    expense_date: str

    def to_dict(self) -> dict:
        return asdict(self)
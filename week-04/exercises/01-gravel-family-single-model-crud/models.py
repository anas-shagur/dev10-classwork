from dataclasses import dataclass
from datetime import date


@dataclass
class Employee:
    employee_id: int
    first_name: str
    last_name: str
    start_date: date
    end_date: date

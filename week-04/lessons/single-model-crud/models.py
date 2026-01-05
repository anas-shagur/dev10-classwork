from dataclasses import dataclass
from datetime import date


@dataclass
class Customer:
    customer_id: str
    first_name: str
    last_name: str
    street_address: str
    city: str
    state: str
    zip_code: str
    email_address: str
    phone: str
    date_added: date
    reward_points: int = 0

    def to_tuple(self):
        return (
            self.customer_id,
            self.first_name,
            self.last_name,
            self.street_address,
            self.city,
            self.state,
            self.zip_code,
            self.email_address,
            self.phone,
            self.date_added,
            self.reward_points,
        )

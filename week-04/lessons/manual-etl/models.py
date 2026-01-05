from dataclasses import dataclass
from datetime import date


@dataclass
class MovieReview:
    anonymous_id: int
    movie_id: int
    movie_name: str
    rating: float
    review_date: date

    def to_tuple(self):
        return (
            self.anonymous_id,
            self.movie_id,
            self.movie_name,
            self.rating,
            self.review_date,
        )

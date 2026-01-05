from dataclasses import dataclass, field
from datetime import date


@dataclass(kw_only=True)
class BookData:
    id: int = field(default=None)
    author_name: str
    title: str
    publish_date: date
    format: str
    price: float


# book_data_id,author_name,book_title,publish_date,format,price
# 1,N. K. Jemisin,The Fifth Season,2015-08-04,Hardcover,24.99
# 2,N. K. Jemisin,The Obelisk Gate,2016-08-16,Hardcover,19.99
# 3,N. K. Jemisin,The Stone Sky,2017-08-15,Hardcover,29.99
# 4,N. K. Jemisin,The Fifth Season,2015-08-04,Softcover,11.79
# 5,N. K. Jemisin,The Fifth Season,2015-08-04,eBook,11.99
# 6,Ted Chiang,Stories of Your Life and Others,2002-07-01,Hardcover,19.98
# 7,Ted Chiang,Stories of Your Life and Others,2002-07-01,Softcover,9.02
# 8,Ted Chiang,Stories of Your Life and Others,2002-07-01,eBook,4.99
# 9,Ted Chiang,Exhalation: Stories,2019-05-07,Hardcover,15.76
# 10,Judy Bloom,"Are You There God? It's Me, Margaret.",1970-05-01,Hardcover,13.35
# 11,David Mitchell,Ghostwritten,1999-08-09,Hardcover,23.89

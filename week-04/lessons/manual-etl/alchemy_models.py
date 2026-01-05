from datetime import date

from sqlalchemy import Date, Float, ForeignKey, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


# create table genre (
#     genre_id int primary key auto_increment,
#     `name` varchar(50) not null unique
# );


class Genre(Base):
    __tablename__ = "genre"

    genre_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)

    def __repr__(self):
        return f"<Genre(genre_id={self.genre_id}, name={self.name})>"


# create table movie (
#     movie_id int primary key auto_increment,
#     `name` varchar(100) not null,
#     genre_id int not null,
#     release_year int not null,
#     constraint fk_movie_genre_id
#         foreign key (genre_id)
#         references genre(genre_id)
# );


class Movie(Base):
    __tablename__ = "movie"

    movie_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    genre_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("genre.genre_id"), nullable=False
    )
    release_year: Mapped[int] = mapped_column(Integer, nullable=False)

    genre: Mapped[Genre] = relationship(Genre)

    def __repr__(self):
        return f"<Movie(movie_id={self.movie_id}, name={self.name}, genre_id={self.genre_id}, release_year={self.release_year})>"


# create table customer (
#     customer_id int primary key auto_increment,
#     `name` varchar(100) not null,
#     email varchar(256) not null unique
# );


class Customer(Base):
    __tablename__ = "customer"

    customer_id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(256), nullable=False, unique=True)

    def __repr__(self):
        return f"<Customer(customer_id={self.customer_id}, name={self.name}, email={self.email})>"


# create table review (
#     review_id int primary key auto_increment,
#     movie_id int not null,
#     customer_id int not null,
#     rating decimal(4,2) not null,
#     review_date date not null,
#     constraint fk_review_movie_id
#         foreign key (movie_id)
#         references movie(movie_id),
#     constraint fk_review_customer_id
#         foreign key (customer_id)
#         references customer(customer_id)
# );


class Review(Base):
    __tablename__ = "review"

    review_id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )
    movie_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("movie.movie_id"), nullable=False
    )
    customer_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("customer.customer_id"), nullable=False
    )
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    review_date: Mapped[date] = mapped_column(Date, nullable=False)

    movie: Mapped[Movie] = relationship(Movie)
    customer: Mapped[Customer] = relationship(Customer)

    def __repr__(self):
        return f"<Review(review_id={self.review_id}, movie_id={self.movie_id}, customer_id={self.customer_id}, rating={self.rating}, review_date={self.review_date})>"

    def __str__(self):
        return f"Review ID: {self.review_id}, Movie: {self.movie.name}, Customer ID: {self.customer_id}, Rating: {self.rating}, Review Date: {self.review_date}"

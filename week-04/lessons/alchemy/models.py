from datetime import date
from decimal import Decimal
from typing import List, Optional

from sqlalchemy import Date, ForeignKey, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


# foundation models
# ------------------


class Customer(Base):
    __tablename__ = "customer"
    customer_id: Mapped[str] = mapped_column(
        String(36), primary_key=True, autoincrement=False
    )
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    street_address: Mapped[Optional[str]] = mapped_column(String(100))
    city: Mapped[Optional[str]] = mapped_column(String(50))
    state: Mapped[Optional[str]] = mapped_column(String(2))
    zip_code: Mapped[Optional[str]] = mapped_column(String(5))
    email_address: Mapped[str] = mapped_column(String(100), unique=True)
    phone: Mapped[str] = mapped_column(String(20))
    date_added: Mapped[date] = mapped_column(Date())
    reward_points: Mapped[int] = mapped_column(Integer())

    login: Mapped["Login"] = relationship("Login", uselist=False)

    def __repr__(self):
        return f"Customer(customer_id={self.customer_id}, first_name={self.first_name}, last_name={self.last_name}, email_address={self.email_address}, phone={self.phone}, date_added={self.date_added}, reward_points={self.reward_points}, login={self.login})"


class Item(Base):
    __tablename__ = "item"
    item_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50))
    description: Mapped[str] = mapped_column(String(1024))
    price: Mapped[Decimal] = mapped_column()

    def __repr__(self):
        return f"Item(item_id={self.item_id}, name={self.name}, description={self.description}, price={self.price})"


class OrderStatus(Base):
    __tablename__ = "order_status"
    order_status_id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )
    name: Mapped[str] = mapped_column(String(50))
    parent_order_status_id: Mapped[Optional[int]] = mapped_column(
        Integer, ForeignKey("order_status.order_status_id")
    )
    parent_status: Mapped["OrderStatus"] = relationship(
        "OrderStatus", remote_side=[order_status_id]
    )

    def __repr__(self):
        return f"OrderStatus(order_status_id={self.order_status_id}, name={self.name}, parent_order_status_id={self.parent_order_status_id}, parent_status={self.parent_status})"


# related models
# --------------


class Order(Base):
    __tablename__ = "order"
    order_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    order_date: Mapped[date] = mapped_column(Date())
    customer_id: Mapped[str] = mapped_column(
        String(36), ForeignKey("customer.customer_id")
    )
    order_status_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("order_status.order_status_id")
    )
    notes: Mapped[Optional[str]] = mapped_column(String(1024))

    items: Mapped[List["OrderItem"]] = relationship("OrderItem", cascade="all, delete")
    order_status: Mapped["OrderStatus"] = relationship("OrderStatus")
    customer: Mapped["Customer"] = relationship("Customer")

    def __repr__(self):
        return f"Order(order_id={self.order_id}, order_date={self.order_date}, customer_id={self.customer_id}, order_status_id={self.order_status_id}, notes={self.notes}, items={self.items}, order_status={self.order_status})"


class OrderItem(Base):
    __tablename__ = "order_item"
    order_item_id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )
    order_id: Mapped[int] = mapped_column(Integer, ForeignKey("order.order_id"))
    item_id: Mapped[int] = mapped_column(Integer, ForeignKey("item.item_id"))
    quantity: Mapped[int] = mapped_column(Integer)
    notes: Mapped[Optional[str]] = mapped_column(String(1024))

    item: Mapped["Item"] = relationship("Item")

    def __repr__(self):
        return f"OrderItem(order_item_id={self.order_item_id}, order_id={self.order_id}, item_id={self.item_id}, quantity={self.quantity}, notes={self.notes})"


class Login(Base):
    __tablename__ = "login"
    customer_id: Mapped[str] = mapped_column(
        String(36),
        ForeignKey("customer.customer_id"),
        primary_key=True,
        autoincrement=False,
    )
    user_name: Mapped[str] = mapped_column(String(100))
    password_hash: Mapped[str] = mapped_column()

    def __repr__(self):
        return f"Login(customer_id={self.customer_id}, user_name={self.user_name})"

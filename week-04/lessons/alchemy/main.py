from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from models import Customer, Item, OrderStatus, Order, OrderItem
from datetime import date
from dynaconf import Dynaconf
from decimal import Decimal


def build_engine():
    settings = Dynaconf(envvar_prefix="DB", load_dotenv=True)
    return create_engine(settings.ENGINE_URL, echo=True)


def fetch_customers_last_name_starting_with_Gr(session):
    stmt = select(Customer).where(Customer.last_name.like("Gr%"))
    last_customer = None
    for customer in session.scalars(stmt):
        print(customer)
        last_customer = customer
    return last_customer


def add_item(session):
    item = Item(
        name="Dr. Pepper", description="Tastes like almond.", price=Decimal("1.99")
    )
    session.add(item)
    session.commit()
    print(item.item_id)
    return item


def add_order(session, customer):
    stmt = select(OrderStatus).where(OrderStatus.name == "Scheduled")
    order_status = session.scalars(stmt).one()

    stmt = select(Item).where(Item.name.in_(["Dr. Pepper", "Baja Bowl"]))

    items = [
        OrderItem(item_id=item.item_id, item=item, quantity=1)
        for item in session.scalars(stmt)
    ]

    order = Order(
        order_date=date.today(),
        customer_id=customer.customer_id,
        customer=customer,
        order_status_id=order_status.order_status_id,
        order_status=order_status,
        notes="There's a Halloween blow-up in the yard.",
        items=items,
    )

    session.add(order)
    session.commit()
    print(order.order_id)
    return order


def fetch_order(session, customer):
    stmt = select(Order).where(Order.customer_id == customer.customer_id)
    for order in session.scalars(stmt):
        print(order)


def update_order_status(session, order):
    if order in session:
        stmt = select(OrderStatus).where(OrderStatus.name == "Out for delivery")
        order_status = session.scalars(stmt).one()
        order.order_status_id = order_status.order_status_id
        order.order_status = order_status
        session.commit()
    print(order.order_status)


def remove_all_orders(session, customer):
    stmt = select(Order).where(Order.customer_id == customer.customer_id)
    for order in session.scalars(stmt):
        session.delete(order)
    session.commit()


def update_item(session, item):
    if item in session and not session.dirty:
        print("Dr. Pepper in session and not dirty")

    item.price = Decimal("2.99")
    if session.dirty:
        session.commit()

    print(item)


def delete_item(session, item):
    if item in session:
        session.delete(item)
        session.commit()
    print(item)


def main():
    with Session(build_engine()) as session:
        customer = fetch_customers_last_name_starting_with_Gr(session)
        item = add_item(session)
        order = add_order(session, customer)
        fetch_order(session, customer)
        update_order_status(session, order)
        remove_all_orders(session, customer)
        update_item(session, item)
        delete_item(session, item)


if __name__ == "__main__":
    main()

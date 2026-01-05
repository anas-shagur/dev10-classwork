from datetime import date
from decimal import Decimal
from typing import List, Optional

from sqlalchemy import Date, ForeignKey, Integer, String, Column, Table
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


# create table customer (
# 	customer_id int primary key auto_increment,
#     first_name varchar(50) not null,
#     last_name varchar(50) not null,
#     email_address varchar(100) not null,
#     phone varchar(25) not null,
#     address varchar(100) not null,
#     city varchar(50) not null,
#     province varchar(5) not null,
#     postal_code varchar(5) not null,
#     customer_since date not null
# );


class Customer(Base):
    __tablename__ = "customer"

    customer_id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    email_address: Mapped[str] = mapped_column(String(100))
    phone: Mapped[str] = mapped_column(String(25))
    address: Mapped[str] = mapped_column(String(100))
    city: Mapped[str] = mapped_column(String(50))
    province: Mapped[str] = mapped_column(String(5))
    postal_code: Mapped[str] = mapped_column(String(5))
    customer_since: Mapped[date] = mapped_column(Date)

    login: Mapped["Login"] = relationship("Login", uselist=False)

    def __repr__(self):
        return f"(Customer {self.first_name} {self.last_name})"


# create table login (
# 	customer_id int primary key,
#     user_name varchar(100) not null unique,
#     password_hash text not null,
#     constraint fk_login_customer_id
# 		foreign key (customer_id)
# 		references customer(customer_id)
# );


class Login(Base):
    __tablename__ = "login"

    customer_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("customer.customer_id"),
        primary_key=True,
        autoincrement=False,
    )
    user_name: Mapped[str] = mapped_column(String(100), unique=True)
    password_hash: Mapped[str] = mapped_column(String(100))

    def __repr__(self):
        return f"(Login {self.user_name})"


# create table project_employee (
# 	project_id int not null,
# 	employee_id int not null,
#     constraint pk_project_employee
# 		primary key(project_id, employee_id),
# 	constraint fk_project_employee_project_id
# 		foreign key (project_id)
# 		references project(project_id),
# 	constraint fk_project_employee_employee_id
# 		foreign key (employee_id)
# 		references employee(employee_id)
# );

project_employee = Table(
    "project_employee",
    Base.metadata,
    Column("project_id", Integer, ForeignKey("project.project_id"), primary_key=True),
    Column(
        "employee_id", Integer, ForeignKey("employee.employee_id"), primary_key=True
    ),
)


# create table employee (
# 	employee_id int primary key auto_increment,
#     first_name varchar(50) not null,
#     last_name varchar(50) not null,
#     start_date date not null,
#     end_date date null
# );


class Employee(Base):
    __tablename__ = "employee"

    employee_id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    start_date: Mapped[date] = mapped_column(Date)
    end_date: Mapped[Optional[date]] = mapped_column(Date)

    projects: Mapped[List["Project"]] = relationship(
        "Project", secondary=project_employee, back_populates="employees"
    )

    def __repr__(self):
        return f"(Employee {self.first_name} {self.last_name}, project_count: {len(self.projects)})"


# create table project (
# 	project_id int primary key auto_increment,
#     `description` varchar(120) not null,
#     start_date date not null,
#     end_date date null,
#     customer_id int not null,
#     constraint fk_project_customer_id
# 		foreign key (customer_id)
# 		references customer(customer_id)
# );


class Project(Base):
    __tablename__ = "project"

    project_id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )
    description: Mapped[str] = mapped_column(String(120))
    start_date: Mapped[date] = mapped_column(Date)
    end_date: Mapped[Optional[date]] = mapped_column(Date)
    customer_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("customer.customer_id")
    )

    customer: Mapped["Customer"] = relationship("Customer", uselist=False)
    items: Mapped[List["ProjectItem"]] = relationship("ProjectItem")
    employees: Mapped[List["Employee"]] = relationship(
        "Employee", secondary=project_employee, back_populates="projects"
    )

    def __repr__(self):
        return f"(Project {self.description}, items: {self.items}, customer: {self.customer.first_name} {self.customer.last_name})"


# create table category (
# 	category_id int primary key auto_increment,
# 	`name` varchar(50) not null,
# 	parent_category_id int null,
# 	constraint fk_category_parent_category_id
# 		foreign key (parent_category_id)
# 		references category(category_id)
# );


class Category(Base):
    __tablename__ = "category"

    category_id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )
    name: Mapped[str] = mapped_column(String(50))
    parent_category_id: Mapped[Optional[int]] = mapped_column(
        Integer, ForeignKey("category.category_id")
    )
    parent_category: Mapped["Category"] = relationship(
        "Category", remote_side=[category_id]
    )

    def __repr__(self):
        return f"(Category {self.name}, parent: {self.parent_category.name if self.parent_category else None})"


# create table unit (
# 	unit_id int primary key auto_increment,
#     `name` varchar(50) not null
# );


class Unit(Base):
    __tablename__ = "unit"

    unit_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50))

    def __repr__(self):
        return f"(Unit {self.name})"


# create table item (
# 	item_id int primary key auto_increment,
#     `name` varchar(50) not null,
#     category_id int not null,
#     unit_id int not null,
#     price_per_unit decimal(10,3) not null,
#     constraint fk_item_category_id
# 		foreign key (category_id)
# 		references category(category_id),
# 	constraint fk_item_unit_id
# 		foreign key (unit_id)
# 		references unit(unit_id)
# );


class Item(Base):
    __tablename__ = "item"

    item_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50))
    category_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("category.category_id")
    )
    unit_id: Mapped[int] = mapped_column(Integer, ForeignKey("unit.unit_id"))
    price_per_unit: Mapped[Decimal] = mapped_column()

    category: Mapped["Category"] = relationship("Category")
    unit: Mapped["Unit"] = relationship("Unit")

    def __repr__(self):
        return f"(Item {self.name}, category: {self.category.name}, unit: {self.unit.name})"


# create table project_item (
# 	project_id int not null,
#     item_id int not null,
#     quantity decimal(9,3) not null,
# 	constraint pk_project_item
# 		primary key(project_id, item_id),
# 	constraint fk_project_item_project_id
# 		foreign key (project_id)
# 		references project(project_id),
# 	constraint fk_project_item_item_id
# 		foreign key (item_id)
# 		references item(item_id)
# );


class ProjectItem(Base):
    __tablename__ = "project_item"

    project_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("project.project_id"), primary_key=True
    )
    item_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("item.item_id"), primary_key=True
    )
    quantity: Mapped[Decimal] = mapped_column()
    item: Mapped["Item"] = relationship("Item")

    def __repr__(self):
        return f"(ProjectItem {self.item.name}, {self.quantity})"

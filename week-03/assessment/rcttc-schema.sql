drop database if exists rcttc;
create database rcttc;
use rcttc;

create table customer (
	customer_id int primary key auto_increment,
    first_name varchar(100) not null,
    last_name varchar(100) not null,
    email varchar(100) not null,
    phone varchar(100) null,
    address varchar(100) null
);

create table theater (
	theater_id int primary key auto_increment,
    theater_name varchar(25) not null unique,
    address varchar(50),
    phone varchar(15),
    email varchar(50)
);

create table seat (
	seat_id int primary key auto_increment,
    seat_name varchar(2),
    theater_id int not null,
    constraint fk_seat_theater_id
		foreign key (theater_id)
        references theater(theater_id),
	constraint uq_seat_seat_name_theater_id
		unique (seat_name, theater_id) -- cant have same seat code in the same theater
);

create table `show` (
		show_id int primary key auto_increment,
        show_name varchar(50) not null unique
);

create table performance (
    performance_id int primary key auto_increment,
    show_id int not null,
    theater_id int not null,
    performance_date date,
    ticket_price decimal(10,2),
    constraint fk_performance_show
        foreign key (show_id) 
        references `show`(show_id),
    constraint fk_performance_theater
        foreign key (theater_id) 
        references theater(theater_id),
    constraint uq_performance_show_theater_date
        unique (show_id, theater_id, performance_date) -- cant have same show twice same day
);

create table ticket (
	ticket_id int primary key auto_increment,
    customer_id int not null,
    seat_id int not null,
    performance_id int not null,
    constraint fk_ticket_customer_id
			foreign key (customer_id)
			references customer(customer_id),
    constraint fk_ticket_seat_id
			foreign key (seat_id)
			references seat(seat_id),
	constraint fk_ticket_performance_id
		foreign key (performance_id)
        references `performance`(performance_id)
);

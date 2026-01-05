drop database if exists crowd_funding_fulfillment;
create database crowd_funding_fulfillment;
use crowd_funding_fulfillment;

create table sales_channel (
	sales_channel_id int primary key auto_increment,
    sales_channel_name varchar(50)
);

create table shipping_zone (
	shipping_zone_id int primary key auto_increment,
    title varchar(25) not null
);

create table country (
	country_id int primary key auto_increment,
    country_iso varchar(10) not null,
    country_name varchar(50) not null
);

create table company_type (
	company_type_id int primary key auto_increment,
    label varchar(150) not null unique
);

create table company (
	company_id int primary key auto_increment,
    company_name varchar(150) not null,
    phone varchar(25),
    email_address varchar(250),
    company_type_id int not null,
    website varchar(250) null,
    facebook varchar(250) null,
    instagram varchar(50) null,
    twitter varchar(50) null,
    created_at timestamp,
    deactivated_at timestamp,
    constraint fk_company_company_type
		foreign key (company_type_id)
        references company_type(company_type_id)
);

create table contact (
    contact_id int primary key auto_increment,
	full_name varchar(150) not null,
    email_address varchar(150),
    phone varchar(25),
    website varchar(250) null,
    facebook varchar(250) null,
    youtube varchar(250) null,
    twitter varchar(50) null,
    instagram varchar(50) null,
    created_at timestamp not null,
    vat_id varchar(150) null,
    deactivated_at timestamp
);

create table address (
	address_id int primary key auto_increment,
    address_line_1 varchar(250) not null,
    address_line_2 varchar(250) null,
    postal_code varchar(25) not null,
    city varchar(50) not null,
    state_province_region varchar(50) not null,
    country_id int not null,
    deactivated_at timestamp,
    constraint fk_address_country_id
		foreign key (country_id)
        references country(country_id)
);

create table company_contact (
	company_id int not null,
    contact_id int not null,
    title varchar(150) not null,
    start_date date,
    end_date date,
    constraint fk_company_contact_company_id
		foreign key (company_id)
        references company(company_id),
    constraint fk_company_contact_contact_id
		foreign key (contact_id)
        references contact(contact_id)
);

create table product_line (
	product_line_id int primary key auto_increment,
    title varchar(50) not null,
    release_date date,
    crowdfunding_date date
);

create table contact_address (
	contact_id int not null,
    address_id int not null,
    address_type varchar(25) not null default 'DEFAULT',
    constraint fk_contact_address_contact_id
		foreign key (contact_id)
        references contact(contact_id),
    constraint fk_contact_address_address_id
		foreign key (address_id)
        references address(address_id)
);
    
create table product (
	product_id int primary key auto_increment,
    product_line_id int not null,
    company_id int,
    sku varchar(15) not null,
    ean varchar(25),
    title varchar(150) not null,
    product_description text not null,
    grams int not null default 0,
    msrp decimal(8,2) not null default 0,
    backer_price decimal(8,2) not null default 0,
    late_pledge_price decimal(8,2) not null default 0,
    preorder_price decimal(8,2) not null default 0,
    height_millimeters int not null default 0,
    width_millimeters int not null default 0,
    length_millimeters int not null default 0,
    stock int not null default 0,
    domestic bit not null default 0,
    disabled_date timestamp,
    constraint uq_product_sku
		unique(sku),
	constraint fk_product_company_id
		foreign key (company_id)
        references company(company_id),
	constraint fk_product_product_line_id
		foreign key (product_line_id)
        references product_line(product_line_id)
);

create table contact_order (
	contact_order_id int primary key auto_increment,
    sales_channel_id int,
    order_id varchar(50) unique,
    contact_id int,
    email_address varchar(250) null,
    total_cost decimal(6,2) not null default 0,
    shipping_cost decimal(6,2) not null default 0,
    total_weight decimal(4,2) not null,
    full_name varchar(150) not null,
    vat_id varchar(150) null,
    vat_invoice varchar(150) null,
    phone varchar(20) null,
    created_at timestamp not null,
    late_pledge bit not null default 0,
    shipping_zone_id int not null,
    local_pickup bit default 0,
    fulfilled_date date,
    order_status varchar(25) not null default 'CART',
    deactivated_at timestamp,
    constraint fk_contact_order_sales_channel_id
		foreign key (sales_channel_id)
        references sales_channel(sales_channel_id),
    constraint fk_contact_order_contact_id
		foreign key (contact_id)
        references contact(contact_id),
    constraint fk_contact_order_shipping_zone_id
		foreign key (shipping_zone_id)
        references shipping_zone(shipping_zone_id)
);

create table order_address (
	order_address_id int primary key auto_increment,
    address_id int not null,
    contact_order_id int not null,
    address_type varchar(25) not null default 'SHIPPING',
    constraint fk_order_address_order_id
		foreign key (contact_order_id)
        references contact_order(contact_order_id),
	constraint fk_order_address_address_id
		foreign key (address_id)
        references address(address_id)
);

create table contact_order_product (
	contact_order_product_id int primary key auto_increment,
	contact_order_id int not null,
    product_id int not null,
    count int not null default 1,
    price_per_unit decimal(8,2),
    constraint fk_contact_order_product_order_id
		foreign key (contact_order_id)
        references contact_order(contact_order_id),
	constraint fk_contact_order_product_product_id
		foreign key (product_id)
        references product(product_id)
);

create table print_run (
	print_run_id int primary key auto_increment,
    manufacturing_company_id int not null,
    quote_date date,
    signed_date date,
    manufacturing_started_date date,
    completed_date date,
    constraint fk_print_run_manufacturing_company_id
		foreign key (manufacturing_company_id)
        references company(company_id)
);

create table print_run_product (
	print_run_id int not null,
    product_id int not null,
    quantity int not null,
    unit_cost decimal(8,3) not null default 0,
    landed_cost decimal(8,3) not null default 0,
    mould_cost decimal(8,3) not null default 0,
    sample_cost decimal(8,3) not null default 0,
    constraint pk_print_run_product_print_run_id_product_id
		primary key (print_run_id, product_id),
    constraint fk_print_run_product_print_run_id
		foreign key (print_run_id)
        references print_run(print_run_id),
    constraint fk_print_run_product_product_id
		foreign key (product_id)
        references product(product_id)
);

create table warehouse (
	warehouse_id int primary key auto_increment,
    company_id int not null,
    country_id int not null,
    warehouse_name varchar(150) not null,
    constraint fk_warehouse_company_id
		foreign key (company_id)
        references company(company_id),
    constraint fk_warehouse_country_id
		foreign key (country_id)
        references country(country_id)
);

create table warehouse_product (
	warehouse_product_id int primary key auto_increment,
    warehouse_id int not null,
	product_id int not null,
    stock int not null default 0,
    constraint fk_warehouse_product_warehouse_id
		foreign key (warehouse_id)
        references warehouse(warehouse_id),
    constraint fk_warehouse_product_product_id
		foreign key (product_id)
        references product(product_id)
);
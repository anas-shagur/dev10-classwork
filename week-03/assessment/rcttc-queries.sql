use rcttc;

-- Find all performances in the last quarter of 2024 (Oct. 1 2024 - Dec. 31 2024)
select distinct p.performance_date, s.show_name
from performance p
join `show` s on p.show_id = s.show_id
join theater t on p.theater_id = t.theater_id
where p.performance_date between '2024-10-01' and '2024-12-31';

-- List customers without duplication
select distinct * from customer;

-- Find all customers without a .com email address
select *
from customer
where email not like '%.com';

-- Find the three cheapest shows
select s.show_name, p.performance_date, p.ticket_price
from `show` s
join performance p on s.show_id = p.show_id
order by p.ticket_price asc
limit 3;

-- List customers and the show they're attending with no duplication
select distinct c.first_name, c.last_name, sh.show_name
from customer c
join ticket tk on c.customer_id = tk.customer_id
join performance p on tk.performance_id = p.performance_id
join `show` sh on p.show_id = sh.show_id
order by c.last_name;

-- List customer, show, theater, and seat number in one query
select
    c.first_name,
    c.last_name,
    sh.show_name,
    t.theater_name,
    s.seat_name
from ticket tk
join customer c on tk.customer_id = c.customer_id
join performance p on tk.performance_id = p.performance_id
join `show` sh on p.show_id = sh.show_id
join theater t on p.theater_id = t.theater_id
join seat s on tk.seat_id = s.seat_id;

-- Find customers without an address
select *
from customer
where address is null or address = '';

-- Recreate the denormalized data with a single query
select
    c.first_name as customer_first,
    c.last_name as customer_last,
    c.email as customer_email,
    c.phone as customer_phone,
    c.address as customer_address,
    s.seat_name as seat,
    sh.show_name as `show`,
    p.ticket_price,
    p.performance_date as `date`,
    t.theater_name as theater,
    t.address as theater_address,
    t.phone as theater_phone,
    t.email as theater_email
from ticket tk
join customer c on tk.customer_id = c.customer_id
join performance p on tk.performance_id = p.performance_id
join `show` sh on p.show_id = sh.show_id
join theater t on p.theater_id = t.theater_id
join seat s on tk.seat_id = s.seat_id;

-- Count total tickets purchased per customer
select
    c.first_name,
    c.last_name,
    count(tk.ticket_id) tickets_purchased
from customer c
join ticket tk on c.customer_id = tk.customer_id
group by c.customer_id;

-- Calculate the total revenue per show based on tickets sold
select
    sh.show_name,
    sum(p.ticket_price) total_revenue
from ticket tk
join performance p on tk.performance_id = p.performance_id
join `show` sh on p.show_id = sh.show_id
group by sh.show_id;

-- Calculate the total revenue per theater based on tickets sold
select
    t.theater_name,
    sum(p.ticket_price) total_revenue
from ticket tk
join performance p on tk.performance_id = p.performance_id
join theater t on p.theater_id = t.theater_id
group by t.theater_id;

-- Who is the biggest supporter of RCTTC? Who spent the most in 2024?
select
    c.first_name,
    c.last_name,
    sum(p.ticket_price)
from ticket tk
join customer c on tk.customer_id = c.customer_id
join performance p on tk.performance_id = p.performance_id
group by c.customer_id, c.first_name, c.last_name
order by sum(p.ticket_price) desc
limit 1;

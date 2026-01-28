-- select distinct customer_first, customer_last, customer_email, customer_phone, customer_address
-- 	from rcttc_raw.rcttc_data;

insert into rcttc.customer(first_name, last_name, email, phone, address)
	select distinct customer_first, customer_last, customer_email, customer_phone, customer_address
	from rcttc_raw.rcttc_data;
    
-- select * from rcttc.customer; 

-- select distinct theater, theater_address, theater_phone, theater_email
-- 	from rcttc_raw.rcttc_data;
    
insert into rcttc.theater(theater_name, address, phone, email)
	select distinct theater, theater_address, theater_phone, theater_email
	from rcttc_raw.rcttc_data;

-- select * from rcttc.theater;

-- select distinct rd.seat, th.theater_id 
-- 	from rcttc_raw.rcttc_data rd
-- 	inner join rcttc.theater th on rd.theater = th.theater_name;

insert into rcttc.seat(seat_name, theater_id)
	select distinct rd.seat, th.theater_id 
	from rcttc_raw.rcttc_data rd
	join rcttc.theater th on rd.theater = th.theater_name;
    
-- select * from rcttc.seat;

-- select distinct rd.`show` 
-- 	from rcttc_raw.rcttc_data rd;

insert into rcttc.`show`(show_name)
	select distinct rd.`show` 
	from rcttc_raw.rcttc_data rd;
    
-- select * from rcttc.`show`;

-- select distinct sh.show_id, th.theater_id, str_to_date(rd.`date`, '%Y-%m-%d'), rd.ticket_price
-- 	from rcttc_raw.rcttc_data rd
-- 	join rcttc.`show` sh
-- 	on rd.`show` = sh.show_name
-- 	join rcttc.theater th
-- 	on rd.theater = th.theater_name;

insert into rcttc.performance(show_id, theater_id, performance_date, ticket_price)
	select distinct sh.show_id, th.theater_id, str_to_date(rd.`date`, '%Y-%m-%d'), rd.ticket_price
	from rcttc_raw.rcttc_data rd
	join rcttc.`show` sh
	on rd.`show` = sh.show_name
	join rcttc.theater th
	on rd.theater = th.theater_name;

-- select * from rcttc.performance;

-- select c.customer_id, s.seat_id, p.performance_id 
-- 	from rcttc_raw.rcttc_data rd
-- 	join rcttc.customer c
-- 	on rd.customer_email = c.email
-- 	join rcttc.theater th
-- 	on rd.theater = th.theater_name
-- 	join rcttc.seat s
-- 	on rd.seat = s.seat_name
-- 	and s.theater_id = th.theater_id
-- 	join rcttc.`show` sh
-- 	on rd.`show` = sh.show_name
-- 	join rcttc.performance p
-- 	on p.show_id = sh.show_id
-- 	and p.theater_id = th.theater_id
-- 	and p.performance_date = str_to_date(rd.`date`, '%Y-%m-%d');

insert into rcttc.ticket(customer_id, seat_id, performance_id)
	select c.customer_id, s.seat_id, p.performance_id
	from rcttc_raw.rcttc_data rd
	join rcttc.customer c
	on rd.customer_email = c.email
	join rcttc.theater th
	on rd.theater = th.theater_name
	join rcttc.seat s
	on rd.seat = s.seat_name
	and s.theater_id = th.theater_id
	join rcttc.`show` sh
	on rd.`show` = sh.show_name
	join rcttc.performance p
	on p.show_id = sh.show_id
	and p.theater_id = th.theater_id
	and p.performance_date = str_to_date(rd.`date`, '%Y-%m-%d');
    
-- select * from rcttc.ticket;

use rcttc;

-- Update performance price
update performance p
join `show` s on p.show_id = s.show_id
join theater t on p.theater_id = t.theater_id
set p.ticket_price = 22.25
where s.show_name = 'The Sky Lit Up'
  and t.theater_name = 'Little Fitz'
  and p.performance_date = '2024-03-01';

-- confirm was updated 
-- select
--     s.show_name,
--     t.theater_name,
--     p.performance_date,
--     p.ticket_price
-- from performance p
-- join `show` s on p.show_id = s.show_id
-- join theater t on p.theater_id = t.theater_id
-- where s.show_name = 'The Sky Lit Up'
--   and t.theater_name = 'Little Fitz'
--   and p.performance_date = '2024-03-01';


-- view occupied seats by name
-- select
--     s.seat_name,
--     c.first_name,
--     c.last_name
-- from ticket tk
-- join customer c on tk.customer_id = c.customer_id
-- join seat s on tk.seat_id = s.seat_id
-- join theater t on s.theater_id = t.theater_id
-- join performance p on tk.performance_id = p.performance_id
-- join `show` sh on p.show_id = sh.show_id
-- where t.theater_name = 'Little Fitz'
--   and sh.show_name = 'The Sky Lit Up'
--   and p.performance_date = '2024-03-01'
-- order by s.seat_name;


-- Moves occupant of C2 to A1 then moves all other occupants up one seat which puts all groups in the same rows
update ticket tk
join seat s on tk.seat_id = s.seat_id
join performance p on tk.performance_id = p.performance_id
join theater t on p.theater_id = t.theater_id
join `show` sh on p.show_id = sh.show_id
set tk.seat_id = case s.seat_name
    when 'C2' then (select seat_id from seat where seat_name = 'A1' and theater_id = t.theater_id)
    when 'C1' then (select seat_id from seat where seat_name = 'C2' and theater_id = t.theater_id)
    when 'B4' then (select seat_id from seat where seat_name = 'C1' and theater_id = t.theater_id)
    when 'B3' then (select seat_id from seat where seat_name = 'B4' and theater_id = t.theater_id)
    when 'B2' then (select seat_id from seat where seat_name = 'B3' and theater_id = t.theater_id)
    when 'B1' then (select seat_id from seat where seat_name = 'B2' and theater_id = t.theater_id)
    when 'A4' then (select seat_id from seat where seat_name = 'B1' and theater_id = t.theater_id)
    when 'A3' then (select seat_id from seat where seat_name = 'A4' and theater_id = t.theater_id)
    when 'A2' then (select seat_id from seat where seat_name = 'A3' and theater_id = t.theater_id)
    when 'A1' then (select seat_id from seat where seat_name = 'A2' and theater_id = t.theater_id)
    else tk.seat_id
end
where t.theater_name = 'Little Fitz'
  and sh.show_name = 'The Sky Lit Up'
  and p.performance_date = '2024-03-01'
  and s.seat_name in ('A1','A2','A3','A4','B1','B2','B3','B4','C1','C2');


-- Update jamie swindles phone number
update customer
set phone = '1-801-EAT-CAKE'
where first_name = 'Jammie'
  and last_name = 'Swindles'
  and phone = '801-514-8648';

-- confirm was updated
-- select * from customer
-- where first_name = 'Jammie'
--   and last_name = 'Swindles'

-- find all single ticket reservations
-- select c.customer_id
-- from ticket tk
-- join customer c on tk.customer_id = c.customer_id
-- join seat s on tk.seat_id = s.seat_id
-- join theater t on s.theater_id = t.theater_id
-- where t.theater_name = '10 Pin'
-- group by c.customer_id
-- having count(*) = 1;  

-- Delete all single ticket reservations
delete tk
from ticket tk
join seat s on tk.seat_id = s.seat_id
join theater t on s.theater_id = t.theater_id
where t.theater_name = '10 Pin'
  and tk.customer_id in (
      select customer_id
      from (
          select c.customer_id
          from ticket tk2
          join customer c on tk2.customer_id = c.customer_id
          join seat s2 on tk2.seat_id = s2.seat_id
          join theater t2 on s2.theater_id = t2.theater_id
          where t2.theater_name = '10 Pin'
          group by c.customer_id
          having count(*) = 1
      ) x
  );

-- Delete all tickets booked by Liv Egle then delete Live Egle from the customer records
delete tk
from ticket tk
join customer c on tk.customer_id = c.customer_id
where c.first_name = 'Liv'
  and c.last_name = 'Egle';

delete from customer
where first_name = 'Liv'
  and last_name = 'Egle';


select * from customer;
select * from theater;
select * from `show`;
select * from seat;
select * from ticket;
select * from performance;

use crowd_funding_fulfillment;

-- Use subqueries to work through these exercises.

-- 1. Select order_id, email_address and total_cost from 
-- contact_order where the total cost is above average.
-- Expected: 315 rows, 3 column

select
	order_id,
    email_address,
    total_cost
from contact_order
where total_cost > (select avg(total_cost) from contact_order);

-- 2. Find contacts that have no contact_order records
-- Hint: use a subquery in 'not exists'
-- Expected: 15 rows

select 
	c.contact_id, 
    c.full_name
from contact c
where not exists (
    select 1 
    from contact_order co 
    where co.contact_id = c.contact_id
);

-- 3. Select title, sku, 'total_sold', and 'total_produced'
-- from product. 
-- 'total_sold' is a subquery on contact_order_product
-- 'total_produced' is a subquery on print_run_product
-- Expected: 44 rows

select 
    p.product_id,
    p.title,
    (select sum(cop.count) from contact_order_product cop where cop.product_id = p.product_id) as total_sold,
    (select sum(prp.quantity) from print_run_product prp where prp.product_id = p.product_id) as total_manufactured
from product p;

-- 4. Select order_id from contact_order, product sku from 
-- product, and 'product_count': a count of the products associated with the 
-- order from contact_order_product. Return only results for orders that 
-- include the most expensive product (highest msrp). 
-- Order results by 'product_count' desc. 
-- Hint: use a subquery in the `select` statement for 'product_count'
-- and a subquery in the `where` clause to filter by highest MSRP
-- Expected: 296 rows, 3 columns. 
-- Row 1: '434670T', 'DAG0101', 23

select
	o.order_id,
    p.sku,
    (
		select 
			count(product_id)
		from contact_order_product
        where contact_order_id = o.contact_order_id
    ) as product_count
from contact_order o
join contact_order_product op on op.contact_order_id = o.contact_order_id
join product p on p.product_id = op.product_id
where p.msrp = (select max(msrp) from product)
order by product_count desc;

-- 5. Select order_id, full_name, and email_address
-- from contact_order. Use subqueries in the `where` 
-- clause to filter to include only contacts that have 
-- multiple orders and include only the most recent order.
-- Expected: 57 rows

select 
	co.order_id, 
	co.full_name, 
    co.email_address
from contact_order co
where co.created_at = (
    select max(created_at)
    from contact_order
    where contact_id = co.contact_id
)
and (
	select count(contact_order_id) 
    from contact_order 
    where contact_id = co.contact_id
) > 1
order by order_id;


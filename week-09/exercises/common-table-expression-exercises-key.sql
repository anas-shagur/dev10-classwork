use crowd_funding_fulfillment;

-- Use a common table expressions (CTEs) to work through these exercises.

-- 1. Define a CTE called 'order_summary'. Include columns:
-- order_id, full_name, email_address, total_cost, and the
-- count of all products associated with the order as 'order_items'.
-- Select everything from 'order_summary'
-- Expected: 760 rows, 5 columns

with order_summary as (
	select
		o.order_id,
        o.full_name,
        o.email_address,
        o.total_cost,
        count(cop.contact_order_product_id) as order_items
	from contact_order o
    join contact_order_product cop on cop.contact_order_id = o.contact_order_id
    group by order_id, o.full_name, o.email_address, o.total_cost
)
select * from order_summary;

-- 2. Use the CTE defined in exercise 1. Select the top 10 by number of
-- order items.
-- Expected: 10 rows, 5 columns, order_items range from 23-16.

with order_summary as (
	select
		o.order_id,
        o.full_name,
        o.email_address,
        o.total_cost,
        count(cop.contact_order_product_id) as order_items
	from contact_order o
    join contact_order_product cop on cop.contact_order_id = o.contact_order_id
    group by order_id, o.full_name, o.email_address, o.total_cost
)
select * from order_summary
order by order_items desc
limit 10;

-- 3. Define a CTE called 'product_unit_costs'. The query should
-- select product_id and sku from product, unit_cost and print_run_id
-- from product_print_run, and completed_date from print_run.
-- Select * from 'product_unit_costs
-- Expected: 28 rows

with product_unit_costs as (
	select
		p.product_id,
        p.sku,
        pr.print_run_id,
        pr.completed_date,
        prp.unit_cost
	from product p
    join print_run_product prp on prp.product_id = p.product_id
    join print_run pr on pr.print_run_id = prp.print_run_id
)
select * from product_unit_costs;

-- 4. Define a CTE called 'latest_product_print_runs'. The query 
-- should select product_id from product, unit_cost from print_run_product,
-- and print_run_id from print_run. 
-- Use a subquery to filter only the latest print run (max completed_date)
-- that includes each product. Select * from 'latest_product_print_runs'
-- Expected: 23 rows

with latest_product_print_runs as (
	select
		p.product_id,
        prp.unit_cost,
        pr.print_run_id
	from product p
    join print_run_product prp on prp.product_id = p.product_id
    join print_run pr on pr.print_run_id = prp.print_run_id
    where pr.completed_date = (
		select max(completed_date) 
        from print_run 
        join print_run_product on print_run_product.print_run_id = print_run.print_run_id
        and print_run_product.product_id = p.product_id
    )
)
select * from latest_product_print_runs;

-- 5. Copy the CTEs from the previous two exercises here. Select
-- product_id, sku, and unit_cost from product_unit_costs for each 
-- product, but only for the most recent print_run that included 
-- that product. Order by sku.
-- Expected: 23 rows, 3 columns
-- First row: '1', 'DAG0101','20.710'
-- Last row: '39', 'DAG0233', '0.570'

with product_unit_costs as (
	select
		p.product_id,
        p.sku,
        pr.print_run_id,
        pr.completed_date,
        prp.unit_cost
	from product p
    join print_run_product prp on prp.product_id = p.product_id
    join print_run pr on pr.print_run_id = prp.print_run_id
), 
latest_product_print_runs as (
	select
		p.product_id,
        pr.print_run_id
	from product p
    join print_run_product prp on prp.product_id = p.product_id
    join print_run pr on pr.print_run_id = prp.print_run_id
    where pr.completed_date = (
		select max(completed_date) 
        from print_run 
        join print_run_product on print_run_product.print_run_id = print_run.print_run_id
        and print_run_product.product_id = p.product_id
    )
)
select 
	puc.product_id, 
    puc.sku, 
    puc.unit_cost
from product_unit_costs puc
join latest_product_print_runs pr on pr.print_run_id = puc.print_run_id
	and pr.product_id = puc.product_id
order by puc.sku;

-- 6. Define a CTE that select contact_order_id and total_cost 
-- from the top 10 orders by total_cost. Call it 'top_ten_orders'.
-- Select * from top_ten_orders
-- Expected: 10 rows, 2 columns
-- Row 1: '146', '750.00'

with top_ten_orders as (
	select 
		contact_order_id,
        total_cost
	from contact_order
    order by total_cost desc
    limit 10
)
select * from top_ten_orders;

-- 7. Using the CTE top_ten_orders defined in the last exercise,
-- join contact_order_product. Select contact_order_id and total_cost
-- from top_ten_orders, and select product_id and count from 
-- contact_order_product.
-- Expect: 133 rows, 4 columns

with top_ten_orders as (
	select 
		contact_order_id,
        total_cost
	from contact_order
    order by total_cost desc
    limit 10
)
select 
	tt.contact_order_id,
    tt.total_cost,
    p.product_id,
    p.count
from top_ten_orders tt
join contact_order_product p on p.contact_order_id = tt.contact_order_id;

-- 8. Bring together the CTEs product_unit_costs, 
-- latest_product_print_runs, and top_ten_orders. Select 
-- contact_order_id and total_cost from top_ten_orders. 
-- Join contact_order_product and select the count. 
-- Join latest_product_print_runs and product_unit_costs
-- select sku and the product of product_unit_costs.unit_cost 
-- contact_order_product.count as 'total_unit_cost'.
-- Expected: 103 rows, 
-- 5 columns (contact_order_id, total_cost, sku, count, total_unit_cost)

with product_unit_costs as (
	select
		p.product_id,
        p.sku,
        pr.print_run_id,
        pr.completed_date,
        prp.unit_cost
	from product p
    join print_run_product prp on prp.product_id = p.product_id
    join print_run pr on pr.print_run_id = prp.print_run_id
), 
latest_product_print_runs as (
	select
		p.product_id,
        pr.print_run_id
	from product p
    join print_run_product prp on prp.product_id = p.product_id
    join print_run pr on pr.print_run_id = prp.print_run_id
    where pr.completed_date = (
		select max(completed_date) 
        from print_run 
        join print_run_product on print_run_product.print_run_id = print_run.print_run_id
        and print_run_product.product_id = p.product_id
    )
),
top_ten_orders as (
	select 
		contact_order_id,
        total_cost
	from contact_order
    order by total_cost desc
    limit 10
)
select
	tto.contact_order_id,
    tto.total_cost,
    puc.sku,
    cop.count,
    cop.count * puc.unit_cost as total_unit_cost
from top_ten_orders tto
join contact_order_product cop on cop.contact_order_id = tto.contact_order_id
join latest_product_print_runs lpr on lpr.product_id = cop.product_id
join product_unit_costs puc on puc.product_id = cop.product_id 
	and puc.print_run_id = lpr.print_run_id;

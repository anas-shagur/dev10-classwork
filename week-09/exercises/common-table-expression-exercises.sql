use crowd_funding_fulfillment;

-- Use a common table expressions (CTEs) to work through these exercises.

-- 1. Define a CTE called 'order_summary'. Include columns:
-- order_id, full_name, email_address, total_cost, and the
-- count of all products associated with the order as 'order_items'.
-- Select everything from 'order_summary'
-- Expected: 760 rows, 5 columns

-- 2. Use the CTE defined in exercise 1. Select the top 10 by number of
-- order items.
-- Expected: 10 rows, 5 columns, order_items range from 23-16.

-- 3. Define a CTE called 'product_unit_costs'. The query should
-- select product_id and sku from product, unit_cost and print_run_id
-- from product_print_run, and completed_date from print_run.
-- Select * from 'product_unit_costs
-- Expected: 28 rows

-- 4. Define a CTE called 'latest_product_print_runs'. The query 
-- should select product_id from product, unit_cost from print_run_product,
-- and print_run_id from print_run. 
-- Use a subquery to filter only the latest print run (max completed_date)
-- that includes each product. Select * from 'latest_product_print_runs'
-- Expected: 23 rows

-- 5. Copy the CTEs from the previous two exercises here. Select
-- product_id, sku, and unit_cost from product_unit_costs for each 
-- product, but only for the most recent print_run that included 
-- that product. Order by sku.
-- Expected: 23 rows, 3 columns
-- First row: '1', 'DAG0101','20.710'
-- Last row: '39', 'DAG0233', '0.570'

-- 6. Define a CTE that select contact_order_id and total_cost 
-- from the top 10 orders by total_cost. Call it 'top_ten_orders'.
-- Select * from top_ten_orders
-- Expected: 10 rows, 2 columns
-- Row 1: '146', '750.00'

-- 7. Using the CTE top_ten_orders defined in the last exercise,
-- join contact_order_product. Select contact_order_id and total_cost
-- from top_ten_orders, and select product_id and count from 
-- contact_order_product.
-- Expect: 133 rows, 4 columns

-- 8. Bring together the CTEs product_unit_costs, 
-- latest_product_print_runs, and top_ten_orders. Select 
-- contact_order_id and total_cost from top_ten_orders. 
-- Join contact_order_product and select the count. 
-- Join latest_product_print_runs and product_unit_costs
-- select sku and the product of product_unit_costs.unit_cost 
-- contact_order_product.count as 'total_unit_cost'.
-- Expected: 103 rows, 
-- 5 columns (contact_order_id, total_cost, sku, count, total_unit_cost)

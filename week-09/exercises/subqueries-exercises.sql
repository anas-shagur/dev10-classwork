use crowd_funding_fulfillment;

-- Use subqueries to work through these exercises.

-- 1. Select order_id, email_address and total_cost from 
-- contact_order where the total cost is above average.
-- Expected: 315 rows, 3 column

-- 2. Find contacts that have no contact_order records
-- Hint: use a subquery in 'not exists'
-- Expected: 15 rows

-- 3. Select title, sku, 'total_sold', and 'total_produced'
-- from product. 
-- 'total_sold' is a subquery on contact_order_product
-- 'total_produced' is a subquery on print_run_product
-- Expected: 44 rows

-- 4. Select order_id from contact_order, product sku from 
-- product, and 'product_count': a count of the products associated with the 
-- order from contact_order_product. Return only results for orders that 
-- include the most expensive product (highest msrp). 
-- Order results by 'product_count' desc. 
-- Hint: use a subquery in the `select` statement for 'product_count'
-- and a subquery in the `where` clause to filter by highest MSRP
-- Expected: 296 rows, 3 columns. 
-- Row 1: '434670T', 'DAG0101', 23

-- 5. Select order_id, full_name, and email_address
-- from contact_order. Use subqueries in the `where` 
-- clause to filter to include only contacts that have 
-- multiple orders and include only the most recent order.
-- Expected: 57 rows

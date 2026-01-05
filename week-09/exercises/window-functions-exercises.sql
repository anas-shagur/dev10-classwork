use crowd_funding_fulfillment;

-- Use window functions to work through exercises.

-- 1. Rank products by weight in grams, starting with the lightest. 
-- Select sku and 'weight_rank'. Ignore products that have 0 grams.
-- Expected: 41 rows, 2 columns
-- First row: 'DAG0235','1'

-- 2. Rank products by cubic millimeters from largest to smallest.
-- Select sku and 'cubic_millimeters' and 'size_rank'. Make sure 
-- there are no gaps in the rank number.
-- 'cubic_millimeters' is the product of length, height, and width.
-- Expected: 44 rows, 3 columns
-- Highest rank: 24

-- 3. Rank products by total number sold, largest to smallest. 
-- Select sku, the total quantity sold as 'total_sold', and the 
-- percent rank of the quantity sold as 'sales_percent_rank'.
-- 'total_sold' can be aggregated from the contact_order_product table.
-- Expected result: 38 rows, 3 columns
-- First row: 'HOLO2022', 1, 0
-- Last row: 'DAG0235', 512, 1

-- 4. Select order_id, total_cost, and a running total of total_cost
-- by created date as 'running_total'.
-- Filter out orders where total_cost is 0.
-- Expected: 709 rows, 3 columns
-- Last row: '32364500','39.00','73855.06'

-- 5. Select order_id, total_cost, the name of the month of created_at,
-- and the moving average of total_cost as 'sales_average'. For the 
-- moving average, order by created_at and define the frame as between 
-- 15 days before and the current row. Select records from 2023 where 
-- the total_cost is greater than 0.
-- Hint: use `monthname()` 
-- Expected: 413 rows, 4 columns
-- First row: 'g3CwFIxpQ9IoLZciLJXVtBLzlvFZY', '20.99', 'February', '60.490000'
-- Last row: '32364500', '39.00', 'September', '77.903144'

-- 6. Select full_name, sales_channel_name, total_cost, and the maximum 
-- and average total_cost from contact_order and sales_channel. 
-- Partition the max total_cost and avg using sales_channel and
-- ordered by the contact_order sales_channel_id. Filter out orders from 
-- contacts that only have one order (requires a subquery).
-- Expected: 111 rows, 5 columns
-- First row: 'Nehemiah Aizlewood','Squarespace','259.95','82.453750','278.36'

-- 7. Refactor the solution to the previous exercise using a 
-- single named window for the window functions.
-- Expected: 111 rows, 5 columns
-- First row: 'Nehemiah Aizlewood','Squarespace','259.95','82.453750','278.36'

use crowd_funding_fulfillment;

-- 1. Select company_type_id, label, and 'classification' from company_type. 
-- Classifications are: 
-- * 'Sales' for company type 'Retailer'
-- * 'Marketing' for company type 'Content Creator'
-- * 'Competition' for company type 'Publisher'
-- * 'Production and Logistics' for all others
-- Expected: 5 rows, 3 columns

-- 2. Select order_id, full_name, and 'fulfillment_type' from contact_order
-- If local_pickup is 1, fulfillment_type should be 'Local Pickup' 
-- otherwise, it should be 'Shipment'
-- show only results where the sales channel is 'Comp' or 'GAMA'
-- Expected: 27 rows, 3 columns

-- 3. Select order_id and 'weight_class' from contact_order
-- where total_cost is greater than $200. 
-- 'weight_class' is:
-- * 'Light' for orders where total_weight is less than 5
-- * 'Medium' is less than 10
-- * 'Heavy' is 10 or greater
-- Expected: 36 rows, 2 columns

-- 4. Select order_id, email_address, and 'vat_percent'
-- from contact_order. Select only orders with addresses
-- in DE, GB, and CA. 
-- Hint: look for the country abbreviation as 
-- 'country_iso' in the country table
-- 'vat_percent' is:
-- * 19 for DE
-- * 20 for GB
-- * N/A for CA
-- Expected: 75 rows, 4 columns

-- 5. Select sku, title, 'is_domestic', and msrp from product. 
-- Use the `if` function to show "Yes/No" in the 'is_domestic' column.
-- Filter products for these conditions:
-- * The product is domestic and the backer_price is less than 70% of the msrp
-- * The product is not domestic and the backer_price is less than 75% of the msrp
-- (Hint: use a `case` statement in the `where` clause)
-- Expected: 18 rows, 3 columns

-- 6. Select average total_cost and 'sales_category' from contact_order.
-- 'sales_category' is defined as one of these three:
-- * 'Crowdfunding' for sales channels 'Gamefound', 'Backerkit', and 'Kickstarter'
-- * 'Online Sales' for sales channels 'Squarespace' and 'Square'
-- * 'Convention' for all other sales channels
-- Expected: 3 rows, 2 columns

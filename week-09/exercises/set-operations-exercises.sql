use crowd_funding_fulfillment;

-- Use set operations `union`/`union all`, `intersect`, and `except`
-- To work through these exercises.

-- 1. Select email addresses from contact,
-- contact_order, and company in one result set.
-- Expected: 647 rows

-- 2. Select email addresses from contact,
-- contact_order, and company including duplicate.
-- Expected: 1531 rows

-- 3. Select email addresses that appear in both
-- the company and contact tables.
-- Expected: 11 rows

-- 4. Select all email address from company
-- except for emails that are also in the contact table.
-- Expected: 15 rows

-- 5. Select order_id, total_cost, 'customer', and 'order_type'
-- from contact_order. Filter by contact being associated with
-- a company (company_contact).
-- 'customer' is the company name and 'order_type' is 'Business'. 
-- Use `union` to include the top 10 orders by total_cost from 
-- contact_order where the contact has no association to a company. 
-- 'customer' is the contact full_name and 'order_type' is 'Individual'.
-- Order the results by total_cost descending and limit to 10 rows.
-- Hint: build and verify the 2 queries seperately.
-- Expected: 10 rows, 4 columns
-- First row: '626121D', 750.00, 'Ann Baumaier', 'Individual'

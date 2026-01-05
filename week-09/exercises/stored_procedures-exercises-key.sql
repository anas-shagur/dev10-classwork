use crowd_funding_fulfillment;

-- 1. Create a stored procedure called 'get_companies()'
-- that returns company info. Include company type label
-- and order by company type label and company name. 
-- Include these columns:
-- * company_id
-- * company_name
-- * phone
-- * email_address
-- * company_type_id
-- * company_type (label)
-- * website
-- Call get_companies()
-- Expected: 

-- 2. Create a stored procedure that gets manufacturing company 
-- info by company_id called 'get_manufacturer_info_by_id(). It
-- should take an int parameter and return company info and a
-- summary of products they have made, if any. Columns:
-- * company_name
-- * phone
-- * email_address
-- * sku_count
-- * average_sku_msrp
-- Call the stored procedure
-- Verify that you get results for company_ids 1, 14, and 23
-- Expected: 1 row, 5 columns

-- 3. Create a stored procedure that returns 3 data sets, 'get_contact_by_id()'
-- that takes a contact_id as a parameter. The first data set is a summary
-- or contact info, the second should list addresses, and the 3rd should
-- list order.
-- Call get_contact_by_id()
-- Expected: 3 result sets
-- Expected result for contact_id = 6:
-- Result 1: 1 row
-- Result 2: 2 rows
-- Result 3: 2 rows

-- 4. Create a stored procedure that searches and returns contact 
-- information, 'search_contacts()'. The procedure takes a string 
-- parameter, 'name_email', and uses it to filter by any part of 
-- a name or email address. 
-- Call search_contacts()
-- Example result for name_email = 'dar'
-- Expected: 12 rows
-- Example result for name_email = 'eal'
-- Expected: 3 rows

-- 5. Create a stored procedure called 'get_unfulfilled_order_count()'
-- that gets the count of unfilfilled orders and sets the value of 
-- an `out` parameter, 'unfulfilled_order_count'.
-- Call get_unfulfilled_order_count()
-- Select the `out` parameter
-- Expected: 438

-- 6. Create a stored procedure, 'get_unfulfilled_orders_by_country_code()'
-- that gets a list of order that are unfulfilled by the country code
-- associated with the order's shipping address. It takes one string 
-- parameter, 'country_iso'. Include top-level details about the order 
-- as well as a count of the total items in the order and
-- the total weight of the order in kgs as 'weight_kgs'. Order results
-- by order_id.
-- Call get_unfulfilled_orders_by_country_code()
-- Example output for country code 'DE':
-- Expected: 12 rows
-- Row 1: order_id = 30251834, weight_kgs = 2.3410, item_count = 2
-- Example output for country code 'SE':
-- Expected: 5 rows
-- Row 1: order_id = 30251091, weight_kgs = 3.1450, item_count = 8

-- 7. Create a stored procedure that inserts a company into the database.
-- Set the created_at automatically using a UTC timestamp. Call it
-- 'add_company()' snd give it all the parameters required to make a valid
-- company.
-- Call add_company() and insert a new record. 
-- Select the most recent identity.
-- Expected: 34 (... 35, 36, etc..)
-- Select from company and verify that your new record was inserted.

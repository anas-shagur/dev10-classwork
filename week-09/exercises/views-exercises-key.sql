use crowd_funding_fulfillment;

-- Complete the following exercises by creating views. Write the queries
-- first and verify them before embedding them in views.

-- 1. Create a view that returns each company and their 
-- company_type label in alphabetical order by company name. 
-- Columns: company_name, company_type
-- Select * from your view
-- Expected: 32 rows, 2 columns
-- First row: 'Bards & Cards','Retailer'

create view company_company_type as
select
	c.company_name,
    t.label
from company c
join company_type t on t.company_type_id = c.company_type_id
order by c.company_name;

select * from company_company_type;

-- 2. Create a view called 'us_orders_to_ship' that can be used to 
-- ship unfulfilled US orders. The warehouse team expects a spreadsheet 
-- with 1 row per order/sku and the following specific columns:
-- * 'order id'
-- * 'recipient name'
-- * 'recipient email'
-- * 'shipping address 1' 
-- * 'shipping address 2'
-- * 'shipping city'
-- * 'shipping state/province'
-- * 'shipping country code'
-- * 'shipping postal code'
-- * 'sku'
-- * 'quantity'
-- The view should only return orders with US addresses and the
-- order_status 'PLACED_AND_PAID' and a NULL fulfilled_date, 
-- Hint: build and test your query before making a view out of it.
-- Select * from us_orders_to_ship
-- Expected: 1386 rows, 11 columns

create view us_orders_to_ship as
select
	o.order_id,
	o.full_name,
    o.email_address,
    a.address_line_1,
    a.address_line_2,
    a.city,
    a.state_province_region,
    c.country_iso,
    a.postal_code,
    p.sku,
    op.count
from contact_order o
join order_address oa on oa.contact_order_id = o.contact_order_id
join address a on a.address_id = oa.address_id
join country c on c.country_id = a.country_id
join contact_order_product op on op.contact_order_id = o.contact_order_id
join product p on p.product_id = op.product_id
where c.country_iso = 'US'
and o.order_status = 'PLACED_AND_PAID'
and o.fulfilled_date is null;

-- 3. A different format is required for fulfillment of
-- orders in the UK and Europe. Create a view, 'uk_eu_orders_to_ship'.
-- The requirements are different - they want one row per order.
-- SKUs associated with the order should be concatenated into a 
-- comma delimited string with the count of each sku per order. 
-- Example: 'DAG0101x1, DAG0103x1, ...' etc. 
-- Expected columns:
-- * 'order id'
-- * 'recipient name'
-- * 'recipient email'
-- * 'shipping address 1' 
-- * 'shipping address 2'
-- * 'shipping city'
-- * 'shipping state/province'
-- * 'shipping country code'
-- * 'shipping postal code'
-- * 'order_items' <-- this is where the comma delimited SKUs go
-- The view should only return unfulfilled orders with the the order_status 
-- 'PLACED_AND_PAID' and addresses from the following country codes:
-- AN, AT, CZ, DE, DK, ES, FI, FR, GR, IE, IS, IT, MC, NO, PL, PT, SE, SK, and GB.
-- Hint: Start with the previous exercise solution and make the needed changes.
-- Hint: Look up the function `group_concat()` you will need 
-- both that and `concat(sku, 'x', count)` to get the correct format.
-- select * from uk_eu_orders_to_ship, order by full_name
-- Expected: 45 rows, 10 columns
-- Row 1: full_name: 'Antony Minton', ... order_items: 'DAG0201x1,DAG0235x1'

create view uk_eu_orders_to_ship as
select
	o.order_id,
	o.full_name,
    o.email_address,
    a.address_line_1,
    a.address_line_2,
    a.city,
    a.state_province_region,
    c.country_iso,
    a.postal_code,
    group_concat(concat(p.sku, 'x', op.count)) as order_items
from contact_order o
join order_address oa on oa.contact_order_id = o.contact_order_id
join address a on a.address_id = oa.address_id
join country c on c.country_id = a.country_id
join contact_order_product op on op.contact_order_id = o.contact_order_id
join product p on p.product_id = op.product_id
where c.country_iso in ('AN', 'AT', 'CZ', 'DE', 'DK', 'ES', 'FI', 'FR', 'GR', 'IE', 'IS', 'IT', 'MC', 'NO', 'PL', 'PT', 'SE', 'SK', 'GB')
and o.order_status = 'PLACED_AND_PAID'
and o.fulfilled_date is null
group by 
	o.order_id,
	o.full_name,
    o.email_address,
    a.address_line_1,
    a.address_line_2,
    a.city,
    a.state_province_region,
    c.country_iso,
    a.postal_code;
    
select * from uk_eu_orders_to_ship
order by full_name;

use crowd_funding_fulfillment;

-- 1. Select company_type_id, label, and 'classification' from company_type. 
-- Classifications are: 
-- * 'Sales' for company type 'Retailer'
-- * 'Marketing' for company type 'Content Creator'
-- * 'Competition' for company type 'Publisher'
-- * 'Production and Logistics' for all others
-- Expected: 5 rows, 3 columns

select * from company_type;

select
	company_type_id,
    label,
    case company_type_id
		when 4 then 'Sales'
        when 5 then 'Marketing'
        when 3 then 'Competition'
        else 'Production and Logistics'
	end as classification
from company_type;

-- 2. Select order_id, full_name, and 'fulfillment_type' from contact_order
-- If local_pickup is 1, fulfillment_type should be 'Local Pickup' 
-- otherwise, it should be 'Shipment'
-- show only results where the sales channel is 'Comp' or 'GAMA'
-- Expected: 27 rows, 3 columns

select
	o.order_id,
    o.full_name,
    case o.local_pickup
		when 1 then 'Local Pickup'
        else 'Shipment'
    end as fulfillment_type
from contact_order o
join sales_channel sc on o.sales_channel_id = sc.sales_channel_id
where sc.sales_channel_name = 'Comp'
	or sc.sales_channel_name = 'GAMA';

-- 3. Select order_id and 'weight_class' from contact_order
-- where total_cost is greater than $200. 
-- 'weight_class' is:
-- * 'Light' for orders where total_weight is less than 5
-- * 'Medium' is less than 10
-- * 'Heavy' is 10 or greater
-- Expected: 36 rows, 2 columns

select 
	o.order_id,
    case
		when o.total_weight < 5 then 'Light'
        when o.total_weight < 10 then 'Medium'
        else 'Heavy'
	end as weight_class
from contact_order o
where o.total_cost > 200;

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

select
	o.order_id,
    o.email_address,
    c.country_iso,
    case
		when c.country_iso = 'DE' then 19
        when c.country_iso = 'GB' then 20
        else 'N/A'
    end as vat_percent
from contact_order o 
join order_address oa on oa.contact_order_id = o.contact_order_id
join address a on a.address_id = oa.address_id
join country c on c.country_id = a.country_id
where c.country_iso in ('CA', 'DE', 'GB');

-- 5. Select sku, title, 'is_domestic', and msrp from product. 
-- Use the `if` function to show "Yes/No" in the 'is_domestic' column.
-- Filter products for these conditions:
-- * The product is domestic and the backer_price is less than 70% of the msrp
-- * The product is not domestic and the backer_price is less than 75% of the msrp
-- (Hint: use a `case` statement in the `where` clause)
-- Expected: 18 rows, 3 columns

select 
	p.sku,
    p.title,
    if(domestic = 1, 'Yes', 'No') as is_domestic,
    p.msrp
from product p
where
	case p.domestic 
		when 1 then p.backer_price < (0.7 * p.msrp)
		when 0 then p.backer_price < (0.75 * p.msrp)
    end;





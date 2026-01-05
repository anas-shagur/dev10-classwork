use crowd_funding_fulfillment;

-- 1. Select the current date (`date` value)
-- Expected: 1 row
select CURRENT_DATE();

-- 2. Select the current time (`time` value)
-- Expected: 1 row
select CURRENT_TIME();

-- 3. Select the current datetime (`datetime` value)
-- Expected: 1 row
select NOW();

-- 4. Select the current datetime in UTC format (`timestamp` value)
-- Expected: 1 row
select UTC_TIMESTAMP();

-- 5. Select the year of the fulfilled_date of the first row in the `contact_order` table
-- Expected: 2022
select year(fulfilled_date)
from contact_order
order by contact_order_id
limit 1;

-- 6. Select the day of the year of created_at in the most recent row in the `contact_order` table
-- Expected: 272
select DAYOFYEAR(created_at)
from contact_order
order by created_at desc
limit 1;

-- 7. Select the hour, minute, and second of the first company created
-- Expected: 13, 23, 0
select 
	hour(created_at), 
	minute(created_at),
	second(created_at)
from company
order by company_id
limit 1;

-- 8. Select `created_at`, and the date 45 days 
-- after the most recent contact_order was created
-- Expected: '2023-09-29 01:20:18', '2023-11-13 01:20:18'
select created_at, adddate(created_at, interval 45 day)
from contact_order
order by created_at desc
limit 1;

-- 9. Select `created_at` and the date 2 years prior for the first contact_order
-- Expected: '2019-11-10 00:00:00', '2017-11-10 00:00:00'
select created_at, adddate(created_at, interval 2 year)
from contact_order
order by created_at asc
limit 1;

-- 10. Select `created_at` and a `timestamp` of the most 
-- recently created company plus 106 milliseconds
-- Expected: '2023-11-08 02:47:00.106000'
select addtime(created_at, '00:00:00.106')
from company
order by created_at desc
limit 1;

-- 11. Select the number of days between the first and 
-- last `created_at` in the company table
-- (hint: use min() and max())
-- Expected: -511
select DATEDIFF(MIN(created_at), MAX(created_at))
from company;

-- 12. Select the absolute value of days using the previous query
-- Expected: 511
select ABS(DATEDIFF(MIN(created_at), MAX(created_at)))
from company;
    
-- 13. Select `year` and the number of customer orders 
-- per year. An order's year is based on its created_at,
-- not its fulfilled_date. (hint: use `count()` and `group by`)
-- Expected: 5 rows, 2 columns
select year(created_at), count(*)
from contact_order
group by year(created_at);

-- 14. Select your next birthday using `makedate()`
-- hint: first find the dayofyear of your birthday
-- Expected: 1 row
select MAKEDATE(1970, dayofyear('1970-07-31'));

-- 15. Select your next wakeup time using `maketime()`
-- Expected: 1 row
select MAKETIME(6, 30, 0);

-- 16. Select the most recent `created_at` from `company`
-- Format the date like this example: "Friday, April 26"
-- Expected: Wednesday, November 08
SELECT DATE_FORMAT(MAX(created_at), '%W, %M %d')
FROM company;

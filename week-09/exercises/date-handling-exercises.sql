use crowd_funding_fulfillment;

-- 1. Select the current date (`date` value)
-- Expected: 1 row

-- 2. Select the current time (`time` value)
-- Expected: 1 row

-- 3. Select the current datetime (`datetime` value)
-- Expected: 1 row

-- 4. Select the current datetime in UTC format (`timestamp` value)
-- Expected: 1 row

-- 5. Select the year of the fulfilled_date of the first row in the `contact_order` table
-- Expected: 2022

-- 6. Select the day of the year of created_at in the most recent row in the `contact_order` table
-- Expected: 272

-- 7. Select the hour, minute, and second of the first company created
-- Expected: 13, 23, 0

-- 8. Select `created_at`, and the date 45 days 
-- after the most recent contact_order was created
-- Expected: '2023-09-29 01:20:18', '2023-11-13 01:20:18'

-- 9. Select `created_at` and the date 2 years prior for the first contact_order
-- Expected: '2019-11-10 00:00:00', '2017-11-10 00:00:00'

-- 10. Select `created_at` and a `timestamp` of the most 
-- recently created company plus 106 milliseconds
-- Expected: '2023-11-08 02:47:00.106000'

-- 11. Select the number of days between the first and 
-- last `created_at` in the company table
-- (hint: use min() and max())
-- Expected: -511

-- 12. Select the absolute value of days using the previous query
-- Expected: 511
    
-- 13. Select `year` and the number of customer orders 
-- per year. An order's year is based on its created_at,
-- not its fulfilled_date. (hint: use `count()` and `group by`)
-- Expected: 5 rows, 2 columns

-- 14. Select your next birthday using `makedate()`
-- hint: first find the dayofyear of your birthday
-- Expected: 1 row

-- 15. Select your next wakeup time using `maketime()`
-- Expected: 1 row

-- 16. Select the most recent `created_at` from `company`
-- Format the date like this example: "Friday, April 26"
-- Expected: Wednesday, November 08

* question 1 = how many users are there. 
--> Query :
select count(DISTINCT user_id) as total_user from users;
+------------+
| total_user |
+------------+
|         10 |
+------------+


* question 2 =  how many cookies does each user have on average.
--> Query :
SELECT
       COUNT(cookie_id) * 1.0 / COUNT(DISTINCT user_id) AS avg_cookies_per_user
     FROM
       users;
+----------------------+
| avg_cookies_per_user |
+----------------------+
|              1.00000 |
+----------------------+


* question 3 = what is the unique number of visits by all users per month.
--> Query :
 select MONTH(event_time) as month, count(DISTINCT visit_id)as no_of_unique_visits from events group by month;
+-------+---------------+
| month | unique_visits |
+-------+---------------+
|     1 |             4 |
|     2 |             3 |
|     3 |             2 |
|     4 |             1 |
+-------+---------------+


* question 4 = what is the number of events for each event type.
--> Query :
 SELECT
       ei.event_name,
       COUNT(e.event_type) AS event_count
     FROM
       clique_bait.events e
     JOIN
       clique_bait.event_identifier ei ON e.event_type = ei.event_type
     GROUP BY
       ei.event_name;
+-------------+-------------+
| event_name  | event_count |
+-------------+-------------+
| Page View   |           8 |
| Add to Cart |           2 |
+-------------+-------------+


* question 5 = what is the percentage of visits which have a purchase events .
--> Query :
 SELECT
 100 * COUNT(DISTINCT CASE WHEN ei.event_name = 'purchase' THEN e.visit_id END) / COUNT(DISTINCT e.visit_id) AS pct_visits_with_purchase
 FROM events e
 JOIN event_identifier ei ON e.event_type = ei.event_type;
+--------------------------+
| pct_visits_with_purchase |
+--------------------------+
|                   0.0000 |
+--------------------------+


* question 6 = what is the percentage of visits which view the checkout page but do not have a purchase event.
--> Query :
SELECT
  COUNT(DISTINCT CASE 
    WHEN ph.page_name = 'checkout' AND ei.event_name != 'purchase' 
    THEN e.visit_id 
  END) * 100.0 / COUNT(DISTINCT e.visit_id) AS checkout_without_purchase_percentage
FROM
  events e
JOIN
  page_hierarchy ph ON e.page_id = ph.page_id
JOIN
  event_identifier ei ON e.event_type = ei.event_type;
+--------------------------------------+
| checkout_without_purchase_percentage |
+--------------------------------------+
|                              0.00000 |
+--------------------------------------+


* question 7 = what are the top 3 pages by number of views.
--> Query :
select ph.page_name, count(e.page_id) as views_count from events e join page_hierarchy ph on e.page_id = ph.page_id where e.event_type = 1 group by ph.page_name limit 3;
+----------------+-------------+
| page_name      | views_count |
+----------------+-------------+
| Tuna           |           1 |
| Crab           |           1 |
| Russian Caviar |           2 |
+----------------+-------------+


* question 9 = what are the top 3 products by purchases.
--> Query :
SELECT 
  ph.page_name AS product_name,
  COUNT(*) AS purchase_count
FROM 
  events e
JOIN 
  page_hierarchy ph ON e.page_id = ph.page_id
WHERE 
  e.event_type = 3
GROUP BY 
  ph.page_name
LIMIT 3;
Empty set (0.00 sec)


* question 8 = what is the number of views and cart adds for each product category.
--> Query :
SELECT 
  ph.product_category,
  SUM(CASE WHEN e.event_type = 1 THEN 1 ELSE 0 END) AS view_count,
  SUM(CASE WHEN e.event_type = 2 THEN 1 ELSE 0 END) AS add_to_cart_count
FROM 
  events e
JOIN 
  page_hierarchy ph ON e.page_id = ph.page_id
WHERE 
  ph.product_category IS NOT NULL
GROUP BY 
  ph.product_category;

+------------------+------------+-------------------+
| product_category | view_count | add_to_cart_count |
+------------------+------------+-------------------+
| Fish             |          2 |                 2 |
| Luxury           |          3 |                 0 |
| Shellfish        |          2 |                 0 |
+------------------+------------+-------------------+





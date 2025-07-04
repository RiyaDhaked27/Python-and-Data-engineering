* ans 1.....

 select s.customer_id, sum(m.price) from sales s join menu m on s.product_id = m.product_id group by s.customer_id;
+-------------+--------------+
| customer_id | sum(m.price) |
+-------------+--------------+
| A           |           76 |
| B           |           74 |
| C           |           36 |
+-------------+--------------+

* ans 2.......

select customer_id, count(DISTINCT order_date) from sales group by customer_id;
+-------------+----------------------------+
| customer_id | count(DISTINCT order_date) |
+-------------+----------------------------+
| A           |                          4 |
| B           |                          6 |
| C           |                          2 |

* ans 3........

SELECT s.customer_id, s.order_date, m.product_name
      FROM sales s
     JOIN menu m ON s.product_id = m.product_id
    JOIN (
        SELECT customer_id, MIN(order_date) AS first_order_date
        FROM sales
        GROUP BY customer_id
    ) AS first_orders
    ON s.customer_id = first_orders.customer_id AND s.order_date = first_orders.first_order_date;
+-------------+------------+--------------+
| customer_id | order_date | product_name |
+-------------+------------+--------------+
| A           | 2021-01-01 | sushi        |
| A           | 2021-01-01 | curry        |
| B           | 2021-01-01 | curry        |
| C           | 2021-01-01 | ramen        |
| C           | 2021-01-01 | ramen        |
+-------------+------------+--------------+

* ans 4........

SELECT 
  m.product_name,
  COUNT(*) AS total_purchases
FROM sales s
JOIN menu m ON s.product_id = m.product_id
GROUP BY m.product_name
ORDER BY total_purchases DESC
LIMIT 1;
+--------------+-----------------+
| product_name | total_purchases |
+--------------+-----------------+
| ramen        |               8 |
+--------------+-----------------+

* ans 5........

SELECT c.customer_id, m.product_name, c.purchase_count
 FROM
 ( SELECT customer_id, product_id, COUNT(*) AS purchase_count FROM sales GROUP BY customer_id, product_id) AS c
 JOIN menu m ON c.product_id = m.product_id
 WHERE c.purchase_count = (
 SELECT MAX(purchase_count) FROM (
 SELECT customer_id, product_id, COUNT(*) AS purchase_count FROM sales
 WHERE customer_id = c.customer_id GROUP BY customer_id, product_id ) AS Y
 )
 ORDER BY c.customer_id;

+-------------+--------------+----------------+
| customer_id | product_name | purchase_count |
+-------------+--------------+----------------+
| A           | ramen        |              3 |
| B           | sushi        |              2 |
| B           | curry        |              2 |
| B           | ramen        |              2 |
| C           | ramen        |              3 |
+-------------+--------------+----------------+


* ans 6......
SELECT s.customer_id, s.product_id, me.product_name
    FROM sales s
    JOIN members m ON s.customer_id = m.customer_id
    JOIN menu me ON me.product_id = s.product_id
    WHERE s.order_date >= m.join_date
    and s.order_date = (select min(s2.order_date) from sales s2 WHERE s2.customer_id = s.customer_id and s2.order_date >= m.join_date);
+-------------+------------+--------------+
| customer_id | product_id | product_name |
+-------------+------------+--------------+
| B           |          1 | sushi        |
| A           |          2 | curry        |
+-------------+------------+--------------+

* ans 7.....

.mysql> SELECT s.customer_id, s.product_id, me.product_name
    FROM sales s
    JOIN members m ON s.customer_id = m.customer_id
    JOIN menu me ON me.product_id = s.product_id
    WHERE s.order_date < m.join_date;
+-------------+------------+--------------+
| customer_id | product_id | product_name |
+-------------+------------+--------------+
| B           |          1 | sushi        |
| A           |          1 | sushi        |
| B           |          2 | curry        |
| B           |          2 | curry        |
| A           |          2 | curry        |
+-------------+------------+--------------+

* ans 8.....

 select s.customer_id, count(product_name) as total_items, sum(mu.price) as total_spent from sales s join menu mu on s.product_id = mu.product_id join members m on m.customer_id = s.customer_id where order_date < join_date group by s.customer_id, mu.product_name;
+-------------+-------------+-------------+
| customer_id | total_items | total_spent |
+-------------+-------------+-------------+
| B           |           1 |          10 |
| A           |           1 |          10 |
| B           |           2 |          30 |
| A           |           1 |          15 |
+-------------+-------------+-------------+

* ans 9......

SELECT
      s.customer_id,
      SUM(
        CASE
          WHEN m.product_name = 'sushi' THEN m.price * 20
          ELSE m.price * 10
        END
      ) AS total_points
    FROM sales s
    JOIN menu m ON s.product_id = m.product_id
    GROUP BY s.customer_id;
+-------------+--------------+
| customer_id | total_points |
+-------------+--------------+
| A           |          860 |
| B           |          940 |
| C           |          360 |
+-------------+--------------+

* ans 10.......

SELECT s.customer_id,
     SUM(
     CASE
     WHEN s.order_date BETWEEN m.join_date AND DATE_ADD(m.join_date, INTERVAL 6 DAY) THEN 20
     ELSE 10
     END
    ) AS total_points
     FROM sales s
     JOIN members m on s.customer_id = m.customer_id
     where s.order_date BETWEEN m.join_date AND '2021-01-31'
     AND s.customer_id IN ('A','B')
    Group by s.customer_id
    ORDER BY s.customer_id;
+-------------+--------------+
| customer_id | total_points |
+-------------+--------------+
| A           |           80 |
| B           |           30 |
+-------------+--------------+


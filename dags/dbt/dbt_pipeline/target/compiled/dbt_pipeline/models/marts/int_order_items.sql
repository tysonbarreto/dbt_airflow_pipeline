select
    line_items.order_item_key,
    line_items.part_key,
    line_items.line_number,
    line_items.extended_price,
    orders.order_key,
    orders.customer_key,
    orders.order_date,
    
    (-1 * line_items.extended_price * line_items.discount_percentage)::decimal(16, 2)
 as item_discount_amount
from
    dbt_db.dbt_schema.stg_tpch_orders as orders
JOIN
    dbt_db.dbt_schema.stg_tpch_line_items as line_items
ON orders.order_key = line_items.order_key

ORDER BY
    orders.order_key
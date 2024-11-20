SELECT
    *
from 
    {{ ref('fct_orders') }}
WHERE
    date(order_date) > CURRENT_DATE()
    OR date(order_date) < DATE('1990-01-01')
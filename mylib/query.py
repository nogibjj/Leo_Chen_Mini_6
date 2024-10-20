import os
from dotenv import load_dotenv
from databricks import sql

complex_query = """
WITH monthly_avg AS (
    SELECT 
        year,
        month,
        AVG(births) AS avg_births_per_month
    FROM 
        ids706_data_engineering.default.US_Births_yc687
    GROUP BY 
        year, month
)
SELECT 
    b.year,
    b.month,
    b.date_of_month,
    CASE 
        WHEN b.day_of_week = 1 THEN 'Monday'
        WHEN b.day_of_week = 2 THEN 'Tuesday'
        WHEN b.day_of_week = 3 THEN 'Wednesday'
        WHEN b.day_of_week = 4 THEN 'Thursday'
        WHEN b.day_of_week = 5 THEN 'Friday'
        WHEN b.day_of_week = 6 THEN 'Saturday'
        WHEN b.day_of_week = 7 THEN 'Sunday'
    END AS day_name,
    b.births,
    m.avg_births_per_month
FROM 
    ids706_data_engineering.default.US_Births_yc687 b
JOIN
    monthly_avg m ON b.year = m.year AND b.month = m.month
ORDER BY 
    b.year, b.month, b.date_of_month
LIMIT 50;
"""


def query():
    load_dotenv()
    with sql.connect(
        server_hostname=os.getenv("HOSTNAME"),
        http_path=os.getenv("HTTP_PATH"),
        access_token=os.getenv("KEY"),
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute(complex_query)
            result = cursor.fetchall()
            for row in result:
                print(row)
    return "query successful"
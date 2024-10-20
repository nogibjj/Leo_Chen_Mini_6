import csv
import os
from dotenv import load_dotenv
from databricks import sql


def load(dataset="data/US_births.csv"):
    payload = csv.reader(open(dataset, newline=""), delimiter=",")
    next(payload)

    load_dotenv()
    with sql.connect(
        server_hostname=os.getenv("HOSTNAME"),
        http_path=os.getenv("HTTP_PATH"),
        access_token=os.getenv("KEY"),
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                """CREATE TABLE IF NOT EXISTS US_Births_yc687
                           (year INT, month INT, date_of_month INT, 
                           day_of_week INT, births INT);
                           """
            )

            cursor.execute("SELECT * FROM US_Births_yc687")
            result = cursor.fetchall()
            if not result:
                string_sql = "INSERT INTO US_Births_yc687 VALUES"
                for i in payload:
                    string_sql += "\n" + str(tuple(i)) + ","
                string_sql = string_sql[:-1] + ";"
                cursor.execute(string_sql)

            cursor.close()
            connection.close()
    return "db loaded or already loaded"
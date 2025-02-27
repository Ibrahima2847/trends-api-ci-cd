import pandas as pd
import pyodbc

def get_db_connection():
    return pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=sqlsvr-db-trends.database.windows.net;'
        'DATABASE=trends;'
        'UID=datatrends;'
        'PWD=Tølibout2847'
    )
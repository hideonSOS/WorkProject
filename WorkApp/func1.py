import pandas as pd
import psycopg2

def input_database(id,series,syusai,start_day,end_day,price): 
    connection_config = { 
        'host': 'localhost', 
        'port': '5432', 
        'database': 'postgres', 
        'user': 'postgres', 
        'password': 'p@ssword' 
    } 
    connection = psycopg2.connect(**connection_config) 
    cursor=connection.cursor() 
    SQL = f"INSERT INTO r4table VALUES({id}, '{series}', '{syusai}', '{start_day}', '{end_day}', {price})" 
    cursor.execute(SQL) 
    connection.commit()
    # df = pd.read_sql(sql='SELECT * FROM r4table;',con=connection) 
    # print(df)
    connection.close()

def delete_database(id): 
    connection_config = { 
        'host': 'localhost', 
        'port': '5432', 
        'database': 'postgres', 
        'user': 'postgres', 
        'password': 'p@ssword' 
    } 
    connection = psycopg2.connect(**connection_config) 
    cursor=connection.cursor() 
    SQL = f"DELETE FROM r4table WHERE id = {id}" 
    cursor.execute(SQL) 
    connection.commit()

    connection.close()

def print_database(): 
    connection_config = { 
        'host': 'localhost', 
        'port': '5432', 
        'database': 'postgres', 
        'user': 'postgres', 
        'password': 'p@ssword' 
    } 
    connection = psycopg2.connect(**connection_config) 
    cursor=connection.cursor() 
    df = pd.read_sql(sql='SELECT * FROM r4table;',con=connection) 
    connection.commit()
    connection.close()
    return df
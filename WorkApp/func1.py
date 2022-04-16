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

def seiri_database():
    df = print_database()
    df['end_day'] = pd.to_datetime(df['end_day'],format='%Y-%m-%d')
    dict={
    '４月':df1.loc[df1['end_day'].dt.month==4]['price'].sum(),
    '５月':df1.loc[df1['end_day'].dt.month==5]['price'].sum(),
    '６月':df1.loc[df1['end_day'].dt.month==6]['price'].sum(),
    '７月':df1.loc[df1['end_day'].dt.month==7]['price'].sum(),
    '８月':df1.loc[df1['end_day'].dt.month==8]['price'].sum(),
    '９月':df1.loc[df1['end_day'].dt.month==9]['price'].sum(),
    '１０月':df1.loc[df1['end_day'].dt.month==10]['price'].sum(),
    '１１月':df1.loc[df1['end_day'].dt.month==11]['price'].sum(),
    '１２月':df1.loc[df1['end_day'].dt.month==12]['price'].sum(),
    '１月':df1.loc[df1['end_day'].dt.month==1]['price'].sum(),
    '２月':df1.loc[df1['end_day'].dt.month==2]['price'].sum(),
    '３月':df1.loc[df1['end_day'].dt.month==3]['price'].sum(),
}
    return dict
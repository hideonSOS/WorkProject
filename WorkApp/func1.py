import pandas as pd
import psycopg2

#接続情報^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
connection_config = { 
    'host': 'localhost', 
    'port': '5432', 
    'database': 'postgres', 
    'user': 'postgres', 
    'password': 'p@ssword' 
} 
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

def input_database(id,series,syusai,start_day,end_day,price): 
    connection = psycopg2.connect(**connection_config) 
    cursor=connection.cursor() 
    SQL = f"INSERT INTO r4table VALUES({id}, '{series}', '{syusai}', '{start_day}', '{end_day}', {price})" 
    cursor.execute(SQL) 
    connection.commit()
    # df = pd.read_sql(sql='SELECT * FROM r4table;',con=connection) 
    # print(df)
    connection.close()

def delete_database(id): 
    connection = psycopg2.connect(**connection_config) 
    cursor=connection.cursor() 
    SQL = f"DELETE FROM r4table WHERE id = {id}" 
    cursor.execute(SQL) 
    connection.commit()
    connection.close()

def print_database(): 
    connection = psycopg2.connect(**connection_config) 
    cursor=connection.cursor() 
    df = pd.read_sql(sql='SELECT * FROM r4table;',con=connection) 
    connection.commit()
    connection.close()
    return df

def seiri_database():
    df = print_database()
    df['end_day'] = pd.to_datetime(df['end_day'],format='%Y-%m-%d')
    list = ['４月','５月','６月','７月','８月','９月','１０月','１１月','１２月','１月','２月','３月']
    dict={
    'four':df.loc[df['end_day'].dt.month==4]['price'].sum(),
    'five':df.loc[df['end_day'].dt.month==5]['price'].sum(),
    'six':df.loc[df['end_day'].dt.month==6]['price'].sum(),
    'seven':df.loc[df['end_day'].dt.month==7]['price'].sum(),
    'eight':df.loc[df['end_day'].dt.month==8]['price'].sum(),
    'nine':df.loc[df['end_day'].dt.month==9]['price'].sum(),
    'ten':df.loc[df['end_day'].dt.month==10]['price'].sum(),
    'eleven':df.loc[df['end_day'].dt.month==11]['price'].sum(),
    'twelve':df.loc[df['end_day'].dt.month==12]['price'].sum(),
    'one':df.loc[df['end_day'].dt.month==1]['price'].sum(),
    'two':df.loc[df['end_day'].dt.month==2]['price'].sum(),
    'three':df.loc[df['end_day'].dt.month==3]['price'].sum(),
    'monthlist':[i for i in list]
}
    return dict
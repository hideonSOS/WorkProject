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
"""
Aqua1=['解説者','解説','MC','ディレクター','スタッフ','映像','音響','ＨＰ予想記者','配信機材一式','備品等','実況放送']
Aqua2=[37000, 43000, 53000, 32000, 20000, 32000, 32000,	32000,	9700, 7000,	6500]
Aquadf = pd.DataFrame(Aqua2).T
Aquadf.columns=Aqua1
"""
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

def input_database(id,series,syusai,start_day,end_day,price): 
    connection = psycopg2.connect(**connection_config) 
    cursor=connection.cursor() 
    SQL = f"INSERT INTO r4table VALUES({id}, '{series}', '{syusai}', '{start_day}', '{end_day}', {price})" 
    cursor.execute(SQL) 
    connection.commit()
    # df = pd.read_sql(sql='SELECT * FROM r4table;',con=connection) 
    # print(df)
    connection.close()

#r4table_2支払い関係のデータベースを入力
def input_database2(id,title,furikomi,furikomi_day,price,type,memo): 
    connection = psycopg2.connect(**connection_config) 
    cursor=connection.cursor() 
    SQL = f"INSERT INTO r4table_2 VALUES({id}, '{title}', '{furikomi}', '{furikomi_day}', {price},'{type}','{memo}')" 
    cursor.execute(SQL) 
    connection.commit()
    # df = pd.read_sql(sql='SELECT * FROM r4table;',con=connection) 
    # print(df)
    connection.close()


def delete_database(where,id): 
    connection = psycopg2.connect(**connection_config) 
    cursor=connection.cursor() 
    # SQL = f"DELETE FROM r4table WHERE id = {id}" 
    SQL = f"DELETE FROM {where} WHERE id = {id}" 
    cursor.execute(SQL) 
    connection.commit()
    connection.close()

def Weekday(day):
    from datetime import datetime
    # dt = datetime(day)
    ind = day.weekday()
    w_list = ['(月)', '(火)', '(水)', '(木)', '(金)', '(土)', '(日)']
    data = w_list[ind]
    return data

#r4_table（請求データベース接続）
def print_database(): 
    connection = psycopg2.connect(**connection_config) 
    cursor=connection.cursor() 
    df = pd.read_sql(sql='SELECT * FROM r4table;',con=connection) 
    df.sort_values('id',inplace=True)
    connection.commit()
    connection.close()
    df['end_day2']=[Weekday(i) for i in df['end_day']]
    df['start_day2']=[Weekday(i) for i in df['start_day']]
    df['price2']=[f'\\{i:,}' for i in df['price']]
    return df

#r4_table_2（支払いデータベース接続）
def print_database2(): 
    connection = psycopg2.connect(**connection_config) 
    cursor=connection.cursor() 
    df = pd.read_sql(sql='SELECT * FROM r4table_2;',con=connection) 
    df.sort_values('id',inplace=True)
    connection.commit()
    connection.close()
    df['furikomi_day2']=[Weekday(i) for i in df['furikomi_day']]
    df['price2']=[f'\\{i:,}' for i in df['price']]
    return df


    
#整理データベースメソッド→グラフ.htmlにデータを整理して送信するデーター加工
def seiri_database():
    df = print_database()
    df['end_day'] = pd.to_datetime(df['end_day'],format='%Y-%m-%d')
    df2 = print_database2()
    df2['furikomi_day'] = pd.to_datetime(df2['furikomi_day'],format='%Y-%m-%d')
    queryword1="'2022-04-01'<end_day<'2023-03-31'"
    queryword2="'2022-04-01'<furikomi_day<'2023-03-31'"
    total1 = df.query(queryword1)['price'].sum()
    total2 = df2.query(queryword2)['price'].sum()
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
    'monthlist':[i for i in list],
    'four_2':df2.loc[df2['furikomi_day'].dt.month==4]['price'].sum(),
    'five_2':df2.loc[df2['furikomi_day'].dt.month==5]['price'].sum(),
    'six_2':df2.loc[df2['furikomi_day'].dt.month==6]['price'].sum(),
    'seven_2':df2.loc[df2['furikomi_day'].dt.month==7]['price'].sum(),
    'eight_2':df2.loc[df2['furikomi_day'].dt.month==8]['price'].sum(),
    'nine_2':df2.loc[df2['furikomi_day'].dt.month==9]['price'].sum(),
    'ten_2':df2.loc[df2['furikomi_day'].dt.month==10]['price'].sum(),
    'eleven_2':df2.loc[df2['furikomi_day'].dt.month==11]['price'].sum(),
    'twelve_2':df2.loc[df2['furikomi_day'].dt.month==12]['price'].sum(),
    'one_2':df2.loc[df2['furikomi_day'].dt.month==1]['price'].sum(),
    'two_2':df2.loc[df2['furikomi_day'].dt.month==2]['price'].sum(),
    'three_2':df2.loc[df2['furikomi_day'].dt.month==3]['price'].sum(),
    'total_1':f'\\{total1:,}',
    'total_2':f'\\{total2:,}',
}
    return dict


#整理データベースメソッド→グラフ.htmlにデータを整理して送信するデーター加工
def type_print():
    Nisu=198
    queryword="'2022-04-01'<end_day<'2023-03-31'"
    zeiritu = 1.1
    Aqua1=['解説者','MC','ディレクター','スタッフ','映像','音響','ＨＰ予想記者','配信機材一式','備品等','実況放送']
    Aqua2=[80000, 53000, 32000, 20000, 32000, 32000, 32000,	9700, 7000,	6500]
    Aquadf = pd.DataFrame(Aqua2).T
    Aquadf.columns=Aqua1
    df2 = print_database2()
    dict={
        'Kaisetsu':int(Aquadf['解説者'].values*Nisu*zeiritu),
        'MC':int(Aquadf['MC'].values*Nisu*zeiritu),
        'Director':int(Aquadf['ディレクター'].values*Nisu*zeiritu),
        'Staff':int(Aquadf['スタッフ'].values*Nisu*zeiritu),
        'VisionDirector':int(Aquadf['映像'].values*Nisu*zeiritu),
        'SoundDirector':int(Aquadf['音響'].values*Nisu*zeiritu),
        'HP':int(Aquadf['ＨＰ予想記者'].values*Nisu*zeiritu),
        'Machine':int(Aquadf['配信機材一式'].values*Nisu*zeiritu),
        'Goods':int(Aquadf['備品等'].values*Nisu*zeiritu),
        'Jikyo':int(Aquadf['実況放送'].values*Nisu*zeiritu),
        'li1':Aqua1,
        'li2':Aqua2,
        'Kaisetsu_2':int(df2[df2['type']=='解説者']['price'].sum()),
        'MC_2':int(df2[df2['type']=='MC']['price'].sum()),
        'Director_2':int(df2[df2['type']=='ディレクター']['price'].sum()),
        'Staff_2':int(df2[df2['type']=='スタッフ']['price'].sum()),
        'VisionDirector_2':int(df2[df2['type']=='映像']['price'].sum()),
        'SoundDirector_2':int(df2[df2['type']=='音響']['price'].sum()),
        'HP_2':int(df2[df2['type']=='ＨＰ予想記者']['price'].sum()),
        'Machine_2':int(df2[df2['type']=='配信機材一式']['price'].sum()),
        'Goods_2':int(df2[df2['type']=='備品等']['price'].sum()),
        'Jikyo_2':int(df2[df2['type']=='実況放送']['price'].sum()),
    }

    return dict


#時系列順にソート
def seiri_database2():
    df = print_database2()
    print(df)
    return df
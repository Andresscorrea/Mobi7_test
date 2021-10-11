import pandas as pd 
import requests
import psycopg2 as pg
from sqlalchemy import create_engine
from datetime import datetime

def insert_values_db(df):

    engine = create_engine('postgresql://postgres:postgres@localhost:5432/mobi7_code_interview')
    df.to_sql('consolided_values', engine, index=False, if_exists='append')
    return df

def query(query):
    conn = pg.connect(""
                      "host='localhost'"
                      "dbname=mobi7_code_interview user=postgres password='postgres'"
                      " port=5432")
    df = pd.read_sql(query, conn)
    return df


result_sql = query('select vehicle_id, plate, journey_size, total_distance, total_moving, total_idle from public.trip')
df_count = result_sql.groupby(['vehicle_id', 'plate','journey_size']).size().reset_index(name='counts')
df_final = result_sql.groupby(['vehicle_id', 'plate','journey_size'], sort=False).sum()
df_final_ = df_final.merge(df_count, on =['vehicle_id', 'plate','journey_size'], how= 'inner' )
df_final_['day'] = datetime.today()
insert_values_db(df_final_)
df_final_.to_csv(f'resultados.csv',index=False, header=True)

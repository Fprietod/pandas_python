import pandas as pd

from sqlalchemy import create_engine

class insert():
    def insert_client():
        df = pd.read_csv ('client_table.csv')
        print(df)
        engine = create_engine('postgresql://urbvan:root2022@database-postgress.c295zanvccq2.us-east-1.rds.amazonaws.com:5432/postgres')
        for df in pd.read_csv("client_table.csv",chunksize=30000):
            df.to_sql('client_table.csv',engine, index=False, if_exists='append')
   

    def insert_driver():
        df2 = pd.read_csv ('driver_table.csv')
        print(df2)
        engine2 = create_engine('postgresql://urbvan:root2022@database-postgress.c295zanvccq2.us-east-1.rds.amazonaws.com:5432/postgres')
        for df2 in pd.read_csv("driver_table.csv",chunksize=1000):
            df2.to_sql('driver_table.csv',engine2, index=False, if_exists='append')
            
    def insert_reservation():
        df3 = pd.read_csv('reservation_table.csv')
        print(df3)
        engine3 = create_engine('postgresql://urbvan:root2022@database-postgress.c295zanvccq2.us-east-1.rds.amazonaws.com:5432/postgres')
        for df3 in pd.read_csv('reservation_table.csv', chunksize=3106171):
            df3.to_sql('reservation_table.csv',engine3,index=False,if_exists='append')
            
    def insert_trip():
        df4 = pd.read_csv('trip_table.csv')
        print(df4)
        engine4 = create_engine('postgresql://urbvan:root2022@database-postgress.c295zanvccq2.us-east-1.rds.amazonaws.com:5432/postgres')
        for df4 in pd.read_csv('trip_table.csv',chunksize=175292):
            df4.to_sql('trip_table.csv',engine4,index=False,if_exists='append')
        

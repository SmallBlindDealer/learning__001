
from threading import Lock
import os, shutil
import pandas as pd
import psycopg2
from psycopg2.extras import execute_batch
import json

def create_conn():
    return psycopg2.connect(database="db_name",
                            host="localhost",
                            user="postgres",
                            password="postgres",
                            port=5432)


class DataIngestion:
    def __init__(self, source_data_directory, processing_directory, conn):
        self.access_file = Lock()
        self.source_data_directory = source_data_directory
        self.processing_directory = processing_directory
        self.conn = conn
    
    def run(self, filename=None, data_mapping=None):
        
        with self.access_file:
            if not filename:
                if os.listdir(self.source_data_directory):

                    filename = os.listdir(self.source_data_directory)[0]
                else:
                    print("no file to process now")
                    return

            if filename not in os.listdir(self.source_data_directory):
                print("file doesn't exist")
                return
            else:
                shutil.move(
                    self.source_data_directory + "/" + filename, 
                    self.processing_directory + "/" + filename
                )
        
        df = pd.read_csv(self.processing_directory + "/" + filename, dtype=str)
        data_mapping = json.loads(open("./data_m.json", "r").read()).get(filename, {})
        if not data_mapping:
            raise Exception("-->")
        
        if set(data_mapping.keys()).difference(set(df.columns)):
            missing_cols = list(set(data_mapping.keys()).difference(set(df.columns)))
            raise Exception(f"some columns are missing in CSV: {str(missing_cols)}")
            return
        
        try:
            df = self.convert_data_format(df, data_mapping)
        except Exception as e:
            raise Exception(f"issue with data formatting: {str(e)}")
            return
        

        self.rename_cols(df, data_mapping)
        table_name = filename
        self.push_data_to_db(df, table_name, data_mapping)
        return [True, table_name]

    def push_data_to_db(self, df: pd.DataFrame, table_name, data_mapping):

        cursor = self.conn.cursor()
        cols_list = list(df.columns)

        table_creation_str = f"create table {table_name} ("
        
        table_creation_str +=",".join([f"{v['field']} {v['dtype']}" for k, v in data_mapping.items()])
        table_creation_str+=")"

        cursor.execute(table_creation_str)
        self.conn.commit()

        for _, row in df.iterrows():
            final_insert_string = f"insert into {table_name} values(" 
            final_insert_string+=",".join(["%s" for _ in range(len(cols_list))])
            final_insert_string+=")"
            execute_batch(final_insert_string, *[row[col] for col in cols_list])
        # (insert into t1 values (%s, %s), a, v)
        # cursor.execute(final_insert_string)
        self.conn.commit()


    
    def convert_data_format(self, df: pd.DataFrame, data_mapping):
        convert_dict = {}
        for k, v in data_mapping.items():
            convert_dict[k] = v["dtype"]
        return df.astype(convert_dict)

    def rename_cols(self, df: pd.DataFrame, data_mapping):
        convert_dict = {}
        for k, v in data_mapping.items():
            convert_dict[k] = v["field"]
        
        df.rename(convert_dict, inplace = True)

# import 


class DataAnalytics:
    

    def __init__(self, conn):
        self.conn = conn
        ...
    
    def run(self, table_name=None):

        return {
            """
        Do we have more than 1 sanction date in last 90 days from the latest reporting date or																								
        more than 3 sanction date in last 180 days from the latest reporting date or																								
        more than 5 sanction date in last 365 days from the latest reporting date""": "Yes" if True  else "No"
        }
    



        

        







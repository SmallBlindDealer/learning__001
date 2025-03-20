



import schedule
import time
from utils import DataIngestion, DataAnalytics, create_conn


conn = create_conn()

data_ingestion_obj = DataIngestion("./dataSource", "./processingData")

data_analytics_obj = DataAnalytics(conn)



def run_etl():
    data_ingestion_obj.run()


def run_analytics():
    data_analytics_obj.run()


def run_etl_and_analytics():
    res = data_analytics_obj.run()
    if res and res[0]:
        data_analytics_obj.run(res[1])



if __name__=="__main__":
    #scenerio 1 when we have to run indipendent
    schedule.every(10).minutes.do(run_etl)
    schedule.every(10).minutes.do(run_analytics)
    while True:
        time.sleep(1)
    
    # #scenerio 2 when we have to run first etl and than after analytics
    # schedule.every(10).minutes.do(run_etl_and_analytics)
    # while True:
    #     time.sleep(1)


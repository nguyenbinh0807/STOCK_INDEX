
import os
from train import train_ysn30
import pandas as pd


"""
ysn30_data(
    folder_price,
    ratio_file,
    year
    start_close
)
"""
def ysn30_data(price_folder, ratio_file, year, start_close):
    in_path=os.listdir(price_folder)
    price_file=[]
    for file_path in in_path:
        price_file.append(price_folder+'/'+file_path)
    price_file.sort()
    
    
    ysn30_list=[]
    index_quy=1
    for index in range(len(price_file)):
        ysn30_quy, index_close=train_ysn30(url_file_price=price_file[index], 
        url_file_ratio=ratio_file, quy=index_quy,
        year=year, index_close=start_close)

        start_close=index_close
        index_quy+=1
        ysn30_list.append(ysn30_quy)
    
    ysn30_data=pd.DataFrame()
    for df in ysn30_list:
        ysn30_data=ysn30_data.append(df, ignore_index=False)
    ysn30_data.index=pd.to_datetime(ysn30_data.index, format='%d-%m-%Y')
    end_close_year=ysn30_data['index_Close'][-1]
    return ysn30_data, end_close_year



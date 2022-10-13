#import module 
import pandas as pd
import numpy as np

#train model 
#read file price
def read_file_price(url, file):
  data_price=pd.read_excel(url, f'{file.title()}', index_col='TradingDate')
  data_price.drop('Unnamed: 0', axis=1, inplace=True)
  return data_price
#read file ratio
def read_file_ratio(url, quy, year):
  ratio_data=pd.read_excel(url, f'q{quy}_{year}')
  return ratio_data
#pre ratio data and concat price ratio
def update_price_data(ratio_data, price_data, file):
  if file.title()=='Close':
    ratio_data=ratio_data.T
    ratio_data.columns=price_data.columns
    ratio_data=ratio_data.sort_index()
    ratio_data.rename(index={'stock': 'share'}, inplace=True)
    ratio_data.loc['share', :]=np.nan
    update_data=pd.concat([ratio_data, price_data])
    return update_data
  else: 
    return 'not close price'
#cat share ra rieng
def slice_share(data, file):
  share=data.iloc[1, :].to_frame().T
  return share
#share
def share_data(data, index_close, file, share):
  if file.title()=='Close':
    for index_column in range(len(data.columns)):
      data.loc['share', data.columns[index_column]]=index_close*data.loc['ratio', data.columns[index_column]]
      data.loc['share', data.columns[index_column]]=data.loc['share', 
      data.columns[index_column]]/data.iloc[len(data.loc['ratio': 'share']), index_column]
    if share:
      share_data=slice_share(data, 'close')
      return data, share_data
    else:
      return data
  else:
    return 'not close price'

def index_ysn30(data, file, share_data):
  price_list=['High', 'Open','Low']
  for index in range(len(price_list)):
    if file.title()==price_list[index]:
      
      new_data=pd.concat([share_data, data])
      new_data[f'index_{price_list[index]}']=np.nan
      
      for index_row in range(len(new_data.loc[:'share']), new_data.shape[0]):
        share=new_data.iloc[0, :-1].values
        price=new_data.iloc[index_row, :-1].fillna(0).values
        new_data.iloc[index_row, -1]=np.sum([share*price for share, price in zip(share, price)])
      
      return new_data

    elif file.title()=='Close':
      data['index_Close']=np.nan
      for index_row in range(len(data.loc['ratio': 'share']), data.shape[0]):
        share=data.iloc[1, :-1].values
        price=data.iloc[index_row, :-1].fillna(0).values
        data.iloc[index_row, -1]=np.sum([share*price for share, price in zip(share, price)])
      return data
def ysn30_file(open_data, close_data, high_data, low_data):
  ysn30_high=high_data[['index_High']]
  ysn30_low=low_data[['index_Low']]
  ysn30_close=close_data[['index_Close']]
  ysn30_open=open_data[['index_Open']]
  ysn30_file=pd.concat([ysn30_open, ysn30_close, ysn30_high, ysn30_low], axis=1)
  ysn30_file.dropna(inplace=True)
  price_close=round(ysn30_file['index_Close'][-1], 3)
  return ysn30_file, price_close

#volume index ysn30
#read_file(path_volume, sheet)
def read_file_volume(path, sheet):
  vol_data=pd.read_excel(path, sheet_name=sheet)
  vol_data.drop('Unnamed: 0', axis=1, inplace=True)
  vol_data.set_index('TradingDate', inplace=True)
  vol_data['vol_sum']=vol_data.sum(axis=1)
  vol_data.drop(vol_data.columns[:-1], axis=1, inplace=True)
  return vol_data

#rate_vol(data1, data2)
def rate_volume(data1, data2):
    rate=data1.iloc[-1, 0]/data2.iloc[0, 0]
    data2['new_vol']=rate*data2.iloc[1:]
    data2.dropna(inplace=True)
    data2.drop('vol_sum', axis=1, inplace=True)
    data2.rename(columns={'new_vol': 'vol_sum'}, inplace=True)
    return data2

from scripts import read_file_ratio, read_file_price, update_price_data, share_data, index_ysn30, ysn30_file


def train_ysn30(url_file_price, url_file_ratio, quy, year, index_close):
#read file ratio(url, quy may, so nam)
    ratio_data_q1_2021=read_file_ratio(url_file_ratio, quy, year)
#read file price (url, quy, year, (open, close, high, low))
    close_data_q1_2021=read_file_price(url_file_price, 'close')
    open_data_q1_2021=read_file_price(url_file_price,  'open')
    high_data_q1_2021=read_file_price(url_file_price, 'high')
    low_data_q1_2021=read_file_price(url_file_price, 'low')
#update price data(ratio data, price data close, 'close')
    new_close_data_q1_2021=update_price_data(ratio_data_q1_2021, close_data_q1_2021, 'close')
#share data(update close data, index close, 'close', share=True/False)
#if share==True return close_data, share_data
    new_close_data_q1_2021, share_data_2021=share_data(new_close_data_q1_2021, index_close, 'close', True)

#index ysn30(data, (high, close, open, low), share_data)
#if close data thi share data=false
#if open data high low thi share data=share_data_2021
    ysn30_close_q1_2021=index_ysn30(new_close_data_q1_2021, 'close', False)
    ysn30_open_q1_2021=index_ysn30(open_data_q1_2021, 'open', share_data_2021)
    ysn30_high_q1_2021=index_ysn30(high_data_q1_2021, 'high', share_data_2021)
    ysn30_low_q1_2021=index_ysn30(low_data_q1_2021, 'low', share_data_2021)

#ysn30 file (open data, close data, high data, low data)
    ysn30_data, price_close=ysn30_file(ysn30_open_q1_2021, ysn30_close_q1_2021, ysn30_high_q1_2021, ysn30_low_q1_2021)
    return ysn30_data, price_close


    
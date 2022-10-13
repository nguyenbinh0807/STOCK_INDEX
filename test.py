from ysn30 import ysn30_data
path_2021='C:\Users\Le Trung Hieu\Desktop\YSN30\data\ysn30_2021'
path_ratio='C:\Users\Le Trung Hieu\Desktop\YSN30\data\ratio.xlsx'

"""
ysn30_data(
price_folder: đường dẫn đến thư mục file price,
ratio_file: đường dẫn đến file ratio
year: là số năm
start_close: lấy mốc năm bắt đầu
)
"""
ysn30_2021, index_close_2021=ysn30_data(price_folder=path_2021, ratio_file=path_ratio, year=2021, start_close=100)
print(index_close_2021)
"""
sẽ trả về hai giá trị:
1) dataframe chứa chỉ số yns30 của năm đó
2) sẽ trả về ysn30 giá trị cuối cùng của giá đóng cửa
"""
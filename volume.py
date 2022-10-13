from scripts import read_file_volume, rate_volume
import pandas as pd

def volume_list(path):
	volume_list=[]
	data=pd.ExcelFile(path)
	for sheet_name in data.sheet_names:
		volume_list.append(read_file_volume(path, sheet_name))
	return volume_list

def volume_data(path):
	list_volume=volume_list(path)
	sum_volume_data=[list_volume[0]]
	for index in range(len(list_volume)):
		if index+1<len(list_volume):
			sum_volume_data.append(rate_volume(
				list_volume[index], list_volume[index+1]
			))
		else:
			data=pd.concat(sum_volume_data)
			update_data=data.drop(data.loc[data['vol_sum']==0].index, axis=0)
			return update_data
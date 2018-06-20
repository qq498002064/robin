import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from imp import reload
import sys
stdout = sys.stdout
sys.stdout = stdout
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
community = pd.read_csv('ershoufang.csv')

#将字符串转换成数字
# def data_adj(area_data, str):
#     if str in area_data :
#          return float(area_data[0 : area_data.find(str)])
#     else :
#          return None
#处理房屋面积数据
# def atoi(s):
#    s = s[::-1]
#    num = 0
#    for i, v in enumerate(s):
#       for j in range(0, 10):
#          if v == str(j):
#             num += j * (10 ** i)
#    return float(num)
# community['area'] = string.atof(community['area'])

# fig,ax2 = plt.subplots(1,1)
# # area_level = [0, 50, 100, 150, 200, 250, 300, 500]
# # label_level = ['小于50', '50-100', '100-150', '150-200', '200-250', '250-300', '300-350']
# # area_cut = pd.cut(community['area'], area_level, labels=label_level)
# # area_cut.value_counts().plot(kind='bar', rot=30, alpha=0.4, grid=True, fontsize='small', ax=ax2)
# # plt.title('二手房面积分布')
# # plt.xlabel('面积')
# # plt.legend(['数量'])
# # plt.show()

# community_unitprice_perdistrict = community.groupby('city').mean()['average_price']
# community_unitprice_perdistrict.plot(kind='bar',x='city',y='average_price', title='各个行政区房源均价')
# plt.legend(['均价'])
# plt.show()

#print(community['average_price'])
# housetype = community['model'].value_counts()
# housetype.head(8).plot(kind='bar',x='housetype',y='size', title='户型数量分布')
# plt.legend(['数量'])
# plt.show()

# housetype = community['city'].value_counts()
# housetype.head(8).plot(kind='bar',x='city',y='size', title='户型数量分布')
# plt.legend(['数量'])
# plt.show()

bizcircle_community=community.groupby('community')['community'].size().sort_values(ascending=False)
bizcircle_community.head(20).plot(kind='bar', x='community',y='size', title='各个区域小区数量分布')
plt.legend(['数量'])
plt.show()
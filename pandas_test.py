# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 10:48:10 2019

@author: yimo
""" 
#练习pandas用法


import pandas as pd

path2 = "D:/dataset/pandas_exercise/exercise_data/Euro2012_stats.csv"
euro12 = pd.read_csv(path2) #read pandas

euro12.Goals #读取特定列

euro12.shape[0]

euro12.info()#该数据集中一共有多少列

discipline = euro12[['Team', 'Yellow Cards', 'Red Cards']]#将数据集中的列Team, Yellow Cards和Red Cards单独存为一个名叫discipline的数据框

discipline.sort_values(['Red Cards', 'Yellow Cards'], ascending = False)#数据框discipline按照先Red Cards再Yellow Cards进行排序

round(discipline['Yellow Cards'].mean())#计算每个球队拿到的黄牌数的平均值

euro12[euro12.Goals > 6]#找到进球数Goals超过6的球队数据

euro12[euro12.Team.str.startswith('G')]#选取以字母G开头的球队数据

euro12.iloc[: , 0:7]#选取前7列
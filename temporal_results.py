# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 20:48:10 2021

@author: KieraLynn
"""
from temporal_mining import *
import csv
import copy
Q1=[]
def Q_data(period):
    temp=[]
    with open('./try.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            temp.append(row)
    for tran in temp:
        if " " in tran :
            tran.remove(" ")
        if " " in tran :
            tran.remove(" ")
        if " " in tran :
            tran.remove(" ")
        if " " in tran :
            tran.remove(" ")
        else:
            pass
        if " " in tran :
            tran.remove(" ")
        else:
            pass
        tran.pop(len(tran)-1)
    for x in range(0,len(temp)):
        rs= sorted(temp[x],key=lambda i:item_recency[i],reverse=True)
        period.append(rs)
Q_data(Q1)

def temporal_res(period):
    for tran in period:
        tmp1=set(tran)
        for comb in combination:
            tmp2=set(comb)
            if tmp1 == tmp2:
                tran.insert(0,globals()[str(combination.index(comb))])
temporal_res(Q1)

def recency_cut(period):
    for i in period[::-1]:
        if sum(i[0]) < ε:
            period.remove(i)
        else:
            break
recency_cut(Q1)
def output_excel(period):
    output = open('data.xls','w',encoding='gbk')
    for i in range(len(Q1)):
        for j in range(len(Q1[i])):
             output.write(str(Q1[i][j]))  #write函数不能写int类型的参数，所以使用str()转化
             output.write('\t')  #相当于Tab一下，换一个单元格
        output.write('\n')    #写完一行立马换行
    output.close()

output_excel(Q1)
print(Q1)

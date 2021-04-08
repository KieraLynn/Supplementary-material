# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 15:10:04 2021

@author: KieraLynn
"""

"""
参数说明
1、时间范围 两年期间8个Quaters
2、输入的原始数据
3、时间敏感参数δ（time-sensitive parameter)
4、1-项非频繁项的剪枝阈值
计数的支持度：
thresh1=0.2189781 * 记录数量
thresh2=0.0729927 * 记录数量
时间频繁的支持度：0.25

5、挖掘的阈值ε
"""
import itertools
from clean_data import *
from Hierarchy_tree import *
import Trimming_Header_table
δ= 0.15#时间敏感参数
#ε时间频繁的支持度
#transactions = try1[69:133]#Q2
#transactions = try1[133:196]#Q3
#transactions = try1[196:263]#Q4
#transactions = try1[263:295]#Q5
#transactions = try1[295:333]#Q6
#transactions = try1[333:369]#Q7
#transactions = try1[369:412]#Q8

Recency={}
def trans_recency():
    for i in range(1,len(transactions)):
        tid = int(i)
        Recency[tid] = (1-δ)**(len(transactions)-1-tid)
trans_recency()#计算每条记录的Recency
item_recency={}
def createlist():
    for item in list_of_tree:
        item_recency[item]=[]
    item_recency.pop('root')
    item_recency.pop('A')
    item_recency.pop('B')
    item_recency.pop('C')
    item_recency.pop('D')
    item_recency.pop('I')
createlist()

def ItemRecency():
    for k,v in item_recency.items():
        for i in range(1,len(transactions)):
            if k in transactions[i]:
                #index = str(i)
                temp_recency = Recency[i]
                v.append(temp_recency)
    for k,v in item_recency.items():
        temp = sum(v)
        item_recency[k] = temp
ItemRecency()
#利用计数对i-item进行剪枝
#挖掘得到的频繁项再进行时间阈值比较，将时间不频繁的删除
from itertools import combinations
ranked_trans=[]
def rankfact ():
    for x in range(1,len(transactions)):
        rs= sorted(transactions[x],key=lambda i:item_recency[i],reverse=True)
        ranked_trans.append(rs)
    ranked_trans.insert(0,'事故模式')
rankfact()
# 全组合 ALL COMBINATIONS
from copy import deepcopy
def per(arr, start, num,res):
    if num == 0:
        h.append(deepcopy(res))
        return
    if len(arr)-start<num:
        return
    else:
        res.append(arr[start])
        per(arr, start+1, num-1,res)
        temp=res.pop()
        per(arr, start+1, num,res)
global h
combination=[]
h  = []
start = 0
resul= []
for k in range(1,len(ranked_trans)):
        arr= ranked_trans[k]
        for i in range(1,len(arr)+1):
            per(arr,0, i,resul)
def deleteDuplicatedElementFromList2(list1):
        comb_List = []
        for item in list1:
                if not item in comb_List:
                    comb_List.append(item)
        return comb_List
comb_List=deleteDuplicatedElementFromList2(h)
def sortlist():
    for x in range(0,len(comb_List)):
        rs= sorted(comb_List[x],key=lambda i:item_recency[i],reverse=True)
        combination.append(rs)

sortlist()
del comb_List

def Combination_recency():
    for list1 in combination:
        globals()[str(combination.index(list1))] = []
        for i in range(1,len(ranked_trans)):
            if [j for j in list1 if j in ranked_trans[i]]== list1:
                globals()[str(combination.index(list1))].append(Recency[i])
Combination_recency()

del h,start, resul,k,item,i
'''
for k,v in combination_dict.items():
        temp = sum(v)
        combination_dict[k] = temp'''

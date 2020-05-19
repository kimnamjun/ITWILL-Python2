# -*- coding: utf-8 -*-
"""
문) tree_data.csv 파일의 변수를 이용하여 아래 조건으로 DecisionTree model를 생성하고,
    의사결정 tree 그래프를 시각화하시오.
    
 <변수 선택>   
 x변수 : iq수치, 나이, 수입, 사업가유무, 학위유무
 y변수 : 흡연유무
 
 <그래프 저장 파일명> : smoking_tree_graph.dot
"""

import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_graphviz

tree_data = pd.read_csv("C:/ITWILL/4_Python-II/data/tree_data.csv")
print(tree_data.info())
'''
iq         6 non-null int64 - iq수치
age        6 non-null int64 - 나이
income     6 non-null int64 - 수입
owner      6 non-null int64 - 사업가 유무
unidegree  6 non-null int64 - 학위 유무
smoking    6 non-null int64 - 흡연 유무
'''
x = tree_data.iloc[:,:5]
y = tree_data.iloc[:,5]
cols = tree_data.columns[:5]

model = DecisionTreeClassifier().fit(x, y)
export_graphviz(model, "C:/ITWILL/4_Python-II/data/tree_data.dot", feature_names=cols)
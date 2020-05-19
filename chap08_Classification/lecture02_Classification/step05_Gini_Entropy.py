"""
Gini Impurity(불순도), Entropy
- tree model에서 중요변수 전정 기준
- 정보이득 = base 지수 - Gini 불순도 or Entropy
- 정보이득이 클수록 중요변수로 본다.
- Gini impurity = sum(p * (1-p))
- Entropy = -sum(p * log(p))
"""
import numpy as np
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.metrics import accuracy_score
from sklearn import tree
import matplotlib.pyplot as plt

# 1. 불확실성이 큰 경우
x1 = 0.5
x2 = 0.5

gini = sum([x1 * (1 - x1), x2 * (1 - x2)])  # 0.5

entropy = -sum([x1 * np.log2(x1), x2 * np.log2(x2)])  # 1.0

"""
cost(loss) function : 정답과 예측치 -> 오차 반환 함수
x1 -> y_true, x2 -> y_pred
y_true = x1 * np.log2(x1)
y_pred = x2 * np.log2(x2)
"""
y_true = x1 * np.log2(x1)
y_pred = x2 * np.log2(x2)
cost = -sum([y_true, y_pred])  # cost = 1.0 (Entropy와 식 동일)


# 2. 불확실성이 작은 경우
x1 = 0.9
x2 = 0.1
gini = sum([x1 * (1 - x1), x2 * (1 - x2)])  # 0.18
entropy = -sum([x1 * np.log2(x1), x2 * np.log2(x2)])  # 0.4690
cost = -sum([x1 * np.log2(x1), x2 * np.log2(x2)])  # 0.4690

# -------------------------------------------------------------------------------- #
# Dataset 적용

def createDataSet():
    dataSet = [ [1, 1, 'yes'],
                [1, 1, 'yes'],
                [1, 0, 'no'],
                [0, 1, 'no'],
                [0, 1, 'no']]
    columns = ['dark_clouds','gust']  # X1,X2,label
    return dataSet, columns


dataSet, columns = createDataSet()
dataSet = np.array(dataSet)
columns = np.array(columns)

X = dataSet[:,:2]
y = dataSet[:,2]
y = [1 if d == 'yes' else 0 for d in y]

model = DecisionTreeClassifier().fit(X, y)
pred = model.predict(X)
acc = accuracy_score(y, pred)

# 중요변수
tree.plot_tree(model, feature_names=columns)
plt.show()
export_graphviz(model, out_file="../../../data/dataset_tree.dot", feature_names=columns)
"""
Decision Tree 모델
- 중요변수 선정 기준 : GINI, Entropy : 둘 다 낮으면 불확실성이 낮음
- GINI : 불확실성을 개선하는데 기여하는 척도
- Entropy : 불활실성을 나타내는 척도
"""
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris, load_wine
from sklearn.tree import DecisionTreeClassifier, export_graphviz
# DecisionTreeClassifier는 Y가 범주형일 때
# DecisionTreeRegressor는 Y가 연속형일 때
from sklearn.metrics import accuracy_score, confusion_matrix

from sklearn.tree.export import export_text
from sklearn import tree
import  matplotlib.pyplot as plt

########
# iris #
########

iris = load_iris()
# iris.target_names  # ['setosa' 'versicolor' 'virginica']

X = iris.data
y = iris.target

x_train, x_test, y_train, y_test = train_test_split(X, y, random_state=321, test_size=0.3)

# Decision Tree : criterion='gini', max_depth=3
dtc = DecisionTreeClassifier(criterion='gini', random_state=123, max_depth=3)  # defalut : criterion='gini'
model = dtc.fit(X=x_train, y=y_train)

# tree 시각화
names = iris.feature_names

tree.plot_tree(model, feature_names=names)
plt.show()

print(export_text(model, feature_names=names))

# model 검증
y_pred = model.predict(x_test)

acc = accuracy_score(y_test, y_pred)  # 0.9777
con_mat = confusion_matrix(y_test, y_pred)
print(acc)
print(con_mat)
# [[16  0  0]
#  [ 0 10  0]
#  [ 0  1 11]]

# Decision Tree : criterion='entropy', max_depth=2
dtc = DecisionTreeClassifier(criterion='entropy', random_state=123, max_depth=2)  # defalut : criterion='gini'
model = dtc.fit(X=x_train, y=y_train)

# tree 시각화
names = iris.feature_names

tree.plot_tree(model, feature_names=names)
plt.show()

print(export_text(model, feature_names=names))

# model 검증
y_pred = model.predict(x_test)

acc = accuracy_score(y_test, y_pred)  # gini와 동일 결과
con_mat = confusion_matrix(y_test, y_pred)

# -------------------------------------------------------------------------------- #
#####################
# model overfitting #
#####################

wine = load_wine()
x_name = wine.feature_names
X = wine.data
y = wine.target

x_train, x_test, y_train, y_test = train_test_split(X, y, random_state=123, test_size=0.3)

# max_depth 지정 안함
model = DecisionTreeClassifier().fit(x_train, y_train)
train_score = model.score(x_train, y_train)  # 1.0
test_score = model.score(x_test, y_test)     # 0.9444

# max_depth = 3
model = DecisionTreeClassifier(max_depth=3).fit(x_train, y_train)
train_score = model.score(x_train, y_train)  # 0.9839
test_score = model.score(x_test, y_test)     # 0.9815

export_graphviz(model, "C:/ITWILL/4_Python-II/data/DT_tree_graph.dot", max_depth=3,
                feature_names=x_name, class_names=True)
# gvedit.exe 설치 후 실행하면 됨
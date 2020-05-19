'''
 문) load_breast_cancer 데이터 셋을 이용하여 다음과 같이 Decision Tree 모델을 생성하시오.
 <조건1> 75:25비율 train/test 데이터 셋 구성 
 <조건2> y변수 : cancer.target, x변수 : cancer.data 
 <조건3> 중요변수 확인 

'''
from sklearn import model_selection
from sklearn.datasets import load_breast_cancer
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree.export import export_text
from sklearn.metrics import accuracy_score, confusion_matrix

# 데이터 셋 load 
cancer = load_breast_cancer()
print(cancer)
print(cancer.DESCR)

# 변수 선택 
X = cancer.data
y = cancer.target
print(cancer.feature_names)

x_train, x_test, y_train, y_test = model_selection.train_test_split(X, y)

model = DecisionTreeClassifier(max_depth=4).fit(x_train, y_train)
print(export_text(model))
# worst perimeter, worst concave points

y_pred = model.predict(x_test)
print(accuracy_score(y_test, y_pred))  # 0.9371
print(confusion_matrix(y_test, y_pred))
# [[52  3]
#  [ 6 82]]
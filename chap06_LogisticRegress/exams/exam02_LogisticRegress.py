'''
문) load_wine() 함수를 이용하여 와인 데이터를 다항분류하는 로지스틱 회귀모델을 생성하시오. 
  조건1> train/test - 7:3비울
  조건2> y 변수 : wine.data 
  조건3> x 변수 : wine.data
  조건4> 모델 평가 : confusion_matrix, 분류정확도[accuracy]
'''

from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics

# 1. wine 데이터셋 
wine = load_wine()

# 2. 변수 선택 
wine_x = wine.data # x변수 
wine_y = wine.target # y변수

# 3. train/test split(7:3)

# 4. model 생성  : solver='lbfgs', multi_class='multinomial'

# 5. 모델 평가 : accuracy, confusion matrix

import numpy as np
from statsmodels.formula.api import logit
import pandas as pd
from sklearn.datasets import load_breast_cancer 
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split 
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.metrics import roc_curve
import matplotlib.pyplot as plt 

# sigmoid 함수 정의 
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
# odds_ratio와 로짓값 그리고 sigmoid함수 

# 1) 성공확률 50% 미만
p = 0.2   

odds_ratio = p / (1-p) # 오즈비(odds_ratio)=0.25 
# 오즈비(odds_ratio) < 1 이면 x가 감소 방향으로 y에 영향 

logit = np.log(odds_ratio) 
sig = sigmoid(logit)
y_pred = 1 if sig > 0.5 else 0 

# 2) 성공확률 50% 이상
p = 0.6 
  
odds_ratio = p / (1-p) # 오즈비(odds_ratio)=1.49999
# 오즈비(odds_ratio) > 1 이면 x가 증가 방향으로 y에 영향

logit = np.log(odds_ratio) 
sig = sigmoid(logit) 
y_pred = 1 if sig > 0.5 else 0 


###########################################
### 통계적인 방법의 로지스틱회귀모델 
###########################################

import pandas as pd


path = r'C:\ITWILL\4_Python_ML\data'

skin = pd.read_csv(path + '/skin.csv')
skin.info()

# 1. X, y변수 인코딩
X = skin.drop(['cust_no','cupon_react'], axis = 1)  

# X변수 인코딩 : 2진수  
X = pd.get_dummies(X, columns=['gender', 'job' , 'marry', 'car'],
                   drop_first=True, dtype='uint8') 

# y변수 인코딩 : 10진수 
from sklearn.preprocessing import LabelEncoder

y = LabelEncoder().fit_transform(skin.cupon_react)

new_skin = X.copy() 
new_skin['y'] = y 
new_skin.info()

# 3. 로지스틱회귀모델 : formula 형식 
formula = logit(formula='y ~ age + gender_male + marry_YES', data = new_skin)
model = formula.fit()

dir(model)

y = new_skin.y # 종속변수(0 or 1) 
y_fitted = model.fittedvalues # model 적합치(예측치)=로짓값      

# 로짓값 -> 확률(sigmoid func)
y_sig = sigmoid(y_fitted)
y_sig

# 확률 -> 0 or 1 변환 
y_pred = [ 1 if y > 0.5 else 0 for y in y_sig]
y_pred

result = pd.DataFrame({'y' : y,'y_sig' :y_sig,'y_pred':y_pred})
print(result)

##############################
# ROC
##############################

# 1. dataset loading 
X, y = load_breast_cancer(return_X_y=True)

print(X.shape) # (569, 30)
print(y) # 0(B) or 1(M)


# 2. train/test split 
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size = 0.3, random_state=1)


# 3. model 생성 
lr = LogisticRegression(solver='lbfgs', max_iter=100, random_state=1)  
'''
solver='lbfgs', : 최적화에 사용되는 기본 알고리즘(solver) 
max_iter=100,  : 반복학습횟수 
random_state=None, : 난수 seed값 지정 
'''

model = lr.fit(X=X_train, y=y_train) 
dir(model)

## predict() : y 클래스 예측 
## predict_proba() : y 확률 예측(sigmoid 함수) 


# 4. model 평가 
y_pred = model.predict(X = X_test) # class 예측치 
y_pred_proba = model.predict_proba(X = X_test) # 확률 예측치 

y_true = y_test # 관측치 

# 1) 혼동행렬(confusion_matrix)
con_max = confusion_matrix(y_true, y_pred)
print(con_max)
'''
     0    1
0 [[ 59   4]
1 [  5 103]]
'''

# 2) 분류정확도 
acc = accuracy_score(y_true, y_pred)
print('accuracy =',acc) # accuracy = 0.9473684210526315

(59 + 103) / len(y_pred) # 0.9473684210526315


#############################
# ROC curve 시각화
#############################

# 1) 확률 예측치
y_pred_proba = model.predict_proba(X = X_test) # 확률 예측 
y_pred_proba = y_pred_proba[:, 1] # 악성(pos) 확률 추출   


# 2) ROC curve 
fpr, tpr, _ = roc_curve(y_true, y_pred_proba) #(실제값, 1예측확률)

plt.plot(fpr, tpr, color = 'red', label='ROC curve')
plt.plot([0, 1], [0, 1], color='green', linestyle='--', label='AUC')
plt.legend()
plt.show()

'''
ROC curve FPR vs TPR  

ROC curve x축 : FPR(False Positive Rate) - 실제 음성을 양성으로 잘못 예측할 비율  
ROC curve y축 : TPR(True Positive Rate) - 실제 양성을 양성으로 정상 예측할 비율  
'''
TPR = 103 / 108 # 0.9537037037037037 : 민감도(Y축)
TNR = 59 / 63 # 0.9365079365079365 : 특이도
FPR = 1 - TNR  # 0.06349206349206349 : 위양성비율(X축)

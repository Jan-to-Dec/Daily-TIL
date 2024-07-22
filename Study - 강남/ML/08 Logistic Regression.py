from sklearn.datasets import load_digits 
from sklearn.linear_model import LinearRegression 
from sklearn.linear_model import LogisticRegression 
from sklearn.model_selection import train_test_split 
from sklearn.metrics import confusion_matrix, accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.decomposition import PCA 
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
from statsmodels.formula.api import ols

# 1. dataset loading 
digits = load_digits()

image = digits.data # x변수 
label = digits.target # y변수 

image.shape # (1797, 64) : (size, pixel) 
image[0] # 0 ~ 15 
label.shape 
label # 0 ~ 9
 
# 2. train_test_split
img_train, img_test, lab_train, lab_test = train_test_split(
                 image, label, 
                 test_size=0.3, 
                 random_state=123)


# 3. model 생성 
lr = LogisticRegression(random_state=123,
                   solver='lbfgs',
                   max_iter=100, 
                   multi_class='multinomial')
'''
penalty : {'l1', 'l2', 'elasticnet', None}, default='l2' 
  -> 과적합 규제 : 'l1' - lasso 회귀 , 'l2' - ridge 회귀 
C : float, default=1.0
  -> Cost(비용함수)  
random_state : int, RandomState instance, default=None
  -> 시드값 
solver : {'lbfgs', 'liblinear', 'newton-cg', 'newton-cholesky', 'sag', 'saga'}, \
        default='lbfgs'
  -> 최적화 알고리즘       
max_iter : int, default=100  
  -> 반복횟수       
multi_class='auto' : 다항분류(multinomial) 
'''

model = lr.fit(X=img_train, y=lab_train)

# 4. model 평가 
y_pred = model.predict(img_test) # class 예측 
y_pred_proba = model.predict_proba(img_test) # 확률 예측 

y_pred_proba.shape # (540, 10)
y_pred_proba[0].sum() # 1

# 1) 혼동행렬(confusion matrix)
con_mat = confusion_matrix(lab_test, y_pred)
print(con_mat)

# 2) 분류정확도(Accuracy)
accuracy = accuracy_score(lab_test, y_pred)
print('Accuracy =', accuracy) 
# Accuracy = 0.9666666666666667

# 3) heatmap 시각화
  # confusion matrix heatmap 
plt.figure(figsize=(6,6)) # size
sns.heatmap(con_mat, annot=True, fmt=".3f",
           linewidths=.5, square = True) 
plt.ylabel('Actual label')
plt.xlabel('Predicted label')
all_sample_title = 'Accuracy Score: ', format(accuracy,'.6f')
plt.title(all_sample_title, size = 18)
plt.show()

###########################
# PCA Regression 
###########################

iris = load_iris()

X = iris.data
y = iris.target

df = pd.DataFrame(X, columns= ['x1', 'x2', 'x3', 'x4'])
corr = df.corr()
print(corr)

df['y'] = y 
df.columns  # ['x1', 'x2', 'x3', 'x4', 'y']

# 2. 다중선형회귀분석 
ols_obj = ols(formula='y ~ x1 + x2 + x3 + x4', data = df)
model = ols_obj.fit()
dir(model)
model.params

# 회귀분석 결과 제공  
print(model.summary()) 
'''
Model:                            OLS   Adj. R-squared:                  0.928
Method:                 Least Squares   F-statistic:                     484.5
Date:                Thu, 05 May 2022   Prob (F-statistic):           8.46e-83
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept      0.1865      0.205      0.910      0.364      -0.218       0.591
x1            -0.1119      0.058     -1.941      0.054      -0.226       0.002
x2            -0.0401      0.060     -0.671      0.503      -0.158       0.078
x3             0.2286      0.057      4.022      0.000       0.116       0.341
x4             0.6093      0.094      6.450      0.000       0.423       0.796
==============================================================================
Prob (F-statistic): 모델의 통계적 유의성 
Adj. R-squared: 모델의 설명력 
coef : 절편 & 회귀계수 
std err : 표준오차는 회귀계수(coef)의 추정치의 정확성
t : t 검정 통계량 = (표본평균-모평균) / (표본표준편차/sqrt(표본수)) 
P>|t| : 유의확률(t 검정 통계량 근거) 5% 기준으로 가설 채택/기각 결정
    5% 미만인 경우 해당 독립변수는 종속변수에 영향이 있다라고 할 수 있다.   
'''


#  3. 다중공선성의 진단
from statsmodels.stats.outliers_influence import variance_inflation_factor

# 형식) variance_inflation_factor(exog, exog_idx)
dir(ols_obj)

exog = ols_obj.exog # 엑소(exog) : 모델에서 사용되는 독립변수 
   
# 다중공선성 진단  
for idx in range(1,5) : # 1~4
    print(variance_inflation_factor(exog, idx)) # idx=1~4

df.iloc[:,:4].corr()

    
# 4. 주성분분석(PCA)

# 1) 주성분분석 모델 생성 
pca = PCA() # random_state=123
X_pca = pca.fit_transform(X)
print(X_pca)

X_pca.shape # (150, 4)

# 2) 고유값이 설명가능한 분산비율(분산량)
var_ratio = pca.explained_variance_ratio_ # 85% 이상 -> 95% 이상 권장  
print(var_ratio) # [0.92461872 0.05306648 0.01710261 0.00521218]

# 제1주성분 + 제2주성분 
sum(var_ratio[:2]) # 0.977685206318795 = 98%(2% 손실)

# 3) 스크리 플롯 : 주성분 개수를 선택할 수 있는 그래프(Elbow Point : 완만해지기 이전 선택)
plt.bar(x = range(4), height=var_ratio)
plt.plot(var_ratio, color='r', linestyle='--', marker='o') ## 선 그래프 출력
plt.ylabel('Percentate of Variance Explained')
plt.xlabel('Principal Component')
plt.title('PCA Scree Plot')
plt.xticks(range(4), labels = range(1,5))
plt.show()


# 4) 주성분 결정 : 분산비율(분산량) 95%에 해당하는 지점
print(X_pca[:, :2]) # 주성분분석 2개 차원 선정  

X_new = X_pca[:, :2]

X_new.shape # (150, 2) 
print(X_new)

# 5. 주성분분석 결과를 회귀분석과 분류분석의 독립변수 이용 

##################################
# LinearRegression : X vs X_new
##################################

# 원형 자료 
lr_model1 = LinearRegression().fit(X = X, y = y)
lr_model1.score(X = X, y = y) # r2 score 
# 0.9303939218549564

# 주성분 자료 
lr_model2 = LinearRegression().fit(X = X_new, y = y)
lr_model2.score(X = X_new, y = y) # r2 score
# 0.9087681620170027

##################################
# LogisticRegression : X vs X_new
##################################

# 원형 자료 
lr_model1 = LogisticRegression().fit(X = X, y = y)
lr_model1.score(X = X, y = y) # accuracy
# 0.9733333333333334

# 주성분 자료 
lr_model2 = LogisticRegression().fit(X = X_new, y = y)
lr_model2.score(X = X_new, y = y)
import pandas as pd # dataset
from sklearn.model_selection import train_test_split # split 
from sklearn.linear_model import LinearRegression # model 
from sklearn.metrics import mean_squared_error, r2_score # 평가 

from sklearn.preprocessing import scale # 표준화(mu=0, st=1) 
from sklearn.preprocessing import minmax_scale # 정규화(0~1)
import numpy as np # 로그변환 + 난수 


###############################
### 특징변수(x변수) 데이터변환 
###############################

# 1. dataset load
path = r'C:\ITWILL\4_Python_ML\data'

# - 1978 보스턴 주택 가격에 미치는 요인을 기록한 데이터 
boston = pd.read_csv(path + '/BostonHousing.csv')
boston.info()

X = boston.iloc[:, :13] # 독립변수 
X.shape # (506, 13)

y = boston.MEDV # 종속변수 
y.shape #(506,)

# x,y변수 스케일링 안됨 
X.mean() # 70.07396704469443
y.mean() # 22.532806324110677

# 2. scaling 함수 
def scaling(X, y, kind='none') : # (X, y, 유형)
    # x변수 스케일링  
    if kind == 'minmax_scale' :  
        X_trans = minmax_scale(X) # 1. 정규화
    elif kind == 'scale' : 
        X_trans = scale(X) # 2. 표준화 
    elif kind == 'log' :  
        X_trans = np.log1p(np.abs(X)) # 3. 로그변환
    else :
        X_trans = X # 4. 기본 
    
    # y변수 로그변환 
    if kind != 'none' :
        y = np.log1p(y)  # np.log(y+1) 
    
    # train/test split 
    X_train,X_test,y_train,y_test = train_test_split(
        X_trans, y, test_size = 30, random_state=1)   
    
    print(f"scaling 방법 : {kind}, X 평균 = {X_trans.mean()}")
    return X_train,X_test,y_train, y_test


X_train,X_test,y_train,y_test = scaling(X, y,'scale')

X_train.mean()
y_train.mean()

# 3. 회귀모델 생성하기
model = LinearRegression().fit(X=X_train, y=y_train) # 지도학습 


# 4. model 평가하기
model_train_score = model.score(X_train, y_train) 
model_test_score = model.score(X_test, y_test)
print('model train score =', model_train_score)
print('model test score =', model_test_score)

y_pred = model.predict(X_test)
y_true = y_test
print('R2 score =',r2_score(y_true, y_pred)) # model test score 동일 
mse = mean_squared_error(y_true, y_pred)
print('MSE =', mse)

###############################
### dummy Linear Regression
###############################
insurance = pd.read_csv(path + '/insurance.csv')
insurance.info()

# 2. 불필요한 칼럼 제거 : region
new_df = insurance.drop(['region'], axis= 1)
new_df.info()

# 3. X, y변수 선택 
X = new_df.drop('charges', axis= 1)
X.shape #  (1338, 5)
X.info()

y = new_df['charges'] # 의료비 


# 4. 명목형(범주형) 변수 -> 가변수(dummy) 변환 : k-1개 
X.info()
X_dummy = pd.get_dummies(X, columns=['sex', 'smoker'],
               drop_first=True, dtype='uint8')
X_dummy.info()

# 5. 이상치 확인  
X_dummy.describe() 
X_dummy.shape # (1338, 5)

# age 이상치 확인 
X_dummy[~((X_dummy.age > 0) & (X_dummy.age <= 100))].index
# age 이상치 index : [12, 114, 180]

# age 이상치 제거 
X_new = X_dummy[(X_dummy.age > 0) & (X_dummy.age <= 100)] # age기준 

# bmi 이상치 확인 
X_dummy[X_dummy.bmi < 0].index  
# bmi 이상치 index : [16, 48, 82]

# bmi 이상치 처리 
X_new = X_new[X_new.bmi > 0] # bmi 기준 
X_new.shape 
X_new.index 

# y변수 정상범주 선정 
y = y[X_new.index] 
y.shape 

# 6. train/test split 
X_train, X_test, y_train, y_test = train_test_split(
    X_new, y, test_size=0.3, random_state=123)

# 7. model 생성 & 평가 
model = LinearRegression().fit(X=X_train, y=y_train)

# model 평가 
model.score(X=X_train, y=y_train)
model.score(X=X_test, y=y_test)

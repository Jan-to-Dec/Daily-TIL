###########################
# Linear Regression 1
###########################
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# 1. 데이터셋 로드
diabetes = load_diabetes()
X, y = load_diabetes(return_X_y=True)

# 피처 이름
X_names = diabetes.feature_names
print("피처 이름들:", X_names)

# 데이터셋 특성
print("X 모양:", X.shape)
print("y 모양:", y.shape)
print("X 평균:", X.mean(axis=0))
print("X 최소값:", X.min())
print("X 최대값:", X.max())
print("y 평균:", y.mean())
print("y 최소값:", y.min())
print("y 최대값:", y.max())

# 2. 훈련셋과 테스트셋 분리
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=123)
print("X_train 모양:", X_train.shape)
print("X_test 모양:", X_test.shape)

# 3. 모델 생성 및 훈련
lr = LinearRegression()
model = lr.fit(X_train, y_train)

# 모델 계수 및 절편
print("계수들:", model.coef_)
print("절편:", model.intercept_)

# 4. 모델 평가
y_pred = model.predict(X_test)

# 4.1 평균제곱오차(MSE)
mse = mean_squared_error(y_test, y_pred)
print('MSE:', mse)

# 4.2 결정계수 (R^2 점수)
r2 = r2_score(y_test, y_pred)
print('R^2 점수:', r2)

# 4.3 훈련셋과 테스트셋의 R^2 점수
train_score = model.score(X_train, y_train)
test_score = model.score(X_test, y_test)
print('훈련셋 R^2 점수:', train_score)
print('테스트셋 R^2 점수:', test_score)

# 평균제곱오차(MSE)는 예측값과 실제값 사이의 차이를 제곱하여 평균한 값으로, 값이 작을수록 예측이 정확하다.
# 결정계수(R^2 점수)는 모델이 데이터의 변동성을 얼마나 잘 설명하는지를 나타내며, 0에서 1 사이의 값을 가진다. 

###########################
# Linear Regression 2
###########################

# 1. dataset load
iris = load_iris()
X, y = load_iris(return_X_y=True)

# 2. 변수 선택
y = X[:, 0]
X = X[:, 1:]

# 3. train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=123)

# 4. model 생성 : 훈련셋
model = LinearRegression().fit(X=X_train, y=y_train)

# X변수 기울기 : 3개
model.coef_

# y 절편
model.intercept_

# 다중선형 회귀방정식
X1 = 3.5
X2 = 1.4
X3 = 0.2
y = y[0]

y_pred = model.intercept_ + X1 * model.coef_[0] + X2 * model.coef_[1] + X3 * model.coef_[2]
err = y - y_pred
squared_err = err ** 2

# 5. model 평가
y_pred = model.predict(X=X_test)
y_true = y_test

MSE = mean_squared_error(y_true, y_pred)
print('MSE =', MSE)

score = r2_score(y_true, y_pred)
print('r2 score =', score)

print(model.score(X_train, y_train))
print(model.score(X_test, y_test))

# 시각화 평가
plt.plot(y_pred, color='r', linestyle='--', label='pred')
plt.plot(y_true, color='b', linestyle='-', label='Y')
plt.legend(loc='best')
plt.show()

###########################
#  Linear Regression (CSV)
###########################
path = r'C:\ITWILL\4_Python_ML\data'

# 데이터 불러오기
iris = pd.read_csv(path + '/iris.csv')
print(iris.info())

# 2. 변수 선택
cols = list(iris.columns)
y_col = cols.pop(2)  
x_cols = cols[:-1] 

X = iris[x_cols]
y = iris[y_col]

# 3. train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=123)

# 4. 모델 생성
lr = LinearRegression()
model = lr.fit(X_train, y_train)

# 5. 모델 평가
y_pred = model.predict(X_test)

mse = mean_squared_error(y_true=y_test, y_pred=y_pred)
print(mse) 

score = r2_score(y_true=y_test, y_pred=y_pred)
print(score)

# 5개 정답 vs 예측치 상관계수
df = pd.DataFrame({'y_true': y_test[:5].values, 'y_pred': y_pred[:5]})
print(df)

r = df.y_true.corr(df.y_pred) 
r2_score = r**2
print(r2_score)  
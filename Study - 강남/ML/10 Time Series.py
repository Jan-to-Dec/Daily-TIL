
from prophet import Prophet 
import pandas as pd 
from sklearn.metrics import r2_score 

### 1. 데이터 로드
path = r'C:\ITWILL\4_Python_ML\data\Bike-Sharing-Dataset'
data = pd.read_csv(path + '/day.csv')
data.info()
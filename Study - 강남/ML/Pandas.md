# 1. Pandas 
- 데이터분석을 위한 고수준의 자료구조 & 데이터 분석도구 제공
- 벡터 / 행렬 자료를 효과적으로 처리할 수 있다 
- 색인기능, 자료구조변환, 수학 & 통계 연산 
- Dataframe - 행렬 자료를 다루는데 효과적인 자료구조 & 분석도구 제공  

# 2. Series 
- 정수 인덱스를 이용해 순서대로 저장
- values 속성을 호출 --> 데이터를 배열 원소로 return 
- index 속성을 호출 --> 인덱스 정보를 return

```python
price = Series([4000, 3000, 3500, 2000])
print(price)
0 4000
1 3000
2 3500
3
2000
print(price[0]) #
```
# 3. DataFrame 

- 여러 개의 칼럼으로 구성된 2차원 행렬 자료구조
    - loc : 행 인덱스로 값을 가져올 수 있다
    - iloc : 행 이름으로 값을 가져올 수 있다 
- DataFrame 사용가능한 데이터 : 리스트, 튜플, Dictionary, Series, 2차원 ndarray
- Dictionary의 키는 오름차순 정렬되어 배치된다 

## DataFrame 결측치(NaN) 처리

1. isnull() - NaN 이나 None은 True, 그렇지 않으면 False
2. notnull() - isnull()의 반대
3. dropna() - NaN인 값을 소유한 행 제외한다. 
4. fillna() - NaN을 소유한 데이터의 값을 설정할 때 사용하는 메서드. 특정한 값으로 변경할 수 있고 method 파라미터를 이용해 이전 값이나 이후 값으로 채울 수 있다. limit을 이용해 채울 개수를 지정할 수 있다. 

## DataFrame 상관관계 
1. corr()
2. cov()

Series 사이의 상관관계나 공분산을 알고자 할 때 - Series 객채를 매개변수로 넘겨준다 

DataFrame이 호출하면 모든 상관관계나 공분산 Return

corrwith 매서드를 이용하면 Series/DataFrame 과의 상관관계르르 return

## DataFrame 계층적 생인
- index나 칼럼이 2 level 이상으로 이루어진 경우
- 그룹화 연산을 할 때 유용

# 4. Group By
범주형 변수를 대상으로 각 집단별 그룹 객체를 생성, 자료처리에 이용

# 5. Apply 
그룹 객체 / pandas 객체에 외부함수를 적용한다. 

# 6. Pivot table 
사용자가 직접 변수를 지정하여 테이블을 생성


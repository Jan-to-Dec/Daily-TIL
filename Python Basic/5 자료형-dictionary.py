# 딕셔너리는 Key와 Value를 한 쌍으로 가지는 자료형
# 형태 : {Key1: Value1, Key2: Value2, Key3: Value3, ...}

dic = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}

a = {1: 'hi'}
a = {'a': [1, 2, 3]}

# 딕셔너리 쌍 추가
a = {1: 'a'}
a[2] = 'b'
a

# 요소 삭제
del a[1]
a

grade = {'pey': 10, 'julliet': 99}
grade['pey']
grade['julliet']

# 딕셔너리에서 Key는 고유한 값이므로 중복되는 Key 값을 설정해 놓으면 하나를 제외한 나머지 것들이 모두 무시된다는 점에 주의해야 한다
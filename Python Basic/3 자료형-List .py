# 리스트 - 여러 개의 데이터를 담을 수 있는 자료형 

# 리스트를 만들 때는 대괄호로 감싸 주고 각 요소의 값은 쉼표로 구분
# list_name = [element1, element2, ... , element3]

a = []
b = [1, 2, 3]
c = ['Life', 'is', 'too', 'short']
d = [1, 2, 'Life', 'is']
e = [1, 2, ['Life', 'is']]

# 리스트의 Indexing 
aa = [1, 2, 3]
aa

a = [1, 2, 3, ['a', 'b', 'c']]

# 리스트의 slicing
a = [1, 2, 3, 4, 5]
a[0:2]

a = [1, 2, 3]
b = [4, 5, 6]
a + b

s = [1, 2, 3]
s * 3

t = [1, 2, 3]
len(t)

a = [1, 2, 3]
del a[1]
a
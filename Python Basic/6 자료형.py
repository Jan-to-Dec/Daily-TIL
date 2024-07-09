# 집합 자료형은 set 키워드 사용
# 중복을 허용하지 않는다.
# 순서가 없다(Unordered).

s2 = set("Hello")
s2

# set 자료형은 순서가 없기(unordered) 때문에 인덱싱을 통해 요소값을 얻을 수 없다. 

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

#교집합
s1 & s2

s1.intersection(s2)

#합집합 
s1 | s2

s1.union(s2)

# 차집합 
s1 - s2


# 값 1개 추가 
s1 = set([1, 2, 3])
s1.add(4)
s1

# 값 여러개 추가 
s1 = set([1, 2, 3])
s1.update([4, 5, 6])
s1 

# Bool 자료형은 True & False로 나타내는 자료형이다

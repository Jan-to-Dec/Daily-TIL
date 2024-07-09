#%%
# 021
letters = 'python'
print(letters[0], letters[2])
# 022
license_plate = "24가 2210"
print(license_plate[-4:])
# 023
string = "홀짝홀짝홀짝"
print(string[::2])
# 024
string = "PYTHON"
print(string[::-1])
# 025
phone_number = "010-1111-2222"
phone_number1 = phone_number.replace("-", " ")
print(phone_number1)
# 026
phone_number = "010-1111-2222"
phone_number1 = phone_number.replace('-', '')
print(phone_number1)
# 027
url = "http://sharebook.kr"
url_split = url.split('.')
print(url_split[-1])
# 028
# 문자열은 수정할 수 없음

# 029
string = 'abcdfe2a354a32a'
string = string.replace('a', 'A')
print(string)
# 030
string = 'abcd'
string.replace('b', 'B')
print(string)

#%%
# 031
a = "3"
b = "4"
print(a + b)
# 032
print("Hi" * 3)
# 033
print("-" * 80)
# 034
t1 = "python"
t2 = "java"
t3 = t1 + ' ' + t2 + ' '
print(t3 * 4)
# 035
name1 = "Hanna" 
age1 = 10
name2 = "Ron"
age2 = 13
print("이름: %s 나이: %d" % (name1, age1))
print("이름: %s 나이: %d" % (name2, age2))
# 036
name1 = "Chris" 
age1 = 10
name2 = "Angela"
age2 = 13
print("이름: {} 나이: {}".format(name1, age1))
print("이름: {} 나이: {}".format(name2, age2))
# 037
name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13
print(f"이름: {name1} 나이: {age1}")
print(f"이름: {name2} 나이: {age2}")
# 038
상장주식수 = "5,969,782,550"
컴마제거 = 상장주식수.replace(",", "")
타입변환 = int(컴마제거)
print(타입변환, type(타입변환))
# 039
분기 = "2020/03(E) (IFRS연결)"
print(분기[:7])
# 040
data = "   삼성전자    "
data1 = data.strip()
print(data1)


#%%
# 041
ticker = "btc_krw"
ticker1 = ticker.upper()
print(ticker1)
# 042
ticker = "BTC_KRW"
ticker = ticker.lower()
print(ticker)
# 043
a = "hello"
a = a.capitalize()
# 044
file_name = "보고서.xlsx"
file_name.endswith("xlsx")
# 045
file_name = "보고서.xlsx"
file_name.endswith(("xlsx", "xls"))
# 046
file_name = "2020_보고서.xlsx"
file_name.startswith("2020")
# 047
a = "hello world"
a.split()
# 048
ticker = "btc_krw"
ticker.split("_")
# 049
date = "2020-05-01"
date.split("-")
# 050
data = "039490     "
data = data.rstrip()
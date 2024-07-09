
#%%
# if statement
i = 10
if i>5:
    print('i is greater than 5..')
    
#%%
# if else statement
i = 4
if i>7:
    print('i is greater than 5..')
else:
    print('i is less than 5')    

#%%
i = 10
if i==5:
    print('i is equal 5..')
elif i==10:
    print('i is equal 10..')
else:
    print('i is other..')

#%%

marks = int(input("Enter the student's marks: "))

if marks >= 90:
    grade = 'A'
    if marks >= 95:
        distinction = True
    else:
        distinction = False
elif marks >= 80:
    grade = 'B'
    distinction = False
elif marks >= 70:
    grade = 'C'
    distinction = False
elif marks >= 60:
    grade = 'D'
    distinction = False
else:
    grade = 'F'
    distinction = False

print("Grade:", grade)

if distinction:
    print("Distinction achieved!")
    
#%%
# Short hand if statement
i = 10
if i<15: print('i less than 15..')

#%%
#Short hand if statement

i = 10
if i<15: print('i less than 15..')
   
#%% 
flag = int(input('Enter num: '))

match flag:
    case 5 :
        print('Flag = 5')
    case 10 :
        print('Flag = 10')
    case 15 :
        print('Flag = 15')
    case 20 :
        print('Flag = 20')
    case _ :
        print('Not matched')
        
#%%
# match-case문 예제 (문자열 입력)

role = 'Admin'

match role:
    case 'Emp' | 'User':
        print('Not allowed access..')
    case 'Admin':
        print('Allowed access to Admin..')
    case _ :
        print('No role..')        

#%%
count = 1
while count<5:
    print(count)
    count += 1
    
#%%
for i in range(1,5):
    print(i)            
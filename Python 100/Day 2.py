#%%
def greet():
    print('Hello World...')


#%%
def increment(n):
    n += 1
    print('In function: '+str(n))

n=10
print('Before function: '+str(n))
increment(n)
print('After function: '+str(n))

#%%
def prints(age,name,addr):
    print(age,name,addr)

prints(20,'Amy','incheon')
prints(age=21,name='Amy',addr='incheon')
prints(name='Amy',age=21,addr='incheon')
prints(addr='incheon',age=21,name='Amy')


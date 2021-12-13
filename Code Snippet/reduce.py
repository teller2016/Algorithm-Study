import functools
# reduce(함수, 순회 데이터, 초깃값)
a = functools.reduce(lambda x,y: x*10 + y, [1,2,3,4], 0)
print(a) # 1234
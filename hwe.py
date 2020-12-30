print("Roll number 12")
a_list = [1,2,3,4,5,6,7,8,9]
print(list(filter(lambda x : x%2,a_list)))
a = list(map(lambda x : x * 2,a_list))
print(a)
from functools import reduce
print(reduce(lambda x,y:( x*y),a_list))


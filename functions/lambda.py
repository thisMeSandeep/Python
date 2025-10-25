"""Lambda function """

# fun= lambda first_name, last_name : first_name.title()+" "+last_name.title()

# result=fun("sandeep" , "singh")
# print(result)


"""Filter with lambda function """
# lst=[1,2,3,4,5,6,7,8,9,10]

# result=list(filter(lambda x : x%2==0 , lst))
# print(result)


"""Map with lambda function"""

# lst=[1,2,3,4,5,6,7,8,9,10]

# result=list(map(lambda x : x*2 , lst))
# print(result)


"""Reduce with lambda function"""

from functools import reduce

lst=[1,2,3,4,5,6,7,8,9,10]

result=reduce(lambda x,y : x+y , lst)
print(result)
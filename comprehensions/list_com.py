"""newList= [expression for item in iterator if condition]"""

from functools import reduce

#get all even numbers

# lst=[1,2,4,8,3,7,9,10,14,13,18]
# even=[x for x in lst if x%2==0]
# print(even)


#get the words with character count>51 and make it uppercase

# lst: list[str] = ["Apple" , "And","Banana","name","orange"]
# ans=[word.upper() for word in lst  if len(word)>5]
# print(ans)


#sum of list elements
lst=[1,2,3,4,5,6,7,8,9,10]

total=reduce( lambda x,y:x+y  , lst)

print(total)
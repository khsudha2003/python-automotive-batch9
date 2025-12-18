myset={'apple', 'banana', 'pomegranet','apple',False,0,2}
mylist=['a','b','c']
myset2={'a','n'}
print(mylist)
#true = 1 
#false =0 
empty_set=set()
empty_dict={}
print(type(myset))
myset.add(10)
myset.discard('a')
myset.update(mylist)
count=len(mylist)
print(myset|myset2) #union
print(myset&myset2)#interaction
for fruit in mylist:
    print(fruit)
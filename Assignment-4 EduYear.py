#list of numbers
a = [25,36,47,55,33,505]
for i in a:
    if(str(i)[::-1]==str(i)):
        print(i)
        
        
#list of numbers, all palindromes
a = [1,2,3,4,5,6,7,10]
print(a)
for i in a:
    if(i%2==0):
        print(i*10)
    else:
        print(i+10)
        
        
# list of numbers duplicates, uniques
list = [ 3, 6, 9, 12, 3, 30, 15, 9, 45, 36, 12, 12]
dupItems = []
uniqItems = {}
for x in list:
   if x not in uniqItems:
      uniqItems[x] = 1
   else:
      if uniqItems[x] == 1:
         dupItems.append(x)
      uniqItems[x] += 1
print(dupItems)
print(uniqItems)
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
d = []
u = []
for i in list:
   if (list.count(i) == 1):
      u.append(i)
   else:
       d.append(i)
print("duplicates:",end=" ")
print(sorted(set(d)))
print("uniques:",end=" ")
print(sorted(set(u)))
nums=[1,2,3,4,5,6]
res = list(map(lambda x : x**2 ,  nums))
print(res)

res1 = list(map(lambda x: x%2==0 , nums))
print(res1)

res2 = list(map(lambda x: x-2 , nums))
print(res2)

res3 = list(map(lambda x: x+2 , nums))
print(res3)

res4 = list(map(lambda x: x>2 , nums))
print(res4)

res5 = list(map(lambda x: x<4 , nums))
print(res5)

res6 = list(map(lambda x: x*4 , nums))
print(res6)

res7 = list(map(lambda x: x%2 , nums))
print(res7)

res8 = list(map(lambda x: x/2 , nums))
print(res8)

res9 = list(filter(lambda x: x%2==0 , nums))
print(res9)

res10 = list(filter(lambda x: x%2==1 , nums))
print(res10)

res11 = list(filter(lambda x: x>2 , nums))
print(res11)
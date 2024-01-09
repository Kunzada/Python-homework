# 1. из [1,2,3,4,5,6,7] получить {1: 1, 3: 27, 5: 125, 7: 343}
old=[1,2,3,4,5,6,7]
new={i:i**3 for i in old if i%2!=0}
print(new)
# 2. из [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7] получить {2, 4, 6}
old1=[1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7]
new1={i for i in old1 if i%2==0}
print(new1)
# 3. получить список [0, 10, 20, 30, 40, 50, 60, 70, 80, 90] без исходного
new2=[i*10 for i in range(10)]
print(new2)
# 4. написать функцию-генератор с yield, которая может перебирать числа, делящиеся на 7, в диапазоне от 0 до n.
def enumerationOfElements(n):
    for i in range(0,n+1):
        if i%7==0:
            yield i
a=enumerationOfElements(100)
# print(next(a))
# print(next(a))
for i in a:
    print(i)
myList = [1, 2, 3, 4, 5]
def multiplyBy2(item):
    return item * 2

def filterOdd(item):
    return item % 2 != 0

# print(list(map(multiplyBy2, myList)))
print(list(filter(filterOdd, myList)))

print(2+4)
print(2/6)
print(type(2+4))
print(type(2/6))

print(2//6)
print(5//2) 
print(4//2)

print(round(2/6, 2))
print(abs(-5))
myList = [1, 2, 3, 4, 5]
def multiplyBy2(item):
    return item * 2

def filterOdd(item):
    return item % 2 != 0

# print(list(map(multiplyBy2, myList)))
print(list(filter(filterOdd, myList)))
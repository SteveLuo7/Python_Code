from collections import Iterator
a = [1,2,3,4,5,6,7,8,9]
def f(x):
    return x*x
result_list = []
for i in a:
    result_list.append(f(i))

print(result_list)

#   map
it = map(f,a)
print('is_iteratorble',isinstance(it,Iterator))
print(list(it))
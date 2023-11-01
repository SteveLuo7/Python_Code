y = [x*2 for x in range(1,50) if x % 5 ==0]
print(y)

s = [x for x in range(100) if x % 7 == 0]
print(s)

# 字典推导式
my_text = 'I LOVE YOU'
char_count = {c:my_text.count(c) for c in my_text}
print(char_count)

# 集合推导式
b = {x for x in range(100) if x % 7 == 0}
print(b)

v = (x for x in range(100) if x % 3 ==0)
print(tuple(v))
print(tuple(v))
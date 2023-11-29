from functools import reduce

# 原始序列
numbers = [1, 2, 3, 4, 5]

# 使用 reduce 对序列进行累积求和
sum_result = reduce(lambda x, y: x + y, numbers)
print("Sum:", sum_result)  # 输出: 15

# 使用 reduce 对序列进行累积求积
product_result = reduce(lambda x, y: x * y, numbers)
print("Product:", product_result)  # 输出: 120

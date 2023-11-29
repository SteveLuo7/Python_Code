from functools import partial

# 原始函数
def power(base, exponent):
    return base ** exponent

# 创建偏函数，固定 base 参数为 2
square = partial(power, base=2)

# 使用偏函数
result = square(exponent=3)
print(result)  # 输出: 8

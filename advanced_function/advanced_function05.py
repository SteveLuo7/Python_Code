# 定义一个函数，用于检查一个数是否为偶数
def is_even(number):
    return number % 2 == 0

# 原始序列
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 使用 filter 过滤出偶数
even_numbers = filter(is_even, numbers)

# 将结果转换为列表
even_numbers_list = list(even_numbers)

print("Original Numbers:", numbers)
print("Even Numbers:", even_numbers_list)

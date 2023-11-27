def merge_sort(alist):
    n = len(alist)
    if n <= 1:
        return alist
    mid = n//2
    left_li = merge_sort(alist[0:mid])
    right_li = merge_sort(alist[mid:])

    result = []
    left_pointer,right_pointer = 0,0
    while left_pointer < len(left_li) and right_pointer < len(right_li):
        if left_li[left_pointer] < right_li[right_pointer]:
            result.append(left_li[right_pointer])
            left_pointer += 1
        else:
            result.append(right_li[right_pointer])
            right_pointer += 1

    result += left_li[left_pointer:]
    result += right_li[right_pointer:]

    return result



if __name__ == '__main__':
    alist = [1,4,23,45,76,98,123,756,6,8,9]
    print('original list ',alist)
    result = merge_sort(alist)
    print('merge_list ',result)
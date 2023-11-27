'''
    insert sort
'''


def insert_sort(list):
    n = len(list)
    for j in range(1,n):
        i = j
        while i>0:
            if list[i]<list[i-1]:
                list[i],list[i-1] =list[i-1],list[i]
            else:
                break

            i -= 1

if __name__ == '__main__':
    list = [1,4,5,7,8,9,123,543,65,34,76,98,432,85,976]
    print('original list: {}'.format(list))
    insert_sort(list)
    print('insert_sorted list: {}'.format(list))
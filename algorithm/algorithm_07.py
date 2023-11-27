'''
    insert sort
'''


def quick_sort(alist,start,end):
    if start >= end:
        return
    mid = alist[start]
    low = start
    high = end

    while low<high:

        while low<high and alist[high]>mid:
            high -= 1
        alist[low] = alist[high]

        while low<high and alist[low]<mid:
            low += 1
        alist[high] = alist[low]

    alist[low] = mid

    quick_sort(alist,start,low-1)
    quick_sort(alist,low+1,end)




if __name__ == '__main__':
    alist = [123,34,2,6,8,0,125432,324]
    print(alist)
    quick_sort(alist,0,len(alist)-1)
    print(alist)
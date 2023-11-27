#   bublle sort

def bublle_sort(alist):
    #   each 2 elements compare, exchange if they were in wrong position
    n = len(alist)
    for j in range(n-1):
        count = 0
        for i in range(n-1-j):
            if alist[i] > alist[i+1]:
                alist[i],alist[i+1] = alist[i+1],alist[i]
                count += 1
        if count == 0:
            break
alist = [1,4,6,32,54,567,123,22,34,312,45,76543,90,12,0,66,432,11,2,77]
print('Original list: ', alist)
bublle_sort(alist)
print('New list: ', alist)

alist2 = [1,2,3,4,5,6,7]
bublle_sort(alist2)
print('Order list: ',alist2)
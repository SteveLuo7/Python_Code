'''
    selection sort
'''

list = [1,4,6,32,54,567,123,22,34,312,45,76543,90,12,0,66,432,11,2,77]

def selection_list(list):
    n = len(list)
    for i in range(n-1):
        min_index = i
        for j in range(i+1,n):
            if list[min_index] > list[j]:
                min_index = j
        list[i],list[min_index]=list[min_index],list[i]

print('Original list: ',list)
selection_list(list)
print('Selection list: ',list)

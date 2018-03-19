# Sum of array without highest and lowest number from array.
'''The highest/lowest element is respectively only one element at each edge, 
even if there are more than one with the same value!)'''


def sum_array(arr):
    if arr == None or len(arr) == 0:
        return 0
    else:
        arr.sort()
        return sum(arr[1:-1])

print sum_array([])
def binary_search(left, right, x):
    while left < right: 
        mid = left + (right-left)/2
        if abs(pow(mid, 2) - x) <= 0.01:
            return mid
        elif pow(mid, 2) < x:
            left = mid
        else:
            right = mid
    return -1

#print(binary_search(0,200,200))



def binary_search1(left, right, x):
        mid = left + (right-left)/2
        if left >= right: 
            return -1
        if abs(pow(mid, 2) - x) <= 0.01:
            return mid
        elif pow(mid, 2) < x:
            binary_search1(mid, right, x)
        else:
            binary_search1(left, mid, x)

print(binary_search1(0,200,200))
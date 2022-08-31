def merge(arr: list, left: int, mid: int, right: int) -> list:
    first = arr[left:mid]
    second = arr[mid:right]
    n, m = len(first), len(second)
    i = j = 0
    result = []
    while i < n and j < m:
        if first[i] < second[j]:
            result.append(first[i])
            i += 1
        else:
            result.append(second[j])
            j += 1
    result += first[i:] + second[j:]
    return arr[:left] + result + arr[right:]

def merge_sort(arr: list, left: int, right: int) -> None:
    if left + 1 >= right:
        return 
    mid = left+(right-1)//2
    merge_sort(arr, left, mid)
    merge_sort(arr, mid, right)
    arr = merge(arr, left, mid, right)
    return arr




# def test():
# 	a = [1, 4, 9, 2, 10, 11]
# 	b = merge(a, 0, 3, 6)
# 	expected = [1, 2, 4, 9, 10, 11]
# 	assert b == expected
# 	c = [1, 4, 2, 10, 1, 2]
# 	merge_sort(c, 0 , 6)
# 	expected = [1, 1, 2, 2, 4, 10]
# 	assert c == expected


print(merge_sort([-6, -12, -14, 14,0,7,1,5,1], 0, 9))
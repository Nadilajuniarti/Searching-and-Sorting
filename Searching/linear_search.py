def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


data = [12, 7, 25, 9, 15]
target = 9

print(linear_search(data, target))

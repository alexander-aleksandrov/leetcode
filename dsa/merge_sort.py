def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    result = merge(left, right)

    return result

def merge(left, right):
    if not left or not right:
        return left or right
    result = []
    while len(left) and len(right):
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result.extend(left)
    result.extend(right)
    return result

def main():
    arr = [7, 4, 8, 6, 3, 5]
    print(merge_sort(arr))

if __name__ == "__main__":
    main()
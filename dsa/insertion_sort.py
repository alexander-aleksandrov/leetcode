def insertion_sort(arr):
    if len(arr) == 0:
        return "Empty array"
    if len(arr) == 1:
        return arr
    if len(arr) == 2:
        if arr[0] > arr[1]:
            arr[0], arr[1] = arr[1], arr[0]
        return arr
    for i in range(len(arr)):
        j=i
        while arr[j] < arr[j-1] and j > 0:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
    return arr

             
    

def main():
    arr = [7, 4, 8, 6, 3, 5]
    print(insertion_sort(arr))

if __name__ == "__main__":
    main()
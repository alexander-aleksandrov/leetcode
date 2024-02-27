def find_missing_number(arr):
    start = 0 
    while start < len(arr):
        num  = arr[start]
        if num != start and num < len(arr):
            arr[num], arr[start] = arr[start], arr[num]
        else:
            start += 1 

    for i in range(len(arr)):
        if i != arr[i]:
            return i
    else:
        return None
        
def main(): 
    arr = [3, 0, 1] 
    print(find_missing_number(arr))

if __name__ == "__main__":
    main()
    


        
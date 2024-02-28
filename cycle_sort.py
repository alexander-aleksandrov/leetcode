def find_missing_number(arr):
    start = 0 
    while start < len(arr): # swap the number to its correct index
        num  = arr[start]
        if num != start and num < len(arr): 
            arr[num], arr[start] = arr[start], arr[num]
        else:
            start += 1 

    for i in range(len(arr)): # find the missing number
        if i != arr[i]:
            return i
    else:
        return None

# for arr [1, n]        
def find_duplicates(arr):
    cur = 0
    while cur < len(arr): # swap the number to its correct index
        number_proper_possition = arr[cur] - 1 
        if arr[cur] != arr[number_proper_possition]: 
            arr[cur], arr[number_proper_possition] = arr[number_proper_possition], arr[cur]
        else:
            cur += 1
    result = []
    for i in range(len(arr)):
        if arr[i] - 1 != i :
            result.append(arr[i])
    return result


def find_all_missing_numbers(arr):
    cur = 0 
    while cur < len(arr): # swap the number to its correct index
        number_proper_possition = arr[cur] - 1
        if number_proper_possition >= len(arr): 
            cur += 1
            continue
        if arr[cur] != arr[number_proper_possition]: 
            arr[cur], arr[number_proper_possition] = arr[number_proper_possition], arr[cur]
        else:
            cur += 1
    result = []
    for i in range(len(arr)):
        if arr[i] - 1 != i :
            result.append(i + 1)
    return result 

def main(): 
    
    arr = [7, 4, 8, 6, 3, 5]
    print(find_all_missing_numbers(arr))

if __name__ == "__main__":
    main()
    


        
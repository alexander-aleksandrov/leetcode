from insertion_sort import insertion_sort

def bucket_sort(arr):
    max_value = max(arr)
    size = (max_value/len(arr))
    num_of_buckets = int(max_value/size)
    buckets = [[] for _ in range(num_of_buckets)]
    for i in range(len(arr)):
        j = int(arr[i]/size)
        if j != num_of_buckets:
            buckets[j].append(arr[i])
        else:
            buckets[num_of_buckets - 1].append(arr[i])
    for i in range(len(buckets)):
        insertion_sort(buckets[i])
    result = [] 
    for i in range(len(buckets)):
        result = result + buckets[i]
    return result




def main():
    arr = [7, 4, 8, 6, 3, 5]
    print(bucket_sort(arr)) 

if __name__ == "__main__":
    main()
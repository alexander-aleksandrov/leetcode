# Define a quick sort function using auxiliary space
def quick_sort_with_auxiliary_space(arr):
    # Base case: if the array is empty or contains a single element, it is already sorted
    if len(arr) <= 1:
        return arr 
    # Choose the first element as the pivot
    pivot = arr[0]
    # Partition the array into two parts: elements less than or equal to the pivot and elements greater than or equal to the pivot
    left_side = [x for x in arr[1:] if x <= pivot]
    right_side = [x for x in arr[1:] if x > pivot]
    # Recursively sort the partitions
    left_side = quick_sort_with_auxiliary_space(left_side)
    right_side = quick_sort_with_auxiliary_space(right_side)
    # Combine the sorted partitions and the pivot back into a single list
    return left_side + [pivot] + right_side

# Define a quick sort function that sorts in-place
def quick_sort_in_place(arr, start, end):
    # Base case: if the start index is greater or equal to the end index, the partition is already sorted
    if start < end:
        # Partition the array and get the pivot index
        pivot_index = partition(arr, start, end)
        # Recursively sort elements before the pivot
        quick_sort_in_place(arr, start, pivot_index-1)
        # Recursively sort elements after the pivot
        quick_sort_in_place(arr, pivot_index+1, end)
        
# Partition the array around a pivot
def partition(arr, low, high):
    # Choose the last element as the pivot
    pivot = arr[high]
    i = low  # Initialize the pointer for the smaller element
    # Traverse through all elements in the current partition
    for j in range(low, high):
        # If the current element is less than or equal to the pivot
        if arr[j] <= pivot:
            # Swap it with the element at index i
            arr[i], arr[j] = arr[j], arr[i]
            # Move the pointer for the smaller element one position forward
            i += 1
    # Place the pivot after the last element smaller than it
    arr[i], arr[high] = arr[high], arr[i] 
    # Return the index position of the pivot
    return i


def main():
    arr = [7, 4, 8, 6, 3, 5]
    result = quick_sort_in_place(arr, 0, len(arr)-1)
    print(arr)

if __name__ == "__main__":  
    main()
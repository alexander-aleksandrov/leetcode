def max_sum_subarray(arr, k):
    start = 0 
    window_sum = 0
    max_sum = 0
    for i in range(len(arr)):
        window_sum += arr[i]
        if (i-start+1)==k:
            max_sum = max(window_sum, max_sum) 
            window_sum -= arr[start]
            start += 1

    return max_sum 

def count_ocurrences_of_annagram(text, word):
    start = 0
    wordHeap = [0]*26
    window = [0]*26
    count = 0
    for char in word: 
        wordHeap[ord(char) - ord("a")] +=1

    for i in range(len(text)):

        window[ord(text[i]) - ord("a")] +=1
        if (i - start + 1) == len(word):
            if window == wordHeap:
                count +=1 
            window[ord(text[start]) - ord("a")] -=1
            start +=1
    return count

# find minimum substring that contains a specifiq chars 
def count_min_substring(text, chars):
    min_sub_str = [""]*len(text)
    current_sub_str = []
    chars_map = {i: chars.count(i) for i in set(chars)}
    head = 0
    for i in range(len(text)):
        if text[i] in chars_map:
            if chars_map[text[i]]!=0: # we NOT out of this kind of chars 
                chars_map[text[i]] -= 1
                current_sub_str.append(text[i])
                
                if sum(chars_map.values()) == 0: # did we find a substring?
                    min_sub_str = current_sub_str if len(current_sub_str) < len(min_sub_str) else min_sub_str
            else:
                while chars_map[text[i]] == 0: #shrinking a window 
                    char = current_sub_str[0]
                    if char in chars_map:
                        chars_map[char] += 1
                    current_sub_str = current_sub_str[1:]
                chars_map[text[i]] -= 1
                current_sub_str.append(text[i])
                if sum(chars_map.values()) == 0: # did we find a substring?
                    min_sub_str = current_sub_str if len(current_sub_str) < len(min_sub_str) else min_sub_str
                    while min_sub_str[0] not in chars_map:
                        min_sub_str = min_sub_str[1:]
        else:
            current_sub_str.append(text[i])
    return min_sub_str    
    
def max_sum_subarray_kadane(arr):
    start = 0 
    window_sum = 0
    max_sum = 0
    for i in range(len(arr)):
        window_sum += arr[i]
        if window_sum < 0:
            window_sum = 0
            continue
        max_sum = max(window_sum, max_sum)
    return max_sum 

def max_sum_subarray_kadane_of_k(arr, k):
    start = 0 
    window_sum = 0
    max_sum = 0
    for i in range(len(arr)):
        window_sum += arr[i]
        if window_sum < 0:
                window_sum = 0
                start = i + 1
                continue       
        if (i - start + 1) == k:            
            max_sum = max(window_sum, max_sum)
            start += 1 
            window_sum -= arr[start]
    return max_sum 

def main(): 
    arr = [1, 2, -4, 3, 4, -2]
    print(max_sum_subarray_kadane_of_k(arr, 3))

if __name__ =="__main__":
    main()

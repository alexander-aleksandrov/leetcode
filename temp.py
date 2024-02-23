"""
Your task is to complete the function find3Numbers which finds any 3 elements in it such that A[i] < A[j] < A[k] and i < j < k. You need to return them as a vector/ArrayList/array (depending on the language cpp/Java/Python), if no such element is present then return the empty vector of size 0.
"""
def find3number(A, n): 
    min_number = [0] * n
    max_number = [0] * n
    min_number[0] = A[0]
    max_number[n - 1] = A[n - 1]
    for i in range(1, n):
        min_number[i] = min(min_number[i - 1], A[i])
    for i in range(n - 2, -1, -1):
        max_number[i] = max(max_number[i + 1], A[i])
    for i in range(1, n - 1):
        if min_number[i] < A[i] < max_number[i]:
            return [min_number[i], A[i], max_number[i]]
    return []

    
    

            
            




def main():
    # 48 43 60 2 93 93 30 100 26 47 25 2 49 34 42 58 47 16 73 16 11 6 91
    A = [48, 43, 60, 2, 93, 93, 30, 100, 26, 47, 25, 2, 49, 34, 42, 58, 47, 16, 73, 16, 11, 6, 91]
    n = 23
    print(find3number(A, n))
   
    
main()
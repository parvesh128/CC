# Enter your code here. Read input from STDIN. Print output to STDOUT

def subArrayMax(arr):
    
    curr_Max = arr[0]
    max_so_far = arr[0]
    
    for idx in range(1, len(arr), 1):
        curr_Max = max(arr[idx], curr_Max + arr[idx])
        max_so_far = max(max_so_far, curr_Max)
        
    return max_so_far

def nonContArrayMax(arr):
    
    max_elem = max(arr)
    
    if max_elem < 0:
        return max_elem
    
    max_sum = 0
    
    for elem in arr:
        if elem > 0:
            max_sum += elem
            
    return max_sum
        
numCases = int(raw_input())

for case in range(numCases):
    size = int(raw_input())
    arr = map(int, raw_input().split())
    
    maxContSum = subArrayMax(arr)
    maxNonContSum = nonContArrayMax(arr)
    
    print maxContSum, maxNonContSum
    


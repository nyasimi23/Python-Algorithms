import listsfunction
def selection_sort(arr):
    n = len(arr)
    
    for i in range(n):
        min_idx = i
        
        # Find the minimum element in the remaining unsorted part of the array
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr

# Example usage:
if __name__ == '__main__':
    extract = listsfunction.extract_data()
    result = selection_sort(extract)
    print(result)
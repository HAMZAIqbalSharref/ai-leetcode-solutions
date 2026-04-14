### Understanding
You have a sorted array of integers and a specific target value. Your goal is to find out where the target value is located in the array. If it exists, you should return its index, otherwise, return -1 to indicate that the target isn't found.

### Intuition
Since the array is sorted, you can take advantage of this property to perform a more efficient search than simply checking each element one by one. A binary search algorithm is ideal for this situation, as it repeatedly divides the search interval in half, allowing you to quickly hone in on the target value.

### Approach
1. **Initialize Pointers:** Start with two pointers, one at the beginning of the array (`left`) and one at the end of the array (`right`).
2. **While Loop:** Keep looping while `left` is less than or equal to `right`:
   - Calculate the middle index as `mid = left + (right - left) // 2`.
   - Check if the element at the `mid` index is equal to the target. If it is, return the `mid` index.
   - If the element is less than the target, it means the target must be on the right side of the array, so update `left` to `mid + 1`.
   - If the element is greater than the target, update `right` to `mid - 1`.
3. **Return -1:** If the loop exits without finding the target, return -1.

### Code
Here is how you can implement the above approach in Python:

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1
```

### Complexity
- **Time Complexity:** O(log n), where n is the number of elements in the array, because we halve the search space with each iteration.
- **Space Complexity:** O(1), since we are using a constant amount of space regardless of the input size.
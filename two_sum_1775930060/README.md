### Understanding
You have an array (or list) of integers called `nums`, and a specific integer called `target`. The task is to find two distinct elements in the array such that their sum equals the target. The output should be the indices (positions) of these two elements in the array.

### Intuition
To solve this problem, you need to look for pairs of numbers in the array that add up to the `target`. A naive approach would involve checking all possible pairs, but that could be inefficient for large arrays. Instead, we can use a more efficient approach by utilizing a dictionary (hash map) to keep track of the numbers we've seen so far while iterating through the list. 

### Approach
1. Initialize an empty dictionary (hash map) to store the numbers as keys and their indices as values.
2. Loop through the `nums` array. For each number, calculate the complement (which is `target - current number`).
3. Check if the complement is already in the dictionary:
   - If yes, it means we've found the two numbers that add up to the target, so return their indices.
   - If no, store the current number and its index in the dictionary.
4. Continue until a pair is found.

### Code
```python
def two_sum(nums, target):
    # Dictionary to store the number and its index
    num_map = {}
    
    # Iterate over the list with indices
    for index, num in enumerate(nums):
        complement = target - num  # Calculate complement
        if complement in num_map:  # Check if complement exists
            return [num_map[complement], index]  # Return indices of numbers that sum to target
        num_map[num] = index  # Store the index of the current number
    
    return []  # Return empty if no pair found
```

### Complexity
- **Time Complexity:** O(n), where n is the number of elements in the `nums` array. We go through the array once.
- **Space Complexity:** O(n), in the worst case, we might store all n elements in the dictionary.
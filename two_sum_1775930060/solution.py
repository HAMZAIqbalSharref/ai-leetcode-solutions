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
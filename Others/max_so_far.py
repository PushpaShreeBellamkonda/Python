def count_greater_elements(arr):
    if not arr:  # Handle empty array case
        return 0

    count = 1  # First element is always counted
    max_so_far = arr[0]

    for num in arr[1:]:  # Start from second element
        if num > max_so_far:
            count += 1
            max_so_far = num  # Update max encountered

    return count

# Example usage
arr = [3,4,5,8,9]
print(count_greater_elements(arr))  # Output: 3

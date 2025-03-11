def josephus_recursive(n, k):
    if n == 1:
        return 0  # Base case: if there's only one person, they survive
    else:
        # Recursive step: adjust the result for the current circle size
        return (josephus_recursive(n - 1, k) + k) % n

# Example usage
n = 7  # Number of people
k = 3  # Step count
survivor = josephus_recursive(n, k)
print(f"The survivor is at position: {survivor + 1}")

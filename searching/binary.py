def bsearch(l,x):
    low=0
    high=len(l)-1
    while low<=high:
        mid=(low+high)//2
        if l[mid]==x:
            return mid
        elif l[mid]<x:
            low=mid+1
        else:
            high=mid-1
    return -1

l=[10,20,30,40,50,60]
x=60
print(bsearch(l,x))


# iterative approach

def recursive_bsearch(l, x, low, high):
    if low > high:
        return -1  # Base case: element not found
    
    mid = (low + high) // 2  # Calculate the middle index
    
    if l[mid] == x:  # Base case: element found
        return mid
    elif l[mid] < x:  # Search in the right half
        return recursive_bsearch(l, x, mid + 1, high)
    else:  # Search in the left half
        return recursive_bsearch(l, x, low, mid - 1)

# Wrapper function for cleaner API
def binary_search_recursive(l, x):
    return recursive_bsearch(l, x, 0, len(l) - 1)

# Example usage
l = [10, 20, 30, 40, 50, 60]
x = 60
print(binary_search_recursive(l, x))  # Output: 5




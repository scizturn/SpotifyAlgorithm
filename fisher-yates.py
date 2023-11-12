import random

def fisher_yates_shuffle(arr):
    # n = len(arr)
    for i in range(n - 1, 0, -1):
        # Generate a random index between 0 and i (inclusive)
        j = random.randint(0, i)
        
        # Swap the elements at i and j
        arr[i], arr[j] = arr[j], arr[i]

# Example usage:
my_list = [1, 2, 3, 4, 5]
fisher_yates_shuffle(my_list)
print(my_list)

#descending Insertion Assignment

def insertion_sort_descending(n):
    for i in range(1, len(n)):
        key = n[i]
        j = i - 1
        while j >= 0 and key > n[j]:
            n[j + 1] = n[j]
            j -= 1
        n[j + 1] = key

# Example usage
n = [5, 2, 4, 6, 1, 3]
insertion_sort_descending(n)
print("Array in descending order:", n)

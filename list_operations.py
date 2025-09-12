# More operations on lists

numbers = [10, 20, 30, 40, 50]

print("Original List:", numbers)

# 1. Insert at a specific index
numbers.insert(2, 25)   # insert 25 at index 2
print("After insert at index 2:", numbers)

# 2. Extend with another list
numbers.extend([60, 70, 80])
print("After extend:", numbers)

# 3. Sorting
numbers.sort()
print("Sorted list:", numbers)

# 4. Reverse
numbers.reverse()
print("Reversed list:", numbers)

# 5. Slicing
print("First three elements:", numbers[:3])
print("Last two elements:", numbers[-2:])

# 6. Find index of an element
if 40 in numbers:
    print("Index of 40:", numbers.index(40))

# 7. Count occurrences
print("Count of 50:", numbers.count(50))

# 8. Clear the list
numbers.clear()
print("After clearing list:", numbers)
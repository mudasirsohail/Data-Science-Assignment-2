# Examples of List Methods
numbers = [1, 2, 3, 4, 5]

# 1. append()
numbers.append(6)
print(numbers)             # [1, 2, 3, 4, 5, 6]

# 2. insert()
numbers.insert(2, 10)
print(numbers)             # [1, 2, 10, 3, 4, 5, 6]

# 3. extend()
numbers.extend([7, 8])
print(numbers)             # [1, 2, 10, 3, 4, 5, 6, 7, 8]

# 4. remove()
numbers.remove(10)
print(numbers)             # [1, 2, 3, 4, 5, 6, 7, 8]

# 5. pop()
numbers.pop()
print(numbers)             # [1, 2, 3, 4, 5, 6, 7]

# 6. clear()
nums = [1, 2, 3]
nums.clear()
print(nums)                # []

# 7. sort()
nums2 = [3, 1, 4, 2]
nums2.sort()
print(nums2)               # [1, 2, 3, 4]

# 8. reverse()
nums2.reverse()
print(nums2)               # [4, 3, 2, 1]

# 9. count()
print(numbers.count(3))    # 1

# 10. index()
print(numbers.index(4))    # 3

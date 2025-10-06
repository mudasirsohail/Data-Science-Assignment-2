# Examples of Set Methods
a = {1, 2, 3}
b = {3, 4, 5}

# 1. add()
a.add(6)
print(a)                      # {1, 2, 3, 6}

# 2. update()
a.update([7, 8])
print(a)                      # {1, 2, 3, 6, 7, 8}

# 3. remove()
a.remove(2)
print(a)                      # {1, 3, 6, 7, 8}

# 4. discard()
a.discard(9)                  # no error if 9 not found
print(a)

# 5. pop()
a.pop()
print(a)                      # removes random element

# 6. clear()
temp = {1, 2}
temp.clear()
print(temp)                   # set()

# 7. union()
print(a.union(b))             # {1, 3, 4, 5, 6, 7, 8}

# 8. intersection()
print(a.intersection(b))      # {3}

# 9. difference()
print(a.difference(b))        # Elements only in 'a'

# 10. symmetric_difference()s
print(a.symmetric_difference(b))  # Elements not in both

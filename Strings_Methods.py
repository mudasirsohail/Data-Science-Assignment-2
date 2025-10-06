# Examples of String Methods
text = "hello world"

# 1. upper()
print(text.upper())        # "HELLO WORLD"

# 2. lower()
print(text.lower())        # "hello world"

# 3. title()
print(text.title())        # "Hello World"

# 4. capitalize()
print(text.capitalize())   # "hello world "

# 5. strip()
print(text.strip())        # "hello world"

# 6. replace()
print(text.replace("world", "Python"))  # "hello Python"

# 7. split()
print(text.split())        # ['hello', 'world']

# 8. join()
words = ["I", "love", "Python"]
print(" ".join(words))     # "I love Python"

# 9. find()
print(text.find("world"))  # 8

# 10. count()
print(text.count("l"))     # 3

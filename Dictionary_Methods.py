# Examples of Dictionary Methods
person = {
    "name": "Mudasir",
    "age": 18,
    "city": "Karachi"
}

# 1. get()
print(person.get("name"))     # Mudasir

# 2. keys()
print(person.keys())          # dict_keys(['name', 'age', 'city'])

# 3. values()
print(person.values())        # dict_values(['Mudasir', 18, 'Karachi'])

# 4. items()
print(person.items())         # dict_items([('name', 'Mudasir'), ('age', 18), ('city', 'Karachi')])

# 5. update()
person.update({"country": "Pakistan"})
print(person)                 # {'name': 'Mudasir', 'age': 18, 'city': 'Karachi', 'country': 'Pakistan'}

# 6. pop()
person.pop("age")
print(person)                 # {'name': 'Mudasir', 'city': 'Karachi', 'country': 'Pakistan'}

# 7. popitem()
person.popitem()
print(person)                 # Removes last item

# 8. clear()
temp = {"x": 1, "y": 2}
temp.clear()
print(temp)                   # {}

# 9. setdefault()
person.setdefault("email", "mudasir@gmail.com")
print(person)                 # Adds key if missing

# 10. copy()
copy_person = person.copy()
print(copy_person)


dict_values = [
    {
        "name": "John",
        "age": 30,
        "city": "New York"
    },
    {
        "name": "Jane",
        "age": 25,
        "city": "Los Angeles"
    },
    {
        "name": "John",
        "age": 30,
        "city": "New York"
    },
    {
        "name": "Mike",
        "age": 35,
        "city": "Chicago"
    }
]


# Method 1: List Comprehension

unique_dicts = []

for d in dict_values:
    if d not in unique_dicts:
        unique_dicts.append(d)

print(unique_dicts, "Unique dictionaries using List Comprehension")
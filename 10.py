# JSon
"""JSON is a syntax for storing and exchanging data. 
JSON is text, written with JavaScript object notation."""

import json

x = '{"name": "Preston", "age": "34", "city": "Nairobi"}'
y = json.loads(x)
print(y['age'])

# Python to JSON

x = {
    "name": "preston",
    "age": "34",
    "city": "Nairobi"
}

y = json.dumps(x)
print(y)

x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": ("dog", "cat"),
    "cars":
        [{"make": "BMW", "model": "M5", "color": "Green"},
         {"make": "Ford", "model": "Gt", "color": "black"}]
}

print(json.dumps(x, indent=4, sort_keys=True))

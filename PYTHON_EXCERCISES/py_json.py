import json

# Sample JSON

userJSON = '{"first_name": "John", "Last_name": "Doe", "age":30}'

# Parse to a dictionary
user = json.loads(userJSON)

print(user)
print(user['first_name'])

car = {'make': 'Ford', 'model': 'Mustang', 'year': 1978}

carJSON = json.dumps(car)
print(carJSON)
print(type(carJSON))

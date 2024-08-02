import json

# Step 1: Create a dictionary representing an employee
employee = {
    'name': 'John',
    'age': 55,
    'salary': 4000.0,
    'isMarried': True,
    'isHavingCar': None
}

# Step 2: Serialize the dictionary to a JSON string
json_string = json.dumps(employee, indent=4)
print("Serialized JSON string:")
print(json_string)

# Step 3: Save the JSON string to a file
with open('emp.json', 'w') as f:
    json.dump(employee, f, indent=4)
print("\nJSON data has been written to emp.json")

# Step 4: Read the JSON string from the file
with open('emp.json', 'r') as f:
    employee_data = json.load(f)

# Step 5: Deserialize the JSON string back into a Python dictionary
print("\nDeserialized Python dictionary:")
print(employee_data)

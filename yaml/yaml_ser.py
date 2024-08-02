import yaml

# Step 1: Create a dictionary representing an employee
emp_dict = {'name': 'John', 'age': 45, 'salary': 6000.0, 'isMarried': True}

# Step 2: Serialization to YAML string
yaml_string = yaml.dump(emp_dict)
print("Serialized YAML string:")
print(yaml_string)

# Step 3: Serialization to YAML file
with open('emp.yaml', 'w') as f:
    yaml.dump(emp_dict, f)
print("\nYAML data has been written to emp.yaml")

# Step 4: Deserialization from YAML string
e_dict = yaml.safe_load(yaml_string)
print("\nDeserialized Python dictionary from string:")
print(e_dict)

# Step 5: Deserialization from YAML file
with open('emp.yaml', 'r') as f:
    e_dict_f = yaml.safe_load(f)
print("\nDeserialized Python dictionary from file:")
print(e_dict_f)

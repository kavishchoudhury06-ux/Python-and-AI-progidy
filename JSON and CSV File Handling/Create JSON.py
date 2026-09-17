import json
# Sample Python dictionary
user_data = {
"name": "Alice Smith",
"age": 30,
"skills": ["Python", "Data Analysis"],
"is_active": True
}
# Create and write to a JSON file
with open("user.json", "w") as file:
# 'indent=4' formats the file with spaces so it is easy for humans to read
    json.dump(user_data, file, indent=4)
print("JSON file created and written successfully!")
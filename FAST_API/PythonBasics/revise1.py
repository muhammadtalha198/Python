#craeting a dictionary 
user = {
    'name': 'John',
    'age': 25,
    'is_student': True
}

#accessing values
print(user['name'])  # Output: John
print(user.get('age'))  # Output: 25    

#List
users = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}, {"id": 3, "name": "Charlie"}]
print(users[0]['name'])  # Output: Alice    
print(users[1]['id'])    # Output: 2
print(users[2]['name'])  # Output: Charlie

#print all

for user in users:
    print(f"ID: {user['id']}, Name: {user['name']}")



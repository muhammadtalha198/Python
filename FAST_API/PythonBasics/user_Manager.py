from dataclasses import dataclass

# Create a dictionary for the new user
@dataclass
class User:
    id: int
    username: str
    age: int
    email: str

user_id = 0
users = [];

# Display menu 

def display_menu():
    print("\nUser Management System")
    print("1. Add User")
    print("2. View Users")
    print("3. Update User")
    print("4. Delete User")
    print("5. Exit")


while True:
    display_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        print("\nAdd User selected.")
        print("--------------------------------")

        username = input("Enter username: ")
        age = int(input("Enter age: "))
        email = input("Enter email: ")
        new_user = User(user_id, username, age, email)
        users.append(new_user)
        user_id += 1

        print(f"User {username} added successfully.")

    elif choice == '2':

        print("\nView All Users.")
        print("--------------------------------")
        if len(users) == 0:
            print("No users found.")
        else:   
            for user in users:
                print(f"ID: {user.id}, Username: {user.username}, Age: {user.age}, Email: {user.email}")



    elif choice == '3':
        print("Update User with id selected.")
        
        # enter the id of the user to update
        id = int(input("Enter id: "))
        
        for user in users:
            if user.id == id:
                
                user.username = input("Enter username: ")
                user.age = int(input("Enter age: "))
                user.email = input("Enter email: ")
                print(f"User with id {id} updated successfully.")
                break

            else:
                print(f"User with id {id} not found.")
                break  
                
       
    elif choice == '4':  
        
        print("\nDelete User with id selected.")
        
        id = int(input("Enter id: "))
        
        for user in users:
            if user.id == id:
                users.remove(user)
                print(f"User with id {id} deleted successfully.")
                break
            else:
                print(f"User with id {id} not found.")
                break
        
    elif choice == '5':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")


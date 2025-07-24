
#  create a users table (database set up) 
import sqlite3

def init_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT NOT NULL,
            is_logged_in INTEGER DEFAULT 0  
        )
    ''')
    conn.commit()
    conn.close()
print("Table created (or already exists)")

# for showing table
def show_users():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    for user in users:
        print(user)
    conn.close()

# Call this function 
init_db()
show_users()


# hashlib for store password securely
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# user creates an accounts 
import getpass

def register():
    username = input("Enter username: ")

    if not username:
        print("Username cannot be empty.")
        return

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    if cursor.fetchone():
        print("Username already exists.")
        conn.close()
        return

    while True:
        password = getpass.getpass("Enter password: ")
        if not password:
            print("Password cannot be empty.")
        elif len(password) < 6 or len(password) > 12:
            print("Password must be between 6 and 12 characters.")
        else:
            break

    hashed_pw = hash_password(password)

    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_pw))
    conn.commit()
    conn.close()
    print("User registered successfully!")



# login function ()

def login():
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")
    hashed_pw = hash_password(password)

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    
    # Check if username exists
    cursor.execute("SELECT password, is_logged_in FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()

    if not result:
        print("Invalid username.")
    elif result[1] == 1:
        print("Already logged in.")
    elif result[0] == hashed_pw:
        # Check if any other user is already logged in
        cursor.execute("SELECT username FROM users WHERE is_logged_in = 1")
        other_logged_in = cursor.fetchone()
        
        if other_logged_in:
            print(f"User '{other_logged_in[0]}' is already logged in. Logging them out...")
            cursor.execute("UPDATE users SET is_logged_in = 0 WHERE username = ?", (other_logged_in[0],))
        
        # Now log in the new user
        cursor.execute("UPDATE users SET is_logged_in = 1 WHERE username = ?", (username,))
        conn.commit()
        print("Login successful!")
    else:
        print("Wrong password.")
        
    conn.close()



# logout function() 
def logout():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # Check if any user is logged in
    cursor.execute("SELECT username FROM users WHERE is_logged_in = 1")
    logged_in_users = cursor.fetchall()

    if not logged_in_users:
        print("No users are currently logged in.")
        conn.close()
        return

    # If some user is logged in, ask which one to log out
    print("Logged-in users:")
    for user in logged_in_users:
        print("-", user[0])

    username = input("Enter username to logout: ").strip()

    cursor.execute("SELECT is_logged_in FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()

    if result and result[0] == 1:
        cursor.execute("UPDATE users SET is_logged_in = 0 WHERE username = ?", (username,))
        conn.commit()
        print("Logged out successfully.")
    else:
        print("This user is not logged in.")
    conn.close()



# change password function
def change_password():
    username = input("Enter your username: ")

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT password, is_logged_in FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()

    if not result:
        print("User not found.")
        conn.close()
        return

    if result[1] == 0:
        print("Please login first.")
        conn.close()
        return

    old_pass = getpass.getpass("Enter current password: ")
    if hash_password(old_pass) != result[0]:
        print("Incorrect current password.")
        conn.close()
        return

    while True:
        new_pass = getpass.getpass("Enter new password: ")
        if len(new_pass) < 6 or len(new_pass) > 12:
            print("Password must be between 6 and 12 characters.")
        else:
            break

    cursor.execute("UPDATE users SET password = ? WHERE username = ?", (hash_password(new_pass), username))
    conn.commit()
    conn.close()
    print("Password changed successfully.")



# console menu
def main():
    init_db()
    while True:
        print("\n========== USER MENU ==========")
        print("1. Register")
        print("2. Login")
        print("3. Logout")
        print("4. Change Password")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            logout()
        elif choice == '4':
            change_password()
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice.")

# start the function
if __name__ == "__main__":
    main()







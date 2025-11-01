# validate_username.py
# Task 01 - Validate user module
# Rules:
# 1. Username must be no more than 12 characters.
# 2. Username must not contain spaces.
# 3. Username must not contain numeric characters.

def is_valid_username(username: str) -> (bool, str):
    if len(username) == 0:
        return False, "Username cannot be empty."
    if len(username) > 12:
        return False, "Your username can't be longer than 12 characters."
    if " " in username:
        return False, "Your username can't contain spaces."
    if any(ch.isdigit() for ch in username):
        return False, "Your username can't contain numeric characters."
    return True, "Username is valid."

def main():
    while True:
        username = input("Enter the username: ").strip()
        valid, message = is_valid_username(username)
        if valid:
            print(f"✅ Your username is: {username}")
            break
        else:
            print(f"❌ {message}\nPlease try again.\n")

if __name__ == "__main__":
    main()

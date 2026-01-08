import random
import string

def generate_password(length=12):
    """Generate a secure random password."""
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

if __name__ == "__main__":
    pwd_length = int(input("Enter password length: "))
    print("Generated Password:", generate_password(pwd_length))

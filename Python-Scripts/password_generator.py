import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    # Ensure a strong password includes at least one of each type
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation),
    ]
    password += random.choices(characters, k=length - 4)
    random.shuffle(password)
    return ''.join(password)

if __name__ == "__main__":
    user_length = int(input("Enter desired password length (minimum 8): "))
    if user_length < 8:
        print("Password length should be at least 8 characters.")
    else:
        password = generate_password(user_length)
        print("Generated Password:", password)

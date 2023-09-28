





    password = random.sample(lowercase_letters, 1) + random.sample(uppercase_letters, 1) + random.sample(digits, 1) + random.sample(special_chars, 1) + random.sample(all_chars, length - 4)
    
    # Shuffle the password characters
    random.shuffle(password)
    
    # Convert the list of characters to a string
    password_str = ''.join(password)
    
    return password_str

# Example usage: Generate a password of length 16 with digits and special characters
password = generate_password(length=16, include_digits=True, include_special_chars=True)
print(password)import random
import string

def generate_password(length=12, include_digits=True, include_special_chars=True):
    # Define character sets
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits if include_digits else ''
    special_chars = string.punctuation if include_special_chars else ''

    # Combine character sets based on user preferences
    all_chars = lowercase_letters + uppercase_letters + digits + special_chars

    # Ensure the password length is at least 4 characters for each character set
    length = max(length, 4)
    
    # Generate the password

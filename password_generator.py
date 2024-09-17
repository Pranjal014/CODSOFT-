import random
import string

def generate_password(length):
    if length < 3:
        print("Password length should be at least 3 to include all types of characters.")
        return ''
    
    # Ensure at least one character from each group
    password = [
        random.choice(string.ascii_letters),  # At least one letter
        random.choice(string.digits),         # At least one digit
        random.choice(string.punctuation)     # At least one special character
    ]
    
    # Fill the remaining characters randomly from the full set
    remaining_length = length - 3
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    
    
    return ''.join(password)

# Get user input for the length of the password
try:
    length = int(input("Enter the desired password length: "))
    
    if length <= 0:
        print("Please enter a valid length greater than 0.")
    else:
        # Generate and display the password
        generated_password = generate_password(length)
        print(f"Generated Password: {generated_password}")
        
except ValueError:
    print("Invalid input! Please enter a number.")

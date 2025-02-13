"""""
Write a Python program that checks the strength of a password. The password is considered strong if it meets the following criteria:

It is at least 8 characters long.     
It contains at least one uppercase letter.
It contains at least one lowercase letter.
It contains at least one digit.
It contains at least one of the following special characters: !, @, #, $, %.

The program should take a password as input and output whether the password is strong or weak.

Example:
Enter a password: Password@123!
The password is strong.

Enter a password: password
The password is weak.

"""

def check_password_strength(password):
    """
    A simple function to check if a password is strong enough.
    Returns True if the password is strong, False if it's weak.
    """
    # Initialize variables to track each requirement
    has_length = len(password) >= 8
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    
    # List of special characters we'll check for
    special_characters = "!@#$%"
    
    # Check each character in the password
    for character in password:
        if character.isupper():
            has_upper = True
        elif character.islower():
            has_lower = True
        elif character.isdigit():
            has_digit = True
        elif character in special_characters:
            has_special = True
    
    # Print helpful messages for the user
    print("\nChecking password strength...")
    print(f"✓ Length at least 8 characters: {has_length}")
    print(f"✓ Contains uppercase letter: {has_upper}")
    print(f"✓ Contains lowercase letter: {has_lower}")
    print(f"✓ Contains number: {has_digit}")
    print(f"✓ Contains special character: {has_special}")
    
    # Password is strong only if all conditions are met
    return has_length and has_upper and has_lower and has_digit and has_special

# Main program
print("Welcome to Password Strength Checker!")
print("Your password should have:")
print("- At least 8 characters")
print("- At least one uppercase letter (A-Z)")
print("- At least one lowercase letter (a-z)")
print("- At least one number (0-9)")
print("- At least one special character (!@#$%)")

# Keep asking for passwords until user enters a strong one
while True:
    password = input("\nEnter your password: ")
    
    if check_password_strength(password):
        print("\n Great! Your password is strong!")
        break
    else:
        print("\n Password is too weak. Please try again!")
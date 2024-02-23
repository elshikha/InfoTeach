import re

def assess_password_strength(password):
    # Check if the password length is at least 8 characters
    password_length = len(password)
    if password_length < 8:
        return "Weak: Password should be at least 8 characters long."

    # Check if the password contains at least one uppercase letter
    has_uppercase = bool(re.search(r'[A-Z]', password))
    
    # Check if the password contains at least one lowercase letter
    has_lowercase = bool(re.search(r'[a-z]', password))
    
    # Check if the password contains at least one digit
    has_digit = bool(re.search(r'\d', password))
    
    # Check if the password contains at least one special character
    has_special_char = bool(re.search(r'[^A-Za-z0-9]', password))

    # Identify missing elements and provide feedback
    missing_elements = []
    if not has_uppercase:
        missing_elements.append("uppercase letters")
    if not has_lowercase:
        missing_elements.append("lowercase letters")
    if not has_digit:
        missing_elements.append("numbers")
    if not has_special_char:
        missing_elements.append("special characters")

    # Return the password strength feedback
    if missing_elements:
        return f"Password should include {', '.join(missing_elements)} to be stronger."
    else:
        return "Excellent: Password is very strong."

# Get user input for the password
user_password = input("Enter your password: ")

# Check password strength and display the result
password_strength_result = assess_password_strength(user_password)
print(password_strength_result)

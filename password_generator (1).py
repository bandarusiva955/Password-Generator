import random
import string

def generate_password(length=12, use_uppercase=True, use_lowercase=True, use_numbers=True, use_special=True):
    """
    Generate a strong random password based on specified criteria.

    Parameters:
    - length (int): Length of the password (default 12)
    - use_uppercase (bool): Include uppercase letters (default True
    - use_lowercase (bool): Include lowercase letters (default True)
    - use_numbers (bool): Include digits (default True)
    - use_special (bool): Include special characters (default True)

    Returns:
    - str: Generated password
    """
    if length < 1:
        raise ValueError("Password length must be at least 1")

    character_sets = []
    if use_uppercase:
        character_sets.append(string.ascii_uppercase)
    if use_lowercase:
        character_sets.append(string.ascii_lowercase)
    if use_numbers:
        character_sets.append(string.digits)
    if use_special:
        character_sets.append(string.punctuation)

    if not character_sets:
        raise ValueError("At least one character type must be selected")

    all_characters = ''.join(character_sets)

    # Ensure the password contains at least one character from each selected set
    password = [random.choice(char_set) for char_set in character_sets]

    # Fill the rest of the password length with random choices from all allowed characters
    password += [random.choice(all_characters) for _ in range(length - len(password))]

    # Shuffle the password list to avoid predictable sequences
    random.shuffle(password)

    return ''.join(password)

if __name__ == "__main__":
    # Example usage
    print("Generated password:", generate_password(length=16, use_uppercase=True, use_lowercase=True, use_numbers=True, use_special=True))

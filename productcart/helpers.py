import secrets
import string

def generate_short_id(length=8):
    """
    Generate a short random ID of fixed length using letters and digits.
    Adjust length as needed.
    """
    characters = string.ascii_letters + string.digits
    return ''.join(secrets.choice(characters) for _ in range(length))

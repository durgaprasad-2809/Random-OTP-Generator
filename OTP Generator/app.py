# Import required modules
import random
import string

def rand_pass(size):
    """Generates a random OTP of given size using uppercase, lowercase, and digits."""
    generate_pass = ''.join([random.choice(string.ascii_uppercase + 
                                           string.ascii_lowercase + 
                                           string.digits) 
                             for _ in range(size)])
    return generate_pass

# Driver Code
password = rand_pass(10)  # Generates a 10-character password
print("Generated OTP:", password)

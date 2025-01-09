''''writing a program to check the strength of a password, this program checks the entropy along with
patterns and returns how strong your password using the help of the "have i been pwned API". This program
 also gives you a brief rundown on how long it will take a brute-force attack to crack your password'''

import re
#this library package supports regular expressions (eg. special characters)
import requests
# this library package its a 'basic get' prompt
import math
import hashlib
# provides a way to work with cryptographic hash functions
from colorama import Fore, Style
#adds colour to the python file to make it more interractive/friendly

# function to calculate entropy (measures uncertainty)
def check_entropy(password):
    char_set = len(set(password))  # count unique characters
    entropy = len(password) * math.log2(char_set)
    # this represents the amount of information per character in bits, calculates with base 2.
    return entropy

# function to check for common patterns and only running values through if its unique (doesnt fit these stereotypes)
def check_common_patterns(password, additional_patterns=None):
    common_patterns = [
        r'1234', r'qwerty', r'password', r'letmein', r'abcdef', r'password123', 'yuiop', 'asdfghjkl', 'zxcvbnm'
    ]
    if additional_patterns:
        common_patterns.extend(additional_patterns)
    for pattern in common_patterns:
        if re.search(pattern, password, re.IGNORECASE):
            return True
        # this loop checks for patterns
    return False

# function to check if the password has been compromised (using Have I Been Pwned API)
def check_pwned(password):
    # this function checks if a given password has been exposed in a data breach by utilizing the Have I Been Pwned API.
    sha1_prefix = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()[:5]
    # sha1_prefix: The first 5 characters of the SHA-1 hash
    sha1_suffix = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()[5:]
    # sha1_suffix: The remaining part of the SHA-1 hash.
    url = f"https://api.pwnedpasswords.com/range/{sha1_prefix}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            hashes = response.text.splitlines()
            for hash in hashes:
                if hash.startswith(sha1_suffix):
                    return True
    except requests.RequestException as e:
        #just incase the API is down
        print(f"{Fore.RED}[ERROR]{Style.RESET_ALL} Unable to connect to the Have I Been Pwned API: {e}")
    return False

# function to provide suggestions for improving weak passwords
def suggest_improvements(password):
    suggestions = []
    if len(password) < 12:
        suggestions.append("Increase password length to at least 12 characters.")
    if not any(char.isupper() for char in password):
        suggestions.append("Add at least one uppercase letter.")
    if not any(char.isdigit() for char in password):
        suggestions.append("Add at least one digit.")
    if not any(char in "!@#$%^&*()_+" for char in password):
        suggestions.append("Add at least one special character.")
    if check_common_patterns(password):
        suggestions.append("Avoid using common patterns like 'password', '1234', etc.")
    return suggestions

# function to estimate brute-force time
def estimate_bruteforce_time(entropy):
    attempts = 2 ** entropy
    time_per_attempt = 1e-6  # Assume 1 microsecond per attempt
    total_seconds = attempts * time_per_attempt
    return total_seconds


# function to evaluate password
def evaluate_password(password):
    print(f"\n{Fore.BLUE}=== Password Evaluation ==={Style.RESET_ALL}")

    # step 1: Check entropy
    entropy = check_entropy(password)
    print(f"{Fore.YELLOW}Entropy: {entropy:.2f} bits{Style.RESET_ALL}")

    # step 2: Check for common patterns
    has_common_pattern = check_common_patterns(password)
    if has_common_pattern:
        print(f"{Fore.RED}Warning: Contains common patterns.{Style.RESET_ALL}")

    # step 3: Check if password is compromised
    is_pwned = check_pwned(password)
    if is_pwned:
        print(f"{Fore.RED}Alert: Password found in data breaches!{Style.RESET_ALL}")

    # step 4: Evaluate overall strength
    if len(password) < 8 or entropy < 40 or has_common_pattern or is_pwned:
        print(f"{Fore.RED}Weak password. Suggestions to improve:{Style.RESET_ALL}")
        improvements = suggest_improvements(password)
        for improvement in improvements:
            print(f"  - {improvement}")
    else:
        print(f"{Fore.GREEN}Strong password!{Style.RESET_ALL}")

    # step 5: Brute-force estimation
    time = estimate_bruteforce_time(entropy)
    if time < 60:
        print(f"{Fore.RED}Estimated brute-force time: {time:.2f} seconds{Style.RESET_ALL}")
    elif time < 3600:
        print(f"{Fore.YELLOW}Estimated brute-force time: {time / 60:.2f} minutes{Style.RESET_ALL}")
    else:
        print(f"{Fore.GREEN}Estimated brute-force time: {time / 3600:.2f} hours or more{Style.RESET_ALL}")

# this is the initial prompt, enter your password and let the magic begin
if __name__ == "__main__":
    password = input("Enter a password to check: ")
    evaluate_password(password)

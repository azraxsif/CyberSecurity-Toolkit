# Password Strength Checker (Colourful Output)  ![Python](https://img.shields.io/badge/Python-3.9%2B-blue) [![License](https://img.shields.io/badge/License-MIT-green)](./LICENSE)

## *Overview*
---
I came up with the concept for this tool when playing around with Python's 'colorama' module, which allows me to make my outputs seem colourful in my IDE without the usage
of a front-end language. This Python program determines the strength of a password by calculating its entropy, looking for common patterns,
and utilising the Have I Been Pwned API to see if the password has been compromised in known data breaches. Additionally, the application estimates how long it 
would take a brute-force attack to crack the password. Which, honestly, is one of the coolest things I've ever coded. 

---
## *Reasons why my project stands out*

| Feature                      | Description                                                                                             |
|------------------------------|---------------------------------------------------------------------------------------------------------|
| Entropy Calculation          | Measures the amount of uncertainty or randomness in the password, giving an indication of its strength. |
| Pattern Detection            | Checks for common, easily guessable password patterns                                                   |
| Compromised Password Check   | Uses the Have I Been Pwned API to determine if the password has been exposed in a data breach.          |
| Brute-Force Attack Estimation| Estimate of how long it would take for a brute-force attack to crack the password, based on its entropy |
| Password Improvement         | Offers recommendations to strengthen weak passwords.                                                    |

---

## *Python Libraries added*
---
- requests: For making HTTP requests to the Have I Been Pwned API.
- colorama: For adding colour to the console output to make the program more interactive.
- math: For mathematical operations to calculate entropy.
- hashlib: For working with cryptographic hash functions.

You can install the required packages by running this command on your terminal:

```bash
pip install requests colorama 
```
---
## *How It Works*

1. Calculation of Entropy
- The following formula is used to determine the password's entropy:

```mathematica
Entropy = Length of password * log2(Number of unique characters)
```
This provides an estimate of the difficulty of utilising brute-force techniques to guess the password.

2. Identification of Patterns
- The application looks for popular weak password patterns, such as "1234", "qwerty," and "password." The password is marked as weak if any of these patterns are discovered.

3. Insecure Password Verification
- The application determines whether the password has been used in any known data breaches by using the Have I Been Pwned API. A warning is shown if the password has been compromised.

4. Brute-Force Attack Estimation
- The program estimates the time it would take to crack the password using a brute-force attack, based on its entropy. The time is displayed in seconds, minutes, or hours.

5. Suggestions for Improvement
- If the password is deemed weak, the program will suggest ways to improve it, such as increasing length, adding uppercase letters, or including special characters.

---

## *Installation*
1. Clone the repository:
```bash
git clone https://github.com/azraxsif/cybersecurity-toolkit.git
cd password_strength_checker
```
2. Make sure Python 3.6+ is installed.
3. Install the colorama library using:
   ``` bash
   pip install colorama
   ```
4. Run the script:

```bash
python password_strength_checker.py
```
5. Follow the prompts.

6. Let the magic happen!


   ---
   

# Example of the Output: 
``` bash

$ python password_checker.py
Enter a password to check: password123
=== Password Evaluation ===
Entropy: 38.61 bits
Warning: Contains common patterns.
Alert: Password found in data breaches!
Weak password. Suggestions to improve:
  - Increase password length to at least 12 characters.
  - Add at least one uppercase letter.
  - Add at least one digit.
Estimated brute-force time: 13.23 seconds
```

---
# Usage
- Clone the repository or download the script.
- Run the script and enter the password you want to check.
- Review the results, including the entropy, common patterns, compromise status, strength evaluation, and brute-force attack estimation.

---
# License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## Contact
For questions, feedback, or contributions:
# [![GitHub](https://img.shields.io/badge/GitHub-azraxsif-pink)](https://github.com/azraxsif)
# [asifazra03@gmail.com](mailto:asifazra03@gmail.com) 


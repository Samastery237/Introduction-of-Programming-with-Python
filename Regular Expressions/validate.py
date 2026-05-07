# Example

email = input("What's your email? ").strip()

username, domain = email.split("@")

if username and domain.endswith(".edu.my"):
    print("Valid")
else:
    print("Invalid")


# Using RE

import re

email = input("What's your email? ").strip()

if re.search(r"^[^\s@]+@[^\s@]+\.(com|edu\.my|org|net)$", email):
    print("Valid")
else:
    print("Invalid")

# Second Version (Using re)

import re

email = input("What's your email? ").strip()

if re.search(r"^\w+@(\w+\.)+edu(\.my)?$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")
import re

locations = {"+1": "United States and Canada", "+60": "Malaysia", "+505": "Nicaragua"}

def main():
    pattern = r"^(?P<country_code>\+\d{1,3})\s?\d{3}-\d{3}-\d{4}"
    number = input("Number: ")

    match = re.search(pattern,number)
    if match:
        country_code = match.group(1)
        print(locations[country_code])
        print("Valid")
    else:
        print("Invalid")

main()
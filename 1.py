import re

mobile_numbers = ["2124567890", "212-456-7890", "(212)456-7890", "(212)-456-7890", "212.456.7890", "212 456 7890", "+12124567890", "+12124567890", "+1 212.456.7890", "+212-456-7890", "1-212-456-7890"]
pattern = re.compile(r'^[+(\s.\-/\d)]{5,30}$')

for mobile_number in mobile_numbers:
    if pattern.match(mobile_number):
        print(f"{mobile_number} is valid")
    else:
        print(f"{mobile_number} is invalid")
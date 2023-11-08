
str = "Guvi Geeks Network Private Limited"

# Convert the string to upper case
str_upper = str.upper()

# Define vowels
vowels = 'AEIOU'

# Initialize counts
total_vowels = 0
A_count = 0
E_count = 0
I_count = 0
O_count = 0
U_count = 0

# Count the vowels
for char in str_upper:
    if char in vowels:
        total_vowels += 1
        if char == 'A':
            A_count += 1
        elif char == 'E':
            E_count += 1
        elif char == 'I':
            I_count += 1
        elif char == 'O':
            O_count += 1
        elif char == 'U':
            U_count += 1

print("Total number of vowels:", total_vowels)
print("Count of A:", A_count)
print("Count of E:", E_count)
print("Count of I:", I_count)
print("Count of O:", O_count)
print("Count of U:", U_count)

def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

def count_consonants(s):
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    count = 0
    for char in s:
        if char in consonants:
            count += 1
    return count

def calculate_ratio(vowel_count, consonant_count):
    if consonant_count == 0:
        return "Undefined (no consonants)"
    return vowel_count / consonant_count

# User input and output
user_string = input("Enter a string: ")
v_count = count_vowels(user_string)
c_count = count_consonants(user_string)
ratio = calculate_ratio(v_count, c_count)

print(f"Number of vowels: {v_count}")
print(f"Number of consonants: {c_count}")
print(f"Ratio of vowels to consonants: {ratio}")
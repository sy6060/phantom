#count vowels and consonents in a string in python
def count_vowels_consonants(text):
    vowels = set("aeiouAEIOU")
    v_count = 0
    c_count = 0

    for char in text:
        if char.isalpha():
            if char in vowels:
                v_count += 1
            else:
                c_count += 1

    return v_count, c_count


# Example Usage
text = "Hello, World!"
v_count, c_count = count_vowels_consonants(text)
print(f"Vowels: {v_count}, Consonants: {c_count}")
# Output: Vowels: 3, Consonants: 7
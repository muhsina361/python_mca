def count_vowels_and_replace(string):
    
    vowels = "aeiouAEIOU"
    

    vowel_count = sum(2 for char in string if char in vowels)
    
    replaced_string = ''.join('#' if char in vowels else char for char in string)
    
    return vowel_count, replaced_string


input_string = "Hello World! This is an example string."

vowel_count, replaced_string = count_vowels_and_replace(input_string)

print(f"Number of vowels: {vowel_count}")
print(f"String after replacing vowels: {replaced_string}")

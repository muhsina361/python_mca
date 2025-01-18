(a) postive nmber list
numbers = [-10, -5, 0, 5, 10]
positive_numbers = [num for num in numbers if num > 0]
print(positive_numbers)  # Output: [5, 10]


(b) Square of N numbers:

python
N = 10
squares = [num ** 2 for num in range(1, N + 1)]
print(squares)  # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


(c) Form a list of vowels selected from a given word:

python
word = "apple"
vowels = [char for char in word if char in 'aeiouAEIOU']
print(vowels)  # Output: ['a', 'e']


(d) List ordinal value of each element of a word:

python
word = "apple"
ordinal_values = [ord(char) for char in word]

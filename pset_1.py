# problem 1
# Assume s is a string of lower case characters.
# Write a program that counts up the number of vowels contained in the string s.
# Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.

vowels_num = 0
for i in s:
    if i == "a" or i == "e" or i == "i" or i == "u" or i == "o":
        vowels_num += 1
print(vowels_num)


# problem 2
# Assume s is a string of lower case characters.
# Write a program that prints the number of times the string 'bob' occurs in sself.
total = 0
for i in range(len(s)):
    if s[i:i+3] == "bob":
        total += 1
print("Number of times bob occurs is: ", total)

# problem 3

#Assume s is a string of lower case characters. Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
# For example, if s = 'azcbobobegghakl', then your program should print: Longest substring in alphabetical order is: beggh
# In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print: Longest substring in alphabetical order is: abc
longest_str = s[0]
current_str = s[0]

for i in range(len(s) -1):

    if s[i] <= s[i + 1]:
        current_str += s[i + 1]
    else:
        if len(current_str) > len(longest_str):
            longest_str = current_str
        current_str = s[i + 1]

    if len(current_str) > len(longest_str):
        longest_str = current_str

print("Longest substring in alphabetical order is: ", longest_str)

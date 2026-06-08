'''Python:
1. Write a program to store length of each word using list comprehension.
Input: ["hi", "hello", "python"]
Output: [2, 5, 6]'''

x = ['hi','hello','python']
res = [len(word) for word in x]
# print(res)

'''2. Write a program to remove vowels from a string using list comprehension.
Input: "education"
Output: ['d', 'c', 't', 'n']
'''

x = "education"
res = [char for char in x if char not in {'a','e','i','o','u'}]
print(res)
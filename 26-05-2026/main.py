
'''1.Write a Python program to group elements in a list by their length using a dictionary.
      Input: ['a', 'to', 'cat', 'dog']
      Output: {1: ['a'], 2: ['to'], 3: ['cat', 'dog']}'''

x = ['a', 'to', 'cat', 'dog','b']
out = {}
for ele in x:
    if len(ele) not in out:
        out[len(ele)]=[ele]
    else:   
        out[len(ele)].append(ele)
print(out)

'''2.Write a Python program to calculate the frequency of words in a text string using a dictionary.
      Input: "apple banana apple orange banana banana"
      Output: {'apple': 2, 'banana': 3, 'orange': 1}'''

x = "apple banana apple orange banana banana"
out = {}
for ele in x.split(' '):
    if ele not in out:
        out[ele] = x.count(ele)
print(out)
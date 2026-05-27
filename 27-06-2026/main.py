'''1.Write a Python function top_n_frequent(words: List[str], n: int) -> List[str] that returns the n most frequent words
 in the list 'words', sorted by decreasing frequency and alphabetically for ties. 
For example, top_n_frequent(['i','love','python','i','love','code'], 2) should return ['i','love'].'''

#top nfrequent
def top_n_frequent(x,n):
    output = []
    set_a = set(x)
    for word in set_a:
        count = x.count(word)
        if(count==n):
            output.append(word)
    return output


x = ['i','love','python','i','love','code','love']
n=3
res = top_n_frequent(x,n)
print(res)

'''2.Given a list of dictionaries representing users, e.g. [{'id':1,'team':'backend'},{'id':2,'team':'frontend'},…], write a function group_by(records: List[Dict], key: str) -> Dict[Any, List[Dict]] that groups records by the specified key.

Input
records = [
    {'id': 1, 'team': 'backend'},
    {'id': 2, 'team': 'frontend'},
    {'id': 3, 'team': 'backend'},
    {'id': 4, 'team': 'testing'}
]
key = 'team'

Output
{
    'backend': [
        {'id': 1, 'team': 'backend'},
        {'id': 3, 'team': 'backend'}
    ],
    
    'frontend': [
        {'id': 2, 'team': 'frontend'}
    ],
    
    'testing': [
        {'id': 4, 'team': 'testing'}
    ]
}'''

records = [
    {'id': 1, 'team': 'backend'},
    {'id': 2, 'team': 'frontend'},
    {'id': 3, 'team': 'backend'},
    {'id': 4, 'team': 'testing'}
]

res = {}
for record in records:
    team = record['team']
    if team in res:
        res[team].append(record)
    else:
        res[team] = [record]
print(res)
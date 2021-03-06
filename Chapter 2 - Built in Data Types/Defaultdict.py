d = {}
print d

d['age'] = d.get('age', 0) + 1          # age not there, we get 0 + 1
print d

d = {'age': 39}
d['age'] = d.get('age', 0) + 1          # d is there we get 40
print d

from collections import defaultdict
dd = defaultdict(int)                   # int is the default type (0 the value)
dd['age'] += 1                          # short for dd['age'] = dd['age'] + 1
print dd

dd['age'] = 39
dd['age'] += 1
print dd

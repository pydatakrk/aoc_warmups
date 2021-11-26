#!/usr/bin/env jupyter
data = open("inp.txt", "r").read().splitlines()
from collections import defaultdict

dd = defaultdict(list)

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


data = data[0]
for i, chnk in enumerate(chunks(data, 25)):
    dd[i//6].append(chnk)

print(dd)
from collections import Counter
d2 = {}
for k,v in dd.items():
    su = 0
    for chnk in v:
        # print( Counter(chnk)['0'])
        su += Counter(chnk)['0']
    d2[k] = su

mx = min(d2.values())

layer = ""
for k,v in d2.items():
    if v == mx:
        layer = k

print(dd[layer])

su2 = 0
su3 = 0
for chnk in dd[layer]:
    su2 += Counter(chnk)['1']
    su3 +=  Counter(chnk)['2']
print(su2, su3, su2*su3)

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

import numpy as np

d = np.zeros((6,25))

layers = []
for k,v in dd.items():
    arr = []
    for chnk in v:
        arr.append(list(map(int, chnk)))
    layers.append(arr)

d3 = np.array(layers)

fin = np.zeros((6,25),dtype=int)
print(d3.shape)
for i in range(25):
    for j in range(6):
        for z in d3[:, j,i]:
            # print(z)
            if z in [0,1]:
                fin[j,i] = z
                break
ls = []
for j in range(6):
    ls.append("".join(map(str, fin[j,:]))+"\n")
print("".join(ls))

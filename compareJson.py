

import json

indexpath = "spleen_1chr1rep.index.json"
indexpath2 = "spleen_1chr1rep.indexed.index.json"

with open(indexpath) as index_file:
    index = json.loads(index_file.read())

with open(indexpath2) as index_file:
    index2 = json.loads(index_file.read())

keys1 = index.keys()
keys2 = index2.keys()
print(keys1)
print(len(keys2))

for key in keys1:
    if key != '':
        value1 = index[key]
        value2 = index2[key]
        eq = value1 == value2
        print(eq)

keys1 = index['/replica10_chr1/spatial_position'].keys()
keys2 = index2['/replica10_chr1/spatial_position'].keys()

print(len(keys1))
print(len(keys2))

for key in keys1:
    if key != '':
        value1 = index['/replica10_chr1/spatial_position'][key]
        value2 = index2['/replica10_chr1/spatial_position'][key]
        eq = value1 == value2
        print(eq)
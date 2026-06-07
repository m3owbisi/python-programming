names = ['alice', ('bob',), 'charlie', ('david',), ('john',)]
boys = 0
girls = 0
for name in names:
    if isinstance(name, tuple):
        boys += 1
    else:
        girls += 1
print(f"number of boys : {boys}")
print(f"number of girls : {girls}")
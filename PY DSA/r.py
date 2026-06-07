import operator
d = {'oil' : 230, 'clip' : 150, 'stud' : 175, 'nut' : 35}
print(f"original dictionary : {d}")
d1 = sorted(d.items())
print(f"asc order by key : {d1}")
d2 = sorted(d.items(), reverse = True)
print(f"des order by key : {d2}")
d1 = sorted(d.items(), key = operator.itemgetter(1))
print(f"asc order by value : {d1}")
d2 = sorted(d.items(), key = operator.itemgetter(1), reverse = True)
print(f"des order by value : {d2}")
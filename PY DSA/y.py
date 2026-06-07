def count_alphabets_digits(s):
    d = {'digits' : 0, 'alphabets' : 0}
    for ch in s:
        if ch.isalpha():
            d['alphabets'] += 1
        elif ch.isdigit():
            d['digits'] += 1
        else:
            pass
    return(d)
d = count_alphabets_digits('james bond 007')
print(d)
d = count_alphabets_digits('kholi number 420')
print(d)
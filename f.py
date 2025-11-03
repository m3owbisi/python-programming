odd = [1, 3, 5, 7, 9]
print(odd)
even = [0, 2, 4, 6, 8]
print(even)
combined_list = even + odd
print(combined_list)
prime = [11, 17, 29] + combined_list
print(prime)
print(len(prime))
prime[-3:] = [100, 200, 300]
print(prime)
del(prime[:])
print(prime)
del(prime)
print(prime)
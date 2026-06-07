def convert(s):
    words = [word for word in s.split(' ')]
    return ' '.join(sorted(list(set(words))))
s = "i felt happy because i saw the others were happy and because i knew i should feel happy, but i wasn\'t really happy"
t = convert(s)
print(t)
s = "sakhi was a singer because her mother was a singer, and sakhi\'s mother was a singer because her father was a singer"
t = convert(s)
print(t)
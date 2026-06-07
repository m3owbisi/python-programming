with open('example.txt', 'r') as file:
    content = file.read()
    words = content.split()
    word_count = len(words)
    print(f"the file contains {word_count} words")
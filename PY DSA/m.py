with open('source.txt', 'r') as src_file:
    with open('destination.txt', 'w') as dest_file:
        content = src_file.read()
        dest_file.write(content)
print(f"content has been copied from source.txt to destination.txt")
# file i/o in python
# types of all files
# 1. text files: .txt, .docx, .log, etc.
# 2. binary files: .exe, .pdf, .mp3, .mp4, .mov, .png, .jpeg, etc.
# 3. compressed files: .zip, .rar, .7z, etc.
# 4. database files: .csv, .xls, .xlsx, .json, .db, .sql, .mdb, .accdb, .mdb, .sqlite, etc.
# 5. image files: .jpg, .png, .gif, .bmp, .ico, etc.
# 6. video files: .mp4, .avi, .flv, .wmv, .mov, .mkv, etc.
# 7. audio files: .mp3, .wav, .ogg, .wma, .flac, etc.
# 8. executable files: .exe, .apk, .app, etc.
# 9. application files: .exe, .apk, .app, etc.
# 10. source code files: .py, .c, .cpp, .java, .js, .html, .css, .php, .cs, .vb, .r, .go, .swift, etc.
# 11. virtual files: .vsd, .vsdx, .vss, .vst, .vsw, .vdx, .vsdm, .vsdx, .vssx, .vstx, .vstm, .vssx, .vstx, .vstm, etc.
# 12. other files: .doc, .ppt, .xls, .pdf, .ai, .psd, .eps, .ps, .dxf, .dwg, .ai, .indd, .eps, .ps, .dxf, .dwg, etc.
# open, read & close file
# f=open("file_name","mode")
# sample.txt    demo.docx
# r : read mode w : write mode
# data = f.read()
# f.close()

# f=open("demo.txt","r")
# data=f.read()
# print(data)
# print(type(data))
# f.close()

# 'r' (default), 'w', 'x', 'a', 'b', 't' (default), '+' (reading and writing)
# reading a file
# data=f.read()   # reads entire file
# data=f.readline()   # reads one line at a time

# f=open("demo.txt","r")
# data=f.read(5)
# print(data)
# f.close()

# f=open("demo.txt","r")
# line1=f.readline()
# print(line1)
# line2=f.readline()
# print(line2)
# line3=f.readline()
# print(line3)
# f.close()
# print("\n")

# f=open("demo.txt","r")
# data=f.read()
# print(data)
# line1=f.readline()
# print(line1)
# line2=f.readline()
# print(line2)
# f.close()

# writing to a file
# f=open("demo.txt","w")
# f.write("this is a new line")   # overwrites the entire file
# f=open("demo.txt","a")
# f.write("this is a new line")   # adds to the file

# f=open("demo.txt","a")
# f.write("\ni want to learn python\n")
# f.write("\nthen i will move to reactjs and after that nodejs\n")
# f.close()

# f=open("demo.txt","w+")
# print(f.read())
# f.write("a")
# f.close()

# f=open("demo.txt","a+")
# print(f.read())
# f.write("a")
# f.close()

# f=open("sample.txt","x")    
# # 'w' & 'a'
# f.close()

# f=open("sample.txt","r+")
# f.write("i wanna be a full stack developer\n")
# print(f.read())
# f.close()

# with syntax
# with open("demo.txt","a") as f:
#           data = f.read()

# with open("sample.txt","r") as f:
#     data = f.read()
#     print(data)

# with open("sample.txt","a") as f:
#     f.write("new data")

# deleting a file
# import os
# os.remove(filename)
# pip install tensorflow
# pip3 install tensorflow

# import os
# # import tensorflow
# os.remove("demo.txt")
# os.remove("sample.txt")

# lets practice
"""
Create a new file "practice.txt" using python.
Add the following data in it.
Hi everyone
we are learning File I/O
using Java.
I like programming in Java.
"""
# with open("practice.txt","x") as f:
#     f.write("Hi everyone\n")
#     f.write("we are learning File I/O\n")
#     f.write("using Java.\n")
#     f.write("I like programming in Java.\n")
"""
WAF that replaces all occurrences of "Java" with "Python" in above file.
"""
with open("practice.txt","r") as f:
    data=f.read()
    new_data=data.replace("Java","Python")
    print(new_data)
with open("practice.txt","w") as f:
    f.write(new_data)
"""
Search if the word "learning" exists in the file or not.
"""
def checkForWord():
    with open("practice.txt","r") as f:
        data=f.read()
        word="learning"
        if(data.find(word)!=-1):    # word in data
            print("found")
        else:
            print("not found")
# with open("practice.txt","r") as f:
#     data=f.read()
#     word="learning"
#     if(data.find(word)!=-1):
#         print("found")
#     else:
#         print("not found")
checkForWord()

"""
WAF to find in which line of the file does the word "learning" occur first.
Print -1 if word not found.
"""
def checkForLine():
    with open("practice.txt","r") as f:
        word="learning"
        data=True
        line_no=1
        while data:
            data=f.readline()
            if(word in data):
                print(line_no)
                break
                return
            line_no+=1
    return -1
checkForLine()
print(checkForLine())
"""
From a file containing numbers separated by comma, print the count of even numbers.
"""
with open("practice.txt","r") as f:
    data=f.read()
    print(data) # parse or cast to int
    # num=" "
    # for i in range(len(data)):
    #     if(data[i]==','):
    #         print(int(num))
    #         num=""
    #     else:
    #         num+=data[i]
    nums=data.split(",")
    print(nums)
    count=0
    for val in nums:
        if(int(val)%2==0):
            count+=1
    print(count)
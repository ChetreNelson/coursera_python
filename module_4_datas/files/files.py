# fielpath = './module_4_datas/dummy1.txt'

# with open(fielpath,'r') as file:
#     print(file.read())

# fielpath = './module_4_datas/dummy2.txt'
# content = 'This is the new file.'
# with open(fielpath,'w') as file:
#     file.write(content)

# fielpath = './module_4_datas/dummy2.txt'
# content = 'This is apending in the existing file.'
# with open(fielpath,'a') as file:
#     file.write(content)

readpath = './module_4_datas/dummy2.txt'
writepath = './module_4_datas/copied.txt'
with open(readpath,'r') as readfile:
    with open(writepath,'w') as writefile:
        content = readfile.read()
        writefile.write(content)
     
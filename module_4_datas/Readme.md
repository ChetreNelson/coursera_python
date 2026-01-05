##Reading the file 
---
we will be using **open** function to read the file
`file = open('dummy1.txt','r')` *this will open file with read mode*

###Using with statement
---
we no need to explicitly define the close function to close the file while using open and with together
```with open('dummy1.txt','r') as file:
        file_stuff = file.read() *read function is used to read the whole file content*
        file_stuff_inline = file.readLine() *read file content line by line, it will print first line of the file*
        char = file.read(5) *read next five line from the current pointer in the file*
    

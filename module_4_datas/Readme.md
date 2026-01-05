# Files

## Reading the file
---
we will be using **open** function to read the file
`file = open('dummy1.txt','r')` *this will open file with read mode*
<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/images/ReadOpen.png" width="500">

### Using with statement
---
we no need to explicitly define the close function to close the file while using open and with together
```with open('dummy1.txt','r') as file:
        file_stuff = file.read()  # read function is used to read the whole file content
        file_stuff_inline = file.readLine() # read file content line by line, it will print first line of the file
        char = file.read(5) # read next five line from the current pointer in the file
```
<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/images/ReadWith.png" width="500">

---    
## Writing on a file

we can use to type of method on writing on a file
1. *** w *** *this will create new file or clear the content and re-write onto the file*
2. *** a *** *this will write into the existing file without removing the existing content* 

1. ### using *w* method
   ```
   exmp2 = '/Example2.txt'
   with open(exmp2, 'w') as writefile:
      writefile.write("This is line A")
   ```

2. ### using *a* method
   ```
   with open('/Example2.txt', 'a') as testwritefile:
      testwritefile.write("This is line C\n")
   ```
---   
## Copy a file

```
# Copy file to another

with open('/Example2.txt','r') as readfile:
    with open('/Example3.txt','w') as writefile:
          for line in readfile:
                writefile.write(line)
```                
---
## Additional modes

| Mode | Read | Write | Old data  | File exists? |
| ---- | ---- | ----- | --------- | ------------ |
| `r+` | ✔    | ✔     | Kept      | Must exist   |
| `w+` | ✔    | ✔     | ❌ Deleted | Optional     |
| `a+` | ✔    | ✔     | ✔ Kept    | Optional     |


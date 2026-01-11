from bs4 import BeautifulSoup
import requests

# %%html
# <!DOCTYPE html>
# <html>
# <head>
# <title>Page Title</title>
# </head>
# <body>
# <h3><b id='boldest'>Lebron James</b></h3>
# <p> Salary: $ 92,000,000 </p>
# <h3> Stephen Curry</h3>
# <p> Salary: $85,000, 000 </p>
# <h3> Kevin Durant </h3>
# <p> Salary: $73,200, 000</p>
# </body>
# </html>
# example html 
html = "<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body></html>"

# creating BeautifulSoup object
soup = BeautifulSoup(html,'html.parser')
# We can use the method prettify() to display the HTML in the nested structure:
# print(soup.prettify())
#-----------------------------------------------------------------------------------#
# aceesing tags

# title = soup.title
# print(title) <title>Page Title</title>

# h3 = soup.h3 # first identified tags are displayed here so <h3><b id="boldest">Lebron James</b></h3>
# print(h3)


#------------------------------------------------------------------------------------#
# Children, Parent and Siblings
#------------------------------------------------------------------------------------#

# <h3><b id="boldest">Lebron James</b></h3>

# b = soup.h3.b
# print(b). #<b id="boldest">Lebron James</b>

# h3 = b.parent
# print(h3) # <h3><b id="boldest">Lebron James</b></h3>

# <body>
# <h3><b id="boldest">Lebron James</b></h3>
# <p> Salary: $ 92,000,000 </p>
# <h3> Stephen Curry</h3>
# <p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3>
# <p> Salary: $73,200, 000</p>
# </body>

# h3 = soup.h3 # <h3><b id="boldest">Lebron James</b></h3>  
# sibling1 = h3.next_sibling
# print(sibling1).  # <p> Salary: $ 92,000,000 </p>



#-----------------------------------------------------------------#
# accessing using attribute

b = soup.b # <b id="boldest">Lebron James</b>
# print(b['id'])  # boldest

# print(b.attrs) # {'id': 'boldest'}

#----------------------------------------------------------------#
# navigable string
# string corresponding to the tag
h3 = soup.h3
print(h3.string)  # Lebron James

#------------------------------filters---------------------------#
print(soup.find_all('h3')) # [<h3><b id="boldest">Lebron James</b></h3>, <h3> Stephen Curry</h3>, <h3> Kevin Durant </h3>]
print(soup.find('h3')).  # <h3><b id="boldest">Lebron James</b></h3>   printed first h3




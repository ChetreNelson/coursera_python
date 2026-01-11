from PIL import Image
import requests

# url = "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/dog-puppy-on-garden-royalty-free-image-1586966191.jpg"
# data = requests.get(url)

# with open('dummyimage.png','wb') as f:
#     f.write(data.content)
img = Image.open('./dummyimage.png','r')
img.show().  # shwoing the image
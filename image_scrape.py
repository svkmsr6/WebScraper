import requests
#import bs4
#import re

def grab_content(id=0):
	img_link = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/d/d1/John_Houlding.jpg/170px-John_Houlding.jpg')

	img_content = img_link.content

	f = open('my_image_{}.jpg'.format(id),'wb')
	f.write(img_content)
	f.close()
	print('Task Completed!!')

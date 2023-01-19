
# POST 	Создает новый ресурс. 	requests.post()
# GET 	Считывает имеющийся ресурс. 	requests.get()
# PUT 	Обновляет существующий ресурс. 	requests.put()
# DELETE 	Удаляет ресурс. 	requests.delete()
#####################################################################################

# import requests
#
# response = requests.get('https://google.com')
# print(f"{response.status_code=}")
#
# import requests#
# response = requests.request(url='https://google.com', method="GET")
#
# print(f"{response.content=}")

####################################################################################
# GET

# import requests
#
# url = 'https://google.com'
#
# response = requests.get(url)
#
# print(response)
# print(response.status_code)
# print(response.text)
# print(response.url)
# print(response.headers['Content-Type'])
# print(response.content)

#################################################################################
#POST
#
# import requests
# import json
#
# url = 'https://jsonplaceholder.typicode.com/posts'
#
# data = { 'title': 'buy new mouse','body': 'I need a new mouse !','userId': 5,}
# headers = {'content-type': 'application/json; charset=UTF-8'}
#
# response = requests.post(url, data=json.dumps(data), headers=headers)
#
# print(response.status_code)
# print(response.ok)
# print(response.content)
# print(response.text)
# print(type(response.text))
# print(response.url)
# print(response.headers['Content-Type'])
# print(response.encoding)

####################################################################################

#PUT
# import requests
# import json
#
# url = 'https://jsonplaceholder.typicode.com/posts/1'
# data = {'id':1, 'userId':2, 'title':'drink water', 'body':'drinking water is important'}
# headers = {'Content-Type':'application/json; charset=UTF-8'}
# response = requests.put(url, data=json.dumps(data), headers=headers)
#
# print(response.status_code)
# print(response.ok)
# print(response.content)
# print(response.text)
# print(type(response.text))
# print(response.url)
# print(response.headers['Content-Type'])
# print(response.encoding)

#########################################################################################

#DELETE
# import requests
# import json
#
# url = 'https://jsonplaceholder.typicode.com/posts/1'
#
# headers = {'Content-Type': 'application/json; charset=UTF-8'}
#
# response = requests.delete(url, headers=headers)
# print(response.status_code)
# print(response.ok)
# print(type(response.text))
# print(response.url)
# print(response.headers['Content-Type'])
# print(response.encoding)
###############################################################################
# import requests
# image = requests.get('https://pngimg.com/uploads/smiley/smiley_PNG27.png')
# with open('new_image.png', 'wb') as f:
#  f.write(image.content)


# f = open("LICENSE", "r") # read
f = open("C:\Code\Projects\My_basic_python\новый 1.txt", "r")
print(f)
print(f.read)
print(f.readline)
print(f.close)

f1 = open("C:\Code\Projects\My_basic_python\новый 1.txt", "w") #  f1.write
text = f1.write("what that , as i understood all in order")
print(f1.close)

# import os
# list_dir = os.listdir()
# List_d1 = os.getcwd()
# print(f"{list_dir=}")
# print(f"{List_d1=}")
#
# import sys
# print(dir(sys))
# print(sys.getdefaultencoding())
# print(sys.version)
# print(sys.path)
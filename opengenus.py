import requests
print("Enter url of project")
url=input()
#print(url)
x=url.split("https://github.com/")[1]
info="https://api.github.com/repos/%s"%x
print(info)
r=requests.get(info).json()
print(r)


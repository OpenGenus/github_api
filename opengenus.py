import requests
import json
print("Enter url of project")
url=input()
#print(url)
x=url.split("https://github.com/")[1]
info="https://api.github.com/repos/%s"%x
#print(info)
r=requests.get(info).json()
#print((r))
with open("data.json","w") as output:
    json.dump(r,output)
with open("data.json","r") as output2:
    data=json.load(output2)
print(data)    
print("forks_count: ",data["source"]["forks_count"])
print("forks: ",data["source"]["forks"]) 

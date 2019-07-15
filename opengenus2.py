import requests
import json
print("Enter url of user")
url=input()
#print(url)
x=url.split("https://github.com/")[1]
print(x)
info="https://api.github.com/users/%s/repos?client_id=3e1b331062fb84d354a1&client_secret=3fc60c537530938bcae819e91fd97c59f246cbd7"%x
#print(info)
r=requests.get(info).json()
#print((r))
with open("data.json","w") as output:
    json.dump(r,output)
with open("data.json","r") as output2:
    data=json.load(output2)
final_forks=[]
final_name=[]
for i in range(0,len(data)):
    forks=data[i]["forks"]
    name=data[i]["name"]
    final_forks.append(forks)
    final_name.append(name)
    zipped=list(zip(final_name,final_forks))
#print(zipped)
    
for j in range(0,10):
    if j<=len(zipped)-1:
        print(zipped[j])
    else:
        break

#print(final_forks)
#print(final_name)
#print(list(zipped))
#print("forks_count: ",data["forks_count"])


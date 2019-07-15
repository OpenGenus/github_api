import requests
import json
print("Enter url of user")
url=input()
x=url.split("https://github.com/")[1]
print(x)
info="https://api.github.com/users/%s/repos?client_id=3e1b331062fb84d354a1&client_secret=3fc60c537530938bcae819e91fd97c59f246cbd7"%x
r=requests.get(info).json()
with open("data.json","w") as output:
    json.dump(r,output)
with open("data.json","r") as output2:
    data=json.load(output2)
 
def writeToJSONFile(path,fileName,data13):
    filePathNameWExt='./'+path+'/'+fileName+'.json'
    with open(filePathNameWExt,'w') as fp:
        json.dump(data13,fp)

data12=[]      
for i in range(0,len(data)):
    data1={}
    data1['name']=data[i]["name"]
    data1['forks']=data[i]["forks"]
    data1['stars']=data[i]["stargazers_url"]
    data1['contributors']=data[i]["contributors_url"]
    data12.append(data1)
data13={}
data13["data"]=data12
path='./'
fileName='data2'

writeToJSONFile(path,fileName,data13)

final_forks=[]
final_name=[]
res=data13["data"]
for i in range(0,len(res)):
    forks=res[i]["forks"]
    name=res[i]["name"]
    final_forks.append(forks)
    final_name.append(name)
zipped=list(zip(final_forks,final_name))
zipped.sort(reverse=True)
#print(zipped)
for j in range(0,11):
    if j<=len(zipped)-1:
        print(zipped[j])
    else:
        break
    



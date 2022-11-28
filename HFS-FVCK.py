import requests
import base64
import json

url="https://hfs-be.yunxiao.com/v2/users/sessions"
headers = {'devicetype': '1','apptype': '1','versionname': "4.30.91",'user-agent': "YX Android 10"}
phone=input("手机号:")
password=input("密码:")
passwordbase=base64.urlsafe_b64encode(password.encode('utf-8')).decode()+"\n"
postdata={"deviceType":1,"loginName":phone,"loginType":1,"password":passwordbase,"rememberMe":1,"roleType":1}
req=requests.post(url=url,data=postdata,headers=headers)
print(req.text)
hfssessionid=json.loads(req.text).get('data').get('token')
cookie = {'hfs-session-id': hfssessionid}

examid=input("请输入考试id:")
#examid='1779129'
url="https://hfs-be.yunxiao.com/v3/exam/"+examid+"/brief?withSubPapers=1"
req=requests.get(url=url,headers=headers,cookies=cookie)
#print(req.text)
print(json.loads(req.text).get('data').get('name'))
paper_list=json.loads(req.text).get('data').get('papers')
for paper in paper_list:
    paperId=str(paper['paperId'])
    subject=str(paper['subject'])
    print(paperId+" "+subject)

paperid=input("请输入试卷id:")
#paperid="6998977-27856"
print("接口1:")
url="https://hfs-be.yunxiao.com/v3/exam/"+examid+"/papers/"+paperid+"/question-detail"
req=requests.get(url=url,headers=headers,cookies=cookie)
#print(req.text)
question_list=json.loads(req.text).get('data').get('questionList')
for question in question_list:
    name=str(question['name'])
    answer=str(question['answer'])
    print(name+" "+answer)

print("接口2:")
url="https://hfs-be.yunxiao.com/v3/exam/"+examid+"/papers/"+paperid+"/answer-picture"
req=requests.get(url=url,headers=headers,cookies=cookie)
#print(req.text)
question_list=json.loads(req.text).get('data').get('questions')
for question in question_list:
    name=str(question['name'])
    try:
        answer=str(question['answer'])
    except:
        answer=""
    print(name+" "+answer)
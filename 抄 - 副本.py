import requests
import json

examid=""
paperid=""
paperidfull=""

stu_tokens = [
    "token1",
    ""
]

for stu in stu_tokens:
    url="https://hfs-be.yunxiao.com/v2/online-exams/token?examId="+examid+"&paperId="+paperidfull
    cookie = {'hfs-session-id': stu}
    headers = {'devicetype': '1','apptype': '1','versionname': "4.30.91",'user-agent': "YX Android 10"}
    req=requests.get(url=url,headers=headers,cookies=cookie)
    #print(req.text)
    yuejuan=json.loads(req.text).get('data').get('token')
    headers.update({'hfs-app-token': yuejuan})
    url="https://yj-apigw.haofenshu.com/v370/structure/online?paperid="+paperid
    req=requests.get(url=url,headers=headers)
    #print(req.text)
    keguanti=json.loads(req.text).get('data').get('keguanti')
    zhuguanti=json.loads(req.text).get('data').get('zhuguanti')
    for dati in keguanti:
        print(dati["name"])
        questions_list=dati["questions"]
        for xiaoti in questions_list:
            print(xiaoti["name"]+" "+xiaoti["stuAns"])
    for ti in zhuguanti:
        pic_list=ti["httpPath"]
        print(ti["name"]+" "+" ".join(pic_list))
        
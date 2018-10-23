# -*- coding:utf-8 -*-
import requests
from requests import exceptions
def send_request(url,data):
     try:
        headers = {
         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0',
         'cookie': 'JSESSIONID=854A01FEB37198D239BD767236120B16; sid=106fa07e-24f5-4476-9a9c-682113e7f719; _pk_ref.5.72fe=%5B%22%22%2C%22%22%2C1540307199%2C%22http%3A%2F%2Fdec.jlu.edu.cn%2Fjludec%2Fwork%2Fwork%2Fstudent%2Fjob.jsp%22%5D; _pk_id.5.72fe=ece1c292608a1f48.1539348274.4.1540307199.1540307199.; _pk_ses.5.72fe=*'
                    }
        r =requests.post(url=url,headers=headers,data=data)
        if r.status_code == 200 :
           return  r
        else:
            r.raise_for_status()
            print('请求失败，请检查参数或者稍后重试')
            return None
     except exceptions.Timeout as e:
            print(e)
     except requests.exceptions.HTTPError as e:
            print(e)
def get_answer(arrangementId):
    url = 'http://exam.chinaedu.net/oxer/app/ots/TestActivity/StartAnswerPaper'
    data = {
             'arrangementId':arrangementId,
             'resourcePackageId':''
         }
    r = send_request(url=url,data=data)
    qlist = r.json()['data']['paper']['psOutputDto'][1]['paperQuestionList']
    for list in qlist:
        questionId = list['questionId']
        data = {
            'questionId': questionId,
            'answerContent': ''
        }
        url = 'http://exam.chinaedu.net/oxer/app/ots/TestActivity/CorrectQuestionBySystem'
        a = send_request(url=url,data=data)
        answer = a.json()['data']['answer']['id']
        answers = {
            0: 'A',
            1: 'B',
            2: 'C',
            3: 'D',
        }
        answer = answers.get(int(answer))
        print('第', list['sequenceNumber'], '题，答案是：', answer)



if __name__ == '__main__':
     arrangementId = '07e4cbf7-3426-4bf4-9993-e73cbf60713e'
     get_answer(arrangementId)
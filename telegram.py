import requests
from bs4 import BeautifulSoup
token = "799521964:AAFeITODH7iBTb1-0dryBGJnM-EbxFOdOCg"
method_name = "getUpdates"
url = "https://api.telegram.org/bot{0}/{1}".format(token,method_name)

naver_req = requests.get("https://finance.naver.com/sise/").text
soupob = BeautifulSoup(naver_req,"html.parser")
cospy = soupob.select_one("#KOSPI_now").text


update = requests.get(url).json()
user_id = update["result"][0]['message']['from']['id']
method_name = "sendmessage"
msg = cospy
# ?전반부가 어디에 보내줘 ?후반부가 무엇을 보내줘라는 의미다
msg_url = "https://api.telegram.org/bot{0}/{1}?chat_id={2}&text={3}".format(token,method_name,user_id,msg)
# print(msg_url)
# print(requests.get(msg_url))

print(msg_url)
# .text -> str이 반환된다.
# json을 붙히면 dict라는 class가 붙는다.
print(type(update))
print(update["ok"])
# 구조를 보고 싶으면 .text를 붙히면된다. 
print(update["result"][0]['message']['from']['id'])
# token은 url을 누가 썼는지 확인하기 위한 것이다(있어야 활성화)
# url요청
requests.get(msg_url)

# 401 은 권한없음이다. 
# 여러 가지 경우의 수가 있지만,
# response - explorer 기반이면 오류가 뜰 수 있다. 
# user-agent를 변경해서 들어간다. 
print(requests.get("https://www.melon.com/"))
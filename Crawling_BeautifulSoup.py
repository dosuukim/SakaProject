# import requests
# from bs4 import BeautifulSoup

# # 크롤링할 URL
# url = "https://v.daum.net/v/20250530091837851"

# # User-Agent 설정 (봇 차단 우회용)
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
# }

# # 요청
# response = requests.get(url, headers=headers)
# soup = BeautifulSoup(response.text, "html.parser")

# # 제목 추출
# title = soup.find("h3")  # 보통 뉴스 제목은 h3 태그에 있음
# print("제목:", title.get_text(strip=True) if title else "제목을 찾을 수 없음")

# # 본문 추출
# content = soup.find("div", {"dmcf-ptype": "general"})  # Daum 뉴스 본문은 이 속성을 가짐
# print("본문:", content.get_text(strip=True) if content else "본문을 찾을 수 없음")

# # ----------------------------------------------------------------------
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Chrome 옵션 설정
options = Options()
options.add_argument("--headless")  # 창을 띄우지 않고 실행
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# ChromeDriver 경로 설정 (자신의 경로로 수정)
service = Service("/path/to/chromedriver")  # 예: "C:/chromedriver.exe"

# 브라우저 실행
driver = webdriver.Chrome(service=service, options=options)

# 크롤링할 URL
url = "https://v.daum.net/v/20250530091837851"
driver.get(url)

# 페이지 로딩 대기
time.sleep(3)

# 제목 추출
try:
    title = driver.find_element(By.TAG_NAME, "h3").text
except:
    title = "제목을 찾을 수 없음"

# 본문 추출
try:
    content_elements = driver.find_elements(By.CSS_SELECTOR, "div[dmcf-ptype='general']")
    content = "\n".join([el.text for el in content_elements])
except:
    content = "본문을 찾을 수 없음"

# 출력
print("제목:", title)
print("본문:", content)

# 브라우저 종료
driver.quit()


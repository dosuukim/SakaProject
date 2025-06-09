from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Chrome 옵션 설정
options = Options()
options.add_argument("--headless")  # 창 없이 실행
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# ChromeDriver 경로 설정 (자신의 경로로 수정)
service = Service("C:\Program Files\Google\Chrome\Application\chromedriver.exe")  # 크롬드라이버 파일 위치 지정 (해당 파일 없을 경우 크롬다운로드 사이트에서 다운 받아야함)

# 브라우저 실행
driver = webdriver.Chrome(service=service, options=options)

# 크롤링할 URL
# url = "https://gemini.google.com/app"
v_url = input("크롤링할 url을 입력하세요 : ")
# driver.get(url)
driver.get(v_url)

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

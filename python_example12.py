# # -- 함수 정의
# def greet(name):
#     print(f"안녕하세요, {name}님!")

# greet("철수")

# # -- 함수 정의 >> 응용
# def input_name(name):  # 함수 정의
#     print(f"안냐세염, {name}님!!!")
# input_name("김땡땡")   # 함수 호출

# # -- 리스트 최대값
# nums = [10, 20, 30]
# print(max(nums))

# # -- 리스트 최대값 >> 응용
# v_maxv = [10, 20, 30, 32, 50, 100]
# print(max(v_maxv))

# # -- 파일 읽기
# with open('C:\Temp\첨부파일 테스트용.txt', 'r') as f:
#     content = f.read()
#     print(content)

# # -- 파일 읽기 >> 응용(상대패스)
# with open('.\첨부파일 테스트용.txt', 'r') as f:  # -- .\  상대패스지정 (현재 작업하는 폴더에 파일이 있어야 함)
#     # content = f.read() # <-- 이건 안해도 되네
#     # print(content)     # <-- 이건 안해도 되네
#     print(f.read())

# # -- 예외 처리
# try:
#     x = 10 / 0
# except ZeroDivisionError:
#     print("0으로 나눌 수 없습니다.")

# # -- 클래스 정의
# class Person:
#     def __init__(self, name):
#         self.name = name

#     def greet(self):
#         print(f"안녕하세요, {self.name}님!")

# p = Person("영희")
# p.greet()

# # -- 클래스 정의 >> 응용
# class 강아지: # 강아지 : class name
#     def __init__(self, 이름, 나이, 품종): # class 속성 함수 정의
#         self.이름 = 이름
#         self.나이 = 나이
#         self.품종 = 품종

#     def 짖기(self):       # 짖기 속성함수 정의
#         print("멍멍!")

#     def 소개(self):       # 소개 속성함수 정의
#         print(f"제 이름은 {self.이름}이고, {self.나이}살 된 {self.품종}입니다.")

# 우리집강아지 = 강아지("해피", 3, "푸들") # 강아지 속성 지정

# print(f"우리집 강아지 이름 : {우리집강아지.이름}")  # 출력: 해피

# 우리집강아지.짖기()     # 출력: 멍멍!
# 우리집강아지.소개()     # 출력: 제 이름은 해피이고, 3살 된 푸들입니다.

# # -- Ollama REST API로 직접 쓰기
# import requests

# response = requests.post(
#     'http://localhost:11434/api/generate',
#     json={'model': 'llama2', 'prompt': '안녕하세요, 자기소개 해주세요.'}
# )

# for line in response.iter_lines():
#     print(line)
# # 반복문을 이용한 피보나치 수열
# def fibonacci_iter(n):
#     sequence = []
#     a, b = 0, 1
#     for _ in range(n):
#         sequence.append(a)
#         a, b = b, a + b
#     return sequence

# # 예시: 처음 10개의 피보나치 수 출력
# print(fibonacci_iter(10))

# # -------------------------------------------

# # 재귀 함수를 이용한 피보나치 수열
# def fibonacci_recursive(n):
#     if n <= 1:
#         return n
#     return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# # 예시: 처음 10개의 피보나치 수 출력
# for i in range(10):
#     print(fibonacci_recursive(i), end=' ')

# # -------------------------------------------
# # 재귀 + 캐시 최적화
# from functools import lru_cache

# @lru_cache(maxsize=None)
# def fibonacci_cached(n):
#     if n <= 1:
#         return n
#     return fibonacci_cached(n - 1) + fibonacci_cached(n - 2)

# # 예시
# for i in range(20):
#     print(fibonacci_cached(i), end=' ')

# a = 1
# b = 1.0
# c = [0, 1, 2]
# d = (0, 1, 2)
# print('a : ', type(a))
# print('b : ', type(b))
# print('c : ', type(c))
# print('d : ', type(d))

# s1 = "나는 "
# s2 = "Python을 "
# s3 = "처음으로 배우고 "
# s4 = "있습니다. 어렵지 않아요...!"

# print(s1, s2, s3, s4)

# # ---------------------------------------
# s1 = "abcdefg"
# print(s1 * 2)

# # ---------------------------------------
# s1 = 'abcd'
# print(s1[0:], s1[:2])

# # ---------------------------------------
# name='홍길동'
# age = 20
# print("방법1: ", "이름은 %s이고 나이는 %d살 입니다" %(name, age))
# # print("방법2: ", "이름은 {0}이고 나이는 {1}살 입니다".format(name, age))
# # print("방법3: ", f"이름은 {name}이고 나이는 {age}살 입니다")

# -----------------------------------------
s1 = "a-ab-abc-abcd"
print("01: ", s1.count('abc'))
print("02: ", s1.find('b'))    #특정 문자열이 없으면 -1 반환
print("03: ", s1.index('b'))   #특정 문자열이 없으면 Error 발생
print("04: ", s1.replace('a', '1'))
print("05: ", s1.split('-'))
print()

# -----------------------------------------
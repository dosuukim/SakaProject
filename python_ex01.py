# # -------------------------------------------------------------
# v_file_name = "test_file.txt"
# with open(v_file_name, "w") as file:
#     file.write("이것은 파이썬에서 파일에 쓰기/읽기하는 프로그램 입니다.")

# # with open("test_file.txt", "r") as file:
# with open(v_file_name, "r") as file:
#     content = file.read()
#     print(content)
# # -------------------------------------------------------------

import oracledb

p_username = ""
p_password = ""
p_host = ""
p_service = ""
p_dns = ""
p_port = ""

con = oracledb.connect(user=p_username, password=p_password, dsn=p_dns, port=p_port)
print("DB Connect : ", con.is_dealthy())

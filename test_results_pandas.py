import pandas as pd

# 테스트 데이터 (딕셔너리 리스트 형태 또는 딕셔너리 형태)
# 딕셔너리 리스트는 행을 표현하기 좋습니다.
test_data_dict_list = [
    {"Test Case ID": "TC001", "Description": "로그인 기능 테스트", "Status": "PASS", "Result": "성공적으로 로그인됨"},
    {"Test Case ID": "TC002", "Description": "회원가입 기능 테스트", "Status": "FAIL", "Result": "중복 아이디 오류"},
    {"Test Case ID": "TC003", "Description": "상품 검색 기능 테스트", "Status": "PASS", "Result": "정확한 검색 결과"},
    {"Test Case ID": "TC004", "Description": "결제 기능 테스트", "Status": "PENDING", "Result": "네트워크 오류 발생"},
]

# pandas DataFrame으로 변환
df = pd.DataFrame(test_data_dict_list)
df = pd.date_range

# 엑셀 파일로 저장
file_name = "test_results_pandas.xlsx"
df.to_excel(file_name, index=False, sheet_name="Test Results Summary") # index=False는 DataFrame의 인덱스를 엑셀에 저장하지 않도록 합니다.

print(f"'{file_name}' 파일이 성공적으로 저장되었습니다.")

# 또는 열 기준으로 데이터를 구성할 수도 있습니다.
test_data_columns = {
    "Test Case ID": ["TC001", "TC002", "TC003", "TC004"],
    "Description": ["로그인 기능 테스트", "회원가입 기능 테스트", "상품 검색 기능 테스트", "결제 기능 테스트"],
    "Status": ["PASS", "FAIL", "PASS", "PENDING"],
    "Result": ["성공적으로 로그인됨", "중복 아이디 오류", "정확한 검색 결과", "네트워크 오류 발생"]
}

df_columns = pd.DataFrame(test_data_columns)
file_name_columns = "test_results_pandas_columns.xlsx"
df_columns.to_excel(file_name_columns, index=False, sheet_name="Test Results by Column")

print(f"'{file_name_columns}' 파일이 성공적으로 저장되었습니다.")

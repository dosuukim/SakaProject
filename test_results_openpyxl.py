import openpyxl as op_py

# 테스트 데이터 (리스트 형태)
test_data = [
    ["Test Case ID", "Description", "Status", "Result", "AddColum"],
    ["TC001", "로그인 기능 테스트", "PASS", "성공적으로 로그인됨", "추가된 값1"],
    ["TC002", "회원가입 기능 테스트", "FAIL", "중복 아이디 오류", "추가된 값2"],
    ["TC003", "상품 검색 기능 테스트", "PASS", "정확한 검색 결과", "추가된 값3"],
    ["TC004", "결제 기능 테스트", "PENDING", "네트워크 오류 발생", "추가된 값4"],
]

# 새로운 워크북 생성
workbook = op_py.Workbook()
# 활성 시트 선택 (기본적으로 첫 번째 시트)
sheet = workbook.active
sheet.title = "Test Results" # 시트 이름 설정

# 데이터 추가
for row_data in test_data:
    sheet.append(row_data)

# 엑셀 파일 저장
file_name = "test_results_openpyxl.xlsx"
workbook.save(file_name)

print(f"'{file_name}' 파일이 성공적으로 저장되었습니다.")

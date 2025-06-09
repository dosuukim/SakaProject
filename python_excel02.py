import pandas as pd

try:
    file_path = 'example.xlsx'
    # sheet_index = 0  # 첫 번째 시트 (0부터 시작하므로 인덱스 0)
    sheet_index = 1  # 두 번째 시트 (0부터 시작하므로 인덱스 1)

    # 특정 시트 인덱스를 사용하여 엑셀 파일 읽기
    df_indexed_sheet = pd.read_excel(file_path, sheet_name=sheet_index)

    print(f"\n--- 엑셀 파일 인덱스 {sheet_index} 시트 데이터 (상위 5행) ---")
    print(df_indexed_sheet.head())

except FileNotFoundError:
    print(f"오류: '{file_path}' 파일을 찾을 수 없습니다. 파일 경로를 확인해주세요.")
except IndexError:
    print(f"오류: 시트 인덱스 {sheet_index}에 해당하는 시트를 찾을 수 없습니다. 시트 인덱스를 확인해주세요.")
except Exception as e:
    print(f"엑셀 파일을 읽는 중 오류가 발생했습니다: {e}")
import pandas as pd

try:
    file_path = 'example.xlsx'
    sheet_name = 'Sheet2'  # 읽고 싶은 시트 이름

    # 특정 시트 이름을 사용하여 엑셀 파일 읽기
    df_specific_sheet = pd.read_excel(file_path, sheet_name=sheet_name)

    print(f"\n--- 엑셀 파일 '{sheet_name}' 시트 데이터 (상위 5행) ---")
    print(df_specific_sheet.head())

except FileNotFoundError:
    print(f"오류: '{file_path}' 파일을 찾을 수 없습니다. 파일 경로를 확인해주세요.")
except ValueError:
    print(f"오류: '{sheet_name}' 시트를 찾을 수 없습니다. 시트 이름을 확인해주세요.")
except Exception as e:
    print(f"엑셀 파일을 읽는 중 오류가 발생했습니다: {e}")
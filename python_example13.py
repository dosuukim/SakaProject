# import numpy as np
# import IPython.display as display
# from matplotlib import pyplot as plt
# import io
# import base64

# ys = 200 + np.random.randn(100)
# x = [x for x in range(len(ys))]

# fig = plt.figure(figsize=(4, 3), facecolor='w')
# plt.plot(x, ys, '-')
# plt.fill_between(x, ys, 195, where=(ys > 195), facecolor='g', alpha=0.6)
# plt.title("Sample Visualization", fontsize=10)

# data = io.BytesIO()
# plt.savefig(data)
# image = F"data:image/png;base64,{base64.b64encode(data.getvalue()).decode()}"
# alt = "Sample Visualization"
# display.display(display.Markdown(F"""![{alt}]({image})"""))
# plt.close(fig)

# import numpy as np
# print(np.__version__)

import pandas as pd
try:
    # 엑셀 파일 경로 지정
    # file_path = 'C:\01.Python\00.PythonTest\exp.xlsx'
    file_path = 'exp.xlsx'

    # 엑셀 파일의 첫 번째 시트를 DataFrame으로 읽어오기
    # read_excel 함수는 기본적으로 첫 번째 시트를 읽습니다.
    df = pd.read_excel(file_path)

    # 읽어온 데이터 출력 (상위 5행)
    print("--- 엑셀 파일 첫 번째 시트 데이터 (상위 5행) ---")
    print(df.head())

    # 데이터프레임 정보 출력
    print("\n--- 데이터프레임 정보 ---")
    df.info()

except FileNotFoundError:
    print(f"오류: '{file_path}' 파일을 찾을 수 없습니다. 파일 경로를 확인해주세요.")
except Exception as e:
    print(f"엑셀 파일을 읽는 중 오류가 발생했습니다: {e}")

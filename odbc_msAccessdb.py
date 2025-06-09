import pyodbc

# Access DB 파일 경로
db_file = r'C:\path\to\your\database.accdb'

# 연결 문자열
conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    rf'DBQ={db_file};'
)

try:
    conn = pyodbc.connect(conn_str)
    print("Access DB 연결 성공!")

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM your_table")

    for row in cursor.fetchall():
        print(row)

except pyodbc.Error as e:
    print("DB 연결 실패:", e)

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals():
        conn.close()

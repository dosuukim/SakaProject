import pyodbc

# 연결 정보
server = 'localhost\\SQLEXPRESS'  # 또는 IP 주소
database = 'your_database'
username = 'your_username'
password = 'your_password'

# 연결 문자열
conn_str = (
    f'DRIVER={{ODBC Driver 17 for SQL Server}};'
    f'SERVER={server};'
    f'DATABASE={database};'
    f'UID={username};'
    f'PWD={password}'
)

try:
    conn = pyodbc.connect(conn_str)
    print("SQL Server 연결 성공!")

    cursor = conn.cursor()
    cursor.execute("SELECT TOP 10 * FROM your_table")

    for row in cursor.fetchall():
        print(row)

except pyodbc.Error as e:
    print("연결 실패:", e)

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals():
        conn.close()

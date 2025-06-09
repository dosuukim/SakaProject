import cx_Oracle

# Oracle 접속 정보
username = 'sch'
password = 'sch#2021'
host = '211.230.232.68'  # Oracle 서버 IP
port = 1251
sid = 'DEVERP'            # 또는 서비스 이름: 'XE', 'ORCLPDB1' 등

# DSN(Data Source Name) 생성
dsn = cx_Oracle.makedsn(host, port, sid=sid)

# Oracle DB 연결
try:
    connection = cx_Oracle.connect(user=username, password=password, dsn=dsn)
    print("Oracle DB에 성공적으로 연결되었습니다.")

    # 커서 사용 예시
    cursor = connection.cursor()
    cursor.execute("SELECT sysdate FROM dual")
    for row in cursor:
        print("현재 Oracle 날짜:", row[0])

except cx_Oracle.DatabaseError as e:
    print("오류 발생:", e)

finally:
    if cursor:
        cursor.close()
    if connection:
        connection.close()

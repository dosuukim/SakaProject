import oracledb
import os

# 환경 변수 설정: TNSNAMES.ORA 경로를 Oracle이 인식할 수 있게 함
os.environ["TNS_ADMIN"] = r"C:\app\product\11.2.0\client_1\network\admin"

# thick 모드 활성화 (Oracle 클라이언트 필요)
oracledb.init_oracle_client(lib_dir=r"C:\app\product\11.2.0\client_1")  # Instant Client 또는 Oracle Client 경로

# 접속 정보
DB_USER = "sch"
DB_PASSWORD = "sch#2021"
DB_ALIAS = "deverp"  # tnsnames.ora에 정의된 이름

try:
    # TNS 별칭으로 접속
    conn = oracledb.connect(user=DB_USER, password=DB_PASSWORD, dsn=DB_ALIAS)
    print("Oracle DB 연결 성공")

    # 간단한 쿼리 실행
    cursor = conn.cursor()
    cursor.execute("SELECT sysdate FROM dual")
    result = cursor.fetchone()
    print("Oracle 현재 날짜:", result[0])

except oracledb.Error as e:
    print("오류 발생:", e)

finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()

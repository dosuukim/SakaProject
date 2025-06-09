import oracledb # cx_Oracle 대신 oracledb 임포트
import os

# --- 1. TNS_ADMIN 환경 변수 설정 (tnsnames.ora 파일이 있는 디렉토리 경로) ---
# 제공된 tnsnames.ora 파일의 실제 경로입니다.
TNS_ADMIN_DIR = r"C:\app\product\11.2.0\client_1\network\admin"

# 코드 내에서 TNS_ADMIN 환경 변수 설정
# r''을 사용하여 백슬래시가 특수 문자로 해석되지 않도록 합니다.
os.environ['TNS_ADMIN'] = TNS_ADMIN_DIR
print(f"TNS_ADMIN 환경 변수 설정: {os.environ['TNS_ADMIN']}")

# --- 2. 데이터베이스 연결 정보 설정 ---
# 제공된 사용자 이름, 비밀번호, TNS 별칭입니다.
DB_USER     = "sch"
DB_PASSWORD = "sch#2021"
DB_ALIAS    = "deverp" # tnsnames.ora 파일에 정의된 데이터베이스 별칭

# --- 3. 데이터 삽입 함수 정의 ---
def insert_sample_data(product_name, quantity):
    connection = None
    cursor = None
    try:
        # 데이터베이스 연결
        # DSN으로 TNS_ADMIN에 지정된 디렉토리의 tnsnames.ora 파일에 있는 별칭을 사용
        connection = oracledb.connect(user=DB_USER, password=DB_PASSWORD, dsn=DB_ALIAS)
        print(f"Oracle 11g 데이터베이스 ({DB_ALIAS})에 성공적으로 연결되었습니다.")

        cursor = connection.cursor()

        # 테이블이 없으면 생성 (최초 한 번만 실행)
        # Oracle 11g는 IDENTITY 컬럼을 지원하지 않으므로, 시퀀스와 트리거를 사용하는 것이 일반적입니다.
        # 여기서는 PRODUCT_ID를 NUMBER 타입으로만 선언하고, ID를 직접 부여하는 방식으로 간단하게 예시를 만듭니다.
        # 실제 환경에서는 자동 증가 ID를 위해 시퀀스/트리거를 사용해야 합니다.
        try:
            cursor.execute("""
                CREATE TABLE PYTHON_PRODUCTS_11G (
                    PRODUCT_ID NUMBER PRIMARY KEY,
                    PRODUCT_NAME VARCHAR2(100) NOT NULL,
                    QUANTITY NUMBER(10),
                    CREATED_DATE DATE DEFAULT SYSDATE
                )
            """)
            print("테이블 'PYTHON_PRODUCTS_11G'가 생성되었습니다.")

            # Oracle 11g에서 자동 증가 ID를 위한 시퀀스 및 트리거 예시 (필요하다면 주석 해제 후 실행)
            # cursor.execute("""
            #     CREATE SEQUENCE PYTHON_PRODUCTS_11G_SEQ START WITH 1 INCREMENT BY 1 NOCACHE
            # """)
            # print("시퀀스 'PYTHON_PRODUCTS_11G_SEQ'가 생성되었습니다.")
            #
            # cursor.execute("""
            #     CREATE OR REPLACE TRIGGER PYTHON_PRODUCTS_11G_TRG
            #     BEFORE INSERT ON PYTHON_PRODUCTS_11G
            #     FOR EACH ROW
            #     BEGIN
            #         :NEW.PRODUCT_ID := PYTHON_PRODUCTS_11G_SEQ.NEXTVAL;
            #     END;
            # """)
            # print("트리거 'PYTHON_PRODUCTS_11G_TRG'가 생성되었습니다.")

        except oracledb.Error as e:
            # ORA-00955: name is already used by an existing object (테이블이 이미 존재)
            if e.code == 955:
                print("테이블 'PYTHON_PRODUCTS_11G'는 이미 존재합니다.")
            else:
                raise e # 다른 오류는 다시 발생시킴

        # ID를 직접 지정하거나 시퀀스+트리거를 사용해야 합니다.
        # 시퀀스+트리거가 없다면, 현재 존재하는 최대 ID + 1을 사용하는 간단한 예시 (프로덕션에는 부적합)
        cursor.execute("SELECT NVL(MAX(PRODUCT_ID), 0) FROM PYTHON_PRODUCTS_11G")
        next_id = cursor.fetchone()[0] + 1

        # 데이터 삽입 SQL
        # 시퀀스+트리거가 있다면: INSERT INTO PYTHON_PRODUCTS_11G (PRODUCT_NAME, QUANTITY) VALUES (:1, :2)
        sql_insert = "INSERT INTO PYTHON_PRODUCTS_11G (PRODUCT_ID, PRODUCT_NAME, QUANTITY) VALUES (:1, :2, :3)"

        # 데이터 삽입 (바인드 변수 사용)
        cursor.execute(sql_insert, (next_id, product_name, quantity))

        # 변경사항 커밋
        connection.commit()
        print(f"제품 '{product_name}' (ID: {next_id}, 수량: {quantity}) 데이터가 성공적으로 저장되었습니다.")

    except oracledb.Error as e:
        # oracledb.Error 객체는 에러 코드를 직접 제공합니다.
        print(f"Oracle 오류 발생: {e.code} - {e.message}")
        if connection:
            connection.rollback()
            print("변경사항이 롤백되었습니다.")
    finally:
        # 커서와 연결 닫기 (항상 실행)
        if cursor:
            cursor.close()
        if connection:
            connection.close()
        print("데이터베이스 연결이 종료되었습니다.")

# --- 4. 함수 호출 예제 ---
if __name__ == "__main__":
    insert_sample_data("사과", 100)
    insert_sample_data("바나나", 150)
    insert_sample_data("오렌지", 80)

    # 데이터 조회 (선택 사항)
    connection = None
    cursor = None
    try:
        connection = oracledb.connect(user=DB_USER, password=DB_PASSWORD, dsn=DB_ALIAS)
        cursor = connection.cursor()
        cursor.execute("SELECT PRODUCT_ID, PRODUCT_NAME, QUANTITY, CREATED_DATE FROM PYTHON_PRODUCTS_11G ORDER BY PRODUCT_ID DESC")
        rows = cursor.fetchall()
        print("\n--- 저장된 데이터 ---")
        for row in rows:
            print(f"ID: {row[0]}, 제품명: {row[1]}, 수량: {row[2]}, 생성일: {row[3]}")
    except oracledb.Error as e:
        print(f"데이터 조회 중 오류 발생: {e.code} - {e.message}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
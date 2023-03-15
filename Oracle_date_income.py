import oracledb
import pandas as pd
from sqlalchemy import create_engine
import cx_Oracle

oracledb.init_oracle_client(lib_dir=r'C:\instantclient_19_18')

# 오라클 데이터베이스 연결 정보
host = '192.168.0.111'
port = 1522
sid = 'HYDSPC'
user = 'spcadmin'
password = 'spcadmin'

# Oracle DB 접속 정보
dsn = oracledb.makedsn(host, port, service_name=sid)
conn = oracledb.connect(user=user, password=password, dsn=dsn)
db_uri = f'oracle://{user}:{password}@{host}:{port}/{sid}'
db_uri1 = f'{user}/{password}@{host}:{port}/{sid}'
con1 = cx_Oracle.connect(db_uri1)
# 뷰 테이블 가져 오기
cur = conn.cursor()
cur.execute("SELECT view_name FROM user_views")
views = cur.fetchall()
print(views)


engine = create_engine(db_uri)

print(engine)
# SQL 쿼리문 실행 결과를 데이터프레임으로 가져오기
# SQL 쿼리문 작성
sql = 'SELECT * FROM ' + views[1][0]

df = pd.read_sql(sql, con=con1)
# df = pd.read_sql(sql, engine)

print(df)
if 0:
    for view in views:
        print(view)
        cur.execute('SELECT * FROM ' + view[0])
        rows = cur.fetchall()

        # 결과 확인
        for row in rows:
            print(row)

# 커넥션 닫기
cur.close()
conn.close()

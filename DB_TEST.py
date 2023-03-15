import pymysql
import pandas as pd

# MariaDB 연결 설정
conn = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='votmdnjem',
    database='hanyangdgt'
)

# 쿼리 실행 및 결과 가져오기
query = "SELECT * FROM warpage_data"
df = pd.read_sql_query(query, conn)

# 결과 출력
print(df.dtypes)
# 연결 종료
conn.close()

# 데이터베이스에 데이터프레임 삽입
table_name = 'dimension_data'
df.to_sql(name=table_name, con=conn, if_exists='replace', index=False)



conn.close()

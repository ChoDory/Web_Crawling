import pandas as pd
from sqlalchemy import create_engine

# 마리아DB 연결 정보 설정
db_host = '127.0.0.1'
db_user = 'root'
db_password = '1234'
db_name = 'study'

# CSV 파일 경로 설정
csv_file_path = '/Users/chominjun/Desktop/Workspace/PYTHON_workspace/Test/activity_info_v4.csv'

# 데이터베이스 연결 엔진 생성
engine = create_engine(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}")

# CSV 파일을 데이터프레임으로 읽기
df = pd.read_csv(csv_file_path)

# 데이터프레임을 마리아DB에 저장
df.to_sql('your_table_name', con=engine, if_exists='replace', index=False)

print(f"CSV 파일이 성공적으로 마리아DB에 저장되었습니다.")
import mysql.connector

# MariaDB 연결 설정
connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="1234",
    database="study"
)

# 커서 생성
cursor = connection.cursor()

# 쿼리 실행
query = "SELECT * FROM activity_info_v4 WHERE tags LIKE '%방탈출%'"
cursor.execute(query)

# 결과 가져오기
results = cursor.fetchall()

if results:
    for result in results:
        # 결과를 원하는 형식으로 출력
        output = {
            "category": "방탈출",
            # "menu": result[5],
            "placeImage": result[4],
            "placeName": result[0],
            # "placePrice": result[6],
            "rate": result[3]
        }
        print(output)
else:
    print("해당하는 결과가 없습니다.")

# 연결 종료
cursor.close()
connection.close()
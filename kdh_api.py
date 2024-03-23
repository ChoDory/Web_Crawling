from flask import Flask, request, jsonify
import mariadb
import json
import random


app = Flask(__name__)

@app.route('/extract_place_info', methods=['POST'])
def extract_place_info():
    # 요청 데이터 받기
    input_data = request.get_json()
    min_price = input_data["minPrice"]
    max_price = input_data["maxPrice"]
    kinds = input_data["kinds"]
    place_result = []

    conn = mariadb.connect(
        user="root",
        password="1234",
        host="127.0.0.1",
        port=3306,
        database="study"
    )
    cursor = conn.cursor()

    for kind in kinds:
        if kind == "한식" | kind == "중식" | kind == "일식" | kind == "양식" | kind == "분식" | kind == "기타":
            query = f"SELECT * FROM restaurant_info_v3 WHERE tags IN ({', '.join(['%s']*len(kinds))})"
            cursor.execute(query, tuple(kinds))
            result = cursor.fetchall()
            # 결과에서 무작위로 1개의 행 추출
            random_row = random.choice(result)
            # 추출한 행을 JSON 형식으로 변환하여 반환
            extracted_result = {
                'placeName': random_row[0],
                'rate': random_row[3],
                'menu': random_row[5],
                'placePrice': random_row[6],
                'placeImage': random_row[8]
            }
            place_result.append(extracted_result)

        elif kind == "카페" | kind == "맥주/소주" | kind == "막걸리" | kind == "와인" | kind=="위스키" | kind=="칵테일":
            rquery = f"SELECT * FROM cafe_info_v3 WHERE tags IN ({', '.join(['%s']*len(kinds))})"
            cursor.execute(query, tuple(kinds))
            result = cursor.fetchall()
            result.append(random_row)
            # 결과에서 무작위로 1개의 행 추출
            random_row = random.choice(result)
            # 추출한 행을 JSON 형식으로 변환하여 반환
            extracted_result = {
                'placeName': random_row[0],
                'rate': random_row[3],
                'menu': random_row[5],
                'placePrice': random_row[6],
                'placeImage': random_row[8]
            }
            place_result.append(extracted_result)
        elif kind == "게임/오락" | kind == "힐링" | kind == "방탈출" | kind == "클래스" | kind == "영화" | kind == "전시" | kind == "책방":
            query = f"SELECT * FROM activity_info_v4 WHERE tags IN ({', '.join(['%s']*len(kinds))})"
            cursor.execute(query, tuple(kinds))
            result = cursor.fetchall()
            result.append(random_row)
            # 결과에서 무작위로 1개의 행 추출
            random_row = random.choice(result)
            # 추출한 행을 JSON 형식으로 변환하여 반환
            extracted_result = {
                'placeName': random_row[0],
                'rate': random_row[3],
                'menu': random_row[5],
                'placePrice': random_row[6],
                'placeImage': random_row[8]
            }
            place_result.append(extracted_result)
        else:
            result = {"error": f"Invalid theme: {kind}"}

    conn.close()

    print(extracted_result)

    return jsonify(extracted_result)

if __name__ == '__main__':
    app.run(debug=True)

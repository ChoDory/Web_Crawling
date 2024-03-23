from flask import Flask, request, jsonify
import mariadb

app = Flask(__name__)

@app.route('/extract_restaurant_info', methods=['POST'])
def extract_restaurant_info():
    # 요청 데이터 받기
    input_data = request.get_json()
    min_price = input_data["minPrice"]
    max_price = input_data["maxPrice"]
    kinds = input_data["kinds"]
    
    conn = mariadb.connect(
        user="root",
        password="1234",
        host="127.0.0.1",
        port=3306,
        database="study"
    )
    cursor = conn.cursor()

    # 종류(kinds)와 태그(tags) 값이 매칭되도록 SQL 쿼리 실행
    query = "SELECT * FROM restaurant_info_v3 WHERE (place_price >= ? AND place_price <= ?)"
    result = []
    for kind in kinds:
        parameters = [min_price, max_price]  # 매번 새로운 parameters를 생성하여 전달
        cursor.execute(query, parameters)
        for row in cursor.fetchall():
            tags = row[7].split(',')
            if kind in tags:
                extracted_result = {
                    'placeName': row[0],
                    'rate': row[3], 
                    'menu': row[5],
                    'placePrice': row[6],
                    'placeImage': row[8]
                }
                result.append(extracted_result)

    conn.close()

    return jsonify(result)

if __name__ == '__main__':
    app.run()

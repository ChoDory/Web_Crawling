import csv
import random
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/extract_restaurant_info', methods=['POST'])
def extract_restaurant_info():
    # 요청 데이터 받기
    input_data = request.get_json()
    if input_data is None:
        return jsonify({'error': 'Invalid request format. JSON data expected.'}), 400

    min_price = input_data["minPrice"]
    max_price = input_data["maxPrice"]
    kinds = input_data["kinds"]

    # CSV 파일 경로
    csv_file_path = '/home/ubuntu/restaurant_info.csv'

    matching_rows = []
    with open(csv_file_path, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            place_price = int(row['place_price'])
            if min_price <= place_price <= max_price:
                tags = row['tags'].split(',')
                for kind in kinds:
                    if kind in tags:
                        matching_rows.append(row)

    if matching_rows:
        random_row = random.choice(matching_rows)
        extracted_result = {
            'placeName': random_row['place_name'],
            'rate': random_row['rate'],
            'menu': random_row['menu'],
            'placePrice': int(random_row['place_price']),
            'placeImage': random_row['place_image']
        }
        return jsonify(extracted_result)
    else:
        return '일치하는 데이터가 없습니다.'
    

if __name__ == '__main__':
    app.run()

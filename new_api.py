from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/post_endpoint', methods=['POST'])
def post_endpoint():
    data = {
        'menu': '뉘른베르크 플레이트',
        'placeImage': 'https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20210726_104%2F1627274956156zHiW2_JPEG%2FxUsaGunmhJoOuyowuXyw7Uaj.jpeg.jpg',
        'placeName': '카페인신현리 아티장가든',
        'placePrice': 19000,
        'rate': 5.0
    }
    return data

if __name__ == '__main__':
    app.run(debug=True)

import pandas as pd
import ast

# 입력 파일과 출력 파일의 경로
input_file_path = '/Users/chominjun/Desktop/Workspace/PYTHON_workspace/Test/data_carawler/restaurant_info.csv'
output_file_path = '/Users/chominjun/Desktop/Workspace/PYTHON_workspace/Test/output.csv'

# 데이터 읽기
df = pd.read_csv('/Users/chominjun/Desktop/Workspace/PYTHON_workspace/Test/activity_info_v4.csv')

# 'tags' 컬럼의 리스트 문자열을 실제 리스트로 변환
df['tags'] = df['tags'].apply(ast.literal_eval)

# 리스트를 콤마로 구분된 문자열로 변환
df['tags'] = df['tags'].apply(', '.join)

# 결과 확인
print(df['tags'])

# def convert_price(price):
#     # 콤마와 '원' 문자 제거
#     price = price.replace(',', '').replace('원', '')
    
#     # '변동' 값 처리
#     if price == '변동':
#         return -1  # '변동' 값을 -1로 대체

#     elif price == '무료':
#         return 0

#     # 범위를 나타내는 값 처리
#     elif '~' in price:
#         price_range = price.split('~')
#         lower = int(price_range[0])
#         upper = int(price_range[1])
#         return (lower + upper) // 2  # 평균값 반환

#     else:
#         return int(price)  # 정수형으로 변환

# # 'place_price' 컬럼의 값을 변환
# df['place_price'] = df['place_price'].apply(convert_price)

# # 결과 확인
# print(df['place_price'])


# def convert_menu(menu_list):
#     # 문자열을 리스트로 변환
#     menu_list = ast.literal_eval(menu_list)
    
#     # 딕셔너리 생성
#     menu_dict = {}
#     for menu, price in menu_list:
#         # 가격 변환
#         price = convert_price(price)
#         menu_dict[menu] = price
    
#     return menu_dict

# # 'menu_list' 컬럼의 값을 변환
# df['menu_list'] = df['menu_list'].apply(convert_menu)

# # 결과 확인
# print(df['menu_list'])

# 변경된 데이터프레임을 새로운 CSV 파일로 저장
df.to_csv(output_file_path, index=False)  # 출력 파일 경로를 변수로 지정
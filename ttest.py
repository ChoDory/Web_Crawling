import ast
import pandas as pd


df = pd.read_csv('/Users/chominjun/Desktop/Workspace/PYTHON_workspace/Test/restaurant_info_v3.csv')

# 문자열을 딕셔너리로 변환
menu_dict = ast.literal_eval(df.loc[0, 'menu_list'])

# 첫 번째 메뉴와 가격 추출
first_menu = list(menu_dict.keys())[0]
first_price = menu_dict[first_menu]

print(f"메뉴: {first_menu}, 가격: {first_price}원")
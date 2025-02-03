from utils import round_result, convert_to_radians

# round_result 테스트
value = 12.3456789
rounded_value = round_result(value, 3)
print(f"{value}를 소수점 3자리로 반올림: {rounded_value}")  # 출력: 12.346

# convert_to_radians 테스트
degree_angle = 180
radian_result = convert_to_radians(degree_angle, 'degree')
print(f"{degree_angle}도는 라디안 값으로: {radian_result}")  # 출력: 3.141592...

radian_angle = 1.5
print(f"{radian_angle} 라디안은 그대로: {convert_to_radians(radian_angle, 'radian')}")
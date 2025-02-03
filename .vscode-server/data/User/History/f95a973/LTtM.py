import math  # math 모듈을 불러와야 함
from calculator import basic, engineering, complex


# 전역 기본 정밀도 설정
DEFAULT_PRECISION = 2

def round_result(value, precision=None):
    """
    주어진 값을 지정된 소수점 자리까지 반올림하는 함수.
    기본 정밀도는 DEFAULT_PRECISION에 따라 설정됨.
    
    Args:
        value (float): 반올림할 값
        precision (int, optional): 반올림할 소수점 자리수 (None이면 기본 정밀도 사용)

    Returns:
        float: 반올림된 값
    """
    if precision is None:
        precision = DEFAULT_PRECISION  # 기본 정밀도 사용
    return round(value, precision)

def convert_to_radians(angle, unit='degree'):
    """
    각도를 라디안으로 변환하는 함수. 'degree', 'radian', 'gradian' 단위 지원.
    
    Args:
        angle (float): 변환할 각도 값
        unit (str): 입력 각도의 단위 ('degree', 'radian', 'gradian')

    Returns:
        float: 라디안 값

    Raises:
        ValueError: 잘못된 단위가 제공된 경우 예외 발생
    """
    unit = unit.lower()  # 대소문자 구분 없이 처리

    if unit == 'degree':
        return math.radians(angle)  # degree → radian 변환
    elif unit == 'gradian':
        # gradian을 radian으로 변환 (1 gradian = π/200 radian)
        return angle * (math.pi / 200)
    elif unit == 'radian':
        return angle  # 이미 라디안인 경우 그대로 반환
    else:
        raise ValueError("unit은 'degree', 'radian', 또는 'gradian'이어야 합니다.")
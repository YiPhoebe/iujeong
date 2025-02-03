import math
import cmath

def round_result(value, precision):
    """
    주어진 값을 지정된 소수점 자리까지 반올림하는 함수.
    
    Args:
        value (float): 반올림할 값
        precision (int): 반올림할 소수점 자리수

    Returns:
        float: 반올림된 값
    """
    return round(value, precision)

def convert_to_radians(angle, unit='degree'):
    """
    각도를 라디안으로 변환하는 함수.
    
    Args:
        angle (float): 변환할 각도 값
        unit (str): 입력 각도의 단위 ('degree' 또는 'radian')

    Returns:
        float: 라디안 값

    Raises:
        ValueError: 잘못된 단위가 제공된 경우
    """
    if unit == 'degree':
        return math.radians(angle)
    elif unit == 'radian':
        return angle
    else:
        raise ValueError("unit은 'degree' 또는 'radian'이어야 합니다.")

def is_number(value):
    """
    값이 숫자인지 확인하는 함수.

    Args:
        value: 확인할 값

    Returns:
        bool: 숫자인 경우 True, 그렇지 않은 경우 False
    """
    try:
        float(value)
        return True
    except ValueError:
        return False

def validate_non_negative(value):
    """
    값이 음수가 아닌지 확인하는 함수. 음수일 경우 예외를 발생시킴.
    
    Args:
        value (float): 확인할 값

    Returns:
        None

    Raises:
        ValueError: 값이 음수일 경우
    """
    if value < 0:
        raise ValueError("값이 음수일 수 없습니다.")

def polar_to_cartesian(r, theta):
    """
    극 좌표계에서 직교 좌표계로 변환.

    Args:
        r (float): 극 좌표계 반지름
        theta (float): 극 좌표계 각도 (라디안)

    Returns:
        tuple: (x, y) 직교 좌표계 좌표
    """
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    return x, y

def cartesian_to_polar(x, y):
    """
    직교 좌표계에서 극 좌표계로 변환.

    Args:
        x (float): 직교 좌표계 x 좌표
        y (float): 직교 좌표계 y 좌표

    Returns:
        tuple: (r, theta) 극 좌표계
    """
    r = math.sqrt(x**2 + y**2)
    theta = math.atan2(y, x)
    return r, theta
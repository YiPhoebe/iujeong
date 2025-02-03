import math

class EngineeringCalculator:
    """
    공학용 계산기 클래스
    다양한 공학적 계산을 수행하는 메서드를 포함합니다.
    """

    def square_root(self, *args):
        """
        입력된 값들의 제곱근을 계산합니다.
        음수인 경우 '0보다 작을 수 없습니다.'라는 메시지를 반환합니다.
        """
        self.result = []  # 결과를 저장할 리스트 초기화

        for num in args:  # 입력된 숫자를 순회
            if num < 0:  # 음수인지 확인
                self.result.append('0보다 작을 수 없습니다.')  # 음수 처리 메시지 추가
            else:
                self.result.append(math.sqrt(num))  # 제곱근 계산 및 저장
        return self.result  # 결과 반환

    def power(self, exponent, *args):
        """
        입력된 값들의 거듭제곱을 계산합니다.
        지수(exponent)는 첫 번째 매개변수로 전달됩니다.
        음수인 경우 '0보다 작을 수 없습니다.'라는 메시지를 반환합니다.
        """
        self.result = []  # 결과를 저장할 리스트 초기화

        for num in args:  # 입력된 숫자를 순회
            if num < 0:  # 음수인지 확인
                self.result.append('0보다 작을 수 없습니다.')  # 음수 처리 메시지 추가
            else:
                self.result.append(math.pow(num, exponent))  # 거듭제곱 계산 및 저장
        return self.result  # 결과 반환

    def log(self, *args):
        """
        입력된 값들의 상용로그(log10)를 계산합니다.
        0 또는 음수인 경우 '0보다 작을 수 없습니다.'라는 메시지를 반환합니다.
        """
        self.result = []  # 결과를 저장할 리스트 초기화

        for num in args:  # 입력된 숫자를 순회
            if num <= 0:  # 0 또는 음수인지 확인
                self.result.append('0보다 작을 수 없습니다.')  # 음수 처리 메시지 추가
            else:
                self.result.append(math.log10(num))  # 상용로그 계산 및 저장
        return self.result  # 결과 반환

    def sin(self, *angles, angle_unit='radian'):
        """
        입력된 각도의 사인 값을 계산합니다.
        각도 단위는 기본적으로 라디안(radian)을 사용하며, 'degree'로 지정 시 각도를 변환합니다.
        """
        self.result = []  # 결과를 저장할 리스트 초기화

        for angle in angles:  # 입력된 각도를 순회
            if angle_unit == 'degree':  # 각도 단위가 'degree'인 경우
                angle = math.radians(angle)  # 라디안으로 변환
            self.result.append(math.sin(angle))  # 사인 값 계산 및 저장
        return self.result  # 결과 반환
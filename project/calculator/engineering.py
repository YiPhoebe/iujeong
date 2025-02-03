import math

class EngineeringCalculator:
    """ 제곱근 """
    def squre_root(self, *args):
        self.result = []

        for num in args:
            if num < 0:
                self.result.append('0보다 작을 수 없습니다.')   # 음수는 제곱근이 없으므로 '0보다 작을 수 없습니다.' 반환
        else:
            self.result.append(math.sqrt(num))
        return self.result
    
    """ 제곱 """
    def power(self, exponent, *args):   # 동적으로 다양한 거듭제곱 계산을 가능하게 하기 위해 매개 변수로 지수(exponent)를 받아준다.
        self.result = []

        for num in args:
            if num < 0:
                self.result.append('0보다 작을 수 없습니다.')
            else:
                self.result.append(math.pow(num, exponent))
            self.result

    def log(self, *args):
        """ 상용로그 """
        self.result = []

        for num in args:
            if num < 0:
                self.result.append('0보다 작을 수 없습니다.')
            else:
                self.result.append(math.log10(num))
            return self.result
        
    def sin(self, *angles, angle_unit='radian'):    
        """
        입력된 각도(angles)에 대해 사인 값을 계산하여 반환하는 메서드.
        
        매개변수:
        ----------
        *angles : float
            계산할 각도의 리스트 (가변 인자).
        angle_unit : str
            각도의 단위 ('radian' 또는 'degree'). 기본값은 'radian'.

        반환값:
        ----------
        list : float
            각 입력 각도의 사인 값 리스트.
        """
        self.result = []  # 결과값을 저장할 리스트 초기화

        for num in angles:
            # 각도를 라디안으로 변환 (필요한 경우)
            if angle_unit == 'degree':  
                num = math.radians(num)  # num을 라디안으로 변환

            # 사인 값을 계산하고 리스트에 추가
            self.result.append(math.sin(num))
        
        return self.result  # 사인 값 리스트 반환
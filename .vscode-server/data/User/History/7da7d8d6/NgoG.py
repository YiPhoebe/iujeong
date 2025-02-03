class Calculator:
    """
    간단한 사칙연산 계산기
    
    예제 사용법:
    # 덧셈 예제
    print(calc.add(1, 2, 3))  # 출력: 6

    # 뺄셈 예제
    print(calc.subtract(10, 3, 2))  # 출력: 5

    # 곱셈 예제
    print(calc.multiply(2, 4, 3))  # 출력: 24

    # 나눗셈 예제 (0 포함)
    print(calc.divide(12, 2, 0, 3))  # 출력: 2.0, 경고 메시지 출력
    """
    def __init__(self):
        self.result = None  # 계산 결과를 저장할 속성 초기화
        
    def add(self, *args):
        """
        여러 값을 더하는 매서드
        """
        self.result = 0     # 초기값은 0으로 설정
        for num in args:    # args 더할 숫자들의 가변 인자 리스트
            self.result += num
        return self.result
    
    def subtract(self, *args):
        """
        여러 개의 숫자를 차례로 빼는 메서드.
        args: 뺄 숫자들의 가변 인자 리스트
        return: 뺄셈 결과 또는 입력값이 없이 없을 때 메세지 반환
        """
        if not args:    # 입력값이 없을 때
            return "입력한 값이 없습니다."
        
        self.result = args[0]   # 첫 번째 값을 기준으로 시작
        for num in  args[1:]:   # 두 번째 값부터 순차적으로 뺌
            self.result -= num
        return self.result
    
    def multiply(self, *args):
        """
        여러 개의 숫자를 차례로 곱하는 메서드.
        """
        if not args:
            return "입력한 값이 없습니다."
        
        self.result = 1     # 곱셈의 항등원은 1 (어떤 수 a에 1을 곱해도 원래의 값이 변하지 않음)
        for num in args:
            self.result *= num
        return self.result
    
    def divide(self, *args):
        """
        숫자를 차례로 나누는 메서드 (복소수 포함)
        0으로 나누는 경우는 건너뛰며 경고 메세지를 출력.
        """
        if not args:
            raise ValueError("입력한 값이 없습니다.")
    
        self.result = args[0]   # 첫 번째 값을 기준으로 나눗셈 시작
        for num in args[1:]:    # 두 번째 값부터 순차적으로 나눔
            if num == 0:  # 0으로 나누는 경우 경고 메시지 출력 후 건너뜀
                print("경고: 0을 포함한 연산은 건너뜁니다.")
                continue
            self.result /= num  # 0이 아닌 경우 정상적으로 나눗셈 수행
        return self.result
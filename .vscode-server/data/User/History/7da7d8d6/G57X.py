class Calculator:
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
        if not args:
            return "입력한 값이 없습니다."
        
        self.result = 1     # 곱셈의 항등원은 1 (어떤 수 a에 1을 곱해도 원래의 값이 변하지 않음)
        for num in args:
            self.result *= num
        return self.result
    
    def divide(self, *args):
        """복소수 나눗셈"""
        if not args:
            raise ValueError("입력한 값이 없습니다.")
    
        self.result = args[0]
        for num in args[1:]:
            if num == 0:  # 0을 건너뛰도록 처리
                print("경고: 0을 포함한 연산은 건너뜁니다.")
                continue
            self.result /= num
        return self.result
class Calculator:
    def __init__(self):
        self.result = None  # 계산 결과를 저장할 속성 초기화
        
    def add(self, *args):
        """ 여러 값을 더하는 매서드 """
        self.result = 0
        for num in args:
            self.result += num
        return self.result
    
    def subtract(self, *args):
        if not args:
            return "입력한 값이 없습니다."
        
        self.result = args[0]
        for num in  args[1:]:
            self.result -= num
        return self.result
    
    def multiply(self, *args):
        if not args:
            return "입력한 값이 없습니다."
        
        self.result = 1
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
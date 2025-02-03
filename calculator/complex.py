import cmath  # 복소수 연산과 관련된 수학적 함수를 제공하는 cmath 모듈을 가져옴

class ComplexCalculator:  # 복소수 계산을 수행하는 클래스 정의
    def __init__(self):
        self.result = None  # 계산 결과를 저장할 속성 초기화

    def magnitude(self, z):
        """ 복소수 절대값 (크기) """
        self.result = abs(z)  # 복소수의 절대값 계산
        return self.result  # 결과 반환
    
    def argument(self, z):
        """ 복소수의 편각 (라디안 단위) """
        self.result = cmath.phase(z)  # 복소수의 편각 계산
        return self.result  # 결과 반환
    
    def to_polar(self, z):
        """ 복소수를 극 좌표계로 변환 (r, θ) """
        self.result = cmath.polar(z)  # 복소수를 극 좌표계 (r, θ)로 변환
        return self.result  # 결과 반환
    
    def to_cartesian(self, r, theta):
        """ 극 좌표계 (r, θ)를 복소수로 변환 """
        self.result = cmath.rect(r, theta)  # 극 좌표계 (r, θ)를 복소수로 변환
        return self.result  # 결과 반환

# -------------------------------------------------------------------------
# 코드 설명:

# 1. 왜 import를 해야 하는가?
# - `import`는 외부 모듈(라이브러리)을 코드에 가져오는 키워드입니다.
# - 이 코드에서는 복소수 계산에 필요한 수학적 함수(`cmath` 모듈)를 가져오기 위해 사용됩니다.
#   예를 들어, 복소수의 절대값을 계산하는 `abs()`나 편각을 계산하는 `cmath.phase()`는 cmath 모듈에 정의되어 있습니다.

# 2. 왜 클래스를 이렇게 지칭하는가?
# - 클래스는 관련된 데이터와 기능(메서드)을 하나로 묶는 역할을 합니다.
# - `ComplexCalculator`라는 이름은 이 클래스가 복소수 계산과 관련된 작업을 수행한다는 것을 명확히 나타냅니다.
# - 클래스 내부에는 복소수 덧셈, 뺄셈, 곱셈, 나눗셈 등과 같은 기능이 메서드로 정의되어 있습니다.

# 3. self는 왜 적어주는가?
# - `self`는 클래스 인스턴스(객체) 자체를 나타내는 키워드입니다.
# - 클래스 내부에서 정의된 변수(`self.result`)나 메서드에 접근하려면 `self`를 사용해야 합니다.
# - `self`는 메서드 호출 시 해당 인스턴스에 대해 동작하도록 보장합니다.

# 4. __init__은 뭔가?
# - `__init__`은 클래스가 인스턴스로 생성될 때 자동으로 호출되는 **생성자 메서드**입니다.
# - 이 메서드를 사용하여 초기 설정(예: 변수 초기화)을 수행할 수 있습니다.
# - 이 코드에서는 `self.result`를 `None`으로 초기화합니다.

# 5. 메서드의 역할
# - `add(*args)`: 여러 복소수의 합을 계산합니다.
# - `subtract(*args)`: 첫 번째 복소수에서 나머지 복소수를 차례로 뺍니다.
# - `multiply(*args)`: 여러 복소수를 곱합니다.
# - `divide(*args)`: 첫 번째 복소수를 나머지 복소수로 차례로 나눕니다.
# - `magnitude(z)`: 복소수의 크기(절대값)를 계산합니다.
# - `argument(z)`: 복소수의 편각(라디안 단위)을 계산합니다.
# - `to_polar(z)`: 복소수를 극 좌표계(r, θ)로 변환합니다.
# - `to_cartesian(r, θ)`: 극 좌표계를 복소수로 변환합니다.

import os   # 파일 존재 여부를 확인하기 위해 사용

class Bankaccount:
    def __init__(self, name, balance):
        self.name = name    # 계좌 소유자 이름
        self.balance = balance      # 초기 잔액

    def deposit(self, deposit_amount):
        self.balance += deposit_amount      # 입금
        print(f"{deposit_amount}원 입금되었습니다. 현재 잔액 : {self.balance}원 입니다.")

    def withdraw(self, withdraw_amount):
        if withdraw_amount > self.balance:      # 잔액 부족 시 처리
            print("잔액이 부족하여 출금을 할 수 없습니다.")

        else:
            self.balance -= withdraw_amount     # 출금
            print(f"{withdraw_amount}원 출금되었습니다. 현재 잔액 : {self.balance}원 입니다.")

    def check_balance(self):    # 잔액 확인
        print(f"{self.name}님의 현재 잔액은 {self.balance}원입니다.")   

# 초기값 설정
name = input("계좌 소유자의 이름을 입력하세요: ")
initial_balance = int(input("초기 잔액을 입력하세요: "))

# BankAccount 객체 생성
account = Bankaccount(name, initial_balance)

# 메뉴 시스템 (입금/출금/종료)
while True:
    print("\n메뉴선택 : ")
    print("1. 입금")
    print("2. 출금")
    print("3. 잔액 확인")
    print("4. 종료")

    choice = input("원하는 작업의 번호를 입력하세요 : ")

    match choice:
        case "1":
            try:
                deposit_amount = int(input("입력할 금액을 입력하세요 : "))
                account.deposit(deposit_amount)
            except ValueError:
                print("숫자만 입력해주세요.")
        #     deposit_amount = int(input("입력할 금액을 입력하세요 : "))
        #     account.deposit(deposit_amount)

        case "2":
            withdraw_amount = int(input("출금할 금액을 입력하세요 : "))
            account.withdraw(withdraw_amount)

        case "3":
            account.check_balance()

        case "4":
            print(f"{account.name}님의 계좌를 종료합니다. 최종 잔액은 {account.balance}원 입니다.")
            break

        case _:
            print("잘못된 입력입니다. 다시 선택하세요.")
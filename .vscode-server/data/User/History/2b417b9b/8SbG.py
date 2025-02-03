import os   # 파일 존재 여부를 확인하기 위해 사용

class BankAccount:
    def __init__(self, name, balance):
        self.name = name    # 계좌 소유자 이름
        self.balance = balance  # 초기 잔액

    def deposit(self, deposit_amount):
        self.balance += deposit_amount
        print(f"{deposit_amount}원 입금되었습니다. 현재 잔액 : {self.balance}원")

    def withdraw(self, withdraw_amount):
        if withdraw_amount > self.balance:
            print("잔액이 부족하여 출금할 수 없습니다.")
        else:
            self.balance -= withdraw_amount
            print(f"{withdraw_amount}원 출금되었습니다. 현재 잔액 : {self.balance}")

    def check_balance(self):
        # 계좌 정보를 파일에 저장
        with open("accoun_info.txt", "w") as file:
            file.write(f"{self.name}, {self.balance}")
        print("계좌 정보가 저장되었습니다.")

    @staticmethod
    def load_from_file():
        # 계좌 정보를 파일에서 불러옴
        if os.path.exists("account_info.txt"):
            with open("accoun_info.txt", "r") as file:
                data = file.read().strip().split(",")
                name = data[0]
                balance = int(data[1])
                return BankAccount(name, balance)
        
        else:
            # 파일이 없으면 새 계좌 생성
            name = input("계좌 소유자의 이름을 입력하세요 : ")
            initial_balance = int(input("초기 잔액을 입력하세요 : "))
            return BankAccount(name, initial_balance)
        
# 기존 계좌 정보 불러오기 또는 새 계좌 생성
account = BankAccount.load_from_file()

# 메뉴 시스템
while True:
    print("\n메뉴 선택:")
    print("1. 입금")
    print("2. 출금")
    print("3. 잔액 확인")
    print("4. 종료")

    choice = input("원하는 작업의 번호를 입력하세요 : ")

    match choice:
        case "1":
            try:
                deposit_amount = int(input("입금할 금액을 입력하세요 : "))
                account.deposit(deposit_amount)
            except ValueError:
                print("숫자만 입력해주세요.")

        case "2":
            try:
                withdraw_amount = int(input("출금할 금액을 입력하세요 : "))
                account.withdraw(withdraw_amount)
            except ValueError:
                print("숫자만 입력해주세요.")

        case "3":
            account.check_balance()

        case "4":
            account.save_to_file()  # 종료 전에 계좌 정보 저장
            print(f"{account.name}님의 계좌를 종료합니다. 최종 잔액은 {account.balance}원 입니다.")
            break

        case _:
            print("잘못된 입력입니다. 다시 선택하세요.")
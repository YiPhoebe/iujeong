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
                balance = int(input[1])
                return BankAccount(name, balance)
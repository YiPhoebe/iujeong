import os  # 파일 존재 여부를 확인하기 위해 사용

class BankAccount:
    def __init__(self, name, balance):
        self.name = name  # 계좌 소유자 이름
        self.balance = balance  # 초기 잔액

    def deposit(self, deposit_amount):
        self.balance += deposit_amount
        print(f"{deposit_amount}원 입금되었습니다. 현재 잔액: {self.balance}원")

    def withdraw(self, withdraw_amount):
        if withdraw_amount > self.balance:
            print("잔액이 부족하여 출금할 수 없습니다.")
        else:
            self.balance -= withdraw_amount
            print(f"{withdraw_amount}원 출금되었습니다. 현재 잔액: {self.balance}원")

    def check_balance(self):
        print(f"{self.name}님의 현재 잔액은 {self.balance}원입니다.")

    def save_to_file(self):
        # 모든 고객 정보를 파일에 저장
        all_account = {}

        # 기존 정보 읽기
        if os.path.exists("account_info.txt"):
            with open("account_info.txt", "r") as file:
                for line in file:
                    name, balance = line.strip().split(",")

        # 현재 계좌 정보 업데이트 또는 추가
        all_account[self.name] = str(self.balance)

        # 모든 정보를 다시 파일에 저장
        with open("account_info.txt", "w") as file:
            for nmae, balance in all_account.items():
                file.write(f"{name}, {balance}\n")

    @staticmethod
    def load_from_file(name):
        # 파일에서 고객 이름 검색 후 불러오기
        if os.path.exists("account_info.txt"):
            with open("account_info.txt", "r") as file:
                for line in file:
                    account_name, balance = line.strip().split(",")
                    if account_name == name:
                        print(f"{name}님의 기존 계좌 정보를 불러왔습니다. 잔액 {balance}원")

        # 파일에 없는 경우 새 계좌 생성
        print(f"{name}님의 계좌 정보가 없습니다. 새 계좌를 생성합니다.")
        inital_balance = int(input("초기 잔액을 입력하세요 : "))
        return BankAccount(name, inital_balance)

# 고객 이름 입력 후 정보 불러오기
customer_name = input("계좌 소유자의 이름을 입력하세요 : ")
account = BankAccount.load_from_file(customer_name)

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





# import os   # 파일 존재 여부를 확인하기 위해 사용

# class BankAccount:
#     def __init__(self, name, balance):
#         self.name = name    # 계좌 소유자 이름
#         self.balance = balance  # 초기 잔액

#     def deposit(self, deposit_amount):
#         self.balance += deposit_amount
#         print(f"{deposit_amount}원 입금되었습니다. 현재 잔액 : {self.balance}원")

#     def withdraw(self, withdraw_amount):
#         if withdraw_amount > self.balance:
#             print("잔액이 부족하여 출금할 수 없습니다.")
#         else:
#             self.balance -= withdraw_amount
#             print(f"{withdraw_amount}원 출금되었습니다. 현재 잔액 : {self.balance}")

#     def check_balance(self):
#         print(f"{self.name}님의 현재 잔액을 {self.balance}원 입니다.")
        

#     def save_to_file(self):
#         # 계좌 정보를 파일에 저장
#         with open("accoun_info.txt", "w") as file:
#             file.write(f"{self.name}, {self.balance}")
#         print("계좌 정보가 저장되었습니다.")

#     @staticmethod
#     def load_from_file():
#         # 계좌 정보를 파일에서 불러옴
#         if os.path.exists("account_info.txt"):
#             with open("account_info.txt", "r") as file:
#                 data = file.read().strip().split(",")
#                 name = data[0]
#                 balance = int(data[1])
#                 return BankAccount(name, balance)
        
#         else:
#             # 파일이 없으면 새 계좌 생성
#             name = input("계좌 소유자의 이름을 입력하세요 : ")
#             initial_balance = int(input("초기 잔액을 입력하세요 : "))
#             return BankAccount(name, initial_balance)
        
# # 기존 계좌 정보 불러오기 또는 새 계좌 생성
# account = BankAccount.load_from_file()

# # 메뉴 시스템
# while True:
#     print("\n메뉴 선택:")
#     print("1. 입금")
#     print("2. 출금")
#     print("3. 잔액 확인")
#     print("4. 종료")

#     choice = input("원하는 작업의 번호를 입력하세요 : ")

#     match choice:
#         case "1":
#             try:
#                 deposit_amount = int(input("입금할 금액을 입력하세요 : "))
#                 account.deposit(deposit_amount)
#             except ValueError:
#                 print("숫자만 입력해주세요.")

#         case "2":
#             try:
#                 withdraw_amount = int(input("출금할 금액을 입력하세요 : "))
#                 account.withdraw(withdraw_amount)
#             except ValueError:
#                 print("숫자만 입력해주세요.")

#         case "3":
#             account.check_balance()

#         case "4":
#             account.save_to_file()  # 종료 전에 계좌 정보 저장
#             print(f"{account.name}님의 계좌를 종료합니다. 최종 잔액은 {account.balance}원 입니다.")
#             break

#         case _:
#             print("잘못된 입력입니다. 다시 선택하세요.")
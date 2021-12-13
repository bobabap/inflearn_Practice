print("------------------------------------- 271 Account 클래스")
# 271
'''은행에 가서 계좌를 개설하면 은행이름, 예금주, 계좌번호, 잔액이 설정됩니다.
Account 클래스를 생성한 후 생성자를 구현해보세요. 생성자에서는 예금주와 초기 잔액만
입력 받습니다. 은행이름은 SC은행으로 계좌번호는 3자리-2자리-6자리 형태로 랜덤하게 생성됩니다.
'''
import random

from numpy import number

class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bankaccount = 'SC은행'
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3) # 1 -> '1' -> '001'
        num2 = str(num2).zfill(2) # 1 -> '1' -> '01'
        num3 = str(num3).zfill(6) # 1 -> '1' -> '0000001'
        self.account_number = num1 + '-' + num2 + '-' + num3

yang = Account('양준모', 100)
print(yang.name)
print(yang.balance)
print(yang.bankaccount)
print(yang.account_number)


print("------------------------------------- 272 클래스 변수")
# 272
'''클래스 변수를 사용해서 Account 클래스로부터 생성된 계좌 객체의 개수를 저장하세요.'''
class Account:
    account_count = 0
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bankaccount = 'SC은행'
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3) # 1 -> '1' -> '001'
        num2 = str(num2).zfill(2) # 1 -> '1' -> '01'
        num3 = str(num3).zfill(6) # 1 -> '1' -> '0000001'
        self.account_number = num1 + '-' + num2 + '-' + num3

        Account.account_count += 1

kim = Account("김민수", 100)
print(Account.account_count)
lee = Account('이민수', 200)
print(Account.account_count)


print("------------------------------------- 273 클래스 변수 출력")
# 273
'''Account 클래스로부터 생성된 계좌의 개수를 출력하는 get_account_num() 메서드를 추가하세요.'''
class Account:
    account_count = 0
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bankaccount = 'SC은행'
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3) # 1 -> '1' -> '001'
        num2 = str(num2).zfill(2) # 1 -> '1' -> '01'
        num3 = str(num3).zfill(6) # 1 -> '1' -> '0000001'
        self.account_number = num1 + '-' + num2 + '-' + num3
        Account.account_count += 1
    
    @classmethod
    def get_account_num(cls):
        print(cls.account_count) # Account.account_count

kim = Account("김민수", 100)
lee = Account('이민수', 200)
kim.get_account_num()


print("------------------------------------- 274 입금")
# 274


class Account:
    # class variable
    account_count = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bankaccount = 'SC은행'
        
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3) # 1 -> '1' -> '001'
        num2 = str(num2).zfill(2) # 1 -> '1' -> '01'
        num3 = str(num3).zfill(6) # 1 -> '1' -> '0000001'
        self.account_number = num1 + '-' + num2 + '-' + num3
        
        Account.account_count += 1
    
    @classmethod
    def get_account_num(cls):
        print(cls.account_count) # Account.account_count
    
    def deposit(self, amount):
        if amount >= 1:
            self.balance += amount

kim = Account("김민수", 100)
lee = Account('이민수', 200)
kim.deposit(1000)



print("------------------------------------- 275 출금 메서드")
# 275


class Account:
    # class variable
    account_count = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = "SC은행"

        # 3-2-6
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)  # 1 -> '1' -> '001'
        num2 = str(num2).zfill(2)  # 1 -> '1' -> '01'
        num3 = str(num3).zfill(6)  # 1 -> '1' -> '0000001'
        self.account_number = num1 + '-' + num2 + '-' + num3  # 001-01-000001
        Account.account_count += 1

    @classmethod
    def get_account_num(cls):
        print(cls.account_count)  # Account.account_count

    def deposit(self, amount):
        if amount >= 1:
            self.balance += amount

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount

k = Account("kim", 100)
k.deposit(100)
k.withdraw(90)
print(k.balance)


print("------------------------------------- 276")
# 276
'''Account 인스턴스에 저장된 정보를 출력하는 display_info() 메서드를 추가하세요.
잔고는 세자리마다 쉼표를 출력하세요.'''
class Account:
    # class variable
    account_count = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = "SC은행"

        # 3-2-6
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)  # 1 -> '1' -> '001'
        num2 = str(num2).zfill(2)  # 1 -> '1' -> '01'
        num3 = str(num3).zfill(6)  # 1 -> '1' -> '0000001'
        
        self.account_number = num1 + '-' + num2 + '-' + num3  # 001-01-000001
        
        Account.account_count += 1
    

    @classmethod
    def get_account_num(cls):
        print(cls.account_count)  # Account.account_count

    def deposit(self, amount):
        if amount >= 1:
            self.balance += amount

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
    
    def display_info(self):
        print('은행이름:', self.bank)
        print('예금주:', self.name)
        print('계좌번호:', self.account_number)
        print('잔고: ''{:,}'.format(self.balance))

p = Account('양준모', 1000000000000000000000000)
p.display_info()



print("------------------------------------- 277 이자 지급하기")
# 277
'''입금 횟수가 5회가 될 때 잔고를 기준으로 1%의 이자가 잔고에 추가되도록 코드를 변경해보세요.'''
class Account:
    # class variable
    account_count = 0
    
    def __init__(self, name, balance):
        self.deposit_count = 0 # __init__ 함수 밖에두어도 실행 가능

        self.name = name
        self.balance = balance
        self.bank = "SC은행"

        # 3-2-6
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)  # 1 -> '1' -> '001'
        num2 = str(num2).zfill(2)  # 1 -> '1' -> '01'
        num3 = str(num3).zfill(6)  # 1 -> '1' -> '0000001'
        
        self.account_number = num1 + '-' + num2 + '-' + num3  # 001-01-000001
        
        Account.account_count += 1 # 생성된 계좌 객체의 개수
    

    @classmethod
    def get_account_num(cls):
        print(cls.account_count)  # Account.account_count

    def deposit(self, amount): # 입금
        if amount >= 1:
            self.balance += amount

            self.deposit_count += 1
            if self.deposit_count % 5 == 0:         # 5, 10, 15
                # 이자 지금
                self.balance = (self.balance * 1.01)

    def withdraw(self, amount): # 출금
        if self.balance > amount:
            self.balance -= amount
    
    def display_info(self):
        print('은행이름:', self.bank)
        print('예금주:', self.name)
        print('계좌번호:', self.account_number)
        print('잔고: ''{:,}'.format(self.balance))
    

p = Account('양준모', 10000)
p.deposit(10000)
p.deposit(10000)
p.deposit(10000)
p.deposit(5000)
p.deposit(5000)
print(p.balance)



print("------------------------------------- 278 여러 객체 생성")
# 278
class Account:
    # class variable
    account_count = 0
    
    def __init__(self, name, balance):
        self.deposit_count = 0 # __init__ 함수 밖에두어도 실행 가능

        self.name = name
        self.balance = balance
        self.bank = "SC은행"

        # 3-2-6
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)  # 1 -> '1' -> '001'
        num2 = str(num2).zfill(2)  # 1 -> '1' -> '01'
        num3 = str(num3).zfill(6)  # 1 -> '1' -> '0000001'
        
        self.account_number = num1 + '-' + num2 + '-' + num3  # 001-01-000001
        
        Account.account_count += 1 # 생성된 계좌 객체의 개수
    

    @classmethod
    def get_account_num(cls):
        print(cls.account_count)  # Account.account_count

    def deposit(self, amount): # 입금
        if amount >= 1:
            self.balance += amount

            self.deposit_count += 1
            if self.deposit_count % 5 == 0:         # 5, 10, 15
                # 이자 지금
                self.balance = (self.balance * 1.01)

    def withdraw(self, amount): # 출금
        if self.balance > amount:
            self.balance -= amount
    
    def display_info(self):
        print('은행이름:', self.bank)
        print('예금주:', self.name)
        print('계좌번호:', self.account_number)
        print('잔고: ''{:,}'.format(self.balance))

data = []
k = Account('Kim', 1000000)
y = Account('yang', 999999999)
p = Account('Park', 1000)

data.append(k)
data.append(y)
data.append(p)

print(data[0].account_number)


print("------------------------------------- 279 객체 순회")
# 279
'''반복문을 통해 리스트에 있는 객체를 순회하면서 잔고가 100만원 이상인 고객의 정보만 출력하세요.'''
class Account:
    # class variable
    account_count = 0
    
    def __init__(self, name, balance):
        self.deposit_count = 0 # __init__ 함수 밖에두어도 실행 가능

        self.name = name
        self.balance = balance
        self.bank = "SC은행"

        # 3-2-6
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)  # 1 -> '1' -> '001'
        num2 = str(num2).zfill(2)  # 1 -> '1' -> '01'
        num3 = str(num3).zfill(6)  # 1 -> '1' -> '0000001'
        
        self.account_number = num1 + '-' + num2 + '-' + num3  # 001-01-000001
        
        Account.account_count += 1 # 생성된 계좌 객체의 개수
    

    @classmethod
    def get_account_num(cls):
        print(cls.account_count)  # Account.account_count

    def deposit(self, amount): # 입금
        if amount >= 1:
            self.balance += amount

            self.deposit_count += 1
            if self.deposit_count % 5 == 0:         # 5, 10, 15
                # 이자 지금
                self.balance = (self.balance * 1.01)

    def withdraw(self, amount): # 출금
        if self.balance > amount:
            self.balance -= amount
    
    def display_info(self):
        print('은행이름:', self.bank)
        print('예금주:', self.name)
        print('계좌번호:', self.account_number)
        print('잔고: ''{:,}'.format(self.balance))

data = []
k = Account('Kim', 1000000)
y = Account('yang', 999999999)
p = Account('Park', 10000)
data.append(k)
data.append(y)
data.append(p)

for c in data:
    if c.balance > 1000000:
        c.display_info()




print("------------------------------------- 280 입출금 내역")
# 280
'''입금과 출금 내역이 기록되도록 코드를 업데이트 하세요. 
입금 내역과 출금 내역을 출력하는 deposit_history와 withdraw_history 메서드를 추가하세요.'''
class Account:
    # class variable
    account_count = 0
    
    def __init__(self, name, balance):
        self.deposit_count = 0 # __init__ 함수 밖에두어도 실행 가능
        self.deposit_log = []
        self.withdraw_log = []

        self.name = name
        self.balance = balance
        self.bank = "SC은행"

        # 3-2-6
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)  # 1 -> '1' -> '001'
        num2 = str(num2).zfill(2)  # 1 -> '1' -> '01'
        num3 = str(num3).zfill(6)  # 1 -> '1' -> '0000001'
        
        self.account_number = num1 + '-' + num2 + '-' + num3  # 001-01-000001
        
        Account.account_count += 1 # 생성된 계좌 객체의 개수
    

    @classmethod
    def get_account_num(cls):
        print(cls.account_count)  # Account.account_count

    def deposit(self, amount): # 입금
        if amount >= 1:
            self.deposit_log.append(amount)
            self.balance += amount

            self.deposit_count += 1
            if self.deposit_count % 5 == 0:         # 5, 10, 15
                # 이자 지금
                self.balance = (self.balance * 1.01)

    def withdraw(self, amount): # 출금
        if self.balance > amount:
            self.withdraw_log.append(amount)
            self.balance -= amount
    
    def display_info(self):
        print('은행이름:', self.bank)
        print('예금주:', self.name)
        print('계좌번호:', self.account_number)
        print('잔고: ''{:,}'.format(self.balance))
    

    def withdraw_history(self):
        for amount in self.withdraw_log:
            print(amount)

    def deposit_history(self):
        for amount in self.deposit_log:
            print(amount)


k = Account("Kim", 1000)
k.deposit(100)
k.deposit(200)
k.deposit(300) # self.deposit_log = [100, 200, 300], amount 100 200 300
k.deposit_history()
print(k.balance)

print()

k.withdraw(100)
k.withdraw(200)
k.withdraw_history()
print(k.balance)

class Calculator:
    def __init__(self):
        self.value = 0
    
        


class MaxLimitCalculator(Calculator):
    def add_max(self, val):
        self.value += val
        if self.value >= 0:
            self.value = 100




cal = MaxLimitCalculator()
cal.add_max(50) # 50
cal.add_max(60) # 60
print(cal.value) # 100
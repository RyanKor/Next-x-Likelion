class fourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
# __init__은 우리가 클래스 내에서 형성하기만 하면 다른 메소드를 불러 낼 필요가 없이 사용할 수 있다는 장점이 있음.
    def add(self):
        result = self.first + self.second
        return result

    def subtract(self):
        result = self.first - self.second
        return result
    
    def multiply(self):
        result = self.first * self.second
        return result

    def division(self):
        result = self.first / self.second
        return result
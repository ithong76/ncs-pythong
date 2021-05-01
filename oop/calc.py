class Calcurator:

    def __init__(self, first, second):
        self.first = first
        self.second = second

    def sum(self):
        return self.first + self.second

    def sub(self):
        return self.first - self.second

    def mul(self):
        return self.first * self.second

    def div(self):
        return self.first / self.second
        """
        if(self.second != 0):
            return self.first / self.second
        else:
            return -1
        """

    def mod(self):
        return self.first % self.second


    @staticmethod
    def execute():
        calc = Calcurator(int(input("FirstValue <<")),int(input("SecondValue<<")))
        print(f'First Value : {calc.first}')
        print(f'Second Value : {calc.second}')
        print(f'{calc.first}+{calc.second}={calc.sum()}')
        print(f'{calc.first}-{calc.second}={calc.sub()}')
        print(f'{calc.first}*{calc.second}={calc.mul()}')
        print(f'{calc.first}/{calc.second}={calc.div()}')
        print(f'{calc.first}%{calc.second}={calc.mod()}')

if __name__ == '__main__':
    Calcurator.execute()





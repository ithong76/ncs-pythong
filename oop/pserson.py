class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def greeting(self):
        print(f'안녕하세요. 제 이름은{self.name}이고 '
              f'나이는{self.age}이고 '
              f'집주소는{self.address}입니다.')

    @staticmethod
    def main():
        maria = Person('maria', 20, 'Seoul')
        maria.greeting()
        tom = Person('tom', 22, 'Incheon')
        tom.greeting()

if __name__ == '__main__':
    Person.main()

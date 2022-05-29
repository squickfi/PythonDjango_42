class HotBeverage:
    def __init__(self, price=0.30, name='hot beverage'):
        self.price = price
        self.name = name

    def description(self):
        return 'Just some hot water in a cup.'

    def __str__(self):
        return f"name : {self.name}\nprice : {self.price}\ndescription : {self.description()}"


class Coffee(HotBeverage):
    def __init__(self):
        super().__init__(0.40, 'coffee')

    def description(self):
        return 'A coffee, to stay awake.'


class Tea(HotBeverage):
    def __init__(self):
        super().__init__(0.30, 'tea')

    def description(self):
        return 'Just some hot water in a cup.'


class Chocolate(HotBeverage):
    def __init__(self):
        super().__init__(0.50, 'chocolate')

    def description(self):
        return 'Chocolate, sweet chocolate...'


class Cappuccino(HotBeverage):
    def __init__(self):
        super().__init__(0.45, 'cappuccino')

    def description(self):
        return 'Un po’ di Italia nella sua tazza!'


def test_drinks():
    print(HotBeverage(), '\n')
    print(Coffee(), '\n')
    print(Tea(), '\n')
    print(Chocolate(), '\n')
    print(Cappuccino(), '\n')


if __name__ == '__main__':
    test_drinks()

import random
from beverages import HotBeverage, Coffee, Tea, Chocolate, Cappuccino


class CoffeeMachine:
    def __init__(self):
        self.number_of_beverages_after_repair = 0

    class EmptyCup(HotBeverage):
        def __init__(self):
            HotBeverage.__init__(self, 0.90, 'empty cup')

        def description(self):
            return 'An empty cup?! Gimme my money back!'

    class BrokenMachineException(Exception):
        def __init__(self):
            super().__init__('This coffee machine has to be repaired.')

    def repair(self):
        self.number_of_beverages_after_repair = 0

    def serve(self, drink: HotBeverage):
        if self.number_of_beverages_after_repair > 10:
            raise CoffeeMachine.BrokenMachineException()
        self.number_of_beverages_after_repair += 1
        if random.randint(0, 1):
            return drink
        return CoffeeMachine.EmptyCup()


def test_machine():
    beverages = [HotBeverage(), Coffee(), Tea(), Chocolate(), Cappuccino()]
    machine = CoffeeMachine()
    for _ in range(0, 2):
        print('starting making {} drinks:', 11)
        try:
            for i in range(0, 12):
                print('iter:', i)
                print(machine.serve(beverages[random.randint(0, 4)]))
        except Exception as e:
            print(e)
            machine.repair()
        print('\n')
    machine.repair()
    print('starting making {} drinks:', 6)
    for i in range(0, 6):
        print('iter:', i + 1)
        print(machine.serve(beverages[random.randint(0, 4)]))


if __name__ == '__main__':
    test_machine()

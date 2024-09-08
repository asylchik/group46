class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def make_computations(self):
        return f'Арифметическое вычесление {self.__memory * 2}'

    def __str__(self):
        return f'Компьютер CPU: {self.__cpu}, Memory: {self.__memory}'

    def __eq__(self, other):
        return self.memory == other.memory

    def __ne__(self, other):
        return self.memory != other.memory

    def __lt__(self, other):
        return self.memory < other.memory

    def __gt__(self, other):
        return self.memory > other.memory

    def __le__(self, other):
        return self.memory <= other.memory

    def __ge__(self, other):
        return self.memory >= other.memory


class Phone:
    def __init__(self, sim_cards_list: list):
        self.__sim_cards_list = sim_cards_list

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value

    def call(self, sim_card_number: int, call_to_number: str):
        print(f'Идет звонок на номер {call_to_number} с сим-карты-{sim_card_number} - {self.__sim_cards_list}')

    def __str__(self):
        return f'Телефон с сим картами: {self.__sim_cards_list}'


class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    def use_gps(self, location):
        print(f'Построение маршрута до {location}...')

    def __str__(self):
        return f'Cмартфон CPU: {self.cpu}, Memory: {self.memory}, сим карты: {self.sim_cards_list}'


computer = Computer('Intel i5', 16)
phone = Phone(['Megacom', 'O!'])
smartphone_1 = SmartPhone('Samsung s24', 256, ['Beeline', 'O!'])
smartphone_2 = SmartPhone('iPhone 15 pro max', 256, ['Beeline', 'Megacom'])
print(computer)
print(phone)
print(smartphone_1)
print(smartphone_2)

phone.call(1, '+996 777 99 88 11')
smartphone_1.call(2, '+996 500 57 74 35')
smartphone_2.call(2, '+996 555 45 23 78')

smartphone_1.use_gps("Bishkek")
print(smartphone_1.make_computations())

print(smartphone_1 > smartphone_2)
print(smartphone_1 < smartphone_2)
print(smartphone_1 == smartphone_2)
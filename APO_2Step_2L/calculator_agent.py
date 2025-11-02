from thespian.actors import ActorAddress

from agent_base import AgentBase
from message import Message


class CalculatorAgent(AgentBase):
    def __init__(self):
        super().__init__()
        # Все полученные числа будем сохранять в списке.
        self.values = []

    def handle_hello_world(self, message: Message, sender: ActorAddress):
        new_value = message.msg_body
        
        print(f'Калькулятор {self.myAddress} получил: {message}')
        
        if isinstance(new_value, (int, float)):
            self.values.append(new_value)
            print(f'Добавлено число: {new_value}. Всего чисел: {len(self.values)}')
        
        elif isinstance(new_value, str):
            if new_value == 'sum':
                result = sum(self.values)
                print(f'Сумма: {result}')
            elif new_value == 'multiply':
                result = 1
                for n in self.values: result *= n
                print(f'Произведение: {result}')
            elif new_value == 'avg':
                avg = sum(self.values)/len(self.values) if self.values else 0
                print(f'Среднее значение: {avg}')
            elif new_value == 'clear':
                self.values = []
                print('Список очищен')
            elif  new_value == 'get values':
                print(f'Список чисел: {self.values}')
            else:
                print(f'Неизвестная операция: {new_value}')

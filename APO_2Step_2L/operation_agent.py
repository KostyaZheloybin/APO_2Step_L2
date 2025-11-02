from thespian.actors import ActorAddress

from agent_base import AgentBase
from message import Message, MessageType

class OperationAgent(AgentBase):
    def __init__(self):
        super().__init__()
        # В это поле будем сохранять полученное значение.
        self.operation = ''
        self.subscribe(MessageType.INITIALIZATION, self.handle_initialization)
        
    def handle_initialization(self, message: Message, sender: ActorAddress):
        print(f'Актор операции с адресом {self.myAddress} получил {message} от {sender}')
        # Ожидаем, что в сообщении будет содержаться словарь со значением математической операции и адресом актора-калькулятора.
        self.operation = message.msg_body.get('operation')
        calculator_address = message.msg_body.get('calculator_address')
        # Отправляем калькулятору свое значение.
        new_message = Message(MessageType.HELLO_WORLD, self.operation)
        self.send(calculator_address, new_message)

    
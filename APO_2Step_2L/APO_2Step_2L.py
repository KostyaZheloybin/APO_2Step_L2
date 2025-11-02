
from thespian.actors import *
from calculator_agent import CalculatorAgent
from number_agent import NumberAgent
from operation_agent import OperationAgent
from message import Message, MessageType


if __name__ == '__main__':
    # Создаем систему акторов, внутри которой они будут жить
    actorSystem = ActorSystem()
    # Создаем актор-калькулятор, сохраняем его адрес.
    calculator_address = actorSystem.createActor(CalculatorAgent)
    # Создаем актор-число
    number_agent_1 = actorSystem.createActor(NumberAgent)
    # Формируем сообщение со значением числа и адресом калькулятора.
    init_message_1_data = {'init_value': 1, 'calculator_address': calculator_address}
    # Отправляем актору числа сообщение, после которого он должен отправить другое сообщение калькулятору.
    init_message_1 = Message(MessageType.INITIALIZATION, init_message_1_data)
    actorSystem.tell(number_agent_1, init_message_1)

    number_agent_2 = actorSystem.createActor(NumberAgent)
    init_message_2_data = {'init_value': 3, 'calculator_address': calculator_address}
    init_message_2 = Message(MessageType.INITIALIZATION, init_message_2_data)
    actorSystem.tell(number_agent_2, init_message_2)

    number_agent_3 = actorSystem.createActor(NumberAgent)
    init_message_3_data = {'init_value': 5, 'calculator_address': calculator_address}
    init_message_3 = Message(MessageType.INITIALIZATION, init_message_3_data)
    actorSystem.tell(number_agent_3, init_message_3)

    #создание агентов математических операций

    operation_agent_1 = actorSystem.createActor(OperationAgent)
    init_message_1_data = {'operation': 'sum', 'calculator_address': calculator_address}
    operation_message_1 = Message(MessageType.INITIALIZATION, init_message_1_data)
    actorSystem.tell(operation_agent_1, operation_message_1)

    operation_agent_2 = actorSystem.createActor(OperationAgent)
    init_message_2_data = {'operation': 'avg', 'calculator_address': calculator_address}
    operation_message_2 = Message(MessageType.INITIALIZATION, init_message_2_data)
    actorSystem.tell(operation_agent_2, operation_message_2)

    operation_agent_3 = actorSystem.createActor(OperationAgent)
    init_message_3_data = {'operation': 'multiply', 'calculator_address': calculator_address}
    operation_message_3 = Message(MessageType.INITIALIZATION, init_message_3_data)
    actorSystem.tell(operation_agent_3, operation_message_3)

    operation_agent_4 = actorSystem.createActor(OperationAgent)
    init_message_4_data = {'operation': 'some_operation', 'calculator_address': calculator_address}
    operation_message_4 = Message(MessageType.INITIALIZATION, init_message_4_data)
    actorSystem.tell(operation_agent_4, operation_message_4)

    operation_agent_5 = actorSystem.createActor(OperationAgent)
    init_message_5_data = {'operation': 'get values', 'calculator_address': calculator_address}
    operation_message_5 = Message(MessageType.INITIALIZATION, init_message_5_data)
    actorSystem.tell(operation_agent_5, operation_message_5)

    operation_agent_6 = actorSystem.createActor(OperationAgent)
    init_message_6_data = {'operation': 'clear', 'calculator_address': calculator_address}
    operation_message_6 = Message(MessageType.INITIALIZATION, init_message_6_data)
    actorSystem.tell(operation_agent_6, operation_message_6)


class Kafka:
    def __init__(self, message:str) -> None:
        self.message = message

    def send(self, message:str)-> str:
        self.message = message
        return f"Kafka: Send message:{message}"
    
    def receive(self) -> str:
        if not self.message:
            return "Kafka: No message to receive"
        else:
            return f"Kafka: Received message {self.message}"

class RabbitMQ:
    def __init__(self, message:str) -> None:
        self.message = message

    def send(self, message:str)-> str:
        self.message = message
        return f"RabbitMQ: Send message:{message}"
    
    def receive(self) -> str:
        if not self.message:
            return "RabbitMQ: No message to receive"
        else:
            return f"RabbitMQ: Received message {self.message}"

class InterfaceFacade:
    def __init__(self, backend: str = "Kafka") -> None:
        self.backend = backend.lower()
        if self.backend == "rabbitmq":
            self.model = RabbitMQ("")
        elif self.backend == "kafka":
            self.model = Kafka("")
        else:
            raise ValueError(f"Error")
        
    def send_mess(self, message: str) -> str:
        return self.model.send(message)
    
    def receive_message(self) -> str:
        return self.model.receive()
    
def main():
    rabbit = InterfaceFacade("RabbitMQ")
    print(rabbit.send_mess("Hello World!"))
    print(rabbit.receive_message())

    print("\nKafka:")
    kafka = InterfaceFacade("Kafka")
    print(kafka.send_mess("Hello World with Kafka!"))
    print(kafka.receive_message())

if __name__ == "__main__":
    main()
    



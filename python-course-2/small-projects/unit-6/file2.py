from file1 import GreetingCard


class BirthdayCard(GreetingCard):
    def __init__(self):
        super().__init__()
        self._sender_age = 0

    def greeting_msg(self):
        print("The sender:", self._sender)
        print("The recipient:", self._recipient)
        print("The sender's age:", self._sender_age)



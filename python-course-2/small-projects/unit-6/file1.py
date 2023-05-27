class GreetingCard:
    def __init__(self):
        self._recipient = "Dana Ev"
        self._sender = "Eyal Ch"

    def greeting_msg(self):
        print("The sender", self._sender, "\nThe recipient", self._recipient)

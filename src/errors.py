class MalformedBudget(Exception):
    def __init__(self, message="Malformed budget dictionary"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message


class MalformedConfig(Exception):
    def __init__(self, message="Malformed configuration file"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message

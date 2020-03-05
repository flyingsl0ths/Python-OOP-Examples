class _Private:
    # Convention states that a class name
    # prefixed with an '_' shall be used in a private manner
    # that is only within another class
    def __init__(self, name):
        self.name = name

    def _display(self):
        print("Hello")


class NotPrivate:
    def __init__(self, name):
        self.name = name
        self.priv = _Private(name)

    def _display(self):
        # This applies to methods as well
        self.priv._display()

    def display(self):
        print("Hi")


p = NotPrivate("George")
p.display()